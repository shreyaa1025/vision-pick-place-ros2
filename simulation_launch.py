from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    perception = Node(
        package='vision_pick_place',
        executable='perception_node',
        name='perception_node',
        output='screen'
    )

    motion = Node(
        package='vision_pick_place',
        executable='motion_planner',
        name='motion_planner',
        output='screen'
    )

    gripper = Node(
        package='vision_pick_place',
        executable='gripper_control',
        name='gripper_controller',
        output='screen'
    )

    return LaunchDescription([
        perception,
        motion,
        gripper
    ])
