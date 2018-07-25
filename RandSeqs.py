#! /usr/bin/env python
import sys, math, os, argparse, csv, random
csv.field_size_limit(sys.maxsize)

base_dict = {0:'A', 1:'C', 2:'G', 3:'T'}
for i in range(1000):
    filename = 'Randseq_'+str(i)+'.fasta'
    seq = open(filename, 'w')
    seq.write('> '+filename+'\n')

    for len in range(random.randint(200000,4000000)):
        k = random.randint(0,3)
        seq.write(base_dict[k])

    seq.close

    os.system("/home/alan/applications/ShortRepeatAnalysis.py -w 14 "+filename)
    os.system("rm Randseq*.fasta")
    os.system("rm *_rep_counts.txt")
    os.system("rm *_rep_table*")
#os.system("cat Rand*binned.txt > All_rands_binned.txt")
#os.system("rm Randseq*binned.txt")



        
    

