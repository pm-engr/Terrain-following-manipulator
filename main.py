
from end_effector import End_eff
from constants import *
from vec3 import Vec3 
import numpy as np
   
# initial setup i.e. setting up end effectors initial orientation and position.
pos = ORIGIN
end_effector = End_eff()
path_dir = Vec3(1, 0, 0)    # direction of the path that the end effector has to travel.
steps = 0

while(steps < MAX_STEPS):
    # taking distance data from the sensors.
    sensor_dist = end_effector.dist_array()     # this currently shows error because of empty function body.

    # main algo to compute the required movement. 
    (disp, theta) = algo(end_effector)          # something like this...[TODO]    

    if (disp > MIN_ds and theta > MIN_dtheta):
        # adjust the end effectors position and orientation
        end_effector.move(disp)
        end_effector.rotate(theta)
    else:
        # move the end effector on the path 
        end_effector.move(path_dir)
        steps += 1




