import numpy as np
import cv2
from scipy.interpolate import interp1d, RegularGridInterpolator

class VelocityModel2D:
    def __init__(self, nx, nz, dx, dz, x0, z0, initial_vel=0) -> None:
        
        self.data = np.ones((nx, nz))*initial_vel
        self.x_coords = np.arange(x0, x0+nx*dx, dx)
        self.z_coords = np.arange(z0, z0+nz*dz, dz)        
        
    # Add a layer defined by 2 arrays of picks. Pick is [Xidx, Zidx] if indexes=True and (X, Z) if indexes=False
    # To get boundary, picks are interpolated and extrapolated to reach X extent
    def add_Vconst_layer(self, upper_boundary_picks, lower_boundary_picks, vel, indexes=True):
        if not indexes:
            # recalculate to indexes
            upper_boundary_picks = np.array([[np.round(ubp[:,0])/self.dx-self.x_coords[0], np.round(ubp[:,1]/self.dz)-self.z_coords[0]] for ubp in upper_boundary_picks])
        
        interpolator = interp1d(upper_boundary_picks[:,0], upper_boundary_picks[:,1], fill_value='extrapolate')     
        ubz = interpolator(np.arange(self.data.shape[0])).astype('int')     
        interpolator = interp1d(lower_boundary_picks[:,0], lower_boundary_picks[:,1], fill_value='extrapolate')  
        lbz = interpolator(np.arange(self.data.shape[0])).astype('int')
       
        for i, x in enumerate(self.x_coords):            
            self.data[i, ubz[i]:lbz[i]+1] = vel
        

    
