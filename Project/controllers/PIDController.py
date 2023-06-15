class PIDController:
    """
    A Proportional-Integral-Derivative (PID) Controller class.

    Args:
        Kp (float): Proportional gain.
        Ki (float): Integral gain.
        Kd (float): Derivative gain.
        output_max (float): Maximum output value.
        output_min (float): Minimum output value.

    Attributes:
        Kp (float): Proportional gain.
        Ki (float): Integral gain.
        Kd (float): Derivative gain.
        output_max (float): Maximum output value.
        output_min (float): Minimum output value.
        prev_error (float): Previous error value.
        accumulative_error (float): Accumulated error value.

    Methods:
        get_control_command: Calculates the control command based on the current error.

    """

    def __init__(self, Kp:float, Ki:float, Kd:float, output_min:float, output_max:float):
        """
        Initialize the PIDController with the specified gains and output limits.

        Args:
            Kp (float): Proportional gain.
            Ki (float): Integral gain.
            Kd (float): Derivative gain.
            output_max (float): Maximum output value.
            output_min (float): Minimum output value.
        """
        # TODO Populate the PID Class, you can name
        # your variables as you see fit.

        # Constants
        
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd

        # Limits
        self.output_max = output_max
        self.output_min = output_min
        
        # relevant errors

        self.prev_error = 0.0
        self.acummulative_error = 0.0

        
    
    def get_control_command(self, current_error: float, dt:float)-> float:
        """
        Calculate the control command based on the current error and time difference.

        Args:
            current_error (float): The current error value.
            dt (float): The time difference since the last control command.

        Returns:
            float: The calculated control command.
        """
        # TODO Calculate control command, remember to cap your control command
        # in the range of [-output_max, output_max]
        
        if dt > 0.00:
            derivative_term = (current_error - self.prev_error)/dt
        else:
            derivative_term = 0.0
            
        self.acummulative_error += current_error*dt
        self.prev_error = current_error
        command = self.Kp*current_error + self.Ki*self.acummulative_error + self.Kd*derivative_term
        if command > self.output_max:
            return self.output_max
        elif command < self.output_min:
            return self.output_min
        else:
            return command
        # return max(min(command, self.output_max), self.output_min)