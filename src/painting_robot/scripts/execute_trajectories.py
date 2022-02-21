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


def move_joints():
    group_variable_values[0] = 0
    group_variable_values[1] = -1.5
    group_variable_values[2] = 1.5
    group_variable_values[3] = 0
    group_variable_values[4] = 1.5
    group_variable_values[5] = 0
    group.set_joint_value_target(group_variable_values)

    plan2 = group.plan()
    group.go(wait=True)

    #rospy.sleep(5)

    # Calling `stop()` ensures that there is no residual movement
    #group.stop()

    # It is always good to clear your targets after planning with poses.
    # Note: there is no equivalent function for clear_joint_value_targets()
    #group.clear_pose_targets()
    #moveit_commander.roscpp_shutdown()
    
def move_to_goal_pose():

    print(group.get_current_pose().pose)

    pose_home = geometry_msgs.msg.Pose()
    pose_goal = geometry_msgs.msg.Pose()
    
    pose_home.orientation.x = 0.7071634004917629
    pose_home.orientation.y = 0.7070491820980549
    pose_home.orientation.z = 0.0008303231214725311
    pose_home.orientation.w = 0.0008304594585345758
    pose_home.position.x = 1.2222525667657456
    pose_home.position.y = 0.2559480623276811
    pose_home.position.z = 0.36641907140655205

    pose_goal.orientation.x = 0.707001
    pose_goal.orientation.y = 0.707001
    pose_goal.orientation.z = 0.000001
    pose_goal.orientation.w = 0.000001
    pose_goal.position.x = 1.184001
    pose_goal.position.y = 0.256001
    pose_goal.position.z = 0.012001

    #group.set_pose_target(pose_goal)
    group.set_approximate_joint_value_target(pose_goal, "arm_ee_link")
    #group.set_goal_orientation_tolerance(0.1)
    group.set_goal_tolerance(1)

    ## Now, we call the planner to compute the plan and execute it.
    plan = group.go(wait=True)
    print(group.get_current_pose().pose)
    # Calling `stop()` ensures that there is no residual movement
    group.stop()

    # It is always good to clear your targets after planning with poses.
    # Note: there is no equivalent function for clear_joint_value_targets()
    #group.clear_pose_targets()
    #moveit_commander.roscpp_shutdown()
    
def move_via_waypoints():
    scale = 0.5
    waypoints = []
    wpose = group.get_current_pose().pose
    print(wpose)
    #wpose.position.z -= scale * 0.5  # First move up (z)
    #waypoints.append(copy.deepcopy(wpose))

    #wpose.position.z += scale * 0.5  # First move up (z)
    #waypoints.append(copy.deepcopy(wpose))
    
    #wpose.position.y -= scale * 0.5  # and sideways (y)
    #waypoints.append(copy.deepcopy(wpose))

    #wpose.position.y += scale * 0.5  # and sideways (y)
    #waypoints.append(copy.deepcopy(wpose))

    #wpose.position.x += scale * 0.5  # Second move forward/backwards in (x)
    #waypoints.append(copy.deepcopy(wpose))

    #wpose.position.x -= scale * 0.5  # Second move forward/backwards in (x)
    #waypoints.append(copy.deepcopy(wpose))

    for i in range(10):
        for i in range(5):
            wpose.position.y -= scale * 0.3  # and sideways (y)
            waypoints.append(copy.deepcopy(wpose))
        
        wpose.position.z -= scale * 0.05  # move down (z)
        waypoints.append(copy.deepcopy(wpose))
        
        for i in range(5):
            wpose.position.y += scale * 0.3  # and sideways (y)
            waypoints.append(copy.deepcopy(wpose))
        
        wpose.position.z -= scale * 0.05  # move down (z)
        waypoints.append(copy.deepcopy(wpose))

    # We want the Cartesian path to be interpolated at a resolution of 1 cm
    # which is why we will specify 0.01 as the eef_step in Cartesian
    # translation.  We will disable the jump threshold by setting it to 0.0 disabling:
    (plan, fraction) = group.compute_cartesian_path(waypoints,0.01,0.0)
    group.execute(plan, wait=True)

    # Calling `stop()` ensures that there is no residual movement
    #group.stop()

    # It is always good to clear your targets after planning with poses.
    # Note: there is no equivalent function for clear_joint_value_targets()
    #group.clear_pose_targets()
    #moveit_commander.roscpp_shutdown()

def initialize():
    move_joints()

def shutdown():
    # Calling `stop()` ensures that there is no residual movement
    group.stop()

    # It is always good to clear your targets after planning with poses.
    # Note: there is no equivalent function for clear_joint_value_targets()
    group.clear_pose_targets()
    moveit_commander.roscpp_shutdown()

def main():
    #move_joints()

    #move_to_goal_pose()
    move_via_waypoints()
    initialize()
    shutdown()
 
if __name__ == '__main__':
    initialize()
    main()
