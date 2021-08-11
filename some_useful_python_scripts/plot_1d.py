import sys
import numpy as np
import matplotlib.pyplot as plt

file_interval = 1
file_start = 1
file_end = 25+file_interval

dx = 0.01
m = 1000

x = np.asarray([float(xa+0.50)*dx for xa in range(m)])

output_series = np.arange(file_start, file_end, step=file_interval, dtype=int)

for i in output_series:
    if i>=10 and i<100:
        filename_eta = "eta_000"+str(i)
        #filename_u = "u_000"+str(i)
        #filename_v = "v_000"+str(i)
    elif i>=100:
        filename_eta = "eta_00"+str(i)
        #filename_u = "u_00"+str(i)
        #filename_v = "v_00"+str(i)
    else:
        filename_eta = "eta_0000"+str(i)
        #filename_u = "u_0000"+str(i)
        #filename_v = "v_0000"+str(i)
        
    eta_picname = "eta-"+str(i)+".png";

    eta = np.loadtxt(filename_eta)
    depth = np.loadtxt('depth')
    total_depth = depth+eta
    
    #u = np.loadtxt(filename_u)
    #v = np.loadtxt(filename_v)
    
    #depth = depth[0,:]
    #u = u[0,:]
    #v = v[0,:]
    
    fig, ax = plt.subplots()
    _ = ax.plot(x, total_depth, 'b-o', markersize=3)
    plt.xlabel('x')
    plt.ylabel('eta+h')
    plt.savefig(eta_picname)
    plt.close(fig)
