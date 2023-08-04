#!/bin/bash


echo 2 | gmx clustsize -f dynamic.xtc -s dynamic.tpr -mc maxclust.xvg -ac avcluste.xvg -nc nclust.xvg -cut 0.6 -n system.ndx -pbc


