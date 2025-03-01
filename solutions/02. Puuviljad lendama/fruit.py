# TODO: Add the first element (with index 0) of the trajectory to the fruit's
#       X-coordinate (self.x) and the second element of of the trajectory
#       to the fruit's Y-coordinate (self.y). Also, replace the trajectory
#       with an updated one, where the first element remains unchanged, but
#       GRAVITY gets added to the second one 
self.x += self.trajectory[0]
self.y += self.trajectory[1]
self.trajectory = (self.trajectory[0], self.trajectory[1] + GRAVITY)
