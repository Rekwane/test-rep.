# We are going to use the psutil command to format a script to check these items.  cpu times, cpu percentatge, disk partion's, users and net connections.  
# You may have to do some extra modification to make the ouput be more readable.


import psutil

def cpu_times_info():
    cpu_times = psutil.cpu_times()
    print("\ncpu times:")
    print(f"User: {cpu_times.user} seconds")
    print(f"System: {cpu_times.system} seconds")
    print(f"Idle: {cpu_times.idle} seconds")
    print(f"Nice: {cpu_times.nice} seconds")
cpu_times_info()

def partitions_info():
    partitions = psutil.disk_partitions()
    print("\nDisk Partitions:")
    print(f"Device: {disk_partitions.device}")
partitions_info()
