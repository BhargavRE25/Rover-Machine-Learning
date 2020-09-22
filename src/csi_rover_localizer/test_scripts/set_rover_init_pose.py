#!/usr/bin/env python

import rospy
import rospkg
from gazebo_msgs.msg import ModelState
from gazebo_msgs.srv import SetModelState


def main():
    rospy.init_node('set_rover_init_pose')

    state_msg = ModelState()
    state_msg.model_name = 'scout_1'
    state_msg.pose.position.x = -60
    state_msg.pose.position.y = -52
    state_msg.pose.position.z = 3.0
    state_msg.pose.orientation.x = 0
    state_msg.pose.orientation.y = 0
    state_msg.pose.orientation.z = 0
    state_msg.pose.orientation.w = 0

    rospy.wait_for_service('/gazebo/set_model_state')
    try:
        set_state = rospy.ServiceProxy('/gazebo/set_model_state', SetModelState)
        resp = set_state(state_msg)
        print(resp)

    except rospy.ServiceException, e:
        print "Service call failed: %s" % e


if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
