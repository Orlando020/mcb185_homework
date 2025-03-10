import sys
import mcb185
import itertools
#python3 52kmercount.py ../MCB185/data/GCF_000005845.2ASM584v2_genomic.fan.gz 5
k = int(sys.argv[2])
kcount = {}
for defline, seq in mcb185.read_fasta(sys.argv[1]):
    for i in range(len(seq)-k+1):
        kmer = seq[i:i+k]
        if kmer not in kcount: kcount[kmer] = 0
        kcount[kmer] += 1
# for kmer, n in kcount.items(): print(kmer,n)
for nts in itertools.product('ACGT', repeat = k):
    kmer = ''.join(nts)
    if kmer in kcount: print(kmer,kcount[kmer])
    else:              print(kmer, 0)