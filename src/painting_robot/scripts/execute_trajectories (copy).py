#! /usr/bin/env python3

import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg

moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('move_group_python_interface_tutorial', anonymous=True)

robot = moveit_commander.RobotCommander()
scene = moveit_commander.PlanningSceneInterface()    
group = moveit_commander.MoveGroupCommander("manipulator")
display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path', moveit_msgs.msg.DisplayTrajectory)

group_variable_values = group.get_current_joint_values()

group_variable_values[0] = 0
group_variable_values[1] = 0
group_variable_values[3] = -1.5
group_variable_values[4] = 1.5
group.set_joint_value_target(group_variable_values)

plan2 = group.plan()
group.go(wait=True)

rospy.sleep(5)

moveit_commander.roscpp_shutdown()
