from datetime import date, datetime
# number of tests
try:
    test_number = int(input())
except Exception as e:
    print("Not a valid test case:",e)
    exit(1) 
fmt = '%a %d %b %Y %H:%M:%S %z'

def checkInput(d):
    try:
        dt=datetime.strptime(d, fmt)
        return True
    except Exception as e:
        print("Wrong Input",e)
        return False
    
for t in range(test_number):
    d1=input()
    d2=input()
    if checkInput(d1) and checkInput(d2):
        dt1=datetime.strptime(d1, fmt)
    
        # error check
        _day1=d1.split(' ')[0]
        if dt1.strftime("%a") !=_day1:
            raise ValueError("Wrong Weekday")
        if int(dt1.strftime("%Y")) > 3000:
            raise ValueError("Year > 3000")
        dt2=datetime.strptime(d2, fmt)
    
        # error check
        _day2=d2.split(' ')[0]
        if dt2.strftime("%a") !=_day2:
            raise ValueError("Wrong Weekday")
        if int(dt2.strftime("%Y")) > 3000:
            raise ValueError("Year > 3000")
        dt2=datetime.strptime(d2, fmt)
        print(abs(int((dt1-dt2).total_seconds())))
        
       
'''
Sun 10 May 2015 13:54:36 -0700
Sun 10 May 2015 13:54:36 -0000
Sat 02 May 2015 19:54:36 +0530
Fri 01 May 2015 13:54:36 -0000
'''