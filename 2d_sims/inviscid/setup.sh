#! /bin/bash
mkdir results
gfortran init_depth_eta_uvw.F -o a
./a
mpirun -np 2 ./nhwave
