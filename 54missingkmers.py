import mcb185
import sys
import itertools
import sequence

for defline, seq in mcb185.read_fasta(sys.argv[1]):
    k = 1
    kmerlist = []
    kfound = False
    revseq = sequence.revcomp(seq)
    while not kfound:
        k += 1
        for nts in itertools.product('ACGT', repeat = k):
            kmer = ''.join(nts)
            if kmer not in seq and kmer not in revseq:
                kfound = True
                kmerlist.append(kmer)
    print(kmerlist,len(kmerlist),k)

# for nts in itertools.product('ACGT', repeat = k):
    # kmer = ''.join(nts)
    # if kmer in kcount: print(kmer,kcount[kmer])
    # else:              print(kmer, 0)
    