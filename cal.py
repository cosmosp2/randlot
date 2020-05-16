from korean_lunar_calendar import KoreanLunarCalendar
import sys

calinfo=str(sys.argv[1])

ca1=calinfo[0:4]
ca2=calinfo[4:6]
ca3=calinfo[6:8]
Calendar = KoreanLunarCalendar()
Calendar.setSolarDate(int(ca1), int(ca2) , int(ca3))

minercal=str(Calendar.LunarIsoFormat())
minercal=minercal.replace("-","",2)
print(ca2+ca3+minercal[4:8])
