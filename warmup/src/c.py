"""
time: 00:03:00
"""
line = input()

hod_dog_count = int(line.split(' ')[0])
participants = int(line.split(' ')[1])

print ("%.2f" % (hod_dog_count / participants))