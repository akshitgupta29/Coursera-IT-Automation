#!/usr/bin/python3
import psutil
import shutil


print (shutil.disk_usage('/'))
print (shutil.disk_usage('/').free)
print (shutil.disk_usage('/').used)
print (psutil.cpu_percent(1.0))