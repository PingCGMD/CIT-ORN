#!/usr/bin/env python

file_to_process = open("volume.dat","r")
corrected_file = open("volume_condense.dat","w")
dilute_file = open("volume_dilute.dat","w")
all_volume = open("volume_all.dat","w")
lines = file_to_process.readlines()

for line in lines:

    if line == "\n":
        continue

    else:
        corrected_file.write(line)
        list_line=line.split()
        str_to_write=list_line[0]+" {}\n".format(14760.21368-float(list_line[1]))
        all_to_write=list_line[0]+" {}".format(list_line[1])+" {}\n".format(16117.58758-float(list_line[1]))
        dilute_file.write(str_to_write)
        all_volume.write(all_to_write)



