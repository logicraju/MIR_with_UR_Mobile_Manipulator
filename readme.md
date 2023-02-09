### Abstract
------------
In this project, a simple zig-zag movement comprising of a sequence of linear and circular moves is generated to paint a surface. The painting is performed by a mobile manipulator (which comprises of a mobile robot, MIR100 and a robotic manipulator, UR10 mounted on top) using the pilz motion planner. Here, we use a mobile manipulator . We can control the manipulator using pilz motion planner in Moveit platform. The avaialble motion planners in Moveit generate random trajectories every time its executed for the same starting and goal points. This causes uncertainty while using these planners. Pilz provides generation of predictable trajectories using simple motion commands such as LIN, CIRC etc for linear, circular movements respectively. There is also an option for grouping together various kinds of movements as a sequence and executing one by one. The movements can be generated and executed either manually using the moveit rviz plugin or programmatically using python api. For more information regarding the motion planner, visit the following link:

https://ros-planning.github.io/moveit_tutorials/doc/pilz_industrial_motion_planner/pilz_industrial_motion_planner.html


### Video Link
--------------
https://youtu.be/iLDIrMVe6z4


### Dependencies
----------------
Install dependencies using the command:

1. Open a terminal
2. Navigate to the workspace root
3. rosdep install --from-paths src --ignore-src -r -y


### How to run
--------------
1. roslaunch painting_robot painting_robot_moveit.launch
2. rosrun painting_robot pilz_zigzag.py



### Contact Us
--------------
ThunDroids LLP  
54/69A, Kumaranasan Road,  
Kadavanthra PO,  
Cochin 20  
Phone: +919656609215  
Email: thundroids@gmail.com  

OR

QboticsLabs  
Address: Door No. 8/428, Kurumassery, Kochi, Kerala 683579  
Phone: +918907590702  
https://qboticslabs.com/  
