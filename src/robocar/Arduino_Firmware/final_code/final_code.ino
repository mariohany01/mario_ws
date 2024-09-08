/************************************************************/
//////////////////////////////include/////////////////////////
/************************************************************/
#include <ros.h>
#include <std_msgs/Int32.h>
#include <std_msgs/Bool.h>
#include <std_msgs/Float32.h>
#include <sensor_msgs/Range.h>
#include <ros/time.h>

/************************************************************/
//////////////////////////////PINS/////////////////////////
/************************************************************/

//////////////////////////////Encoder/////////////////////////
int encoder_pinA = 2;    
int encoder_pinB = 3;
volatile int pulses1 = 0;  
volatile int pulses2 = 0; 
//////////////////////////////MOTOR A/////////////////////////
int enableA = 5;
int MotorA1 = 6;
int MotorA2 = 7;
//////////////////////////////MOTOR B/////////////////////////
int enableB = 10;
int MotorB1 = 8;
int MotorB2 = 9;   
//////////////////////////////IR PIN//////////////////////////
#define IR_PIN A0
//////////////////////////////Ultrasonoic//////////////////////                        
const int echoPin = 11;  //Echo pin
const int trigPin = 12;  //Trigger pin

/************************************************************/
//////////////////////////////Ta3reefat//////////////////////
/************************************************************/

//Left and right speed
int r_speed = 0;
int l_speed = 0;

//Direction flag for encoder
int left_direction = 1;
int right_direction = 1;

//Ultrasonic Data
const int maxRange = 200.0;   //Maximum range in centimeters
const int minRange = 0.0;     //Minimum range in centimeters

unsigned long range_timer;    //Used to measure 50 ms interval


char frameid[] = "/ultrasound";   // global frame id string //Kan taht el get range

/************************************************************/
//////////////////////////////ROS/////////////////////////////
/************************************************************/

//ROS Node handle
ros::NodeHandle  nh;

//////////////////////////////PUBLISHER/////////////////////////////

///Pub Ultrasound Topic
sensor_msgs::Range range_msg;
ros::Publisher pub_range( "ultrasound", &range_msg);
///Pub Left ticks encoder data topics
std_msgs::Int32 l_encoder_msg;
ros::Publisher l_enc_pub("left_ticks", &l_encoder_msg);
///Pub Right ticks encoder data topics
std_msgs::Int32 r_encoder_msg;
ros::Publisher r_enc_pub("right_ticks", &r_encoder_msg);
//Pub Sharp IR obstacle Distance Topic
std_msgs::Float32 sharp_msg;
ros::Publisher sharp_distance_pub("obstacle_distance", &sharp_msg);

//////////////////////////////SUBSCRIBER/////////////////////////////

///cmd_vel callback function definition
void left_speed_cb(const std_msgs::Int32& msg)
  {

   digitalWrite(LED_BUILTIN, HIGH-digitalRead(LED_BUILTIN));   // blink the led
   l_speed = msg.data;

  }
///cmd_vel callback function definition
void right_speed_cb(const std_msgs::Int32& msg)
  {
   digitalWrite(LED_BUILTIN, HIGH-digitalRead(LED_BUILTIN));   // blink the led
   r_speed = msg.data;

  }
///cmd_vel callback function definition
void reset_cb(const std_msgs::Bool& msg)
  {

    l_speed = 0;
    r_speed = 0;

    pulses1 = 0;
    pulses2 = 0;

  
  }



// creation of subscriber object sub for recieving the cmd_vel
ros::Subscriber<std_msgs::Int32> left_speed_sub("set_left_speed",&left_speed_cb);
// creation of subscriber object sub for recieving the cmd_vel  
ros::Subscriber<std_msgs::Int32> right_speed_sub("set_right_speed",&right_speed_cb);  
// creation of subscriber object sub for recieving the cmd_vel
ros::Subscriber<std_msgs::Bool> reset_sub("reset",&reset_cb);  


/************************************************************/
//////////////////////////////FUNCTIONS///////////////////////
/************************************************************/

///This function reads the time duration of the echo and converts it to centimeters
float getRange(){
    int sample;      //Holds time in microseconds
    
    // Trigger pin goes low then high for 10 us then low
    //  to initiate the ultrasonic burst
    digitalWrite(trigPin, LOW);
    delayMicroseconds(2);
    
    digitalWrite(trigPin, HIGH);
    delayMicroseconds(10);
    digitalWrite(trigPin, LOW);
    
    // read pulse length in microseconds on the Echo pin
    sample = pulseIn(echoPin, HIGH);
    
    // sample in microseconds converted to centimeters
    // 343 m/s speed of sound;  time divided by 2
    return sample/58.3;
  }

