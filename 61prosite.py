import mcb185
import sys
import re

#python3 61prosite.py ../MCB185/data/GCF_000005845.2_ASM584v2_protein.faa.gz

#normal way, finds protein seq with DKTGT
for defline, seq in mcb185.read_fasta(sys.argv[1]):
    if 'DKTGT' in seq:print (defline)
print('///////')
#doing it with regular expression
for defline, seq in mcb185.read_fasta(sys.argv[1]):
    if re.search('DKTGT', seq): print(defline)
print('///////')
#D-K-T-G-T-[LIVM]-[TI], fuller search, of a p type atpase phos site, with regular terminology from regex: basically grep
for defline, seq in mcb185.read_fasta(sys.argv[1]):
    if re.search('DKTGT[LIVM][TI]', seq): print(defline)
print('///////')
#C-x(2,4)-C-x(3)-[LIVMFYWC]-x(8)-H-x(3,5)-H, zinc finger search
for defline, seq in mcb185.read_fasta(sys.argv[1]):
    if re.search('C.{2,4}C.{3}[LIVMFYWC].{8}H.{3,5}H',seq): print(defline)
    
print('////////')
pat = '(C.{2,4}C.{3}[LIVMFYWC].{8}H.{3,5}H)'
for defline,seq in mcb185.read_fasta(sys.argv[1]):
    m = re.search(pat,seq)
    if m: print(m.group(1))# what defines a group, prints what the function was searching for
