import sys
import mcb185

#library to iterate through fasta file and open it gunzip automatially
#python3 41fasta.py ../MCB185/data/C.elegans.fa.gz
for defline, seq in mcb185.read_fasta(sys.argv[1]):
    print(defline[:30], seq[:40], len(seq)) 
    