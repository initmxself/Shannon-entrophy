import collections
import math
import re

def shannon_entropy(s):
    char_seq = re.sub(r'[^a-zЁёа-я]', '', s.strip(' '))
    all_freq={}
    m = len(char_seq)
    bases = collections.Counter([tmp_base for tmp_base in char_seq])
    shannon_entropy_value = 0
                
    for base in bases:
        n_i = bases[base]
        p_i = n_i / float(m)
        entropy_i = p_i * (math.log(p_i, 2))
        
        shannon_entropy_value += entropy_i
        print('|',base,"\t|",bases[base],"\t  |")
    return "Entrophy: " +str(shannon_entropy_value *-1)
        
dt = input('enter a string: ').lower()
print('\n|Symbol\t|Frequency|')
print('|-------|---------|')
shannon_entropy(dt)
