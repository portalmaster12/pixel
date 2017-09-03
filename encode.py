#python3.5
"""
This program encodes information into hex.

Author: Ethan Bartlett
"""

#preliminaries



#functions


#encoding

alphabet = [' ','a','b','c',
            'd','e','f','g',
            'h','i','j','k',
            'l','m','n','o',
            'p','q','r','s',
            't','u','v','w',
            'x','y','z']
hexcode = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
txt = raw_input("Input your message:\n")



mul= []
num = []
numd = []

for l in txt:
    num.append(alphabet.index(l))

print(num)



for l in (num):
    if l>15:
         if (l/2)*2==l:
             mul.append(1)
             numd.append(l/2)
         else:
             mul.append(2)
             #print(l)
             numd.append(l/2)
                    
        
        
    else:
        mul.append(0)
        numd.append(l)

numhex=[]
for h in numd:
    numhex.append(hexcode[h])


print (numhex)
















        
print (mul)
print (numd)
print (h)
print (numhex)
