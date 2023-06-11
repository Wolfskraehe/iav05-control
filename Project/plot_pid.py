import os
import pandas as pd
import matplotlib.pyplot as plt

def read_steer_data():
 steer_file = 'steer_pid_data.txt'
 steer_df = pd.read_csv(steer_file, delim_whitespace = True, header = None, usecols = [0, 1, 2])
 steer_df.columns = ['Iteration', 'Error Steering', 'Steering Output']
 print(f'Steer data:\n{steer_df.head()}\n')
 return steer_df


def read_throttle_data():
 throttle_file = 'throttle_pid_data.txt'
 throttle_df = pd.read_csv(throttle_file, delim_whitespace = True, header = None, usecols = [0, 1, 2, 3])
 throttle_df.columns = ['Iteration', 'Error Throttle', 'Brake Output', 'Throttle Output']
 print(f'Throttle data:\n{throttle_df.head()}\n')
 return throttle_df


def plot_steer_data(steer_df, n_rows):   
 steer_df2 = steer_df[:n_rows]
 steer_df2.plot(x = steer_df.columns[0], y = [steer_df.columns[1], steer_df.columns[2]], kind = 'line')
 plt.show()
 
    
def plot_throttle_data(throttle_df, n_rows):   
 throttle_df2 = throttle_df[:n_rows]
 throttle_df2.plot(throttle_df.columns[0],throttle_df.columns[2])
 throttle_df2.plot(throttle_df.columns[0],throttle_df.columns[1])
 plt.show()
 
    
def main():
  PATH = os.path.dirname(os.path.abspath(__file__))
  control_df = pd.read_csv(f"{PATH}/control_log.csv")
  
  # plot steering
  fig, ax = plt.subplots(2,2)
  control_df.plot(y=["desired_heading", "heading"], ax=ax[0][0])
  control_df.plot(y=["steer_output"], ax=ax[1][0])
  
  ax[0][0].grid()
  ax[0][0].set_title(r"$\psi$")
  ax[0][0].set_ylabel("rad")
  ax[1][0].grid()
  ax[1][0].set_title(r"$\delta$")
  ax[1][0].set_ylabel("rad")

  # Plot throttle
  control_df.plot(y=["desired_velocity", "velocity"], ax=ax[0][1])
  control_df.plot(y=["throttle_output"], ax=ax[1][1])
  ax[0][1].grid()
  ax[0][1].set_title("Vehicles velocity")
  ax[0][1].set_ylabel("m/s")
  ax[1][1].grid()
  ax[1][1].set_title("Throttle command")
  fig.tight_layout()
  plt.show()
    
if __name__ == '__main__':
    main()
