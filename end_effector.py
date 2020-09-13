from sensor import Sensor
import numpy as np

class End_eff:
    def __init__(self):     # and some more arguments later.[TODO]
        # self.pos          # global
        # self.orientation      # orientation will hold a transformation matrix.
        sensor_array = np.array((3, 3), dtype=Sensor)
        pass

    def move(self, ds):
        """
        moves the end effector in the given direction ds

        ds: (float, float, float) a tuple of floats of (x, y, z) direction 
        """
        pass

    
    
    def rotate(self, dtheta):
        """
        rotate the end effctor to assume correct orientation and update it.

        dtheta: either angle or Vec3(theta_x, theta_y, theta_z)
        """
        pass
    
    def dist_array(self):   # should take surface as an input?[TODO]
        """
        returns: numpy array(3x3) containing the distance to each sensor from
        the surface
        """
        pass
    



