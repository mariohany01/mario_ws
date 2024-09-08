#include <ros/ros.h>
#include <geometry_msgs/Twist.h>
#include <termios.h>
#include <stdio.h>
#include <unistd.h>
#include <sys/select.h>
#include <map>

// Message to display instructions for controlling the robot.

const char* msg = R"(
Control: 
u    i    o
j    k    l
m    ,    .

q/z : increase/decrease max speeds by 10%
w/x : increase/decrease only linear speed by 10%
e/c : increase/decrease only angular speed by 10%
space key, k : force stop
anything else : stop smoothly
CTRL-C to quit
)";


// Move bindings for controlling the robot
std::map<char, std::pair<int, int>> moveBindings = {
    {'i', {1, 0}},
    {'o', {1, -1}},
    {'j', {0, 1}},
    {'l', {0, -1}},
    {'u', {1, 1}},
    {',', {-1, 0}},
    {'.', {-1, 1}},
    {'m', {-1, -1}},
};

// Speed bindings for adjusting the speed and turn rate
std::map<char, std::pair<double, double>> speedBindings = {
    {'q', {1.1, 1.1}},
    {'z', {0.9, 0.9}},
    {'w', {1.1, 1.0}},
    {'x', {0.9, 1.0}},
    {'e', {1.0, 1.1}},
    {'c', {1.0, 0.9}},
};

struct termios orig_termios;

void reset_terminal_mode() {
    tcsetattr(STDIN_FILENO, TCSANOW, &orig_termios);
}

void set_conio_terminal_mode() {
    struct termios new_termios;
    tcgetattr(STDIN_FILENO, &orig_termios);
    memcpy(&new_termios, &orig_termios, sizeof(new_termios));
    atexit(reset_terminal_mode);
    cfmakeraw(&new_termios);
    tcsetattr(STDIN_FILENO, TCSANOW, &new_termios);
}

int kbhit() {
    struct timeval tv = { 0L, 0L };
    fd_set fds;
    FD_ZERO(&fds);
    FD_SET(STDIN_FILENO, &fds);
    return select(STDIN_FILENO + 1, &fds, NULL, NULL, &tv);
}

char getch() {
    char c;
    if (read(STDIN_FILENO, &c, 1) < 0) {
        perror("read()");
        return '\0';
    }
    return c;
}

std::string vels(double speed, double turn) {
    char buffer[50];
    snprintf(buffer, sizeof(buffer), "currently:\t speed %.2f \t turn %.2f", speed, turn);
    return std::string(buffer);
}

int main(int argc, char** argv) {
    // Initialize the ROS node
    ros::init(argc, argv, "BoB_teleop");
    ros::NodeHandle nh;
    ros::Publisher pub = nh.advertise<geometry_msgs::Twist>("/cmd_vel", 10);

    double speed = 1.0;
    double turn = 1.0;
    int x = 0, th = 0;
    int count = 0;
    double target_speed = 0, target_turn = 0;
    double control_speed = 0, control_turn = 0;
    char key;

    set_conio_terminal_mode();
    std::cout << msg << std::endl;
    std::cout << vels(speed, turn) << std::endl;

    try {
        while (ros::ok()) {
            if (kbhit()) {
                key = getch();

                if (moveBindings.count(key)) {
                    x = moveBindings[key].first;
                    th = moveBindings[key].second;
                    count = 0;
                }
                else if (speedBindings.count(key)) {
                    speed *= speedBindings[key].first;
                    turn *= speedBindings[key].second;
                    count = 0;
                    std::cout << vels(speed, turn) << std::endl;
                }
                else if (key == 'k') {
                    x = 0;
                    th = 0;
                    control_speed = 0;
                    control_turn = 0;
                }
                else {
                    count++;
                    if (count > 2) {
                        x = 0;
                        th = 0;
                    }
                    if (key == 3) {  // Ctrl-C
                        break;
                    }
                }

                target_speed = speed * x;
                target_turn = turn * th;

                if (target_speed > control_speed)
                    control_speed = std::min(target_speed, control_speed + 0.1);
                else if (target_speed < control_speed)
                    control_speed = std::max(target_speed, control_speed - 0.1);
                else
                    control_speed = target_speed;

                if (target_turn > control_turn)
                    control_turn = std::min(target_turn, control_turn + 0.5);
                else if (target_turn < control_turn)
                    control_turn = std::max(target_turn, control_turn - 0.5);
                else
                    control_turn = target_turn;

                geometry_msgs::Twist twist;
                twist.linear.x = control_speed;
                twist.angular.z = control_turn;
                pub.publish(twist);
            }

            ros::spinOnce();
        }
    } catch (...) {
        ROS_WARN("An error occurred!");
    }

    // Cleanup code: this will always run even after an exception
    geometry_msgs::Twist twist;
    twist.linear.x = 0;
    twist.angular.z = 0;
    pub.publish(twist);
    reset_terminal_mode();

    return 0;
}
