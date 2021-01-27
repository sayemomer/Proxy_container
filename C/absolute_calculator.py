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
        

    def checkInput(self,d):
        fmt = '%a %d %b %Y %H:%M:%S %z'
        try:
            datetime.strptime(d, fmt)
            return True
        except Exception as e:
            print("Wrong Input", e)
            return False

    def calculator(self,inputs):
        fmt = '%a %d %b %Y %H:%M:%S %z'
        for t in range(self._iterator):
            d1 = inputs.pop(0)
            d2 = inputs.pop(0)
            result =[]
            if self.checkInput(d1) and self.checkInput(d2):
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
            return result
