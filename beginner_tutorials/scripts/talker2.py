#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
def talker2():
       pub=rospy.Publisher("/autonomy",String,queue_size=10)
       rospy.init_node('talker2',anonymous=True)

       talker2_str=String()
       
       talker2_str.data="fueled by autonomy."
       
       rospy.loginfo(talker2_str)
       pub.publish(talker2_str)

if __name__=='__main__':
   try:
      talker2()
   except rospy.ROSInterruptException:
      pass
