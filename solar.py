"""Assignment-8
Author: Srikanth Thadigol Reddappa
Date: 08/26/2017
Date: 08/26/2017
This python script will print the date and places where you can see the total solar in the 21st century for a given period
and plots the bar graph of magnitude for every year during the period
"""

import csv
import matplotlib.pyplot as plt
import numpy as np
import sys
import time

#.csv containing the data on year, date, magnitude and places you will see the total solar eclipse
myfile="data.csv"

# initiate dictionary to create key value pairs from the csv file
my_dict=[]

try:
    file=csv.DictReader(open(myfile, 'r'))
except FileNotFoundError:
    print("File doesn't exist")
except Exception as e:
    print("Error:", e)
finally:
     if file:
        # create key value pairs from the csv file
        for row in file:
            my_dict.append(row)

def remove_non_ascii(text):
    """
    Arguments:
    string: input string for which special characters need to replaces with space
    """
    return ''.join(i for i in text if ord(i)<128)


def main(start,end):
    """
         Arguments:
         start : starting year from when you want to search the data file for solar eclipse
         end: end year until when you want to search the data file for solar eclipse
    """
    print (start,end)
    dict_key_start = start
    dict_key_end = end
    y_key="year"
    m_key="magnitude"
    counter=0
    # lists to store the year and magnitude to plot the graph
    list_year=[]
    list_magnitude=[]

    # parsing each column of a row to find the solar eclipse based on the user inputs
    for row in my_dict:
        for col in row:
            if int(row[y_key]) >= int(dict_key_start) and int(row[y_key]) <= int(dict_key_end):
                print(col,": ",remove_non_ascii(row[col]))
                counter = counter + 1
                if col==m_key:
                    list_magnitude.append(row[col])
                    print("\n")
                if col==y_key:
                    list_year.append(row[col])
            else:
                pass

    if counter>1:
        print("you will see total eclipse {} time during {} and {}" .format(int(counter/3), dict_key_start,dict_key_end), "in the following years:")
        for i in list_year:
            print(i)
        plt.ylim([1.0, 1.09])
        y_pos = np.arange(len(list_year))
        plt.bar(y_pos, list_magnitude, align='center', alpha=0.5, color='r')
        plt.xticks(y_pos, list_year)
        plt.xlabel('Year')
        #naming the y-axis
        plt.ylabel('Magnitude')
        #plot title
        plt.title('Solar Eclipse during the period of {} and {}'.format(dict_key_start, dict_key_end))
        plt.show()
    else:
         print("No Total Solar eclipse during this period")

if __name__ == "__main__":
    if len(sys.argv)!=3:
        print("usage: python solar.py <start year> <end year>")
    elif sys.argv[2]< sys.argv[1]:
        print("<end year> should be greater than <start year>")
    elif int(sys.argv[1])<2000 or int(sys.argv[1])>2100:
        print("<start year> should be in the 21st century")
    elif int(sys.argv[2])<2000 or int(sys.argv[2])>2100:
        print("<end year> should be in the 21st century")
    elif len(sys.argv)==3:
        start_year = sys.argv[1]
        end_year = sys.argv[2]
        print ("fecthing data............................................")
        time.sleep(3)
        main(start_year, end_year)
