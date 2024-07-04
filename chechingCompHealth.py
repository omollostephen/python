import shutil #checking diskusage
import psutil #checking cpu usage

#checking diskusage
#du = shutil.disk_usage("/")
#print(du.free/du.total*100)
#print(du)

def check_disk_usage(disk):
    du = shutil.disk_usage(disk)
    free = du.free/du.total*100
    return free>20

#checking cpu usage
# cpu = psutil.cpu_percent(0.1)
# print("Cpu: ",cpu)
def check_cpu_usage():
    usage = psutil.cpu_percent(1)
    return usage<75

if not check_disk_usage or not check_cpu_usage:
    print("Error!!!")
else:
    print("Everything is as expected")