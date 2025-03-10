import argparse

#in posititional arguemnts
#python3 53dust.py -h

# parser = argparse.ArgumentParser(description='DNA entropy filter')
# parser.add_argument('file', type=str, help='name of fasta file')
# parser.add_argument('size', type=int, help='window size')
# parser.add_argument('entropy', type=float, help ='entropy threshold')
# arg = parser.parse_args()
# print('dusting with', arg.file, arg.size, arg.entropy)




#with defaults and stuff
#python3 53dust.py ../MCB185/data/GCF_000005845.2_ASM584v2_genomic.fna.gz --size 15 --entropy 1.2


# parser = argparse.ArgumentParser(description='DNA entropy filter')
# parser.add_argument('file', type=str, help='name of fasta file')
# parser.add_argument('--size',type=int,default=20,help='window size [%(default)i]')
# parser.add_argument('--entropy', type=float, help ='entropy threshold[%(default).3f]')
# arg = parser.parse_args()
# print('dusting with', arg.file, arg.size, arg.entropy)

#with flages and abbrev
#python3 53dust.py ../MCB185/data/GCF_000005845.2_ASM584v2_genomic.fna.gz --size 15 --entropy 1.2 --lower

parser = argparse.ArgumentParser(description='DNA entropy filter.')
parser.add_argument('file', type=str, help='name of fasta file')
parser.add_argument('-s','--size', type=int, default=20,
    help='window size [%(default)i]')
parser.add_argument('-e','--entropy', type=float, default=1.4,
    help='entropy threshold [%(default).3f]')
parser.add_argument('--lower', action='store_true', help='soft mask')
arg = parser.parse_args()
print('dusting with', arg.file, arg.size, arg.entropy, arg.lower)


#dust was window and shannon plogp , seq in and n seq out

import sys
import mcb185
import math

window = int(arg.size)
thresh = arg.entropy

# exseq = 'AAAAAAAAAAACGATCACTACGTACTGACGTAGCTAGCTGATCGATGCTGACTGATCGATCGTACGATCGATCGATCGATCGTACTAGCTAG'
 # time python3 53dust.py ../MCB185/data/C.elegans.fa.gz --size 20 --entropy 1.2 --lower
# this command works but trying to do it with ecoli will an unkown amount of time, need better way of writing over a string, size of string greatly extends time
for defline, seq in mcb185.read_fasta(sys.argv[1]):
    print(defline[:30])
    ndna = seq
    # print(len(seq))
    for i in range(0, len(seq)):
        windstr = seq[i:i+window]
        shannon = 0
        nucleo = {}
        for ntp in windstr:
            if ntp not in nucleo: nucleo[ntp] = 0
            nucleo[ntp]+=1
        for k, v in nucleo.items():
            plogp = -(v/window)*(math.log(v/window))
            shannon += plogp
        if shannon < thresh:
            ndna = ndna[0:i] + 'N'*window + ndna[i+window:]
            # print(ndna[0:40])
        
    print(ndna)
    
# debug section
# string = 'AAAAAAACGATCACTACGTA'
# string = 'AAAAAACGATCACTACGTAC'
# dico = {}
# shann = 0
# for ntp in string:
    # if ntp not in dico: dico[ntp] = 0
    # dico[ntp] += 1
# for k, v in dico.items():
    # plogp = -(v/window)*(math.log(v/window))
    # shann += plogp
    # print(shann, len(string))
    
