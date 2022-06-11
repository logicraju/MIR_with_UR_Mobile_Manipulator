#!/usr/bin/env python3
from geometry_msgs.msg import Pose, Point
from pilz_robot_programming import *
import math
import rospy
import copy

__REQUIRED_API_VERSION__ = "1"
__ROBOT_VELOCITY__ = 0.3
__ROBOT_ACC__ = 0.1

RELATIVE_VALUE_Y = 0.0
RELATIVE_VALUE_Z = 0.0
STEPS_COUNT_Y = 1
STEPS_COUNT_Z = 5
STEP_SIZE_Y = 0.5
STEP_SIZE_Z = 0.05
CIRCLE_RADIUS = STEP_SIZE_Z/2

def goto_zero_pose():
    zero_pos = [0, 0, 0, 0, 0, 0]   # joint values
    r.move(Ptp(goal=zero_pos, vel_scale=__ROBOT_VELOCITY__, reference_frame="arm_base_link"))

def initialize():
    global STEPS_COUNT_Y, STEPS_COUNT_Z, STEP_SIZE_Y, STEP_SIZE_Z
    start_pos = [0, -1.5, 1.5, 0, 1.5, 0]   # joint values
    r.move(Ptp(goal=start_pos, vel_scale=__ROBOT_VELOCITY__, reference_frame="arm_base_link"))

# main program
def start_program():
    global RELATIVE_VALUE_Y, RELATIVE_VALUE_Z, STEPS_COUNT_Y, STEPS_COUNT_Z, STEP_SIZE_Y, STEP_SIZE_Z
    # Blend sequence
    blend_sequence = Sequence()

    try:
        r.move(Ptp(goal=Pose(position=Point(0, (STEP_SIZE_Y*STEPS_COUNT_Y)/2, 0)), vel_scale=__ROBOT_VELOCITY__, acc_scale=__ROBOT_ACC__, reference_frame="arm_ee_link", relative=True))
        for j in range(STEPS_COUNT_Z):
            for i in range(STEPS_COUNT_Y):
                current_pose_old = r.get_current_pose()
                RELATIVE_VALUE_Y = RELATIVE_VALUE_Y - STEP_SIZE_Y # move sideways (y)
                blend_sequence.append(Lin(goal=Pose(position=Point(0, RELATIVE_VALUE_Y, RELATIVE_VALUE_Z)), vel_scale=__ROBOT_VELOCITY__, acc_scale=__ROBOT_ACC__, reference_frame="arm_ee_link", relative=True))
            RELATIVE_VALUE_Z = RELATIVE_VALUE_Z + STEP_SIZE_Z # move down (z)
            blend_sequence.append(Circ(goal=Pose(position=Point(0, RELATIVE_VALUE_Y, RELATIVE_VALUE_Z)), center=Point(0, RELATIVE_VALUE_Y+CIRCLE_RADIUS, RELATIVE_VALUE_Z-CIRCLE_RADIUS), reference_frame="arm_ee_link"))
            
            for i in range(STEPS_COUNT_Y):
                RELATIVE_VALUE_Y = RELATIVE_VALUE_Y + STEP_SIZE_Y # move sideways (y)
                blend_sequence.append(Lin(goal=Pose(position=Point(0, RELATIVE_VALUE_Y, RELATIVE_VALUE_Z)), vel_scale=__ROBOT_VELOCITY__, acc_scale=__ROBOT_ACC__, reference_frame="arm_ee_link", relative=True))
            RELATIVE_VALUE_Z = RELATIVE_VALUE_Z + STEP_SIZE_Z # move down (z)
            blend_sequence.append(Circ(goal=Pose(position=Point(0, RELATIVE_VALUE_Y, RELATIVE_VALUE_Z)), center=Point(0, RELATIVE_VALUE_Y-CIRCLE_RADIUS, RELATIVE_VALUE_Z-CIRCLE_RADIUS), reference_frame="arm_ee_link"))
        r.move(blend_sequence)
    except RobotMoveFailed:
        rospy.loginfo("Command failed ...")
    except Exception as e:
        print("Exception: " + str(e))

if __name__ == "__main__":
    rospy.init_node('robot_program_node')
    r = Robot(__REQUIRED_API_VERSION__)
    initialize()
    start_program()
    #goto_zero_pose()
    exit(0)
