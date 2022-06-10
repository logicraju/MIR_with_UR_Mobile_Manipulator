#!/usr/bin/env python3
from geometry_msgs.msg import Pose, Point
from pilz_robot_programming import *
import math
import rospy
import copy

__REQUIRED_API_VERSION__ = "1"
__ROBOT_VELOCITY__ = 0.5
__ROBOT_ACC__ = 0.5

def initialize():
    rospy.set_param('truth', True)
    cartesian_limits:
  max_trans_vel: 1
  max_trans_acc: 2.25
  max_trans_dec: -5
  max_rot_vel: 1.57
    start_pos = [0, -1.5, 1.5, 0, 1.5, 0]   # joint values
    #r.move(Lin(goal=start_pos, vel_scale=__ROBOT_VELOCITY__))
    r.move(Ptp(goal=start_pos, vel_scale=__ROBOT_VELOCITY__))
# main program
def start_program():

    # Blend sequence
    blend_sequence = Sequence()
    scale = 1.0
    current_pose = r.get_current_pose()
    #print("current_pose: " + str(current_pose.position))
    
    try:

        for i in range(10):
            for i in range(10):
                new_pose = copy.deepcopy(current_pose)
                new_pose.position.y -= scale * 0.5  # and sideways (y)
                #blend_sequence.append(Ptp(goal=Pose(position=new_pose.position), relative=False, vel_scale=__ROBOT_VELOCITY__, acc_scale=__ROBOT_ACC__))
                blend_sequence.append(Lin(goal=Pose(position=new_pose.position), vel_scale=__ROBOT_VELOCITY__, relative=False))
                print("new_pose: " + str(new_pose.position))
            new_pose.position.z -= scale * 0.1  # move down (z)
            #blend_sequence.append(Ptp(goal=Pose(position=new_pose.position), relative=False, vel_scale=__ROBOT_VELOCITY__, acc_scale=__ROBOT_ACC__))
            blend_sequence.append(Lin(goal=Pose(position=new_pose.position), vel_scale=__ROBOT_VELOCITY__, relative=False))
            print("new_pose: " + str(new_pose.position))
            
            for i in range(10):
                new_pose = copy.deepcopy(current_pose)
                new_pose.position.y += scale * 0.5  # and sideways (y)
                #blend_sequence.append(Ptp(goal=Pose(position=new_pose.position), relative=False, vel_scale=__ROBOT_VELOCITY__, acc_scale=__ROBOT_ACC__))
                blend_sequence.append(Lin(goal=Pose(position=new_pose.position), vel_scale=__ROBOT_VELOCITY__, relative=False))
                print("new_pose: " + str(new_pose.position))
            new_pose.position.z -= scale * 0.1  # move down (z)
            #blend_sequence.append(Ptp(goal=Pose(position=new_pose.position), relative=False, vel_scale=__ROBOT_VELOCITY__, acc_scale=__ROBOT_ACC__))
            blend_sequence.append(Lin(goal=Pose(position=new_pose.position), vel_scale=__ROBOT_VELOCITY__, relative=False))
            print("new_pose: " + str(new_pose.position))

        r.move(blend_sequence)
    except Exception as e:
        print("Exception: " + str(e))
if __name__ == "__main__":
    rospy.init_node('robot_program_node')
    r = Robot(__REQUIRED_API_VERSION__)
    initialize()
    start_program()
    initialize()
    exit(0)
