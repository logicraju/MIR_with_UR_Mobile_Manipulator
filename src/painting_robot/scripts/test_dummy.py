#!/usr/bin/env python3
from geometry_msgs.msg import Pose, Point
import rospy
import copy

# main program
def start_program():
    current_pose = Pose()
    current_pose.position.x = 1
    current_pose.position.y = 2
    current_pose.position.z = 3

    new_pose = copy.deepcopy(current_pose)
    new_pose.position.y += 5

    print("Current Pose:" + str(current_pose))
    print("New Pose:" + str(new_pose))

if __name__ == "__main__":
    # init a rosnode
    rospy.init_node('robot_program_node')
    start_program()
