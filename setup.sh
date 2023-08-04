gmx editconf -f system.pdb -o system.gro -d 1.0 -bt cubic -box 25.2 25.2 25.2

#minim-vac
gmx grompp -f minimization-vac.mdp -c system.gro -p system.top -o minimization-vac.tpr

gmx mdrun -deffnm minimization-vac -v

#add water
gmx solvate -cp minimization-vac.gro -cs water.gro -radius 0.21 -o system_W.gro

#add Ions
gmx grompp -f ions.mdp -c system_W.gro -p system.top -o ions.tpr

gmx genion -s ions.tpr  -p system.top  -neutral -conc 0.15 -pname NA+ -nname CL- -o system_WI.gro 






