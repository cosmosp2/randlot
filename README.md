# randlot

This repositries is make randomic numbers program for Lotto of korea (6/45)

## Version

0.1-11

## 설명

본 프로그램은 인터넷에 연결된 상태로 작동 되므로 "동행로또(https://dhlottery.co.kr/)" 사이트에서 직접 데이타를 받아 번호를 연산 (고/저, 홀짝,소수 분석,미출현 번호,2진수 분석,양력,음력분석) 하여 추천 미지수 번호를 추출 합니다.

## 지원 운영체제

linux - debian - ubuntu

## 지원 아키텍쳐

all

## 의존성 패키지

python3, python3-openpyxl, gnumeric

## 설치 (Install)

	git clone https://github.com/cosmosp2/randlot.git
	cd randlot
	
## 업데이트 사항 

	1. 주역숫자 계산 도입

## 우분투 이거나 apt-get 사용의 경우 의존성 설치

	sudo apt-get install python3 python3-openpyxl gnumeric
	python3-korean_lunar_calendar

## 사용 방법

	./start [이전 회차] [데이타 적용 범위 회차] [출력 수(default 10)] [사전 조합 생성 개수(default 31459)] [반자동 출력 유무] [양력,음력날짜] [주역숫자 네자리] [테스트 여부]

## 예제

	./start 867 850 100 50000 half 04040312 3458 test

	./start 867 850

	./start 867

# 제작자 (Maintainer)

  COSMOS Project.2015
  https://cosmosproject2015.tistory.com/
  cosmosproject15@gmail.com

# 라이센스 (License)

	GPL2.0


