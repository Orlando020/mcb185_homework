# python3 46dust.py A.thaliana.fa.gz 20 1.4
# 1.4 seems like a really high shannon entropy value its all n
import sys
import mcb185
import math

window = int(sys.argv[2])
entro_thresh = float(sys.argv[3])

# seq = 'ACGTATCGATCGTAGCTGCTATAAAAAAAAAAAAAAAAAAAATAGCTGACTGAC'

for defline, seq in mcb185.read_fasta(sys.argv[1]):
    print(defline[:30], seq[:40], len(seq))
    newstring = ''
    win_string = ''
    for i in range(len(seq)):
        if i <= len(seq)-window: win_string = seq[i:i+window] #freezes window at end point
        
        aprob = win_string.count('A')/window #acounts for math.log(0)
        if aprob == 0: a = 0
        else: a = math.log(aprob)*aprob
        
        cprob = win_string.count('C')/window
        if cprob == 0: c = 0
        else: c = math.log(cprob)*cprob
       
        gprob = win_string.count('G')/window
        if gprob == 0: g = 0
        else: g = math.log(gprob)*gprob

        tprob = win_string.count('T')/window
        if tprob == 0: t = 0
        else: t = math.log(tprob)*tprob
        
        shannon = -(a + c + g + t)
        
        if shannon < entro_thresh: newstring = newstring + 'N'
        elif shannon > entro_thresh: newstring = newstring + seq[i]
    print(newstring[:500]) #will literally fill entire console elsewise, remove for full look