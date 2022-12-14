'''
# Maths Functions
'''
def add(num1, num2):
    sum = num1 + num2
    return sum

def text_add(num1, num2):
    sum = num1 + num2
    return f"The sum is {sum}"

def subtract(num1, num2):
    dif = num1 - num2
    return dif

def text_subtract(num1, num2):
    dif = num1 - num2
    return f"The difference is {dif}"

def multiply(num1, num2):
    prod = num1*num2
    return prod

def text_multiply(num1, num2):
    prod = num1*num2
    return f"The Product is {prod}"

def divide(num1, num2):
    div = num1/num2
    return div

def text_divide(num1, num2):
    div = num1/num2
    return f"The quotient is {div}"

# Graphs
import numpy as np
import matplotlibpyplot as plt

'''
# Cosine Graph
'''
def cosine(x,y):
    x = np.arange(0, 10, 0.1);

    y = np.cos(x)

    plt.plt(x, y)

    plt.title('cosine wave')

    plt.xlabel('x')

    plt.ylabel('y = cos(x)')
    plt.grid(True, which='both')
    plt.axhline(y=0, color='k')

    plt.show()

'''
# Cubic Graph
'''
def cubic(x,y):
    x = np.linspace(-5,5,100)
    y = x**3

    figure = plt.figure()
    figure.add_subplot(1,1,1).spines['left'].set_position('center')
    figure.add_subplot(1,1,1).spines['bottom'].set_position('center')
    figure.add_subplot(1,1,1).spines['right'].set_color('none')
    figure.add_subplot(1,1,1).spines['top'].set_color('none')
    figure.add_subplot(1,1,1).xaxis.set_ticks_position('bottom')
    figure.add_subplot(1,1,1).yaxis.set_ticks_position('left')

    plt.plot(x,y, 'g')

    plt.show()

'''
# Logistic Map
'''
def logistic_map(rate, init_percentage, iterations):
    years = []
    percentages = []
    for year in range(iterations+1):
        years.append(year)
        if year==0:
            percentage = init_percentage

        else:
            percentage = rate*percentages[-1]*(1-percentages[-1])

        percentages.append(percentage)
        print(f"{year} - {percentage*100}%")

    plt.plot(years,percentages)
    plt.ylabel('Value%')
    plt.xlabel('Year')
    plt.title(f"Percentage graph for {iterations} years \nif initial_percentage = {init_percentage*100}% and Growth Rate = {rate}")
    plt.show()

'''
# Quadratic Graph
'''
def quad(x,y):
    x = np.linspace(-5,5,100)
    y = x**2

    figure = plt.figure()
    figure.add_subplot(1,1,1).spines['left'].set_position('center')
    figure.add_subplot(1,1,1).spines['bottom'].set_position('zero')
    figure.add_subplot(1,1,1).spines['right'].set_color('none')
    figure.add_subplot(1,1,1).spines['top'].set_color('none')
    figure.add_subplot(1,1,1).xaxis.set_ticks_position('bottom')
    figure.add_subplot(1,1,1).yaxis.set_ticks_position('left')

    plt.plot(x,y, 'r')

    plt.show()

'''
# Text to File Converter
'''
def convert_to_file(enter_text):
    import os

    while True:
        enterText = input("Enter Text to Input into File:- \n")
        with open("text.txt", "a") as f:
            f.write(enterText)
        
        with open("text.txt", "r") as f:
            print(f"The text in the file is '{f.read()}'\n")

        qontinue = input("Do you want to add more text?(y/n/clear text)")
        
        if qontinue in ["y","yes","Yes","YES", "Y"]:
            continue
        
        elif qontinue in ["n","no","No","NO", "N", ""]:
            break

        elif qontinue in ["clear text", "cleartext", "clear", "Clear Text", "CLEARTEXT", "clearText", "CLEAR"]:
            file = "text.txt"
            os.remove(file)
            break

        else:
            print("Please enter y, n, clear text")
            continue

'''
# CSV to Excel Converter
'''
import pandas as pd 
def makeExcel(CSV, Excel):
    CSV = input("Enter the path to your CSV: ")
    excelconvert = pd.read_csv(CSV)
    excel = input("Enter papth where you have to save excel file")
    excelconvert.to_excel(excel)
    print(f"{CSV} converted to .xlsx")
'''
# Convert Your Age to Months and Days
'''
import time
from calendar import isleap
def age_to_months(age):
    # judge the leap year
    def judge_leap_year(year):
        if isleap(year):
            return True
        else:
            return False


    # returns the number of days in each month
    def month_days(month, leap_year):
        if month in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        elif month in [4, 6, 9, 11]:
            return 30
        elif month == 2 and leap_year:
            return 29
        elif month == 2 and (not leap_year):
            return 28

    localtime = time.localtime(time.time())

    year = int(age)
    month = year * 12 + localtime.tm_mon
    day = 0

    begin_year = int(localtime.tm_year) - year
    end_year = begin_year + year

    # calculate the days
    for y in range(begin_year, end_year):
        if (judge_leap_year(y)):
            day = day + 366
    else:
        day = day + 365

    leap_year = judge_leap_year(localtime.tm_year)
    for m in range(1, localtime.tm_mon):
        day = day + month_days(m, leap_year)

    day = day + localtime.tm_mday
    print("Your age is %d years or " % (year), end="")
    print("%d months or %d days" % (month, day))

'''
# Autoclicker
'''
import pyautogui
import time

def auto_click(x, y, clicks, time):
    for i in range(clicks):
        pyautogui.click(x, y)
        time.sleep(time)