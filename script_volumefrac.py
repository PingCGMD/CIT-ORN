#!/usr/bin/env python

file_to_process = open("volume.dat","r")
file_to_NMchain = open("NN.dat","r")
corrected_file = open("volume_condense.dat","w")
dilute_file = open("volume_dilute.dat","w")
all_volume = open("volume_all.dat","w")
fraction_condense = open("volume_fraction_condense","w")
fraction_dilute = open("volume_fraction_dilute","w")
all_fraction = open("volume_fraction_all.xvg","w")

lines1 = file_to_process.readlines()
lines2 = file_to_NMchain.readlines()

for line in lines1:

    if line == "\n":
        continue

    else: 
        corrected_file.write(line)
        list_line=line.split()
        
        for line2 in lines2:
            list_line2=line2.split()
            #print (list_line[0],list_line2[0]) 
            
            if int(round(float(list_line[0]),0)) == int(list_line2[0]):
                output1_line2=float(list_line2[1])
                output2_line2=float(list_line2[2])
                break
        

        str_to_write=list_line[0]+" {}\n".format(14756.60365-float(list_line[1]))
        all_to_write=list_line[0]+" {}".format(list_line[1])+" {}".format(14756.60365-float(list_line[1]))+ " {}".format(21.22*output1_line2/float(list_line[1]))+" {}\n".format(21.22*output2_line2/(14756.60365-float(list_line[1])))
        fraction_condense_to_write=list_line[0]+" {}\n".format(21.22*output1_line2/float(list_line[1]))
        fraction_dilute_to_write=list_line[0]+" {}\n".format(21.22*output2_line2/(14756.60365-float(list_line[1])))
        all_fraction_to_write=list_line[0]+" {}".format(21.22*output1_line2/float(list_line[1]))+" {}\n".format(21.22*output2_line2/(14756.60365-float(list_line[1])))

        dilute_file.write(str_to_write)
        all_volume.write(all_to_write)
        fraction_condense.write(fraction_condense_to_write)
        fraction_dilute.write(fraction_dilute_to_write)
        all_fraction.write(all_fraction_to_write)



