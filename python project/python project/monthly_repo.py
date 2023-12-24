# reading data of a particular store from train.csv and writing in data.csv
import csv
import sys
import numpy as np
import matplotlib.pyplot as plt
def monthly_data(filename):
     months=["01","02","03","04","05","06","07","08","09","10","11","12"]


     years=[2013,2014,2015,2016]
     month_arr=["Jan","Feb","March","April","May","June","July","Aug","Sep","Oct","Nov","Dec"]
     a = [[0 for x in range(4)] for y in range(12)]#Five rows 12 for years, columns for months
     avg=list(range(4))#for average of total (jan to dec)12 months in 5 years average
     total_annual_s=list(range(4))
     total_annual_sale=0.0

     for m in range(0,12):
     
     
     
          for i in range(0,4):
    
               csv_file = csv.reader(open(filename,"r"), delimiter=",")
          
               sum=0.0
               #loop through csv list
               for row in csv_file:
               #print(row[1])
                   arr=row[1].split("-")
          
                   if arr[0] ==str(years[i]) and arr[1]==months[m]:
                        #print (row[4])
                        sum=sum+float(row[4])
               #print("sum is %f"%sum)
               a[m][i]=sum
     
          #print(a[m][i]) 
     for k in range(0,4):
          total_annual_sale=0.0
          for i in range(0,12):
               total_annual_sale=total_annual_sale+a[i][k]
          avg[k]=total_annual_sale/12
          total_annual_s[k]=total_annual_sale
     

     print("Average of Annual Sale\n")
     print(avg)
     print("\n Monthly Sale\n")
     print(a)

#################For plotting monthly sale for five years 


     plt.figure(1,figsize=(8, 8))
     plt.subplot(211)
     plt.plot(month_arr,a,marker='+')
     plt.ylabel('Total Monthly Sale')
     plt.xlabel('Months')
     plt.title('Graph for Monthly Sale')
     plt.grid(True)
     plt.legend(years)

     plt.subplot(212)
     plt.plot(years,avg,marker='o', linestyle='--', color='r', label='Square') 
     plt.ylabel('Average Sale')
     plt.xlabel('Years')
     plt.title('Annual Sale')

     plt.show()          
     
             
             
              
#smonths=["01","02","03","04","05","06","07","08","09","10","11","12"]
'''months=["01","02"]

month_arr=["Jan","Feb","March","April","May","June","July","Aug","Sep","Oct","Nov","Dec"]
for m in range(0,2):
    monthly_data(months[m],month_arr[m])'''

