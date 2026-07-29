from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():

    world = LaunchConfiguration('world')

    gz_node = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(PathJoinSubstitution([
            FindPackageShare('ros_gz_sim'),
            'launch',
            'gz_sim.launch.py'
        ])),
        launch_arguments={
            'gz_args': [
                '-r -s -v4 ', world,
                ' --physics-engine gz-physics-bullet-featherstone-plugin'
            ]
        }.items(),
    )

    rsp_node = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(PathJoinSubstitution([
            FindPackageShare('skarpulator_description'),
            'launch',
            'rsp.launch.py'
        ])),
        launch_arguments={
            'description_file': PathJoinSubstitution([
                FindPackageShare('skarpulator_description'),
                'models',
                'robot.urdf.xacro'
            ])
        }.items(),
    )

    ros_gz_bridge_node = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        arguments=[
            '/clock@rosgraph_msgs/msg/Clock[gz.msgs.Clock',
        ],
        output='screen',
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
        DeclareLaunchArgument(
            'world',
            default_value='empty.sdf',
            description='Gazebo world file containing a custom world.',
        ),
        gz_node,
        rsp_node,
        ros_gz_bridge_node,
        entity_spawner_node,
        joint_state_broadcaster_spawner_node,
        joint_controller_spawner_node,
        gripper_controller_spawner_node
    ])
