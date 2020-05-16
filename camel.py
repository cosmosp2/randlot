#!/usr/bin/env python
#-*- coding:utf-8 -*-
import random
import sys
import operator
camel=str(sys.argv[1])
avera=int(sys.argv[2])
print("주역 숫자를 계산 합니다. 주역숫자 :",camel)
camel=str(camel)
sik="+-*"
rcs=[]
for i in range(avera):
	a=[]
	while len(a) < 6:
		math_lenth=random.randint(1,9)
		if math_lenth == 1:
			camel_math=camel[random.randint(0,3)]
		if math_lenth == 2:
			camel_math=camel[random.randint(0,3)]+camel[random.randint(0,3)]
		if math_lenth == 3:
			camel_math=camel[random.randint(0,3)]+sik[random.randint(0,2)]+camel[random.randint(0,3)]
		if math_lenth == 4:
			camel_math=camel[random.randint(0,3)]+camel[random.randint(0,3)]+sik[random.randint(0,2)]+camel[random.randint(0,3)]
		if math_lenth == 5:
			camel_math=camel[random.randint(0,3)]+camel[random.randint(0,3)]+sik[random.randint(0,2)]+camel[random.randint(0,3)]+camel[random.randint(0,3)]
		if math_lenth == 6:
			camel_math=camel[random.randint(0,3)]+sik[random.randint(0,2)]+camel[random.randint(0,3)]+sik[random.randint(0,2)]+camel[random.randint(0,3)]
		if math_lenth == 7:
			camel_math=camel[random.randint(0,3)]+camel[random.randint(0,3)]+sik[random.randint(0,2)]+camel[random.randint(0,3)]+sik[random.randint(0,2)]+camel[random.randint(0,3)]
		if math_lenth == 8:
			camel_math=camel[random.randint(0,3)]+camel[random.randint(0,3)]+sik[random.randint(0,2)]+camel[random.randint(0,3)]+camel[random.randint(0,3)]+sik[random.randint(0,2)]+camel[random.randint(0,3)]
		if math_lenth == 9:
			camel_math=camel[random.randint(0,3)]+sik[random.randint(0,2)]+camel[random.randint(0,3)]+camel[random.randint(0,3)]+sik[random.randint(0,2)]+camel[random.randint(0,3)]
		math_answer=eval(camel_math)
		if 0 < int(math_answer) < 46:
			if int(math_answer) not in a:
				a.append(int(math_answer))
				rcs.append(int(math_answer))
			
	a.sort()
	print(a)


rcsd={}
for i in range(45):
	ai=i+1
	count_lotnum=rcs.count(ai)
	rcsd[ai]=count_lotnum
	
rcsd=sorted(rcsd.items(), key=operator.itemgetter(1), reverse=True )

for i in range(6):
	print(rcsd[i])
