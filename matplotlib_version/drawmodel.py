import matplotlib.pyplot as plt
import numpy as np
import sys
sys.path.append('..')
from lib.model import VelocityModel2D


def show_model(title, last=False):      
           
    plt.figure(figsize=(14,10))
    
    fignums = plt.get_fignums() 
    if len(fignums) > 1:
        plt.close(fignums[1])
    plt.title(title)
    plt.imshow(model.data.T, aspect='auto')   
    if last:
        plt.colorbar()
   


def pick_boundary(title):
    show_model(title)    
    picks = plt.ginput(n=-1, timeout=5000)  
    plt.show()  
    return np.array(picks)

plt.ion()

model = VelocityModel2D(401, 201, 10, 10, 0, 0, 1600)
n_boundaries = 3
upper_picks = np.array([[0,0], [200, 0]])
for n in range(n_boundaries):    
    lower_picks = pick_boundary(f"Bottom of layer {n}")
    
    model.add_Vconst_layer(upper_picks, lower_picks, 1600+(n+1)*100)
    upper_picks = lower_picks
show_model('Final Model', True)
plt.waitforbuttonpress()

