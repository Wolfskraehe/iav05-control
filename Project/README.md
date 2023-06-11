# Project Instructions

In this project, you will have to design a PID controller that can effectively track a vehicle's trajectory. You will be provided with a trajectory represented as an array of locations, as well as a simulation environment that includes the vehicle and possible perturbations.

To accomplish this, you are required to design and implement a PID controller. You will also need to integrate this controller with the CARLA simulator, which is widely used in the industry.

Your deliverable for this project will include the code for the PID controller, along with detailed explanations of how you selected the controller's parameters. Additionally, you are expected to provide a thorough analysis of the simulation results, demonstrating the efficiency of your controller.

Please ensure that you followed the [installation](../Installation/) procedures before running the this project.

To successfully complete this project, please follow the outlined steps:

- Design the PID (Proportional - Integral - Derivative) controller.
- Integrate the PID controller with the CARLA simulator.
- Utilize appropriate techniques to fine-tune the controller's parameters.
- Develop a comprehensive strategy to thoroughly test the performance of your controller.
- Generate plots that visually illustrate the effectiveness of the controller, and include a video of the simulator to support your analysis.
- Discuss any noteworthy instances of the controller's recovery or other relevant observations.

## Instructions

To enhance the overall scope of the course, we will incorporate the path planning algorithms developed in Project 4 into this assignment. By doing so, we aim to build upon the previous project and further develop the steer and throttle controllers necessary for effectively following the calculated path.

You can access the relevant files in the [controllers](./controllers/) directory, specifically the [PIDController.py](./controllers/PIDController.py) files. This is where you will implement your PID controller. The function "pid" is called within [SimulatorAPI.py](./SimulatorAPI.py). Your primary objective is to successfully complete the following steps:

### Step 1: Build the PID controller object

Complete the TODO in the [PIDController.py](./controllers/PIDController.py)

Run the simulator and see in the desktop mode the car in the CARLA simulator. Take a screenshot and add it to your report. The car should not move in the simulation.

You can use the [test_PID.ipynb](./controllers/test_PID.ipynb) to check if you PID is working. The behaviour of the PID should be the same as the one provided in the examples. 

### Step 2: PID controller for throttle :

In [SimulatorAPI.py](./SimulatorAPI.py) (line 881), complete the TODO to compute the error for the throttle pid. The error is the speed difference between the actual speed and the desired speed.

Useful variables:

- The last point of **v_points** vector contains the velocity computed by the path planner.
- velocity contains the actual velocity.
- The output of the controller should be inside [-1, 1].

- Comment your code to explain why you computed the error the way you did.

- Tune the parameters of the pid until you get satisfying results (a perfect trajectory is not expected).

### Step 3: PID controller for steer:

1. In [SimulatorAPI.py](./SimulatorAPI.py) (line 886), complete the TODO to compute the error for the steer pid. The error is the angle difference between the actual steer and the desired steer to reach the planned position.

Useful variables:

- The variable y_points and x_point gives the desired trajectory planned by the path_planner.
- yaw gives the actual rotational angle of the car.
- The output of the controller should be inside [-1.2, 1.2].
- If needed, the position of the car is stored in the variables **x_position**, **y_position** and **z_position**

2. Comment your code to explain why you computed the error the way you did.

3. Tune the parameters of the pid until you get satisfying results (a perfect trajectory is not expected).

### Step 4: Evaluate the PID efficiency

The values of the error and the pid command are saved in thottle_data.txt and steer_data.txt. Plot the saved values using the command

```
python3 plot_pid.py
```

Tips:

- When you wil be testing your code, restart the Carla simulator to remove the former car from the simulation.
- If the simulation freezes on the desktop mode but is still running on the terminal, close the desktop and restart it.

---
## Running whole project

After completition of the code, you can check that the project is running by running the simulator. For this you need to:

1. Run CARLA 
2. Run [SimulatorAPI.py](./SimulatorAPI.py)

```
python SimulartorAPI.py
```

You should see a car moving in the simulator. The project will be considered correct if the car is able to:

- Avoid the 3 obstacles.

Note that the whole turning is not expected. Just reaching to the first intersection is considered as success.

---
## Submission Template


The submission must be done in a zip file containing the implemented code and a report in a **PDF** with the following specifications:

### Project Overview

This section should contain a brief description of the project and what you are trying to achieve.

### Set up

This section should contain a brief description of the steps to follow to run the code. There must be a detailed explanation of how to run the implemented code so we can see run them on our local machine.

### Controllers

This section should describe the PID controller, specifically:

- Brief explanation of what is control?.
- Explanation of PID controllers.
- Explanation of each component. 
- Explanation of the code.
- Explanation of your tunning procedure.

### Analysis

This section should include a extensive analysis of the whole program, including most important iterations of the tunning process. Explain how each component affects the controlled car, benefits and disadvantages of using the PID.

Please note that your report should be in PDF format, and your submission should include the implemented code and any additional materials necessary for us to replicate your results.

Please commence the project promptly and ensure that all aspects of the assignment are completed within the designated timeframe. Should you encounter any difficulties or require clarification, do not hesitate to reach out to me for assistance. Best of luck with your project!

Good luck with your task! 🚀👍

