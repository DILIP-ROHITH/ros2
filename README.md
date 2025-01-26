1. Install ROS2 - HUMBLE , GAZEBO and necessary packages to use the files
2. Create a folder named ros2_ws in your system and create directory named src in it
3. Download the folders from here and move them to src directory
4. open terminal and type "cd ~/ros2_ws"
5. Enter comand "colcon build" 
6. Now open your ros2_ws folder and you can see 3 other folders created apart from src (build, log, install)
7. Now open terminal again and enter command "source install/setup.bash"
8. Next enter the command "ros2 launch twowheel_drive gazebo_model.launch.py" - and you can see a gazebo window is opened
9. Click on it you can see a "TWO WHEEL DIFFERENTIAL ROBOT"
10. Open the terminal again and click on new tab this time make sure that terminal stays on top
11. Enter the command "ros2 run teleop_twist_keyboard teleop_twist_keyboard"
12. Now you can control the robot with the command provided by teleop keyboard
13. To stop the process press ctrl+c in both terminals
14. To run the other project that is nave_base_description
15. Enetr "cd ~/ros2_ws" and next "source install/setup.bash"
16. Next enter "ros2 launch nav_base_description gazebo.launch.py"
17. And then you can follow the same process 10 -13

(Note make sure you intstall teleop package to contol the model using your pc)
