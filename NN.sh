#!/bin/bash

b=1000
e=7000000
d=1000
rm NN*.dat

for ((t = $b; t <= $e; t = $t+1000))
do
   let "tb=$t-$d"
   let "te=$t"
        
   file=./NM_$te

   for num in $(<"$file"); do
       if ((num>4176)); then 
	       paste -d' ' <(echo "$te") <(echo "$((num/348-1/348))") <(echo "$((24-num/348+1/348))") >> NN.dat
	    
       fi
   done 
   
done

