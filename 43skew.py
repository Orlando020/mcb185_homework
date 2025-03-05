import sequence
import mcb185
import sys
# seq = 'ACGTACGTGGGGGACGTACGTCCCCC'

w = 1000

for defline, seq in mcb185.read_fasta(sys.argv[1]):
    print(defline[:30], seq[:40], len(seq)) 
    for i in range(len(seq)-w+1):
        s= seq[i:i+w]
        print(i, sequence.gc_comp(s),sequence.gc_skew(s))