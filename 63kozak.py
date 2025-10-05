#would have to use gbff.gz and fna in conjunction, foward and reverse, not sure what 14th bp in kozak would be
#kozak consensus is a sequence, genbank flat file
#with notation find tl start site then match to larger seq to obtain ATCG seq then count up to make pwm then print it out
#wiki says its 13 ntp on both sides of Methionine, expample shows 14,  I can just have an adjustable range and call whatever best fitting data is
#-20 to +20 of each cds on both strands is what is of intrest, need  a list of strings, can visibly see atg to adjust

import sys
import gzip
import re
import mcb185


#python3 63kozak.py ../MCB185/data/GCF_000005845.2_ASM584v2_genomic.gbff.gz

revbad = []
fow = []
seqtime = False
seqlist = []
#ripout coords of TL starts
with gzip.open(sys.argv[1],'rt') as fp:
    for line in fp:
        if line[5:8] == 'CDS':
            # print(line)
            if 'complement' in line:
                revcoord = re.findall(r'\d+', line)
                revcoord.pop(0)
                revbad.append(int(revcoord[0]))
            else:
                fowcoord = re.findall(r'\d+', line)
                fowcoord.pop(1)
                fow.append(int(fowcoord[0]))
        if 'ORIGIN' in line: seqtime = True # extract seq as a str
        if seqtime:
            orgi = re.findall(r'\w+', line)
            if orgi == []: orgi.append('slapdash')#weird case of empty last line causes errors as it makes a empty list
            orgi.pop(0)
            joinorgi = ''.join(orgi)
            seqlist.append(joinorgi)




seqlist.pop()
seq = ''.join(seqlist)
revseq = mcb185.anti_seq(seq)

rev = [] #gets reversed list of revcoords of TL sites adjusted for rev strand
for coord in revbad:
    rev.append(len(seq)-coord+1)

def pwmextract(relativecoord, seq, tlcoord):
    ntp = [0,0,0,0]
    for coord in tlcoord:
        koza = coord +  relativecoord
        if seq[koza] == 'a': ntp[0] += 1
        if seq[koza] == 'c': ntp[1] += 1
        if seq[koza] == 'g': ntp[2] += 1
        if seq[koza] == 't': ntp[3] += 1
    return ntp
    
print('AC dunno\nXX\nID kozak\nXX\nDE ntp around TL start site')
print(f'{"P0":<8}', f'{"A":<8}', f'{"C":<8}', f'{"G":<8}', f'{"T":<8}')

for rel in range(-10,4):
    pwm = [0,0,0,0]
    fowpwm = pwmextract(rel,seq,fow)
    revpwm = pwmextract(rel,revseq,rev)
    for i in range(4):
        pwm[i] = fowpwm[i] + revpwm[i] 
    print(f'{rel+11:<8}', f'{pwm[0]:<8}', f'{pwm[1]:<8}',f'{pwm[2]:<8}',f'{pwm[3]:<8}',)
    
print('XX')