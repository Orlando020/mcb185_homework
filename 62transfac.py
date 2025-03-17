import sys
import gzip

#python3 62transfac.py ../MCB185/data/jaspar2024_core.transfac.gz 

finlist = []
id_dict = {}
curr_id = 0
curr_pwm = 0
curr_pwmlist = []
curr_pwmdict = {}
fourdown = 6
doingpo = False

with gzip.open(sys.argv[1],'rt') as fp:
    for line in fp:
        if line[0:2] == 'ID':
            curr_id = line[2:].rstrip()
            fourdown -= 1
            
        if fourdown < 6: fourdown -= 1
        
        if doingpo:
            if line[0:2] == 'XX':
                id_dict['"id"'] = curr_id
                id_dict['"pwm"'] = curr_pwmlist
                finlist.append(id_dict)
                id_dict = {}
                curr_pwmlist = []
                doingpo = False
            else:
                curr_pwm = line.rstrip().split()
                curr_pwmdict['"A"'] = curr_pwm[1]
                curr_pwmdict['"C"'] = curr_pwm[2]
                curr_pwmdict['"G"'] = curr_pwm[3]
                curr_pwmdict['"T"'] = curr_pwm[4]
                curr_pwmlist.append(curr_pwmdict)
                curr_pwmdict = {}
            
        if fourdown == 0:
            curr_pwm = line.rstrip().split()
            curr_pwmdict['"A"'] = curr_pwm[1]
            curr_pwmdict['"C"'] = curr_pwm[2]
            curr_pwmdict['"G"'] = curr_pwm[3]
            curr_pwmdict['"T"'] = curr_pwm[4]
            curr_pwmlist.append(curr_pwmdict)
            curr_pwmdict = {}
            fourdown = 6
            doingpo = True
        

print('[')
for firstdict in finlist:
    print('     ' , '{' , sep='')
    print('         "id": "',firstdict['"id"'], '",', sep = '')
    print('             "pwm": [ ', sep = '')
    for secdict in firstdict['"pwm"']:
        print('                 {')
        for ntp, val in secdict.items():
            print('                     ',ntp,': ',val,sep='')
        print('                 }')
    print('     ' , '},' , sep='')