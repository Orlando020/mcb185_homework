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

print(s[0:0])

string = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
def rep_string(string, startex, replat):
    newstring = string[0:startex] + replat + string[len(replat):]
    return newstring

# print(rep_string(string, 5, 'bbbbbbbbbb'))
print(string)