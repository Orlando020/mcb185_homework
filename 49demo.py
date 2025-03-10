import sys
import gzip


# filepath = sys.argv[1]
# fp = open(filepath)
# for line in fp:
    # cols = line.split()
    # print(cols[0])
    # print(type(cols[1]))
    
filepath = sys.argv[1]
fp = gzip.open(filepath, 'rt')
for line in fp:
    cols = line.split()
    if cols[2] != 'exon': continue
    print(line,end='')
    
    
# will close file once block is left
# with gzip.open(filepath, 'rt') as fp:
        # for line in fp:
            # f = line.split()
            # print(int(f[3]),int(f[4]))
            # if f[2] != 'exon':continue
            