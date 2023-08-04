#!/bin/bash

b=10000
e=14990000
d=10000

for ((t = $b; t <= $e; t = $t+10000))
do
   let "tb=$t-$d"
   let "te=$t+$d"
   echo 2 | gmx clustsize -f dynamic.xtc -s dynamic.tpr -n system.ndx -cut 0.6 -pbc -mcn maxclust.ndx -b $tb -e $te > maxclust_$tb.xvg










   #fe=`grep Potential energy.out | awk '{print $6}'`
   #echo $t $fe >> freenrj.dat
   #rm energy.out energy.xvg
done

