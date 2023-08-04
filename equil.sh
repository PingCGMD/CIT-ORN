# Equil 
gmx grompp -f equilibration.mdp -c minimization.gro -p system.top -o equilibration.tpr -n system.ndx
gmx mdrun -deffnm equilibration -v

