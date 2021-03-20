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


import multiprocessing
import time
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
import warnings


nnum=int(sys.argv[1])
bnum=int(sys.argv[2])
amount=int(sys.argv[3])
avera=int(sys.argv[4])
half=int(sys.argv[5])
date=str(sys.argv[6])
camel=str(sys.argv[7])
test=str(sys.argv[8])

cc=os.cpu_count()
stime=time.time()

snum=nnum-bnum
value=2
warnings.simplefilter("ignore")

load_wb = load_workbook("/tmp/randlot_data.xlsx", data_only=True)
sheet=load_wb.active
warnings.simplefilter("default")
warnings.simplefilter("ignore")

sheet.title = "1"
load_ws = load_wb["1"]


# 오리지날 리스트
olist=list(range(1,46))
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
print("\n기본 분석 현황")
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
	print("이전 회차는 소수가 더 많이 출현 했었습니다.")
	
if len(sosuc) < 3:
	print("이전 회차는 소수가 더 적게 출현 했습니다.")
	
	
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
			

print("사전 조합 개수 자동 설정... 총 ",avera,"개로 계산됨.")


		
for i in range(cc*2):
	shuffle(first)

for i in range(cc*2):
	shuffle(second)

for i in range(cc*2):
	shuffle(third)

for i in range(cc*2):
	shuffle(fourth)

for i in range(cc*2):
	shuffle(five)

for i in range(cc*2):
	shuffle(six)

# 기초 확률 순위 계산

ranlists=first+second+third+fourth+five+six

with open('/tmp/randlot/nums', 'r') as f:
	list_file = f.readlines()
alist = [line.rstrip('\n') for line in list_file] 
for i in range(len(alist)):
	ai=alist[i]
	ai=ai.split()
	ai=list(map(int, ai))
	ais=ai[1]/7
	ais=int(ais)
	for i in range(ais):
		ranlists.append(ai[0])

ranlists_dict={}
for i in range(45):
	ai=i+1
	aic=ranlists.count(ai)
	ranlists_dict[ai]=aic
sort_of_ranlists_dict=sorted(ranlists_dict.items(), key=operator.itemgetter(1), reverse=True )

# 기초 난수 평준화 및 재작성

print("기초 평준화 계산 및 재작성")
nums=0


nums=int(nums/45/8)


ptn=[3,2,1,0,1,2,3,3,2,1,0,1,2,3,3,2,1,0,1,2,3,3,2,1,0,1,2,3,3,2,1,0,1,2,3,3,2,1,0,1,2,3,3,2,1]
for i in range(45):
	ia=i+1
	selptn=ptn[i]
	for item in range(selptn*nums):
		ranlists.append(ia)


# 본격 사전 조합 생성 함수 

for i in range(2):
	shuffle(ranlists)

def make_num():
	r=random.choice(ranlists)
	if r in mlist:
		make_num()		
	for i in range(1):
		ranlists.append(r)	
	return r

def make_mlist():
	global mlist
	mlist=[]
	for i in range(6):
		r=make_num()
		mlist.append(r)
	miner_nums=list(set(olist)-set(mlist))
	for i in range(len(miner_nums)):
		sel_num=miner_nums[i]	
		for i in range(2):
			ranlists.append(sel_num)
	return mlist
	

rcs=[]
rcss=[]

proc_avera=int(avera/cc)
numproc=range(0,cc)

if cc > 1:
	print("\n귀하의 PC의 코어가",cc,"개 로 확인 되었습니다. 멀티프로세싱을 활용 하여 연산 합니다.")
	ac=int(cc/2)
else:
	ac=1

# 멀티 프로세싱 기반의 연산 작업 시작

os.system('cat /dev/null > /tmp/randlot_averas')


def proc_make(numproc):
	file=open('/tmp/randlot_averas' , 'a')
	for i in range(proc_avera):
		mlist=make_mlist()
		mlist.sort()
		data=str(mlist)
		data=data.strip('[]')
		file.write(data+"\n")
	file.close()

if __name__ == '__main__':
	#멀티 쓰레딩 Pool 사용
	pool = multiprocessing.Pool(processes=cc) # 현재 시스템에서 사용 할 프로세스 개수
	pool.map(proc_make, numproc)
	pool.close()
	pool.join()

with open('/tmp/randlot_averas', 'r') as f:
	list_file = f.readlines()
alist = [line.rstrip('\n') for line in list_file] 

rcs=[]
for i in range(len(alist)):
	ai=alist[i]
	dot=','
	ai=ai.split(dot)
	ai=list(map(int, ai))
	chk_ai=list(set(ai))
	if len(chk_ai) == 6:
		
		rcs.append(ai)

for i in range(cc):
	
	shuffle(rcs)
print("\n실제 연산된 리스트 개수 :", len(rcs))


# 연산된 난수 총 순위

ranlists=[]
for i in range(len(rcs)):
	ai=rcs[i]
	for i in range(6):
		ri=ai[i]
		ranlists.append(ri)
		
ranlists_dict={}
for i in range(45):
	ai=i+1
	aic=ranlists.count(ai)
	ranlists_dict[ai]=aic
sort_of_coumputed_list=sorted(ranlists_dict.items(), key=operator.itemgetter(1), reverse=True )

# 연산된 난수 평준화 및 재작성

favorit_list=[]
for i in range(23):
	favorit=sort_of_ranlists_dict[i]
	favorit=favorit[0]
	favorit_list.append(favorit)

