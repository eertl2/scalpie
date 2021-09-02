#Default values
PRINT_TO_CONSOLE = True
PRINT_TO_LOGS = True
PRINT_SCREENSHOT = True
MAX_THREADS = 2
MAX_RETRYS_PER_TASK = 1
MIN_REFRESH_TIME = 3
MAX_REFRESH_TIME = 5
HIDE_CHROME = False
GUEST = True

def str2bool(v):
  return v.lower() in ("true")

#Open user-details.txt
lines = {}
try:
    f = open("glv.txt", "r")
    if f:
        for line in f:
            split = line.strip().split("=")
            split[0] = split[0].strip()
            split[1] = split[1].strip()

            if split[0] == "PRINT_TO_CONSOLE":
                PRINT_TO_CONSOLE = str2bool(split[1])
            if split[0] == "PRINT_TO_LOGS":
                PRINT_TO_LOGS = str2bool(split[1])
            if split[0] == "PRINT_SCREENSHOT":
                PRINT_SCREENSHOT = str2bool(split[1])
            if split[0] == "MAX_THREADS":
                MAX_THREADS = int(split[1])
            if split[0] == "MAX_RETRYS_PER_TASK":
                MAX_RETRYS_PER_TASK = int(split[1])
            if split[0] == "MIN_REFRESH_TIME":
                MIN_REFRESH_TIME = int(split[1])
            if split[0] == "MAX_REFRESH_TIME":
                MAX_REFRESH_TIME = int(split[1])
            if split[0] == "HIDE_CHROME":
                HIDE_CHROME = str2bool(split[1])
            if split[0] == "GUEST":
                GUEST = str2bool(split[1])
        f.close()
        
except FileNotFoundError:
    print("glv.txt cannot be found. Continuing with default glv settings.")
    
