import psutil
import os

process = psutil.Process(os.getpid())
print(str(process.memory_info().rss/100000))