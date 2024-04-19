@echo off
setlocal

set N_values=100, 1000, 10000, 100000, 1000000,10000000,100000000,1000000000,10000000000
for %%N in (%N_values%) do (
    mpiexec -n 24 python compute_pi_mpi.py %%N
)

endlocal