low_list=[]
for i in range(22):
	seven=sort_of_ranlists_dict[-i]
	seven=seven[0]
	low_list.append(seven)

seven_list=[]
for i in range(7):
	seven=sort_of_ranlists_dict[i]
	seven=seven[0]
	seven_list.append(seven)


ranlists_average=len(ranlists)/45

upper_count=int(ranlists_average/45*3)


if upper_count < 2 and upper_count < 1:
	upper_count = 2
	half_upper_count=1

half_upper_count=int(upper_count/2)

if half_upper_count < 1:
	half_upper_count = 1

print("\n연산된 승격 합산 수:", upper_count, half_upper_count)


ranlists_dict_average={}
for i in range(45):
	ai=i+1
	ranlists_dict_average[ai]=(ranlists_dict[ai]-ranlists_average)/3.14/45+ranlists_average
	

after_flist=[]
for i in range(23):
	favorit=sort_of_coumputed_list[i]
	favorit=favorit[0]
	after_flist.append(favorit)


print("\n연산된 난수 순위와 평준화")
computed_lists=[]
for i in range(45):
	computed_list=[]
	ai=i+1
	fnum=sort_of_coumputed_list[i]
	fnum=fnum[0]
	computed_list.append(sort_of_coumputed_list[i])
	computed_list.append(ranlists_dict_average[fnum])
	computed_lists.append(computed_list)

print(computed_lists)

ranlists=[]
for i in range(45):
	ai=i+1
	wr=ranlists_dict_average[ai]
	wr=int(wr)
	for i in range(wr):
		ranlists.append(ai)

	
computed_favorit_list=[]
for i in range(23):
	seven=sort_of_coumputed_list[i]
	seven=seven[0]
	computed_favorit_list.append(seven)


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
			print("\n테스트 적용 회차: ", after_num, " 의 당첨번호는 ",after_list,"입니다.")

	after_list=set(after_list)

# 각 연산 전 연산 후 상위 리스트 

top_of_sort_of_ranlists_dict=[]
for i in range(23):
	li=sort_of_ranlists_dict[i]
	top_of_sort_of_ranlists_dict.append(li)

top_sort_of_coumputed_list=[]
for i in range(7):
	li=sort_of_coumputed_list[i]
	top_sort_of_coumputed_list.append(li)


hists=[]

rate_per=0
hist=[]
dnot_hist_list=olist
firsts=[]
lasts=[]
three=[]
brc=nrc=random.choice(rcs)
rcns=[]
not_list=list(range(1,46))
print("\n추천 번호 출력")


for i in range(amount):
	
	folk_lists=[]
	rc=[]
	while len(set(computed_favorit_list) & set(rc)) < 3 and len(set(favorit_list) & set(rc)) < 3:
		rc=[]
		for i in range(6):
			crs=set(ranlists) - set(rc)
			crs=list(crs)
			r=random.choice(crs)
			
			# 연산된 난수의 승격
			for i in range(half_upper_count):
				ranlists.append(r)
			rc.append(r)
	rc.sort()
	
	miner_nums=list(set(olist)-set(rc))
	for i in range(len(miner_nums)):
		sel_num=miner_nums[i]	
		for i in range(upper_count):
			ranlists.append(sel_num)
	brc=rc
	rcns.append(rc)
	for i in range(6):
		if rc[i] in not_list:
			not_list.remove(rc[i])

	if rc in not_list:
		not_list.remove(i)

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

# 테스트 출력

if test =="test":
	check_top_nums=set(after_list) & set(favorit_list)

	per_fav=len(check_top_nums)/23 *100
	print("\n기초 확률 상위 리스트 적중 확률 :",per_fav,"%")
	print(check_top_nums)

	check_top_nums=set(after_list) & set(computed_favorit_list)
	per_fav=len(check_top_nums)/23 *100
	print("\n연산 상위 리스트 적중 확률 :",per_fav,"%")
	print(check_top_nums)
	a3=0
	a4=0
	a5=0
	a6=0
	for i in range(len(rcs)):
		rcs_list = rcs[i]
		chk_rcs_list=set(rcs_list) & set(after_list)
		if len(chk_rcs_list) == 3:
			a3=a3+1
		if len(chk_rcs_list) == 4:
			a4=a4+1
		if len(chk_rcs_list) == 5:
			a5=a5+1	
		if len(chk_rcs_list) == 6:
			a6=a6+1
	print("전체 연산된 리스트", len(rcs),"가지 경우 중... 3개 적중 :",a3," 4개 적중 :",a4,"  5개 적중 :",a5," 6개 적중 :",a6)

if test =="test":
	rate_per=rate_per/amount*100
	print("\n총 출력 된 추천 번호들의 총 당첨 확률 :",rate_per,"%")
	a3=0
	a4=0
	a5=0
	a6=0
	for i in range(len(rcns)):
		rcs_list=rcns[i]
		chk_rcs_list=set(rcs_list) & set(after_list)
		if len(chk_rcs_list) == 3:
			a3=a3+1
		if len(chk_rcs_list) == 4:
			a4=a4+1
		if len(chk_rcs_list) == 5:
			a5=a5+1	
		if len(chk_rcs_list) == 6:
			a6=a6+1
	print("전체 출력된 추천 리스트", len(rcns),"개 중... 3개 적중 :",a3," 4개 적중 :",a4,"  5개 적중 :",a5," 6개 적중 :",a6)
		
etime=time.time()
proc_time=etime-stime
print("\n연산에 걸린 총 시간은", int(proc_time) , "초 입니다.")

print("비출현 번호 : ", not_list)


