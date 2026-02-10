Vision-Based Pick and Place using ROS2

This project implements a simplified simulation pipeline for a robotic pick-and-place system.

Pipeline:
Camera → Object Detection → Pose Estimation → Motion Planning → Execution

Technologies:
ROS2
Gazebo
RViz
MoveIt2

Nodes:
perception_node – publishes detected object pose  
motion_planner – plans pick and place  
gripper_controller – controls gripper  

The system demonstrates task and motion planning pipeline using a simulated robot arm.
