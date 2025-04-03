import os
 import time
 
 # ANSI escape codes for colors
 ANSI_COLOR_RED = "\x1b[31m"
 ANSI_COLOR_GREEN = "\x1b[32m"
 ANSI_COLOR_YELLOW = "\x1b[33m"
 ANSI_COLOR_RESET = "\x1b[0m"
 
 def main():
     total_file_size = 1000000000
     one_time_size = 100
     total_time = 0
 
     # Write 10^9 bytes to a file, 100 bytes each time
     with open("dummyOneBillionBytes.txt", "wb") as output_file_handler:
         start = time.time()
         output_buffer = bytearray(b'A' * one_time_size)
         bytes_written_so_far = 0
 
         while bytes_written_so_far < total_file_size:
             output_file_handler.write(output_buffer)
             bytes_written_so_far += one_time_size
 
         end = time.time()
         total_time = end - start
         # Read a whole file of 10^9 bytes, 100 bytes each time
     with open("dummyOneBillionBytes.txt", "rb") as input_file_handler:
         start = time.time()
         input_buffer = bytearray(one_time_size)
 
         while input_file_handler.readinto(input_buffer) == one_time_size:
             pass
 
         end = time.time()
         total_time += end - start
 
     # Print benchmarking data in different colors
      print(ANSI_COLOR_YELLOW + "Benchmark 4:" + ANSI_COLOR_RESET)
     print(ANSI_COLOR_GREEN + "Hard Drive benchmark 1" + ANSI_COLOR_RESET)
     print(ANSI_COLOR_RED + f"Which includes reading from, and writing to file, 100 bytes each time is: {total_time} seconds" + ANSI_COLOR_RESET)
 
     # Delete the file after benchmarking
     os.remove("dummyOneBillionBytes.txt")
 
 if __name__ == "__main__":
     main()