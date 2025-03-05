import sys
import mcb185
aalist = ['I','V','L','F','C','M','A','G','T','S','W','Y','P','H','E','Q','D','N','K','R','U']
hydrolist = [4.5,4.2,3.8,2.8,2.5,1.9,1.8,-0.4,-0.7,-0.8,-0.9,-1.3,-1.6,-3.2,-3.5,-3.5,-3.5,-3.5,-3.9,-4.5,0]

#python3 48transmembrane.py ../MCB185/dta/GCF_000005843.2_ASM584v2_protein.faa.gz

for defline, seq in mcb185.read_fasta(sys.argv[1]):
    totsignal = 0
    sig = False
    mid = False
    for i in range(8):
        aastart = aalist.index(seq[i])
        totsignal += hydrolist[aastart]
    if totsignal/8 > 2.5: sig = True
    for i in range(29,len(seq)-11):
        totmid = 0
        for j in range(11):
            aamid = aalist.index(seq[i+j])
            totmid += hydrolist[aamid]
        if totmid/11 >= 2.0: mid = True
    if sig and mid:print(defline[:50])