#!/usr/bin/env python
#-*- coding:utf-8 -*-

## LICENSE : GPL 2
# Maintainer : cosmosproject15@gmail.com
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
# 


import random
import re
import sys
import subprocess
import linecache
import os
import operator
import pandas as pd
from random import shuffle
from openpyxl import load_workbook

nnum=int(sys.argv[1])
bnum=int(sys.argv[2])
amount=int(sys.argv[3])
avera=int(sys.argv[4])
half=int(sys.argv[5])
date=str(sys.argv[6])
camel=str(sys.argv[7])
test=str(sys.argv[8])


snum=nnum-bnum
value=2


load_wb = load_workbook("/tmp/randlot_data.xlsx", data_only=True)
sheet=load_wb.active
sheet.title = "1"
load_ws = load_wb["1"]

# 오리지날 리스트
olist=[]
for i in range(45):
	al=1+i
	olist=olist+[al]
	
# 적용 소수 설계

n=45
a = [False,False] + [True]*(n-1)
primes=[]

for i in range(2,n+1):
	if a[i]:
		primes.append(i)
		for j in range(2*i, n+1, i):
			a[j] = False


# 기초 난수 설계  
	
def make_nums(cnum):
	list_name=[]
			
	for i in range(45):
		ai=i+1
		for i in range(3):
			
			list_name.append(ai)
		if ai < cnum:
			chai=cnum-ai
			chai=40-chai
			for i in range(chai):
				list_name.append(ai)
				
		if ai > cnum:
			chai=ai-cnum
			chai=40-chai
			for i in range(chai):
				list_name.append(ai)

		if ai == cnum:
			for i in range(40):
				list_name.append(ai)
	return list_name


first=make_nums(1)

for i in range(3):
	shuffle(first)

second=make_nums(13)

for i in range(3):
	shuffle(second)
third=make_nums(17)

for i in range(3):
	shuffle(third)
fourth=make_nums(27)

for i in range(3):
	shuffle(fourth)

five=make_nums(34)

for i in range(3):
	shuffle(five)

six=make_nums(43)

for i in range(3):
	shuffle(six)




# 추가 적용 함수 

def add(num):
	for i in range(3):
		
		first.append(num)
		second.append(num)
		third.append(num)
		fourth.append(num)
		five.append(num)
		six.append(num)

# 제외 적용 함수 

def dels(num):
	first.remove(num)
	second.remove(num)
	third.remove(num)
	fourth.remove(num)
	five.remove(num)
	six.remove(num)
	
dnotlist=[]
for i in range(snum):
	a=4+i
	datasel1="B"+str(a)
	data=load_ws[datasel1].value
	data1=int(data)

	datasel2="N"+str(a)
	data=load_ws[datasel2].value
	data2=int(data)

	datasel3="O"+str(a)
	data=load_ws[datasel3].value
	data3=int(data)


	datasel4="P"+str(a)
	data=load_ws[datasel4].value
	data4=int(data)

	datasel5="Q"+str(a)
	data=load_ws[datasel5].value
	data5=int(data)


	datasel6="R"+str(a)
	data=load_ws[datasel6].value
	data6=int(data)

	datasel7="S"+str(a)
	data=load_ws[datasel7].value
	data7=int(data)
	nowlist=[data2]+[data3]+[data4]+[data5]+[data6]+[data7]

	if a ==4:
		print("이전 회차 : ", data1,"의 당첨번호는 ",nowlist,"입니다.")




