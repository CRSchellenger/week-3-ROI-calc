
import math
from operator import sub

class investment():
    def __init__(self):
        self.income = []
        self.expenses = []
        self.cashflow = []
        self.roi_1 = []
        self.total_r =[]
    def income_0(self):
        total= int(input('What is your income a month? '))
        print('=============================================')
        self.income.append(total)
    def expenses_0(self):
        expenses_1 = int(input('What is your expenses? '))
        print('=============================================')
        self.expenses.append(expenses_1)
    def cashflow_0(self):
        total_e = list(map(sub, self.income, self.expenses))
        for i in total_e:
            total_p = i *12
            self.total_r.append(total_p)
            total_c = i *1
        print(f'Your total annual cash flow is {total_p}')
        print(f'Your total monthly cash flow is {total_c}')
        print('=============================================')
    def roi(self):
	    downpayment = int(input('What is your downpayment? '))
	    print('=============================================')
	    closingcost = int(input('What is your closing cost '))
	    print('=============================================')
	    budget = int(input('What is your budget for the remodel if needed? '))
	    print('=============================================')
	    for i in self.total_r:
	        total_2 = downpayment + closingcost + budget
	        total_1 = i / total_2
	    print(f'your ROI is {total_1} %')

my_i = investment() #call function
my_i.income_0() #passed
my_i.expenses_0() #passed 
my_i.cashflow_0() #passed  
my_i.roi() #passed
