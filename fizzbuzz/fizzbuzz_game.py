class FizzBuzz:
    def __init__(self):
        pass

    def isDivisibleBy(self, divisor, dividend):
        return divisor % dividend == 0

    def calculate(self, number):
        number = int(number)
        buffer = ""

        if not (self.isDivisibleBy(number, 3) or self.isDivisibleBy(number, 5)):
            buffer = str(number)
        else:
            if self.isDivisibleBy(number, 3):
                buffer += "fizz"
            if self.isDivisibleBy(number, 5):
                buffer += "buzz"
        
        return buffer