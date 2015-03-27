__author__ = 'David Rossiter'

from Sensors import sonar_reading

# Sensor Test

# Get sonar readings
fsd = sonar_reading("FSD")
rsd = sonar_reading("RSD")
lsd = sonar_reading("LSD")
bsd = sonar_reading("BSD")

print fsd
print rsd
print lsd
print bsd