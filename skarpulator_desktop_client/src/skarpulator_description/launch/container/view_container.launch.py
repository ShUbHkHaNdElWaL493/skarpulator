from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import Command, FindExecutable, LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():

    rviz_config = LaunchConfiguration('rviz_config')

    robot_description = Command([
        PathJoinSubstitution([FindExecutable(name='xacro')]),
        ' ',
        PathJoinSubstitution([
            FindPackageShare('skarpulator_description'),
            'models',
            'container.urdf.xacro'
        ]),
        ' ',
        'origin_xyz:=',
        '"0 0 0"',
        ' ',
        'origin_rpy:=',
        '"0 0 0"',
    ])

    rsp_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='both',
        parameters=[{
            'use_sim_time': True,
            'robot_description': robot_description
        }]
    )

    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='log',
        arguments=['-d', rviz_config]
    )

    joint_state_publisher_node = Node(
        package='joint_state_publisher',
        executable='joint_state_publisher',
        name='joint_state_publisher'
    )

    return LaunchDescription([
        DeclareLaunchArgument(
            'rviz_config',
            default_value=PathJoinSubstitution([
                FindPackageShare('skarpulator_description'),
                'rviz',
                'view.rviz'
            ]),
            description='Rviz config file (absolute path) to use when launching rviz.'
        ),
        rsp_node,
        rviz_node,
        joint_state_publisher_node
    ])
