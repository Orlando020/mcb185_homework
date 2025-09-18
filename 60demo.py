import json

truc = {
    'animals': {'dog': 'woof', 'cat': 'meow', 'pig': 'oink'},
    'numbers': [1.09, 2.72, 3.14],
    'is_complete': False,
}
print(json.dumps(truc, indent=4))


# import sys

# print(sys.argv)
# print(sys.argv[0:5])
# print(type(sys.argv))

import sys

# def read_catalog(filepath):
    # catalog = []
    # with open(filepath) as fp:
        # for line in fp:
            # if line.startswith('#'): continue
            # name, length, seq, desc = line.rstrip().split(',')
            # record = {
            # 'Name': name,
            # 'Length': length,
            # 'Sequence': seq,
            # 'Description': desc
            # }
            # catalog.append(record)
        # return catalog
  # python3 60demo.py ../MCB185/data/primers.csv

# print(sys.argv[1])
# print(read_catalog(sys.argv[1]))

#kmer countig of seq
# kcount = {}
# for i in range(len(seq) - k +1):
    # kmer = seq[i:i+k]
    # if kmer not in kcount: kcount[kmer] = 0
    # kcount[kmer] += 1

# dicitionary of lists of kmer locations
# seq = 'AGCTTTTCATTTGACTGCGATAGCATCGACTGATCAGCTGATCGATCGATGCATCATCGAAAAAAAGAGT'
# k = 4
# kloc = {}
# kcount = {}
# for i in range(len(seq) - k +1):
    # kmer = seq[i:i+k]
    # if kmer not in kloc: kloc[kmer] = []
    # kloc[kmer].append(i)
# print(kloc)