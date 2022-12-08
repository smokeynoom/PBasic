'''
Maths Functions
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
Cosine Graph
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
Cubic Graph
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
Logistic Map
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
Quadratic Graph
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
Text to File Converter
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