gmx grompp -f dynamic.mdp -c equilibration.gro -p system.top -o dynamic.tpr -n system.ndx

gmx mdrun -deffnm dynamic -v

