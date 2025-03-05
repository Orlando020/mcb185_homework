import sys
import mcb185

w = 1000

# seq = 'ACGTACGTGGGGGACGTACGTCCCCC'

for defline, seq in mcb185.read_fasta(sys.argv[1]):
    print(defline[:30], seq[:40], len(seq)) 
    winofseq = seq[0:w]
    
    curr_g = winofseq.count('G')
    curr_c = winofseq.count('C')
    curr_gc_count = curr_g+curr_c
 

    print(0, curr_gc_count/w, (curr_g-curr_c)/(curr_g+curr_c))
    for i in range (1, len(seq)-w):
        if seq[i+w] == 'G': curr_g +=1
        if seq[i+w] == 'C': curr_c +=1
        if seq[i-1] == 'G': curr_g -=1
        if seq[i-1]  == 'C': curr_c -=1
        if curr_g+curr_c == 0: curr_skew = 'Over0'
        else:curr_skew = (curr_g-curr_c)/(curr_c+curr_g)
        print(i, (curr_g+curr_c)/w, curr_skew)
    
# print(seq[0:len(seq)-w])
#less efficient than 43skew.py not sure why