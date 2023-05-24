import psutil

print('RAM memory % used:', psutil.virtual_memory()[2])
print('RAM Used (GB):', psutil.virtual_memory()[3]/100000000)
