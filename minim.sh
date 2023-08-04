
gmx grompp -f minimization.mdp -c system_WI.gro -p system.top -o minimization.tpr 

gmx mdrun -deffnm minimization -v
.
