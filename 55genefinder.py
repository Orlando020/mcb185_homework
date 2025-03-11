import sequence
import mcb185
import argparse
import sys

# frame = 0 #0 1or 2 it does not look like gff files bother with frame just start and end
#NC_000913.3     RefSeq  CDS     190     255     .       +       0

def seq_to_codingregion(seq, frame,minimum_ORF):
    protseq = mcb185.translate(seq, frame)
    protdict = dict()#string and coord
    for ntp in range(len(protseq)):
        for i in range(len(protseq)-ntp):
            if protseq[ntp] != 'M': break
            if protseq[ntp+i] == '*' and i >= minimum_ORF/3:
                # print(protseq[ntp:ntp+40])
                protdict[ntp] = ntp+i+1
                break
            elif protseq[ntp+i] == '*':
                break
    return protdict

parser = argparse.ArgumentParser(description='Gene Finder, Fasta to Gff')
parser.add_argument('fasta', type=str, help='name of fasta file')
parser.add_argument('--minimumORFlength', type=int,default=300, help='Minimum size to be considered a coding sequence [%(default)i]')
arg = parser.parse_args()

for defline, seq in mcb185.read_fasta(arg.fasta):
    for framm in range(3):
        fowdict = seq_to_codingregion(seq, framm, arg.minimumORFlength)
        for k,v in fowdict.items():
            print(defline[0:12],'   ','55genefinder.py','   ','CDS','   ',k,'   ',v,'   ','+','   ',0)
    revseq = sequence.revcomp(seq)
    for framm in range(3):
        revdict = seq_to_codingregion(revseq, framm, arg.minimumORFlength)
        seqlen = len(seq)
        for k,v in revdict.items():
            print(defline[0:12],'   ','55genefinder.py','   ','CDS','   ',seqlen-k-1,'   ',seqlen-v-1,'   ','-','   ',0)