# 범위 수 적용
		def drange(arg):
			seldata=arg-5
			for i in range(10):
				onum=seldata+i
				if 46 > onum > 0:
					add(onum)
		
		for i in range(3):
			
			drange(data2)
			drange(data3)
			drange(data4)
			drange(data5)
			drange(data6)
			drange(data7)

			h=0
			z=0
			if data2%2 ==1:
				h=h+1
			else:
				z=z+1

			if data3%2 ==1:
				h=h+1
			else:
				z=z+1
			if data4%2 ==1:
				h=h+1
			else:
				z=z+1
			if data5%2 ==1:
				h=h+1
			else:
				z=z+1
			if data6%2 ==1:
				h=h+1
			else:
				z=z+1
			if data7%2 ==1:
				h=h+1
			else:
				z=z+1
			if h > 3  :
				for i in range(45):
					sel=1+i
					if sel%2 == 1:
						pass
					else:
						add(sel)
			if z > 3:
				for i in range(45):
					sel=1+i
					if sel%2 == 1:
						add(sel)


			
			sosuc=set(nowlist) & set(primes)
			

			
			if len(sosuc) > 3:
				for i in range(45):
					sel=1+i
					c=primes.count(sel)
					if c == 0:
						add(sel)
			if len(sosuc) < 0:
				for i in range(45):
					sel=1+i
					c=primes.count(sel)
					if c == 1:
						add(sel)

			hap=data2+data3+data4+data5+data6+data7
			if hap > 128 :
				for i in range(22):
					sel=1+i
					for i in range(3):
						add(sel)


			if hap < 128 :
				for i in range(23):
					sel=23+i
					for i in range(3):
						add(sel)

	dnot=set(olist) - set(nowlist)

	dnot=list(dnot)
	dnotlist=dnotlist+dnot


# 프린트

if h > 3  :
	print("이전회차는 홀수가 더 많았습니다.")

if z > 3:
	print("이전회차는 짝수가 더 많았습니다.")
	
if z == 3:
	print("이전 회차는 홀짝이 공동 출현 했습니다.")

print("소수 출현 횟수 :", len(sosuc), sosuc)

if len(sosuc) == 3:
	print("소수와 비소수가 공동 출현 했습니다.")


if len(sosuc) > 3:
	print("소수가 더 많이 출현 했었습니다.")
	
	
if len(sosuc) < 0:
	print("소수가 더 적게 출현 했습니다.")
	
	
if hap > 128 :
	print("이전회차는 고저값이 높습니다.")
	
if hap < 128 :
	print("이전회차는 고저값이 낮습니다.")
# 미출현 번호 결과 연산
	
for i in range(3):
	

	for i in range(45):
		ai=1+i
		dnot_count=dnotlist.count(ai)*value
		for i in range(dnot_count):
			add(ai)




# 양력 , 음력 변수를 도입

if int(date) > 0:
	print("날짜 적용이 되었습니다.")
	print("양력 :", date[0],date[1],"월",date[2],date[3],"일")
	print("음력 :", date[4],date[5],"월",date[6],date[7],"일")

	for i in range(135):
		choice_from_date=random.randint(0,7)
		if choice_from_date > 0:
			choice_1num=date[choice_from_date]
			choice=0
			
			while choice == 0:
				choice_lot_num=random.randint(1,45)
				choice_lot_num=choice_lot_num
				cln_str=str(choice_lot_num)
				for cln_str in str(choice_1num):
					choice=choice_lot_num
			add(choice)


print("출력 개수: ",amount)


# 2진수 조합 생성 


