#!/usr/bin/env python
#-*- coding:utf-8 -*-

## LICENSE
# Maintainer : cosmosproject15@gmail.com
#  Apache License
#  Version 2.0

import random
import re
import sys
import subprocess
import linecache
import os
import operator
from openpyxl import load_workbook

nnum=int(sys.argv[1])
bnum=int(sys.argv[2])
amount=int(sys.argv[3])
avera=int(sys.argv[4])
half=int(sys.argv[5])
date=str(sys.argv[6])
test=str(sys.argv[7])
snum=nnum-bnum
value=2

n=45
a = [False,False] + [True]*(n-1)
primes=[]

for i in range(2,n+1):
	if a[i]:
		primes.append(i)
		for j in range(2*i, n+1, i):
			a[j] = False

load_wb = load_workbook("/tmp/randlot_data.xlsx", data_only=True)
sheet=load_wb.active
sheet.title = "1"
load_ws = load_wb["1"]


# 오리지날 리스트
olist=[]
for i in range(45):
	al=1+i
	olist=olist+[al]

#  컴퓨팅 데이타 설계
cdata={}
for i in range(45):
	li=1+i
	cdata[li]=2

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
		cdata[data2]=float(cdata[data2])-value
		cdata[data3]=float(cdata[data3])-value
		cdata[data4]=float(cdata[data4])-value
		cdata[data5]=float(cdata[data5])-value
		cdata[data6]=float(cdata[data6])-value
		cdata[data7]=float(cdata[data7])-value

# 범위 수 적용
		def drange(arg):
			seldata=arg-5
			for i in range(10):
				onum=seldata+i
				if 46 > onum > 0:
					cdata[onum]=float(cdata[onum])+1
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
			print("이전회차는 홀수가 더 많았습니다.")
			for i in range(45):
				sel=1+i
				if sel%2 == 1:
					pass
				else:
					cdata[sel]=cdata[sel]+value
		if z > 3:
			print("이전회차는 짝수가 더 많았습니다.")
			for i in range(45):
				sel=1+i
				if sel%2 == 1:
					cdata[sel]=cdata[sel]+value


		if z == 3:
			print("이전 회차는 홀짝이 공동 출현 했습니다.")
		sosuc=set(nowlist) & set(primes)
		print("소수 출현 횟수 :", len(sosuc), sosuc)

		if len(sosuc) == 3:
			print("소수와 비소수가 공동 출현 했습니다.")
		if len(sosuc) > 3:
			print("소수가 더 많이 출현 했었습니다.")
			for i in range(45):
				sel=1+i
				c=primes.count(sel)
				if c == 0:
					cdata[sel]=cdata[sel]+value
		if len(sosuc) < 0:
			print("소수가 더 적게 출현 했습니다.")
			for i in range(45):
				sel=1+i
				c=primes.count(sel)
				if c == 1:
					cdata[sel]=cdata[sel]+value

		hap=data2+data3+data4+data5+data6+data7
		if hap > 128 :
			print("이전회차는 고저값이 높습니다.")
			for i in range(22):
				sel=1+i
				cdata[sel]=cdata[sel]+(value*2)


		if hap < 128 :
			print("이전회차는 고저값이 낮습니다.")
			for i in range(23):
				sel=23+i
				cdata[sel]=cdata[sel]+(value*2)


	dnot=set(olist) - set(nowlist)

	dnot=list(dnot)
	dnotlist=dnotlist+dnot



# 미출현 번호 결과 연산
for i in range(45):
	ai=1+i
	cdata[ai]=float(cdata[ai])+(dnotlist.count(ai)*value)
lists=[]
for i in range(45):
	sel=1+i
	a=cdata[sel]
	for i in range(int(a)):
		lists=lists+[sel]
for i in range(314):
	rnum=random.randint(1,45)
	lists=lists+[rnum]


# 양력 , 음력 변수를 도입

if int(date) > 0:
	print("날짜 적용이 되었습니다.")
	print("양력 :", date[0],date[1],"월",date[2],date[3],"일")
	print("음력 :", date[4],date[5],"월",date[6],date[7],"일")

	for i in range(avera):
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
			lists=lists+[choice]
				
		


print("출력 개수: ",amount)


random.shuffle(lists)
a=lists

# 2진수 조합 생성 

twomount=avera/17

for i in range(int(twomount)):
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

	a=a+[ans1]+[ans2]+[ans3]+[ans4]+[ans5]+[ans6]

print("사전 조합 개수 자동 설정... 총 ",avera,"개로 계산됨.")

# 섞기 및 반자동을 위한 '0' 포함 

if half == 1:
	print("반자동을 위한 0값을 포함 합니다")

if half == 0:
	print("반자동을 포함하지 않습니다.")


random.shuffle(a)

# 본격 사전 조합 생성 

def rc1(lists):
	a=lists
	p = random.choice(a)
	def p1com():
		global p1
		p1 = random.choice(a)
		if p1 == p:
			if half == 1:
				p1=0
			else:
				p1com()
	def p2com():
		global p2
		p2 = random.choice(a)
		
		if p2 == p1 or p2 == p :
			if half == 1:
				p2=0
			else:
				p2com()
	def p3com():
		global p3
		p3 = random.choice(a)
		if p3 == p2 or p3 == p1 or p3 == p:
			if half == 1:
				p3=0
			else:
				p3com()
	def p4com():
		global p4
		p4 = random.choice(a)
		if p4 == p3 or p4 == p2 or p4 == p1 or p4 == p:
			if half == 1:
				p4=0
			else:
				p4com()
	def p5com():
		global p5
		p5 = random.choice(a)
		if p5 == p4 or p5 == p3 or p5 == p2 or p5 == p1 or p5 == p:
			if half == 1:
				p5=0
			else:
				p5com()
	p1com()
	p2com()
	p3com()
	p4com()
	p5com()
	global A
	A = [p1, p2, p3, p4, p5, p]
	A.sort()
	return A

AO=[]
AN=0

rcs=[]
for i in range(avera):
	
	rc=rc1(a)
	rcs.append(rc)

random.shuffle(rcs)

answer_list=[]
for i in range(amount):
	sel=random.randint(0,len(rcs))
	answer=rcs[sel]
	answer_list.append(answer)
	print(answer)

if test == "test":
	

	nowlist=set(nowlist)
	for i in range(len(rcs)):
		nline=rcs[i]
		nline=set(nline)
		chk=nowlist&nline
		if len(chk) > 3:
			print(i, nline, chk, len(chk))


