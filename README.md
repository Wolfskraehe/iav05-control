Decision and Path Planning Module
=============================

This directory presents an  opportunity for students to immerse themselves in the realm of control systems, fostering invaluable hands-on experience in the design, implementation, and rigorous testing of control algorithms. By actively engaging in this project, participants will cultivate a profound comprehension of fundamental control principles, while acquiring practical skills that can be readily deployed across diverse industries and applications.

---

## Repository File Structure

📦Decision and Path planning module<br>
 ┣ 📂.devcontainer --> Contains the configuration of the development container for those who are using docker <br>
 ┃<br>
 ┣ 📂Exercises--> Contains examples of the modules discussed in the lesson. <br> 
 ┃ ┣ Vehicle_Model.ipynb --> Example implementation of the kinematic bycicle model for vehicles. <br>
 ┃ ┣ PID.ipynb --> Example implementation of a PID. <br>
 ┃ ┗ MPC.ipynb --> Example implemenation of an MPC for Autonomous Vehicles. <br> 
 ┃ <br>
 ┣ 📂Installation --> Contains the installation instruction for both linux and windows<br>
 ┃ ┣ Installation_win.md  <br>
 ┃ ┗ Installation_linux.md  
 ┃ <br>
 ┣ 📂Project<br>
 ┃ ┣ 📂planners <br>
 ┃ ┃ ┣  BehavioralPlannerFSM.py --> Behevioral planner algorithm<br>
 ┃ ┃ ┣  cost_functions.py --> Cost functions for calculated paths<br>
 ┃ ┃ ┣  CubicSpiral.py --> Algorithm to generate cubic spirals<br>
 ┃ ┃ ┣  MotionPlanner.py --> Motion planner algorithm<br>
 ┃ ┃ ┣  PathPlanner.py --> Module that generate the paths in the simulation<br>
 ┃ ┃ ┣  PlanningParams.py --> General Parameters for the algorithms<br>
 ┃ ┃ ┣  SpiralBase.py --> Base spiral generater<br>
 ┃ ┃ ┣  SpiralEquations.py --> Main equations to generate the spirals<br>
 ┃ ┃ ┣  Structures.py --> Data structures used for the algorithms<br>
 ┃ ┃ ┣  utils.py --> Utility functions for the path planning algorithm<br>
 ┃ ┃ ┗  VelocityProfileGenerator.py --> Algorithms to generate the velocity profile for each maneuver<br>
 ┃ ┃ <br>
 ┃ ┣ 📂controllers <br>
 ┃ ┃ ┗ PID.py --> Main PID control module <br>
 ┃ ┃<br>
 ┃ ┣ 📂PythonAPI -->  <br>
 ┃ ┃ ┣  📂carla --> Carla Binary files<br>
 ┃ ┃ ┣  📂examples --> Carla Examples<br>
 ┃ ┃ ┗  📂util --> Carla utility functions<br>
 ┃ ┃<br>
 ┃ ┃ SimulatorAPI.py -->  Main API to interact with the simulation<br>
 ┃ ┗ PerfectControl.py --> Script that runs the simulation assuming perfect control of the vehicle<br>
 ┃<br>
 ┣ Dockerfile --> Dockerfile to generate the devcontainer <br>
 ┣ requirements.txt --> General requirements for the project<br>
 ┗ run_carla.sh --> Script to run carla under **UBUNTU** <br>

---
## Installation

We have provided a set of instructions to install all the necessary requirements for the course in the [installation](./Installation/) directory. To ensure a seamless installation process, please follow the instructions that correspond to your operating system.

* [windows](./Installation/Installation_win.md)
* [linux](./Installation/Installation_linux.md)
---
## Project Instructions

The instructions for the project pertaining to this module are compiled within the [README.md](./Project/README.md
) file with the [Project](./Project/) directory. Please read them carefully and be sure to follow them closely.Once the project is complete, submit it to Moodle as a **zip** file that includes this repository. If you want to reduce the size of your submission, feel free to delete the **PythonAPI** directory.

---
## Disclaimer

If you are taking the course Introduction to Autonomous Vehicles and encounter any issues with the setup or tasks, please reach out to your instructors as soon as possible. They are there to help you and want to ensure you have a smooth and successful learning experience. Don't hesitate to ask them any questions you may have, and they will provide you with the support you need.


Good luck with your task! 🚀👍