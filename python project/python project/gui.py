from tkinter import *
from tkinter import messagebox

import myfilenew
import monthly_repo
import sevenmonthcom

def repo():
    try:
        print(item_id.get(),mon.get(),years.get())
        i=int(item_id.get())
        if i==956014:
           f="data2.csv"
        elif i==956013:
           f="data3.csv"
        elif i==956012:
           f="data4.csv"
        elif i==956011:
           f="data5.csv"
        elif i==119624:
           f="data6.csv"
        elif i==123601:
           f="data7.csv"   
        elif i==153267:
           f="data8.csv"
        elif i==122425:
           f="data9.csv"
        elif i==153239:
           f="data10.csv"
        elif i==111397:
           f="data11.csv"
        if (int(years.get())<=2016) or (int(years.get())>2023):
            messagebox.showerror(title="Error",message="Please Enter correct values years range should be(2017-2023)",parent=window)
        else:    
            myfilenew.predict_data(f,mon.get(),int(years.get()))
    except:
        messagebox.showerror(title="Error",message="Please Enter correct values year's range should be(2017-2021)\nPlease Enter correct Month First Letter Should be Capital",parent=window)
def clear():
    item_id.set('')
    mon.set('')
    years.set('')
 
def monrepo():
    try:
        print(item_id.get())
        i=int(item_id.get())
        if i==956014:
           f="data2.csv"
           monthly_repo.monthly_data(f)
        elif i==956013:
           f="data3.csv"
           monthly_repo.monthly_data(f)
        elif i==956012:
           f="data4.csv"
           monthly_repo.monthly_data(f)
        elif i==956011:
           f="data5.csv"
           monthly_repo.monthly_data(f)
        elif i==119624:
           f="data6.csv"
           monthly_repo.monthly_data(f)
        elif i==123601:
           f="data7.csv"   
        elif i==153267:
           f="data8.csv"
           monthly_repo.monthly_data(f)
        elif i==122425:
           f="data9.csv"
           monthly_repo.monthly_data(f)
        elif i==153239:
           f="data10.csv"
           monthly_repo.monthly_data(f)
        elif i==111397:
           f="data11.csv"
           monthly_repo.monthly_data(f)
        else:  
            messagebox.showerror(title="Error",message="Please Enter correct Item Code",parent=window)
      
        #print(f)
        
    except:
        messagebox.showerror(title="Error",message="Please Enter correct Item Code",parent=window)  
       

def accuracy():
    try:
        print(item_id.get())
        i=int(item_id.get())
        if i==956014:
           f="data2.csv"
           sevenmonthcom.testing_data(f)
        elif i==956013:
           f="data3.csv"
           sevenmonthcom.testing_data(f)
        elif i==956012:
           f="data4.csv"
           sevenmonthcom.testing_data(f)
        elif i==956011:
           f="data5.csv"
           sevenmonthcom.testing_data(f)
        elif i==119624:
           f="data6.csv"
           sevenmonthcom.testing_data(f)
        elif i==123601:
           f="data7.csv"
           sevenmonthcom.testing_data(f)
        elif i==153267:
           f="data8.csv"
           sevenmonthcom.testing_data(f)
        elif i==122425:
           f="data9.csv"
           sevenmonthcom.testing_data(f)
        elif i==153239:
           f="data10.csv"
           sevenmonthcom.testing_data(f)
        elif i==111397:
           f="data11.csv"
           sevenmonthcom.testing_data(f)
        else:
            messagebox.showerror(title="Error",message="Please Enter correct Item Code",parent=window)
            
    except:
        messagebox.showerror(title="Error",message="Please Enter correct Item Code",parent=window)
        
    
window=Tk()

item_id=StringVar()
mon=StringVar()
years=StringVar()



window.title("My App")
window.geometry("800x400+700+200")

ptitle=Label(window,text='SALES FORECASTINGT USING MACHINE LEARNING',fg="red",bg="white")
ptitle.place(x=50,y=30)


l0=Label(window,text="Item Code",width=20,font=("bold",10),anchor='w')
l0.place(x=80,y=100)
e0=Entry(window,textvariable=item_id)
e0.place(x=150,y=100)
l1=Label(window,text="Month",width=20,font=("bold",10),anchor='w').place(x=80,y=130)
e1=Entry(window,textvariable=mon).place(x=150,y=130)
l2=Label(window,text="Year",width=20,font=("bold",10),anchor='w').place(x=80,y=160)
e2=Entry(window,textvariable=years).place(x=150,y=160)



b4=Button(window,text="Generate Forcast Report",command=repo).place(x=50,y=190)
b5=Button(window,text="Clear",command=clear).place(x=220,y=190)

b6=Button(window,text="Predicting Accuracy",command=accuracy).place(x=300,y=190)
b7=Button(window,text="Monthly Report",command=monrepo).place(x=420,y=190)
        


window.mainloop()
