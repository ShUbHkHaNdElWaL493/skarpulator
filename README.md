# skarpulator

This project aims to visualize a UR5e manipulator along with cubes and a container that will be used for pick-and-place using QR codes in an AR environment.

---

## Prerequisites
- Docker
- Android 8+

---

## Development
The development of this project consists of the following phases:
1. Creating a working digital twin of the manipulator using ROS2.
2. Handling how the computer will communicate with the app.
3. Creating an AR app for handling the projection of the manipulator, cube and container into the real world.
4. [Future] Transfering the full code into a single android app.
This is just a brief overview of how I am planning to develop the project.

---

## Progress
The following things have been done:
1. Creating a working digital twin of the manipulator using ROS2 and gz sim.
2. Launching the sim inside a container.
The following things need to be done next:
1. Connecting the container nodes with the base computer nodes.
2. Creating a MoveIt config for the robot.
3. Integrating the robot with MoveIt2.

---

## Contributions
If you want to contribute to this project, feel free to mail me.