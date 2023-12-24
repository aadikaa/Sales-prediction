import csv
import sys
import numpy as np
import matplotlib.pyplot as plt
def testing_data(filename):
     months=["01","02","03","04","05","06","07"]
     years=[2017]
     yearrs=[2013,2014,2015,2016]
     month_arr=["Jan","Feb","March","April","May","June","July","Aug","Sep","Oct","Nov","Dec"]
     month_arr2=["Jan","Feb","March","April","May","June","July"]
     a = [[0 for x in range(1)] for y in range(7)]#Five rows 12 for years, columns for months
     avg=list(range(4))#for average of total (jan to dec)12 months in 5 years average
     total_annual_s=list(range(4))
     total_annual_sale=0.0
     ys=[]
     frcst=[]
     arrr=[]
     act=[]
     tempr=[]
     temp=0.0
     s=0
     b = [[0 for x in range(4)] for y in range(7)]#Five rows 12 for years, columns for months
     for m in range(0,7):
     
     
     
          for i in range(0,1):
    
               csv_file = csv.reader(open(filename,"r"), delimiter=",")
          
               sum=0.0
               #loop through csv list
               for row in csv_file:
                   arr=row[1].split("-")
                   
                   if arr[0] ==str(years[i]) and arr[1]==months[m]:
                        sum=sum+float(row[4])
                   
               a[m][i]=sum   
     for k in range(0,1):
          total_annual_sale=0.0
          for i in range(0,7):
               total_annual_sale=a[i][k]
               act.append(total_annual_sale)
     print("Actual values of "+str(month_arr2)+" in 2017 ")
     print(act)
     for m in range(0,7):
     
     
     
          for i in range(0,4):
    
               csv_file = csv.reader(open(filename,"r"), delimiter=",")
          
               sum=0.0
               #loop through csv list
               for row in csv_file:
                   arrr=row[1].split("-")
          
                   if arrr[0] ==str(yearrs[i]) and arrr[1]==months[m]:
                        sum=sum+float(row[4])
               b[m][i]=sum
     
     for ab in range(0,7):
          for ac in range(0,4):
               ys.append(b[ab][ac])     
               if len(ys)==len(yearrs):
                    x=np.array(yearrs)
                    y=np.array(ys)
                    m=((( np.mean(x)* np.mean(y))-np.mean(x*y))/((np.mean(x)*np.mean(x))-np.mean(x*x)))
                    m=round(m,2)
                    b1=(np.mean(y)-np.mean(x)*m)
                    b1=round(b1,2)
                    reg_line=[(m*x)+b1 for x in yearrs]
                    print("Values of "+str(month_arr2[ab])+" in "+str(yearrs))
                    print(ys)
                    predict=(m*2017)+b1
                    frcst.insert(0,ys[0])       
                    for i in range(1,len(ys)):   
                         temp=frcst[i-1]
                         temp=((.2*ys[i])+(.8*temp))
                         frcst.insert(i+1,round(temp))
                    print("forcast using equation "+str(frcst[(len(frcst)-1)]))
                    ys.append(round(frcst[(len(frcst)-1)]))
                    yearrs.append(2017)
                    if len(ys)==len(yearrs):
                         x=np.array(yearrs)
                         y=np.array(ys)
                         m=((( np.mean(x)* np.mean(y))-np.mean(x*y))/((np.mean(x)*np.mean(x))-np.mean(x*x)))
                         m=round(m,2)
                         b1=(np.mean(y)-np.mean(x)*m)
                         b1=round(b1,2)
                         reg_line1=[(m*x)+b1 for x in yearrs]
                         predict=round((m*2017))+b1
                    avrge=round((predict+frcst[(len(frcst)-1)])/2)
                    tempr.append(round(avrge))
                    print("Predicted Sale of "+str(month_arr2[ab])+" = "+str(avrge))
          ys.clear()
          yearrs.remove(2017)
          frcst.clear()                                                                           
     print("Predicted values for "+str(month_arr2)+" in 2017")
     print(tempr)
     plt.plot(month_arr2,act,marker='+',color="green",label="Actual Values")
     plt.plot(month_arr2,tempr,marker='*',color="red",label="Predicted Values")
     plt.legend()
     plt.show()





