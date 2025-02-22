import sys

seq = sys.argv[1]
match = sys.argv[2]
mismatch = sys.argv[3]

#prepping 1st row
# print(seq)
altseqone = ' ' + seq
listseqone = list(altseqone)
# print(listseqone)
joinedlist = '  '.join(listseqone)
print(joinedlist)

#rest of it
seqlist = list(seq)
for rows in seqlist:
    print(rows, end = ' ')
    for col in seqlist:
        if rows == col: print(match, end = ' ')
        else: print(mismatch, end = ' ')
    print()
    
 #git looks a little different, assuming its one of the iconic typo gatchyou moments