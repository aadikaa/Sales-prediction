# reading data of a particular store from train.csv and writing in data.csv
import csv
import sys

#input number you want to search
Store_number = input('Enter number to find\n')
item_no=input('Enter item number\n')#111397
#read csv, and split on "," the line
csv_file = csv.reader(open('train.csv',"r"), delimiter=",")
f=open('data11.csv', 'w')

#loop through csv list
for row in csv_file:
    #if current rows 2nd value is equal to input, print that row
    if Store_number ==row[2] and item_no==row[3]:
         #print (row)
          for l in row:
             f.write(l)
             f.write(',')
          f.write('\n')   
f.close()             
             
              
