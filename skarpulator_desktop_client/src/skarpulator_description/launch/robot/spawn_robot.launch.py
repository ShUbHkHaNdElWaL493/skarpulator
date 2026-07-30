from launch import LaunchDescription
from launch.substitutions import Command, FindExecutable, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():

    robot_description = Command([
        PathJoinSubstitution([FindExecutable(name='xacro')]),
        ' ',
        PathJoinSubstitution([
            FindPackageShare('skarpulator_description'),
            'models',
            'robot.urdf.xacro'
        ])
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

    entity_spawner_node = Node(
        package='ros_gz_sim',
        executable='create',
        output='screen',
        arguments=[
            '-name',
            'ur',
            '-topic',
            'robot_description',
            '-allow_renaming',
            'true'
        ],
    )

    joint_state_broadcaster_spawner_node = Node(
        package='controller_manager',
        executable='spawner',
        arguments=['joint_state_broadcaster', '-c', '/controller_manager']
    )

    joint_controller_spawner_node = Node(
        package='controller_manager',
        executable='spawner',
        arguments=['scaled_joint_trajectory_controller', '-c', '/controller_manager']
    )

    gripper_controller_spawner_node = Node(
        package='controller_manager',
        executable='spawner',
        arguments=['robotiq_gripper_controller', '-c', '/controller_manager']
    )

    return LaunchDescription([
        rsp_node,
        entity_spawner_node,
        joint_state_broadcaster_spawner_node,
        joint_controller_spawner_node,
        gripper_controller_spawner_node
    ])
