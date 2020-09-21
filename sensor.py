from vec3 import Vec3

#just checking if i am able to run git properly
class Sensor:
    def __init__(self, x, y):
        # relative_pos = Vec3(x, y, 0)     # position relative to end effectors origin
        # global_pos =          [TODO]
        pass
    
    def dist(self, surface, direction):
        """
        computes distance of the sensor from the surface in the direction of the
        z-axis of the end effector using Ray marching algorithm.
        
        returns: (float) distance of the sensor from the surface.

        surface: is the representation of the surface [TODO]
        direction: (Vec3) z axis of the end effector wrt Global Coordinates.
        """
        pass
	pass

    def update_pos(self, dx, dy, dz):
        """
        updates the global position of the sensors.

        dx = (float) disp in global x direction
        dy = (float) disp in global y direction
        dz = (float) disp in global z direction
        """
        pass



    
    
