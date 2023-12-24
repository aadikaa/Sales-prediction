from tkinter import *

class Welcome():
    def __init__(self,master):
        self.master=master
        self.master.geometry("600x400+100+200")
        self.master.title("WELCOME")

        
        Label(master,text="Welcome To Wages Calculator GUI", fg="red",font=("bold",10),anchor='w').place(x=100,y=50)
        
       


        Button(master, text="OK",bg="red",fg="white", command=self.gotowages).place(x=200,y=100)
        
        Button(master, text="QUIT",bg="red",fg="white", command=self.finish).place(x=250,y=100)
        
    def finish(self):
         self.master.destroy()
         
    def gotowages(self):
         root2=Toplevel(self.master)
         MyGUI=Polution(root2)

class Polution():
    def __init__(self,master):
        self.master=master
        self.nhours=DoubleVar()
        self.salaryh=DoubleVar()
        
        self.master.geometry("500x200+100+200")
        self.master.title("Wages CAlculator")

        
        Label(master,text="Welcome To Wages Calculator GUI", fg="red",font=("bold",10),anchor='w').grid(row=0,column=2)
        
        Label(master,text="Enter your Salary per hour", fg="red",font=("bold",10),anchor='w').grid(row=3,column=0)
        
        
        Label(master,text="Enter the number of hours worked ", fg="red",width=20,font=("bold",10),anchor='w').grid(row=4,column=0)    

        self.mysalary=Entry(self.master,textvariable=self.salaryh).grid(row=3,column=2)
        self.myhours=Entry(self.master,textvariable=self.nhours).grid(row=4,column=2)
       


        Button(master, text="Calculate Salary",bg="red",fg="white",command=self.calcsal).grid(row=5,column=4)
        
        Button(master, text="Back",bg="red",fg="white",command=self.myquit).grid(row=5,column=6)

        
    def myquit(self):
          self.master.destroy()
         
    def calcsal(self):
           hours=self.nhours.get()
           print(hours)
           hsal=self.salaryh.get()
           salary=hours*hsal
           print(salary)
           Label(self.master,text="your salary is %.2f Rs."%salary).grid(row=7,column=2)
           

def main():
    root=Tk()
    myGUIWelcome=Welcome(root)
    root.mainloop()

    
if __name__=='__main__':
    main()
