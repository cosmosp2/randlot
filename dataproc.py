#!/usr/bin/env python
#-*- coding:utf-8 -*-

# COSMOS Project.2015 https://cosmosproject2015.tistory.com/ 
# cosmosproject15@gmail.com

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
	
	for i in range(5):
		ia=i+1
		nn=nowlist[ia]
		for i in range(2):
			
			add(nn)

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
	
dnot_dict={}
for i in range(45):
	ai=1+i
	dnot_count=dnotlist.count(ai)
	dnot_dict[ai]=dnot_count
	for i in range(2):
		for i in range(dnot_count):
			add(ai)

print("미출현 번호 목록\n",dnot_dict)




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


print("사전 조합 개수 자동 설정... 총 ",avera,"개로 계산됨.")

# 섞기 및 반자동을 위한 '0' 포함 

if half == 1:
	print("반자동을 위한 0값을 포함 합니다")

if half == 0:
	print("반자동을 포함하지 않습니다.")




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
	mlist=[]
	mlist.append(random.choice(first))
	
	sec=random.choice(second)
	while sec in mlist:
		sec=random.choice(second)
	mlist.append(sec)
	
	thi=random.choice(third)
	while thi in mlist:
		thi=random.choice(third)
	mlist.append(thi)	
	
	
	four=random.choice(fourth)
	while four in mlist:
		four=random.choice(fourth)
	mlist.append(four)
	
	fiv=random.choice(five)
	while fiv in mlist:
		fiv=random.choice(five)
	mlist.append(fiv)
	
	
	si=random.choice(six)
	while si in mlist:
		si=random.choice(six)
	mlist.append(si)
	
	
	mlist.sort()
	chk_mlist=list(set(mlist))
	if len(chk_mlist) != 6 :
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
 
rate1=0
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
			rate1=rate1+1
	rate1=rate1/len(rcs)*100
	print("처음 작성 확률(%):", rate1)

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
rcs2=[]
for i in range(avera):
	
	mlist2=make_mlist()
	chk_rc=set(rcsd_rds) & set(mlist2)
	while len(chk_rc) == 0:  
		mlist2=make_mlist()
		chk_rc=set(rcsd_rds) & set(mlist2)
	rcs2.append(mlist2)

# 재작성된 리스트 테스트

rate2=0
if test == "test":

	for i in range(len(rcs2)):
			nline=rcs2[i]
			nline=set(nline)
			chk=after_list&nline
			if len(chk) > 3:
				rate2=rate2+1
	rate2=rate2/len(rcs2)*100
	print("재작성 확률(%):", rate2)

rcchk=0

rate_per=0
brc=random.choice(rcs2)
for i in range(amount):
	rc=random.choice(rcs2)
	brc_chk=set(rc) & set(brc)
	rcsd_rds_chk=set(rcsd_rds) & set(rc)
	while len(brc_chk) < 1 and len(brc_chk) > 1 and len(rcsd_rds_chk) < 1 and len(rcsd_rds_chk) > 3:
		rc=random.choice(rcs2)
		brc_chk=set(rc) & set(brc)
		rcsd_rds_chk=set(rcsd_rds) & set(rc)
		
	chk_rc=set(rcsd_rds) & set(rc)
	brc=rc

	if half == 1:
		for i in range(3):
			sel=random.choice(rc)
			rc.remove(sel)
			rc.append(0)
			
	if test =="test":
		test_rc=set(after_list) & set(rc)
		if len(test_rc) > 2:
			rated=len(test_rc)*0.25
			rate_per=rate_per+rated
		print(rc, test_rc, len(test_rc))
	if test != "test":
		
		print(rc)
if test =="test":
	rate_per=rate_per/amount*100
	print("총 당첨 확률 :",rate_per,"%")
