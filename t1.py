import random
a=[4,5,7]
c=[4,5,7,8]
b=random.choice(c)
chk=set(a) & set(c)
print(chk)
