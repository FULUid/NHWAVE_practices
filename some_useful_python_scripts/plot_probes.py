import sys
import numpy as np
import matplotlib.pyplot as plt

n_probes = 3

probe_series = np.arange(1, n_probes+1, step=1, dtype=int)

for i in probe_series:
    if i>=10 and i<100:
        filename_eta = "probe_00"+str(i)
        #filename_u = "u_000"+str(i)
        #filename_v = "v_000"+str(i)
    elif i>=100:
        filename_eta = "probe_0"+str(i)
        #filename_u = "u_00"+str(i)
        #filename_v = "v_00"+str(i)
    else:
        filename_eta = "probe_000"+str(i)
        #filename_u = "u_0000"+str(i)
        #filename_v = "v_0000"+str(i)
        
    probe_picname = "probe-eta-"+str(i)+".png";

    probe_data = np.loadtxt(filename_eta)
    time = probe_data[:,0]
    eta = probe_data[:,1]
    
    #u = np.loadtxt(filename_u)
    #v = np.loadtxt(filename_v)
    
    #depth = depth[0,:]
    #u = u[0,:]
    #v = v[0,:]
    
    fig, ax = plt.subplots()
    _ = ax.plot(time, eta, 'b-o', markersize=3)
    plt.xlabel('t')
    plt.ylabel('eta')
    plt.title("probe-"+str(i))
    plt.savefig(probe_picname) 
