#! /bin/bash
mkdir results
gfortran init_depth_eta_uvw.f -o a
./a
./nhwave
# mpirun -np 2 ./nhwave