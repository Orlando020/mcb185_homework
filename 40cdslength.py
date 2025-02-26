import gzip
import sys

# with gzip.open(sys.argv[1],'rt') as fp:
    # for line in fp:
        # if line[0] != '#': #excluding start text
            # words = line.split()
            # if words[2] == 'CDS':    #NC_000913.3     RefSeq  CDS     190     255    
                # beg = int(words[3])
                # end = int(words[4])
                # print(end - beg)
                
                
# with gzip.open(sys.argv[1], 'rt') as fp:
     # for line in fp:
         # if not line[0] == '#':
             # words = line.split()
             # if words[2] == 'CDS':
                # begin = int(words[3])
                # end = int(words[4])
                # print(begin,end)

# print(type(fp))

# with gzip.open(sys.argv[1], 'rt') as fp:
    # for line in fp:
        # print(line[0],line[2])
        # if line[0] != '#' and line[25] == 'C':
            # words = line.split
            # print(words[3] - words[4])
            
            
with gzip.open(sys.argv[1], 'rt') as fp:
    for line in fp:
        if line[0] != '#':
            words = line.split()
            if words[2] == 'CDS':
                print(int(words[4]) - int(words[3]))