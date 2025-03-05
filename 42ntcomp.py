import sys
import mcb185

for defline, seq in mcb185.read_fasta(sys.argv[1]):
    defwords = defline.split()
    name = defwords[0]
    gc = 0
    # for nt in seq:
        # if nt == 'C' or nt == 'G': gc += 1
    # print(name, gc/len(seq))
    # a = 0
    # c = 0
    # g = 0
    # t = 0
    # n = 0
    # for nt in seq:
        # if nt =='A': a+=1
        # elif nt == 'C': c+=1
        # elif nt == 'G': g+=1
        # elif nt == 'T': t+=1
        # else: n+=1
    # print(name, a/len(seq), c/len(seq), g/len(seq), t/len(seq), n/len(seq))
    
    # nts = 'ACGTN'
    # counts = [0] *len(nts)
    # for nt in seq:
        # idx = nts.find(nt)
        # counts[idx] += 1
    # print(name, end='')
    # for n in counts: print (n/len(seq),end='')
    # print()
    nts = []
    counts = []
    for nt in seq:
        if nt not in nts:
            nts.append(nt)
            counts.append(0)
        idx = nts.index(nt)
        counts[idx] +=1
    print(name)
    for nt,n in zip(nts,counts):
        print(nt,n,n/len(seq))
    print()