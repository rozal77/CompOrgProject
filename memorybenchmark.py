import numpy as np
 import time
 
 # ANSI escape codes for colors
 ANSI_COLOR_RED = "\x1b[31m"
 ANSI_COLOR_GREEN = "\x1b[32m"
 ANSI_COLOR_YELLOW = "\x1b[33m"
 ANSI_COLOR_RESET = "\x1b[0m"
 
 def main():
     # Create a NumPy array with the desired size
     my_arr = np.zeros(500000000)
     dummy_read_value = 0
     total_time = 0
 
     start = time.time()
 
     # Write to 5 × 10^9 different array elements, 4 bytes each time
     for i in range(len(my_arr)):
         my_arr[i] = i
 
     # Read from 5 × 10^9 different array elements, 4 bytes each time
     for i in range(len(my_arr)):
         dummy_read_value = my_arr[i]