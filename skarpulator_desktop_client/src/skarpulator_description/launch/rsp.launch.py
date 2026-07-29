from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import Command, FindExecutable, LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node


def generate_launch_description():

    description_file = LaunchConfiguration('description_file')

    robot_description = Command([PathJoinSubstitution([
        FindExecutable(name='xacro')]),
        ' ',
        description_file
    ])

    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='both',
        parameters=[{
            'use_sim_time': True,
            'robot_description': robot_description
        }]
    )

    return LaunchDescription([
        DeclareLaunchArgument(
            'description_file',
            description='URDF/XACRO description file (absolute path) with the robot.'
        ),
        robot_state_publisher_node
    ])
