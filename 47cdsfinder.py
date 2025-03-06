import sys
import mcb185
import sequence# for revcomp

protmin = 100

#python3 cdsfinder.py ../MCB185/data/GCF_000005845.2_ASM584v2_genomic.fna.gz

# for defline, seq in mcb185.read_fasta(sys.argv[1]):
    # print('>',defline[:30], seq[:40], len(seq))
    # for frame in range(3):
        # protstring = ''
        # print('frame:',frame+1, 'fow')
        # okprot = []
        # active_protein = False
        # for i in range(0+frame,len(seq),3):
            # codon = seq[i:i+3]
            # if codon == 'ATG':
                # protstring = protstring + 'M'
                # active_protein = True
            # if active_protein:  
                # if codon != 'ATG' and codon != 'TAA' and codon != 'TAG' and codon != 'TGA':
                    # protstring = protstring + 'P'
                # elif codon == 'TAA' or codon == 'TAG' or codon == 'TGA':
                    # protstring = protstring + '*'
                    # if len(protstring) < protmin:
                        # protstring = ''
                        # active_protein = False
                    # else:
                        # okprot.append(protstring)
                        # protstring = ''
                        # active_protein = False
        # print(okprot[1])

    # revseq = sequence.revcomp(seq)
    # for frame in range(3):
        # protstring = ''
        # print('frame:',frame+1, 'rev')
        # okprot = []
        # active_protein = False
        # for i in range(0+frame,len(revseq),3):
            # codon = revseq[i:i+3]
            # if codon == 'ATG':
                # protstring = protstring + 'M'
                # active_protein = True
            # if active_protein:  
                # if codon != 'ATG' and codon != 'TAA' and codon != 'TAG' and codon != 'TGA':
                    # protstring = protstring + 'P'
                # elif codon == 'TAA' or codon == 'TAG' or codon == 'TGA':
                    # protstring = protstring + '*'
                    # if len(protstring) < protmin:
                        # protstring = ''
                        # active_protein = False
                    # else:
                        # okprot.append(protstring)
                        # protstring = ''
                        # active_protein = False
        # print(okprot[1])
        

        # protseq = mcb185.translate(seq,frame)
        # protstring = ''
        # prot_on = False
        # compleprot = []
        # for ntp in protseq:
            # if ntp == 'M' and not prot_on:
                # prot_on = True
                
            
        # print('fowseq',defline, mcb185.translate(seq, frame)[:500])
    # revseq = sequence.revcomp(seq)
    # for frame in range(3):
        # print('revseq', defline, mcb185.translate(revseq, frame)[:500])
        
def prot_to_prot(seq, frame):
    protseq = mcb185.translate(seq, frame)
    prot_on = False
    compleprot = []
    protstring = ''
    for aa in protseq:
        if aa == 'M' and not prot_on:
            prot_on = True
            protstring += aa
        elif prot_on and aa == '*':
            prot_on = False
            protstring += aa
            if len(protstring) > 100: 
                compleprot.append(protstring)
                protstring = ''
            else: protstring = ''
        elif prot_on:
            protstring += aa
    return compleprot
            
for defline, seq in mcb185.read_fasta(sys.argv[1]):
    for frame in range(3):
        print(defline,'foward seq', prot_to_prot(seq, frame)[:50])
    revseq = sequence.revcomp(seq)
    for frame in range(3):
        print(defline, 'reverse seq',prot_to_prot(revseq, frame)[:50])