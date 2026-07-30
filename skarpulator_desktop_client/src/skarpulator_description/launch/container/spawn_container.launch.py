from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import Command, FindExecutable, LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():

    x = LaunchConfiguration('x')
    y = LaunchConfiguration('y')
    z = LaunchConfiguration('z')
    rx = LaunchConfiguration('rx')
    ry = LaunchConfiguration('ry')
    rz = LaunchConfiguration('rz')

    robot_description = Command([
        PathJoinSubstitution([FindExecutable(name='xacro')]),
        ' ',
        PathJoinSubstitution([
            FindPackageShare('skarpulator_description'),
            'models',
            'container.urdf.xacro'
        ]),
        ' ',
        'origin_xyz:="',
        x, ' ', y, ' ', z,
        '" ',
        'origin_rpy:="',
        rx, ' ', ry, ' ', rz,
        '"'
    ])

    rsp_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='both',
        parameters=[{
            'use_sim_time': True,
            'robot_description': robot_description
        }],
        remappings=[('/robot_description', '/container_description')]
    )

    entity_spawner_node = Node(
        package='ros_gz_sim',
        executable='create',
        output='screen',
        arguments=[
            '-name',
            'container',
            '-topic',
            'container_description'
        ],
    )

    return LaunchDescription([
        DeclareLaunchArgument(
            'x',
            default_value='0.0',
            description='Origin x co-ordinate',
        ),
        DeclareLaunchArgument(
            'y',
            default_value='0.0',
            description='Origin y co-ordinate',
        ),
        DeclareLaunchArgument(
            'z',
            default_value='0.0',
            description='Origin z co-ordinate',
        ),
        DeclareLaunchArgument(
            'rx',
            default_value='0.0',
            description='Origin rx co-ordinate',
        ),
        DeclareLaunchArgument(
            'ry',
            default_value='0.0',
            description='Origin ry co-ordinate',
        ),
        DeclareLaunchArgument(
            'rz',
            default_value='0.0',
            description='Origin rz co-ordinate',
        ),
        rsp_node,
        entity_spawner_node
    ])
