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
	for i in range(2):
		
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
	for i in range(2):
		
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
	
dnotlist=olist
dnot_dict={}

# 미출현 dict 작성 
for i in range(45):
	ai=i+1
	dnot_dict[ai]=0
	
	

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
		first_list=nowlist
		print("이전 회차 : ", data1,"의 당첨번호는 ",first_list,"입니다.")
		
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

	# 연속 미출현 번호 연산

	dnot=set(dnotlist) - set(nowlist)

	dnotlist=list(dnot)
	
	for i in range(len(dnotlist)):
		dnot_num=dnotlist[i]
	
		dnot_dict[dnot_num]=dnot_dict[dnot_num]+1
	
		add(dnot_num)
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
	

dnots=sorted(dnot_dict.items(), key=operator.itemgetter(1), reverse=True )
print("미출현 번호 목록 (내림차순)\n",dnots)

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
		
for i in range(11):
	shuffle(first)

for i in range(11):
	shuffle(second)

for i in range(11):
	shuffle(third)

for i in range(11):
	shuffle(fourth)


for i in range(11):
	shuffle(five)


for i in range(11):
	shuffle(six)

# 난수 순위 계산

ranlists=first+second+third+fourth+five+six
ranlists_dict={}
for i in range(45):
	ai=i+1
	aic=ranlists.count(ai)
	ranlists_dict[ai]=aic
sort_of_ranlists_dict=sorted(ranlists_dict.items(), key=operator.itemgetter(1), reverse=True )

print("연산된 난수  총 순위 (내림차순)\n",sort_of_ranlists_dict)

favorit_list=[]
for i in range(23):
	favorit=sort_of_ranlists_dict[i]
	favorit=favorit[0]
	favorit_list.append(favorit)

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
	
	# Mmlist 에서 치환 
	
	choice_num=random.randint(0,5)
	
	mlist[choice_num]=random.choice(favorit_list)
	return mlist

rcs=[]
rcss=[]
bmlist=[]
for i in range(avera):
	numi=i
	mlist=make_mlist()
	if len(bmlist) == 6:
		addnums=set(bmlist)-set(mlist)
		if len(addnums) > 1:
			
			addnums_len=len(addnums)-1
			addnums=list(addnums)
			addnums_choice=random.choice(addnums)
			choice_mlist=random.randint(0,5)
			mlist[choice_mlist]=addnums_choice
	
	
	len_of_mlist=len(list(set(mlist)))
	if len_of_mlist != 6:
		mlist=list(set(mlist))
		selnum=random.randint(1,45)
		
		while selnum in mlist:
			selnum=random.randint(1,45)
		
		mlist.append(selnum)
	
	mlist.sort()
	bmlist=mlist
	rcs.append(mlist)
	
for i in range(3):
	
	shuffle(rcs)
print("avera 개수 :", len(rcs))

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
global rcb
def nrc_make(rcb):
	nrc=random.choice(rcs)
	nrc_chk=set(nrc) & set(rcb)
	if len(nrc_chk) < 1:
		nrc_make(rcb)

	nrc_same_chk=list(set(nrc))
	
	if len(nrc_same_chk) > 6:
		nrc_make(rcb)

	return nrc

def choice_rc(rcb):
	
	if len(rcb) == 6:
		
		rc=nrc_make(rcb)
		
	else:
		rc=random.choice(rcs)
	rcb=rc
	return rc
rate_per=0

rcb=[0]
for i in range(amount):
	rc=choice_rc(rcb)
	
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
		print(rc, test_rc, len(test_rc), )
	if test != "test":
			
			print(rc)
if test =="test":
	check_top_nums=set(first_list) & set(favorit_list)
	per_fav=len(check_top_nums)/23 *100
	print("상위 리스트 적중 확률 :",per_fav,"%")
	print(list(check_top_nums))
	rate_per=rate_per/amount*100
	print("총 당첨 확률 :",rate_per,"%")
	a3=0
	a4=0
	a5=0
	a6=0
	for i in range(len(rcs)):
		rcs_list=rcs[i]
		chk_rcs_list=set(rcs_list) & set(after_list)
		if len(chk_rcs_list) == 3:
		
			a3=a3+1
		if len(chk_rcs_list) == 4:
		
			a4=a4+1
		if len(chk_rcs_list) == 5:
		
			a5=a5+1	
		if len(chk_rcs_list) == 6:
		
			a6=a6+1
			
	print("전체 연산된 리스트 중... 3개 적중 :",a3," 4개 적중 :",a4,"  5개 적중 :",a5," 6개 적중 :",a6)
		
	
