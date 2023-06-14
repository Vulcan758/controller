# controller
This is a controller package. Used as a controller for different kinds of robots

The cmd_2_wasd.py node converts cmd_vel messages to wasd string messages. I made this because the ROS-Mobile app sends cmd_vel messages from its joystick. The configuration I use for this specific node is I have a joystick, 2 buttons and a logger. One button publishes to /speed_increase and another button publishes to /speed_decrease. The logger is used to log the speed so that we can check the speed on the app.
