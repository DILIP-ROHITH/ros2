import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, LogInfo
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration

def generate_launch_description():

    package_name = 'twowheel_drive'

    # Get the path to your custom world file
    world_file_path = os.path.join(
        get_package_share_directory(package_name),
        'world',
        'test.world'
    )

    # Path to your SLAM Toolbox parameter file
    slam_params_file = os.path.join(
        get_package_share_directory(package_name),
        'config',
        'mapper_params_online_async.yaml'
    )

    # Configure Gazebo to use your world
    use_sim_time = LaunchConfiguration('use_sim_time', default='true')

    disp = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            get_package_share_directory(package_name), 'launch', 'disp.launch.py'
        )]), launch_arguments={'use_sim_time': 'true'}.items()
    )

    # Include the Gazebo launch file, provided by the gazebo_ros package
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            get_package_share_directory('gazebo_ros'), 'launch', 'gazebo.launch.py'
        )]),
        launch_arguments={'world': world_file_path}.items()
    )

    # Run the spawner node from the gazebo_ros package
    spawn_entity = Node(
        package='gazebo_ros', 
        executable='spawn_entity.py',
        arguments=[
            '-topic', 'robot_description',
            '-entity', 'twowheel_drive'
        ],
        output='screen'
    )

    rviz_config_path = os.path.join(
        get_package_share_directory(package_name),
        "config",
        "drive.rviz",
    )

    rviz_node = Node(
        package="rviz2",
        executable="rviz2",
        name="rviz2",
        output="screen",
        arguments=["-d", rviz_config_path],
        parameters=[
            {'use_sim_time': use_sim_time},
        ],
    )

    teleop_info = LogInfo(
        msg="Gazebo and robot launched successfully! To control the robot, open a new terminal and run: ros2 run teleop_twist_keyboard teleop_twist_keyboard"
    )

    # Include SLAM Toolbox online_async_launch.py
    slam_toolbox = Node(
        parameters=[
        slam_params_file,
        {'use_sim_time': use_sim_time}
        ],
        package='slam_toolbox',
        executable='async_slam_toolbox_node',
        name='slam_toolbox',
        output='screen'
    )
    
    # Launch them all!
    return LaunchDescription([
        DeclareLaunchArgument(
            'use_sim_time',
            default_value='true',
            description='Use sim time if true'),
        disp,
        gazebo,
        spawn_entity,
        slam_toolbox,
        rviz_node,
        teleop_info,
    ])
