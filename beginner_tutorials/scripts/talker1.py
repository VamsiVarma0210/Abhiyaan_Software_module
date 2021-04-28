#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
def talker1():
       pub=rospy.Publisher("/team_abhiyaan",String,queue_size=10)
       rospy.init_node('talker1',anonymous=True)
       
       talker1_str=String()
       
       talker1_str.data="Team Abhiyaan:"
       
       rospy.loginfo(talker1_str)
       pub.publish(talker1_str)
       
if __name__=='__main__':
   try:
      talker1()
   except rospy.ROSInterruptException:
      pass
