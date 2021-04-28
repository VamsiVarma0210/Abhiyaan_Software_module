#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def callback(data):
    print(data.data,end="")
    #print the messages after the listener program ends(same line).
    
def listener():
    print()
    rospy.init_node('listener', anonymous=True)
    #initialising node listener

    rospy.Subscriber("team_abhiyaan",String,callback)
    #Subscribing to topic team_abhiyaan
    rospy.Subscriber("autonomy",String,callback)
    #Subscribing to topic autonomy
    rospy.spin()
if __name__=='__main__':
   listener()
