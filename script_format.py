#!/usr/bin/env python
import os 
liste_name = ["PEG114_PolyOC_seq_ratio_90_177_23_8a_80.itp","PEG114_PolyOC_seq_ratio_90_713_23_8a_80.itp", "PEG114_PolyOC_seq_ratio_90_208_23_2a_80.itp","PEG114_PolyOC_seq_ratio_90_728_23_9a_80.itp","PEG114_PolyOC_seq_ratio_90_240_23_6a_80.itp","PEG114_PolyOC_seq_ratio_90_777_23_4a_80.itp", "PEG114_PolyOC_seq_ratio_90_255_23_3a_80.itp","PEG114_PolyOC_seq_ratio_90_816_23_7a_80.itp", "PEG114_PolyOC_seq_ratio_90_294_23_3a_80.itp", "PEG114_PolyOC_seq_ratio_90_85_23_4a_80.itp", "PEG114_PolyOC_seq_ratio_90_322_23_4a_80.itp", "PEG114_PolyOC_seq_ratio_90_857_23_5a_80.itp", "PEG114_PolyOC_seq_ratio_90_336_23_0a_80.itp", "PEG114_PolyOC_seq_ratio_90_897_23_1a_80.itp", "PEG114_PolyOC_seq_ratio_90_350_23_0a_80.itp", "PEG114_PolyOC_seq_ratio_90_910_23_7a_80.itp", "PEG114_PolyOC_seq_ratio_90_428_23_8a_80.itp", "PEG114_PolyOC_seq_ratio_90_924_23_4a_80.itp", "PEG114_PolyOC_seq_ratio_90_525_23_9a_80.itp", "PEG114_PolyOC_seq_ratio_90_936_23_0a_80.itp", "PEG114_PolyOC_seq_ratio_90_531_23_1a_80.itp", "PEG114_PolyOC_seq_ratio_90_950_23_1a_80.itp", "PEG114_PolyOC_seq_ratio_90_537_23_5a_80.itp", "PEG114_PolyOC_seq_ratio_90_962_23_4a_80.itp"]

for i in liste_name:
    fichier = open("/home/ping/Non_bonded_Prodrug/PEG_Orn_Cit/PEG114_ORN_CIT_old/" + i, "r")
    lines = fichier.readlines()
    
    for line in lines:
        if '    1    P2     1   CIT    BB     1  0.0000 ; C' in line:
            seq = i.split(".")[0]
            out = i+"_edit" 
            name = seq+"_edit"
            os.system("sed -i '708,1329 !column -t' {}".format(i,seq,out,name))

#os.system("polyply gen_coords -p system.top -o PEG_Orn_Cit.gro -name PEG_Orn_Cit -box 25 25 25") 


    