//Mapping function one range to another range
float mapFloat(float value, float fromLow, float fromHigh, float toLow, float toHigh) {
  return (value - fromLow) * (toHigh - toLow) / (fromHigh - fromLow) + toLow;
  }

///

/************************************************************/
//////////////////////////////Ta3refat///////////////////////
/************************************************************/

// The value will quickly become too large for an int to store
unsigned long previousMillis = 0;        
// Loop frequency: 100 ms
const long interval = 50;


//ISR for two encoders
void counter1(){
 
        pulses1 = pulses1 + left_direction;    
     
  }

void counter2(){
 
        pulses2 = pulses2 + right_direction;    
     
  }

////


//////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//Setting encoder pins as interrupts

void setup_wheelencoder()
  {
 
   pinMode(encoder_pinA, INPUT);
   attachInterrupt(digitalPinToInterrupt (encoder_pinA), counter1, RISING);
   pulses1 = 0;
   pinMode(encoder_pinB, INPUT);
   attachInterrupt(digitalPinToInterrupt (encoder_pinB), counter2, RISING);
   pulses2 = 0;
   
  }

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//Read IR values and publish
void update_IR()
  {
 
  float volts = analogRead(IR_PIN)*0.0048828125;  // value from sensor * (5/1024)
  float distance = 13*pow(volts, -1); // worked out from datasheet graph

  sharp_msg.data = distance;
  sharp_distance_pub.publish(&sharp_msg);
 
  }


//Read The motor and Publish
void update_Motor()
  {

  //If left speed is greater than zero
  if(l_speed >= 0)
  {
    digitalWrite (MotorA1, LOW);
    digitalWrite (MotorA2, HIGH);

    analogWrite(enableA,abs(l_speed));  

    left_direction = 1;
    
  }
  else
  {

    digitalWrite (MotorA1, HIGH);
    digitalWrite (MotorA2, LOW);

    analogWrite(enableA,abs(l_speed));    

    left_direction = -1;

    
  }

  if(r_speed >= 0)
  {

    digitalWrite (MotorB1, HIGH);
    digitalWrite (MotorB2, LOW);
    analogWrite(enableB,abs(r_speed));    

    right_direction = 1;

     
  }
  else
  {

    digitalWrite (MotorB1, LOW);
    digitalWrite (MotorB2, HIGH);
    analogWrite(enableB,abs(r_speed));    

    right_direction = -1;

   
  }
  

  
  }

/************************************************************/
//////////////////////////////VOID SETUP///////////////////////
/************************************************************/
void setup() {
  //Setting Serial1 and bluetooth as default serial port for communication via Bluetooth
  
  //nh.getHardware()->setPort(&Serial1);
  nh.getHardware()->setBaud(57600);

  pinMode (enableA, OUTPUT);
  pinMode (MotorA1, OUTPUT);
  pinMode (MotorA2, OUTPUT);  
   
  pinMode (enableB, OUTPUT);
  pinMode (MotorB1, OUTPUT);
  pinMode (MotorB2, OUTPUT); 
   
  pinMode(LED_BUILTIN, OUTPUT);  

  // set the digital I/O pin modes
  pinMode(echoPin, INPUT);
  pinMode(trigPin, OUTPUT);

  //Setup wheel encoders
  setup_wheelencoder();

  //Initialize ROS node
  nh.initNode();

  //Setup publisher
  nh.advertise(l_enc_pub);
  nh.advertise(r_enc_pub);
  nh.advertise(sharp_distance_pub);

  //Setup subscriber
  nh.subscribe(left_speed_sub);
  nh.subscribe(right_speed_sub);
  nh.subscribe(reset_sub);
  

  //ultrasonic
  nh.advertise(pub_range);

  // fill the description fields in the range_msg
  range_msg.radiation_type = sensor_msgs::Range::ULTRASOUND;
  range_msg.header.frame_id =  frameid;
  range_msg.field_of_view = 0.26;
  range_msg.min_range = minRange;
  range_msg.max_range = maxRange;
}

void loop() {
 unsigned long currentMillis = millis();

  if (currentMillis - previousMillis >= interval) 
  {
    previousMillis = currentMillis;

    l_encoder_msg.data = pulses1;
    r_encoder_msg.data = pulses2;

    l_enc_pub.publish(&l_encoder_msg);
    r_enc_pub.publish(&r_encoder_msg);

    update_IR();
  
  }

  update_Motor();

    // sample the range data from the ultrasound sensor and
  // publish the range value once every 50 milliseconds
  if ( (millis()-range_timer) > 50){
    range_msg.range = getRange();
    range_msg.header.stamp = nh.now();
    pub_range.publish(&range_msg);
    range_timer =  millis() + 50;
  }

  nh.spinOnce();

  delay(20);
}


