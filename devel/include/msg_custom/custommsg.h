// Generated by gencpp from file msg_custom/custommsg.msg
// DO NOT EDIT!


#ifndef MSG_CUSTOM_MESSAGE_CUSTOMMSG_H
#define MSG_CUSTOM_MESSAGE_CUSTOMMSG_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace msg_custom
{
template <class ContainerAllocator>
struct custommsg_
{
  typedef custommsg_<ContainerAllocator> Type;

  custommsg_()
    : id(0)
    , name()
    , temperature(0.0)
    , humidity(0.0)  {
    }
  custommsg_(const ContainerAllocator& _alloc)
    : id(0)
    , name(_alloc)
    , temperature(0.0)
    , humidity(0.0)  {
  (void)_alloc;
    }



   typedef int32_t _id_type;
  _id_type id;

   typedef std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> _name_type;
  _name_type name;

   typedef float _temperature_type;
  _temperature_type temperature;

   typedef float _humidity_type;
  _humidity_type humidity;





  typedef boost::shared_ptr< ::msg_custom::custommsg_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::msg_custom::custommsg_<ContainerAllocator> const> ConstPtr;

}; // struct custommsg_

typedef ::msg_custom::custommsg_<std::allocator<void> > custommsg;

typedef boost::shared_ptr< ::msg_custom::custommsg > custommsgPtr;
typedef boost::shared_ptr< ::msg_custom::custommsg const> custommsgConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::msg_custom::custommsg_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::msg_custom::custommsg_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::msg_custom::custommsg_<ContainerAllocator1> & lhs, const ::msg_custom::custommsg_<ContainerAllocator2> & rhs)
{
  return lhs.id == rhs.id &&
    lhs.name == rhs.name &&
    lhs.temperature == rhs.temperature &&
    lhs.humidity == rhs.humidity;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::msg_custom::custommsg_<ContainerAllocator1> & lhs, const ::msg_custom::custommsg_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace msg_custom

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::msg_custom::custommsg_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::msg_custom::custommsg_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::msg_custom::custommsg_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::msg_custom::custommsg_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::msg_custom::custommsg_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::msg_custom::custommsg_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::msg_custom::custommsg_<ContainerAllocator> >
{
  static const char* value()
  {
    return "16767b4b63fd3551b69c6c06672a0bf6";
  }

  static const char* value(const ::msg_custom::custommsg_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x16767b4b63fd3551ULL;
  static const uint64_t static_value2 = 0xb69c6c06672a0bf6ULL;
};

template<class ContainerAllocator>
struct DataType< ::msg_custom::custommsg_<ContainerAllocator> >
{
  static const char* value()
  {
    return "msg_custom/custommsg";
  }

  static const char* value(const ::msg_custom::custommsg_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::msg_custom::custommsg_<ContainerAllocator> >
{
  static const char* value()
  {
    return "int32 id\n"
"string name\n"
"float32 temperature\n"
"float32 humidity\n"
;
  }

  static const char* value(const ::msg_custom::custommsg_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::msg_custom::custommsg_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.id);
      stream.next(m.name);
      stream.next(m.temperature);
      stream.next(m.humidity);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct custommsg_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::msg_custom::custommsg_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::msg_custom::custommsg_<ContainerAllocator>& v)
  {
    s << indent << "id: ";
    Printer<int32_t>::stream(s, indent + "  ", v.id);
    s << indent << "name: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>>::stream(s, indent + "  ", v.name);
    s << indent << "temperature: ";
    Printer<float>::stream(s, indent + "  ", v.temperature);
    s << indent << "humidity: ";
    Printer<float>::stream(s, indent + "  ", v.humidity);
  }
};

} // namespace message_operations
} // namespace ros

#endif // MSG_CUSTOM_MESSAGE_CUSTOMMSG_H