for i in range(135):
	sc1=[0,0,1]
	sc2=[1,1,0]
	num1 = data2
	num2 = data3
	num3 = data4
	num4 = data5
	num5 = data6
	num6 = data7
	def num_com(a):
		global s1; global s2; global s3; global s4; global s5; global s6
		if a >= 32:
			a = a-32
			s1=sc1
		else:
			s1=sc2
		if a >= 16:
			a = a-16
			s2=sc1
		else:
			s2=sc2
		
		if a >= 8:
			a = a-8
			s3=sc1
		else:
			s3=sc2
		
		if a >= 4:
			a = a-4
			s4=sc1
		else:
			s4=sc2
		if a >= 2:
			a = a-2
			s5=sc1
		else:
			s5=sc2

		if a >= 1:
			a = a-1
			s6=sc1
		else:
			s6=sc2


	def ans_make():
		global ansp
		a1=random.choice(s1)*32
		a2=random.choice(s2)*16
		a3=random.choice(s3)*8
		a4=random.choice(s4)*4
		a5=random.choice(s5)*2
		a6=random.choice(s6)*1
		ansp = a1+a2+a3+a4+a5+a6
		if ansp > 45:
			ans_make()
		if ansp == 0:
			ans_make()

	num_com(num1)
	ans_make()
	ans1=ansp

	ans1=[ans1]
	ans1=random.choice(ans1)
	def ans2_make():
		global ans2
		num_com(num2)
		ans_make()
		if ans1 == ansp:
			ans2_make()
		ans2 = ansp
		ans2=[ans2]
		ans2=random.choice(ans2)
	ans2_make()

	def ans3_make():
		global ans3
		num_com(num3)
		ans_make()
		if ans1 == ansp or ans2 == ansp:
			ans2_make()
		ans3=ansp
		ans3=[ans3]
		ans3=random.choice(ans3)
	ans3_make()

	def ans4_make():
		global ans4
		num_com(num4)
		ans_make()
		if ans1 == ansp or ans2 == ansp or ans3 == ansp:
			ans4_make()
		ans4=ansp
		ans4=[ans4]
		ans4=random.choice(ans4)
	ans4_make()

	def ans5_make():
		global ans5
		num_com(num5)
		ans_make()
		if ans1 == ansp or ans2 == ansp or ans3 == ansp or ans4 == ansp:
			ans5_make()
		ans5=ansp
		ans5=[ans5]
		ans5=random.choice(ans5)
	ans5_make()

	def ans6_make():
		global ans6
		num_com(num6)
		ans_make()
		if ans1 == ansp or ans2 == ansp or ans3 == ansp or ans4 == ansp or ans5 == ansp:
			ans6_make()
		ans6=ansp
		ans6=[ans6]
		ans6=random.choice(ans6)
	ans6_make()

	add(ans1)
	add(ans2)
	add(ans3)
	add(ans4)
	add(ans5)
	add(ans6)

print("사전 조합 개수 자동 설정... 총 ",avera,"개로 계산됨.")

# 섞기 및 반자동을 위한 '0' 포함 

if half == 1:
	print("반자동을 위한 0값을 포함 합니다")

if half == 0:
	print("반자동을 포함하지 않습니다.")


if int(camel) > 0:
	print("주역 숫자를 계산 합니다. 주역 숫자 :",camel)

	camel=str(camel)



	sik="+-*"


	for i in range(90):
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
		if 0 < int(math_answer) and int(math_answer) < 46:
			
			add(int(math_answer))



# 제외수 

for i in range(6):
	ai=nowlist[i]
	chk_count=first.count(ai)*0.03
	for i in range(int(chk_count)):
		first.remove(ai)
		
	chk_count=second.count(ai)*0.03
	for i in range(int(chk_count)):
		second.remove(ai)
	
	chk_count=third.count(ai)*0.03
	for i in range(int(chk_count)):
		third.remove(ai)
	
	chk_count=fourth.count(ai)*0.03
	for i in range(int(chk_count)):
		fourth.remove(ai)
	
	chk_count=five.count(ai)*0.03
	for i in range(int(chk_count)):
		five.remove(ai)
		
	chk_count=six.count(ai)*0.03
	for i in range(int(chk_count)):
		six.remove(ai)
		
for i in range(3):
	shuffle(first)


for i in range(3):
	shuffle(second)

for i in range(3):
	shuffle(third)

for i in range(3):
	shuffle(fourth)


for i in range(3):
	shuffle(five)


for i in range(3):
	shuffle(six)

# 본격 사전 조합 생성 

def make_mlist():
	mlist=[random.choice(first),random.choice(second),random.choice(third),random.choice(fourth),random.choice(five),random.choice(six) ]
	mlist.sort()
	chk_mlist=list(set(mlist))
	if len(chk_mlist) > 6 :
		make_mlist()
	return mlist


