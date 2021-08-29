# randlot

This Repositries is make randomic numbers program for Lotto of korea (6/45)

## Version

Version=0.1-29

## 설명

본 프로그램은 인터넷에 연결된 상태로 작동 되므로 "동행로또(https://dhlottery.co.kr)" 사이트에서 직접 데이타를 받아 번호를 연산 (고/저, 홀짝,소수 분석, 미출현 번호 분석, 날짜분석) 하고 그에 따른 확률을 기반으로 추천 미지수 번호를 추출 합니다.

## 지원 운영체제

linux - debian - ubuntu

## 지원 아키텍쳐

all

## 의존성 패키지

python3, fonts-nanum, python3-openpyxl, gnumeric, python3-korean_lunar_calendar, python3-pandas, language-pack-ko, lynx

## 설치 (Install)

	git clone https://github.com/cosmosp2/randlot.git
	cd randlot
	
## 업데이트 사항 

	1. 버그 수정 및 최적화 
	2. 매치 포인트 연산 도입

## 우분투 이거나 apt-get 사용의 경우 의존성 설치

	sudo apt-get install language-pack-ko python3 python3-openpyxl gnumeric python3-pandas fonts-nanum lynx

## 파이썬 라이브러리 설치

	pip3 install korean_lunar_calendar

## 사용 방법

	./randlot --help

### 문답형으로 시작할 경우

	./randlot 

### 옵션파일을 적용하여 바로 시작할 경우

	./randlot option.conf

# 제작자 (Maintainer)

Hanle Os를 꿈꾸며  https://cosmosproject2015.tistory.com/

Email : cosmosproject15@gmail.com

# 라이센스 (License)

GPL-2.0
