class computer:
    def __init__(self):
        self.__maxprice=900
    def sell(self):
        print('Selling price:',self.__maxprice)
    def setmaxprice(self,price):
        self.__maxprice=price
com=computer()
com.sell()
com.__maxprice=1200  
com.sell()
com.setmaxprice(1200)
com.sell()              
        