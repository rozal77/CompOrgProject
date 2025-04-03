import time
 
 # ANSI escape codes for colors
 ANSI_COLOR_RED = "\x1b[31m"
 ANSI_COLOR_GREEN = "\x1b[32m"
 ANSI_COLOR_YELLOW = "\x1b[33m"
 ANSI_COLOR_RESET = "\x1b[0m"
 
 def main():
     total_time = 0
     dummy_value = 7
     res = 0
 
     # 10^10 additions (of integer constants)
     start = time.time()
     for i in range(100000):
         for j in range(100000):
             res = dummy_value + dummy_value
     end = time.time()
     total_time += end - start
      # 5 × 10^9 multiplication (of integer constants)
     start = time.time()
     for i in range(100000):
         for j in range(50000):
             res = dummy_value * dummy_value
     end = time.time()
     total_time += end - start
 
     # 2 × 10^9 division (of integer constants)
      start = time.time()
     for i in range(100000):
         for j in range(20000):
             res = dummy_value // dummy_value
     end = time.time()
     total_time += end - start
 
     # Print benchmarking data in different colors
     print(ANSI_COLOR_YELLOW + "Benchmark 1:" + ANSI_COLOR_RESET)
     print(ANSI_COLOR_GREEN + "32-bit Integer operation benchmark" + ANSI_COLOR_RESET)