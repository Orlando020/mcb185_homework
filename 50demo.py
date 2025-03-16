# d = {'dog':'woof','cat':'meow'}
# print(d['cat'])
# d['pig'] = 'oink'
# d['cat'] = 'mew'
# del d['cat']
# print(d['rat'])
# print(d['cat'])
# if 'dog' in d:
    # print(d['dog'])
# for key in d: print(f'{key} says {d[key]}')
# for k, v in d.items(): print(k,'says',v)
# print(type(d.items))
# print(d.keys(),d.values())
# listo = d.values()
# print(listo)

# import argparse
# parser = argparse.Argu

s = 'abcdefg'

# print(s[0:0])

# string = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
# def rep_string(string, startex, replat):
    # newstring = string[0:startex] + replat + string[len(replat):]
    # return newstring

# print(rep_string(string, 5, 'bbbbbbbbbb'))
# print(string)

import sys
import mcb185

# for defline, seq in mcb185.read_fasta(sys.argv[1]):
    
# print(type(mcb185.read_fasta(sys.argv[1])))

# listo = [1,41,511,617,3]
# for io in listo:
    # print(io)
# stringo = 'adasvaavaablknablnabkabnlabnlaabklnbasaaaaaaaaald'
# print(stringo.count('aaa'))

# for nts in itertools.product('ACGT', repeat = k):
    # kmer = ''.join(nts)

# do without itertools

# Designate order ACGT #ATG = 032 to 033 to 100, infinite number of variable to contain the counters or an infinley expending list to index if list not all threes next up digit should be added, 4 will be null, yet to be filled but kmer requres
#                 0123
#044, 144, 244,344,004, 014, 024,034,104,
#swap for easy conditionals 0 is null 1234 is ACGT so 000, 100, 200, 300, 400, 110,120,
# divvy up by k or purely by iteration, function should delive list of kmers up to k
ntplisto = ['A','C','G','T']

# def kmergen(k):
    # kmerraw = []
    # indexing_list = []
    # active = None
    # for i in range(k):
        # indexing_list.append(1) #indexing list constructed
    # print(indexing_list)
    # while True:
        # if 0 not in indexing_list:
            # break
        # if 0 in indexing_list:
            # active = indexing_list.index(0)
        # else: break
        # if indexing_list[active] < 4:
            # indexing_list[active] += 1
            # continue
        # elif indexing_list[active] == 4 and active >= 1:
            # if indexing_list[active - 1] == 4: continue
            # else: indexing_list[active-1] += 1
        # print(indexing_list)
        # break
    
#function that takes a list of kmers and adds a k on it a c g takes
# takes list of x returns list of 4x
# print(kmergen(3))
# print(type(kmergen(3)))
# itetools: k = 3
nucleo = ['a','c','g','t']

def addacgt(listo):
    kmerlist = []
    for kmer in listo:
        for ntp in nucleo:
            prodkmer = kmer+ntp
            kmerlist.append(str(prodkmer))
    return kmerlist

# print(addacgt(addacgt(['a','c','g','t'])))
#can give kmer at k
#now want kmer below k
k = 4
finlist = []
for i in range(k-1):
    if i == 0:currk = k
    for i in range(currk-1):
        if i == 0:innie = ['a','c','g','t']
        outie = addacgt(innie)
        innie = outie
    finlist.append(outie)
    currk -= 1
print(finlist)