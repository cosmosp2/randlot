#!/bin/bash
import random


avera=35000
a=[]

camel=2458
camel=str(camel)


sik="+-*/"


for i in range(avera):
	math_lenth=random.randint(1,9)



	if math_lenth == 1:
		
		camel_math=camel[random.randint(0,3)]
		
		
	if math_lenth == 2:
		
		camel_math=camel[random.randint(0,3)]+camel[random.randint(0,3)]



	if math_lenth == 3:


		camel_math=camel[random.randint(0,3)]+sik[random.randint(0,3)]+camel[random.randint(0,3)]

	if math_lenth == 4:


		camel_math=camel[random.randint(0,3)]+camel[random.randint(0,3)]+sik[random.randint(0,3)]+camel[random.randint(0,3)]



	if math_lenth == 5:

		camel_math=camel[random.randint(0,3)]+camel[random.randint(0,3)]+sik[random.randint(0,3)]+camel[random.randint(0,3)]+camel[random.randint(0,3)]



	if math_lenth == 6:


		camel_math=camel[random.randint(0,3)]+sik[random.randint(0,3)]+camel[random.randint(0,3)]+sik[random.randint(0,3)]+camel[random.randint(0,3)]

	if math_lenth == 7:


		camel_math=camel[random.randint(0,3)]+camel[random.randint(0,3)]+sik[random.randint(0,3)]+camel[random.randint(0,3)]+sik[random.randint(0,3)]+camel[random.randint(0,3)]

	if math_lenth == 8:


		camel_math=camel[random.randint(0,3)]+camel[random.randint(0,3)]+sik[random.randint(0,3)]+camel[random.randint(0,3)]+camel[random.randint(0,3)]+sik[random.randint(0,3)]+camel[random.randint(0,3)]

	if math_lenth == 9:


		camel_math=camel[random.randint(0,3)]+sik[random.randint(0,3)]+camel[random.randint(0,3)]+camel[random.randint(0,3)]+sik[random.randint(0,3)]+camel[random.randint(0,3)]

	math_answer=eval(camel_math)
	if 0 < math_answer and math_answer < 46:
		
		a.append(math_answer)

print(a)
print(len(a))








