from datetime import date, datetime


class AbsoluteDifference:

    def __init__(self,input_number):
        self._input_number = input_number
        

    def checkTestCaseNumber(self):
        try:
            self._iterator = int(self._input_number)
            return True
        except Exception:
            return False
        
    def correctZone(self,d):
        zone=d.split(' ')[-1]
        if len(zone)==4:
            d=d.replace(f" {zone}","+"+zone)
        return d
        

    def checkInput(self,d):
        fmt = '%a %d %b %Y %H:%M:%S %z'
        d=self.correctZone(d)
        try:
            datetime.strptime(d, fmt)
            return True
        except Exception as e:
            print("Wrong Input", e)
            return False

    def calculator(self,inputs):
        fmt = '%a %d %b %Y %H:%M:%S %z'
        # print(self._iterator)
        result =[]
        if int(self._input_number)>0:
            inputs=inputs[:2*int(self._input_number)]    
            for idx in range(0,len(inputs),2):
                d1 = inputs[idx]#.pop(0)
                d2 = inputs[idx+1]
                
                if self.checkInput(d1) and self.checkInput(d2):
                    d1=self.correctZone(d1)
                    d2=self.correctZone(d2)
                    dt1 = datetime.strptime(d1, fmt)

                    # error check
                    _day1 = d1.split(' ')[0]
                    if dt1.strftime("%a") != _day1:
                        raise ValueError("Wrong Weekday")
                    if int(dt1.strftime("%Y")) > 3000:
                        raise ValueError("Year > 3000")
                    dt2 = datetime.strptime(d2, fmt)

                    # error check
                    _day2 = d2.split(' ')[0]
                    if dt2.strftime("%a") != _day2:
                        raise ValueError("Wrong Weekday")
                    if int(dt2.strftime("%Y")) > 3000:
                        raise ValueError("Year > 3000")
                    dt2 = datetime.strptime(d2, fmt)
                    x = abs( int((dt1-dt2).total_seconds()) )
                    result.append(x)
            if int(self._input_number)>int(len(inputs)//2):
                result.append("Skipped some inputs")    
        return result

