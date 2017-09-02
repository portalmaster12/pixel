#python3.5
"""
This program encodes information into hex.

Author: Ethan Bartlett
"""

#preliminaries



#functions


#encoding

txt = raw_input("Input your message:\n")

alphabet = [' ','a','b','c',
            'd','e','f','g',
            'h','i','j','k',
            'l','m','n','o',
            'p','q','r','s',
            't','u','v','w',
            'x','y','z']
mul= []
num = []
numd = []

for l in txt:
    num.append(alphabet.index(l))

print(num)

#f = num/2

for l in (num):
    if l>16:
#         if f*2==l:            
        mul.append(1)
        numd.append(l/2)
        
    else:
        mul.append(0)
        numd.append(l)
        
print (mul)
print (numd)
