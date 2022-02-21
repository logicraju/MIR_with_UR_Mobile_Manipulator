#!/usr/bin/env python3
from geometry_msgs.msg import Pose, Point
from pilz_robot_programming import *
import math
import rospy

__REQUIRED_API_VERSION__ = "1"    # API version
__ROBOT_VELOCITY__ = 0.5          # velocity of the robot

# main program
def start_program():

    rospy.loginfo("Program started") # log

    # important positions
    start_pos = [1.49, -0.54, 1.09, 0.05, 0.91,-1.67]   # joint values

    pick_pose = Pose(position=Point (0, -0.5, 0.25), orientation=from_euler(0, math.radians(180), math.radians(0))) # cartesian coordinates
    work_station_pose = Pose(position=Point(-0.5, 0.1, 0.2) , orientation=from_euler(0, math.radians(-135), math.radians(90)))  # cartesian coordinates
    place_pose = Pose(position=Point(-0.1,0.4,0.25) , orientation=from_euler(0, math.radians(180),  math.radians(90))) # cartesian coordinates
    
  
    # move to start point with joint values to avoid random trajectory
    r.move(Ptp(goal=start_pos, vel_scale=__ROBOT_VELOCITY__))

    rospy.loginfo("Start loop") # log
    #while(True):
        # do infinite loop

        # pick the PNOZ
    rospy.loginfo("Move to pick position") # log
    r.move(Ptp(goal=pick_pose, vel_scale = __ROBOT_VELOCITY__, relative=False))
    rospy.loginfo("Pick movement") # log


if __name__ == "__main__":
    # init a rosnode
    rospy.init_node('robot_program_node')
    # initialisation
    r = Robot(__REQUIRED_API_VERSION__)  # instance of the robot
    # start the main program
    start_program()