rcs=[]
rcss=[]
for i in range(avera):
	numi=i
	mlist=make_mlist()
	rcs.append(mlist)
	for i in range(6):
		ai=mlist[i]
		rcss.append(ai)
for i in range(3):
	

	shuffle(rcs)
 

if test == "test":
	
	after_num=nnum+1
	load_wb = load_workbook("/tmp/randlot_after_data.xlsx", data_only=True)
	sheet=load_wb.active
	sheet.title = "1"
	load_ws = load_wb["1"]



	for i in range(1):
		a=4+i
		datasel1="B"+str(a)
		data=load_ws[datasel1].value
		data1=int(data)

		datasel2="N"+str(a)
		data=load_ws[datasel2].value
		data2=int(data)

		datasel3="O"+str(a)
		data=load_ws[datasel3].value
		data3=int(data)


		datasel4="P"+str(a)
		data=load_ws[datasel4].value
		data4=int(data)

		datasel5="Q"+str(a)
		data=load_ws[datasel5].value
		data5=int(data)


		datasel6="R"+str(a)
		data=load_ws[datasel6].value
		data6=int(data)

		datasel7="S"+str(a)
		data=load_ws[datasel7].value
		data7=int(data)
		after_list=[data2]+[data3]+[data4]+[data5]+[data6]+[data7]

		if a ==4:
			print("테스트 적용 회차: ", after_num, " 의 당첨번호는 ",after_list,"입니다.")

	after_list=set(after_list)
	for i in range(len(rcs)):
		nline=rcs[i]
		nline=set(nline)
		chk=after_list&nline
		if len(chk) > 3:
			print(i, nline, chk, len(chk))



rcss=[]
for i in range(len(rcs)):
	rcs_line=rcs[i]
	for i in range(6):
		
		rcss.append(rcs_line[i])
	
rcsd={}
for i in range(45):
	ai=i+1
	count_lotnum=rcss.count(ai)
	rcsd[ai]=count_lotnum
	
rcsd=sorted(rcsd.items(), key=operator.itemgetter(1), reverse=True )


rcsdi0_list=[]
for i in range(23):
	rcsdi=rcsd[i]
	rcsdi0=rcsdi[0]
	rcsdi0_list.append(rcsdi0)
rcsd_rds=rcsdi0_list
print("출현 횟수 순위")
print(rcsd_rds)

print("기초 출현 횟수 순위")

rcsd={}
for i in range(45):
	ai=i+1
	
	count_lotnum=first.count(ai)+second.count(ai)+third.count(ai)+fourth.count(ai)+five.count(ai)+six.count(ai)
	
	rcsd[ai]=count_lotnum
	
rcsd=sorted(rcsd.items(), key=operator.itemgetter(1), reverse=True )


rcsdi0_list=[]
for i in range(23):
	rcsdi=rcsd[i]
	rcsdi0=rcsdi[0]
	rcsdi0_list.append(rcsdi0)
print(rcsdi0_list)

print("공통 수들")
rcsd_rds=set(rcsd_rds) | set(rcsdi0_list)
print(rcsd_rds)

if test == "test":
	
	chk_rcsd_rds=set(rcsd_rds) & set(after_list)
	print("공통 수 테스트 확인")
	print(chk_rcsd_rds, len(chk_rcsd_rds))

print("공통 수 를 토대로 리스트를 추출 합니다.")

# 리스트 재작성


for i in range(amount):
	rc=random.choice(rcs)
	chk_rc=set(rcsd_rds) & set(rc)
	
	while len(chk_rc) < 5:  
		rc=random.choice(rcs)
		chk_rc=set(rcsd_rds) & set(rc)
		
	if half == 1:
		for i in range(3):
			sel=random.choice(rc)
			rc.remove(sel)
			rc.append(0)
			
	if test =="test":
		test_rc=set(after_list) & set(rc)
		print(rc, test_rc, len(test_rc))
	if test != "test":
		
		print(rc)
	

