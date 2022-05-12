import pandas as pd
import numpy as mp
import yfinance as yf
import requests
from yahoo_fin import stock_info as si
import matplotlib.pyplot as plt

def s():
    x = input("Enter Your Company Ticker:")
    stock = yf.Ticker(x)
    def p_value():
        y = input("Use Company PEG or Peter's PEG(C/P):")
        if y.lower() == 'c':
            a = si.get_stats_valuation(x)
            df = pd.DataFrame(a)
            PEG = float((df.iloc[4, 1]))
            return PEG
        elif y.lower() == 'p':
            PEG = 1
            return PEG
        else:
            print('Invalid Input! Try Again')
            p_value()
    PEG = p_value()
    
    print("Gathering Data.....")
   
    str1 = 'https://www.marketwatch.com/investing/stock/{}/company-profile?mod=mw_quote_tab'
    url = str1.format(x)

    df1 = pd.read_html(url, header=0)
    dfebitda = df1[4]
    EBITDA = float(dfebitda.iloc[5, 1])

    b = si.get_quote_table(x)

    EPS = float((b['EPS (TTM)']))

    fairvalue = PEG * EBITDA * EPS

    currentprice = stock.history()
    last_quote = (currentprice.tail(1)['Close'].iloc[0])

    print("{} has a PEG Ratio of {}".format(x.upper(), PEG))
    print("{} has an Enterprise Value to EBITDA of {}".format(x.upper(), EBITDA))
    print("{} has a Trailing Twelve Months EPS of {}".format(x.upper(), EPS))
    print("Generating Peter Lynch Fair Value for {}.....".format(x.upper()))
    print("Fair Value of {} is ${}".format(x.upper(), round(fairvalue, 2)))
    print("Current Trade Price of {} is {} and Fair Value is {}".format(x.upper(), round(last_quote,2), round(fairvalue,2)))

    plt.bar(-0.2, last_quote, width=0.04, color='b', align='center')
    plt.bar(+0.2, fairvalue, width=0.04, color='r', align='center')
    plt.title("{} Current Price vs. Peter Lynch Fair Value".format(x.upper()))
    plt.ylabel("Price($)")
    plt.xticks([])
    plt.legend(["Current Price", "P.Lynch Fair Value"])
    plt.show()
    y_n()
def y_n ():
    j = input("Check Another Stock(Y/n)?:")
    if j.upper() == 'Y':
        print("------------------------------------")
        s()
    elif j.upper() == 'N':
        exit()
    else:
        print("Invalid Input, Try Again!")
        y_n()

s()

