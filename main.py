import datetime
import tkinter
from tkinter import *
from tkinter import messagebox, ttk

import mysql.connector


class restaurantManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Restaurant Management System")
        self.root.geometry("1920x1080+0+0")


        # variable
        self.customer_var=StringVar()
        self.id_var=StringVar()
        self.firstname_var=StringVar()
        self.lastname_var=StringVar()
        self.phoneno_var=StringVar()
        self.orderid_var=StringVar()
        self.ordername_var=StringVar()
        self.timetP_var=StringVar()
        self.calories_var=StringVar()
        self.date_var=StringVar()
        self.gst_var=StringVar()
        self.serving_var=StringVar()
        self.totPrice_var=StringVar()


        



        lbltitle=Label(self.root,text="RESTAURANT MANAGEMENT SYSTEM",bg="powder blue",fg="navy blue",bd=20,relief=RIDGE,font=("times new roman",50,"bold"),padx=2,pady=6)
        lbltitle.pack(side=TOP, fill=X)


        frame=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        frame.place(x=0,y=130,width=1530,height=400)

        # Left Frame

        DataFrameLeft=LabelFrame(text="Customer Information",bg="powder blue",fg="navy blue",bd=12,relief=RIDGE,font=("times new roman",15,"bold"),padx=2,pady=6)
        DataFrameLeft.place(x=20,y=150,width=900,height=350)

        lblCustomer=Label(DataFrameLeft,bg="powder blue",text="Customer Type",font=("arial",12,"bold"),padx=2,pady=6)
        lblCustomer.grid(row=0,column=0,sticky=W)

        comCustomer=ttk.Combobox(DataFrameLeft,textvariable=self.customer_var,font=("arial",12),width=27,state="readonly")
        comCustomer["value"]=("Staff","Student","Lecturer")
        comCustomer.grid(row=0,column=1)

        lblID=Label(DataFrameLeft,bg="powder blue",text="Customer ID",font=("arial",12,"bold"),padx=2,pady=6)
        lblID.grid(row=1,column=0,sticky=W)

        entID=Entry(DataFrameLeft,textvariable=self.id_var,font=("arial",12),width=29)
        entID.grid(row=1,column=1)

        lblFirstName=Label(DataFrameLeft,bg="powder blue",text="First Name",font=("arial",12,"bold"),padx=2,pady=6)
        lblFirstName.grid(row=2,column=0,sticky=W)

        entFN=Entry(DataFrameLeft,textvariable=self.firstname_var,font=("arial",12),width=29)
        entFN.grid(row=2,column=1)

        lblLastName=Label(DataFrameLeft,bg="powder blue",text="Last Name",font=("arial",12,"bold"),padx=2,pady=6)
        lblLastName.grid(row=3,column=0,sticky=W)

        entLN=Entry(DataFrameLeft,textvariable=self.lastname_var,font=("arial",12),width=29)
        entLN.grid(row=3,column=1)

        lblPhone=Label(DataFrameLeft,bg="powder blue",text="Phone Number",font=("arial",12,"bold"),padx=2,pady=6)
        lblPhone.grid(row=4,column=0,sticky=W)

        entPhone=Entry(DataFrameLeft,textvariable=self.phoneno_var,font=("arial",12),width=29)
        entPhone.grid(row=4,column=1)

        lblOID=Label(DataFrameLeft,bg="powder blue",text="Order ID",font=("arial",12,"bold"),padx=2,pady=6)
        lblOID.grid(row=0,column=2,sticky=W)

        entOID=Entry(DataFrameLeft,textvariable=self.orderid_var,font=("arial",12),width=29)
        entOID.grid(row=0,column=3)

        lblOName=Label(DataFrameLeft,bg="powder blue",text="Order Name",font=("arial",12,"bold"),padx=2,pady=6)
        lblOName.grid(row=1,column=2,sticky=W)

        entOName=Entry(DataFrameLeft,textvariable=self.ordername_var,font=("arial",12),width=29)
        entOName.grid(row=1,column=3)

        lblDate=Label(DataFrameLeft,bg="powder blue",text="Date",font=("arial",12,"bold"),padx=2,pady=6)
        lblDate.grid(row=4,column=2,sticky=W)

        entDate=Entry(DataFrameLeft,textvariable=self.date_var,font=("arial",12),width=29)
        entDate.grid(row=4,column=3)

        lblPrice=Label(DataFrameLeft,bg="powder blue",text="Total Price",font=("arial",12,"bold"),padx=2,pady=6)
        lblPrice.grid(row=7,column=2,sticky=W)

        entPrice=Entry(DataFrameLeft,textvariable=self.totPrice_var,font=("arial",12),width=29)
        entPrice.grid(row=7,column=3)

        lblTime=Label(DataFrameLeft,bg="powder blue",text="Time to prepare",font=("arial",12,"bold"),padx=2,pady=6)
        lblTime.grid(row=2,column=2,sticky=W)

        entTime=Entry(DataFrameLeft,textvariable=self.timetP_var,font=("arial",12),width=29)
        entTime.grid(row=2,column=3)

        lblGST=Label(DataFrameLeft,bg="powder blue",text="GST Charges",font=("arial",12,"bold"),padx=2,pady=6)
        lblGST.grid(row=5,column=2,sticky=W)

        entGST=Entry(DataFrameLeft,textvariable=self.gst_var,font=("arial",12),width=29)
        entGST.grid(row=5,column=3)

        lblSC=Label(DataFrameLeft,bg="powder blue",text="Serving Charges",font=("arial",12,"bold"),padx=2,pady=6)
        lblSC.grid(row=6,column=2,sticky=W)

        entSC=Entry(DataFrameLeft,textvariable=self.serving_var,font=("arial",12),width=29)
        entSC.grid(row=6,column=3)

        lblCal=Label(DataFrameLeft,bg="powder blue",text="Calories",font=("arial",12,"bold"),padx=2,pady=6)
        lblCal.grid(row=3,column=2,sticky=W)

        entCal=Entry(DataFrameLeft,textvariable=self.calories_var,font=("arial",12),width=29)
        entCal.grid(row=3,column=3)

        # Right Frame

        DataFrameRight=LabelFrame(text="Order Details",bg="powder blue",fg="navy blue",bd=12,relief=RIDGE,font=("times new roman",15,"bold"),padx=2,pady=6)
        DataFrameRight.place(x=930,y=150,width=580,height=350)

        self.txtBox=Text(DataFrameRight,font=("arial",12,"bold"),width=30,height=15,padx=2,pady=6)
        self.txtBox.grid(row=0,column=2)


        listScroll=Scrollbar(DataFrameRight)
        listScroll.grid(row=0,column=1,sticky="ns")


        listFood=['Samosa','Aloo Patty','Paneer Patty','French Fries','Chhole Bhature','Masala Dosa','Pao Bhaji',
                                               'Fried Roll','Chicken Biryani','Simple Dosa','Fried Rice','Maggi','Tea','Coffee','Veg Thali','Non Veg Thali']


        def SelectOrder(event=""):
            value=str(listBox.get(listBox.curselection()))
            x=value
            if(x=="Samosa"):
                self.orderid_var.set("ON202215137")
                self.ordername_var.set("Samosa")
                self.timetP_var.set("0")
                self.calories_var.set("260 cal")
                self.date_var.set(datetime.datetime.today())
                self.gst_var.set("Rs.0 min")
                self.serving_var.set("Rs.2")
                self.totPrice_var.set("Rs.12")

            elif(x=="Aloo Patty"):
                self.orderid_var.set("ON202287462")
                self.ordername_var.set("Aloo Patty")
                self.timetP_var.set("0 min")
                self.calories_var.set("135 cal")
                self.date_var.set(datetime.datetime.today())
                self.gst_var.set("Rs.0")
                self.serving_var.set("Rs.3")
                self.totPrice_var.set("Rs.15")

            elif(x=="Paneer Patty"):
                self.orderid_var.set("ON202237485")
                self.ordername_var.set("Paneer Patty")
                self.timetP_var.set("0 min")
                self.calories_var.set("105 cal")
                self.date_var.set(datetime.datetime.today())
                self.gst_var.set("Rs.0")
                self.serving_var.set("Rs.5")
                self.totPrice_var.set("Rs.20")

            elif(x=="French Fries"):
                self.orderid_var.set("ON202245346")
                self.ordername_var.set("French Fries")
                self.timetP_var.set("10 min")
                self.calories_var.set("300 cal")
                self.date_var.set(datetime.datetime.today())
                self.gst_var.set("Rs.2")
                self.serving_var.set("Rs.3")
                self.totPrice_var.set("Rs.30")

            elif(x=="Chhole Bhature"):
                self.orderid_var.set("ON202287462")
                self.ordername_var.set("Chhole Bhature")
                self.timetP_var.set("20 min")
                self.calories_var.set("400 cal")
                self.date_var.set(datetime.datetime.today())
                self.gst_var.set("Rs.5")
                self.serving_var.set("Rs.5")
                self.totPrice_var.set("Rs.40")

            elif(x=="Pao Bhaji"):
                self.orderid_var.set("ON202287863")
                self.ordername_var.set("Chhole Bhature")
                self.timetP_var.set("20 min")
                self.calories_var.set("400 cal")
                self.date_var.set(datetime.datetime.today())
                self.gst_var.set("Rs.2")
                self.serving_var.set("Rs.3")
                self.totPrice_var.set("Rs.35")

            elif(x=="Masala Dosa"):
                self.orderid_var.set("ON202213492")
                self.ordername_var.set("Masala Dosa")
                self.timetP_var.set("20 min")
                self.calories_var.set("540 cal")
                self.date_var.set(datetime.datetime.today())
                self.gst_var.set("Rs.5")
                self.serving_var.set("Rs.5")
                self.totPrice_var.set("Rs.45")

            elif(x=="Fried Roll"):
                self.orderid_var.set("ON202246583")
                self.ordername_var.set("Fried Roll")
                self.timetP_var.set("10 min")
                self.calories_var.set("540 cal")
                self.date_var.set(datetime.datetime.today())
                self.gst_var.set("Rs.2")
                self.serving_var.set("Rs.3")
                self.totPrice_var.set("Rs.30")

            elif(x=="Fried Rice"):
                self.orderid_var.set("ON202238757")
                self.ordername_var.set("Fried Rice")
                self.timetP_var.set("15 min")
                self.calories_var.set("160 cal")
                self.date_var.set(datetime.datetime.today())
                self.gst_var.set("Rs.5")
                self.serving_var.set("Rs.5")
                self.totPrice_var.set("Rs.45")

            elif(x=="Chicken Biryani"):
                self.orderid_var.set("ON2022387653")
                self.ordername_var.set("Chicken Biryani")
                self.timetP_var.set("25 min")
                self.calories_var.set("150 cal")
                self.date_var.set(datetime.datetime.today())
                self.gst_var.set("Rs.10")
                self.serving_var.set("Rs.10")
                self.totPrice_var.set("Rs.80")

            
            elif(x=="Simple Dosa"):
                self.orderid_var.set("ON202273428")
                self.ordername_var.set("Simple Dosa")
                self.timetP_var.set("15 min")
                self.calories_var.set("130 cal")
                self.date_var.set(datetime.datetime.today())
                self.gst_var.set("Rs.2")
                self.serving_var.set("Rs.3")
                self.totPrice_var.set("Rs.35")

            elif(x=="Tea"):
                self.orderid_var.set("ON202274263")
                self.ordername_var.set("Tea")
                self.timetP_var.set("5 min")
                self.calories_var.set("1 cal")
                self.date_var.set(datetime.datetime.today())
                self.gst_var.set("Rs.0")
                self.serving_var.set("Rs.0")
                self.totPrice_var.set("Rs.10")

            elif(x=="Coffee"):
                self.orderid_var.set("ON202209875")
                self.ordername_var.set("Coffee")
                self.timetP_var.set("5 min")
                self.calories_var.set("1 cal")
                self.date_var.set(datetime.datetime.today())
                self.gst_var.set("Rs.0")
                self.serving_var.set("Rs.0")
                self.totPrice_var.set("Rs.15")

            elif(x=="Maggi"):
                self.orderid_var.set("ON202283497")
                self.ordername_var.set("Maggi")
                self.timetP_var.set("10 min")
                self.calories_var.set("300 cal")
                self.date_var.set(datetime.datetime.today())
                self.gst_var.set("Rs.2")
                self.serving_var.set("Rs.3")
                self.totPrice_var.set("Rs.25")

            elif(x=="Veg Thali"):
                self.orderid_var.set("ON202257658")
                self.ordername_var.set("Veg Thali")
                self.timetP_var.set("25 min")
                self.calories_var.set("900 cal")
                self.date_var.set(datetime.datetime.today())
                self.gst_var.set("Rs.10")
                self.serving_var.set("Rs.5")
                self.totPrice_var.set("Rs.75")

            elif(x=="Non Veg Thali"):
                self.orderid_var.set("ON202243562")
                self.ordername_var.set("Non Veg Thali")
                self.timetP_var.set("25 min")
                self.calories_var.set("1000 cal")
                self.date_var.set(datetime.datetime.today())
                self.gst_var.set("Rs.10")
                self.serving_var.set("Rs.5")
                self.totPrice_var.set("Rs.85")


        listBox=Listbox(DataFrameRight,font=("arial",12,"bold"),width=20,height=15)
        listBox.bind("<<ListboxSelect>>",SelectOrder)
        listBox.grid(row=0,column=0,padx=4)
        listScroll.config(command=listBox.yview)


        for item in listFood:
            listBox.insert(END,item)

        #Buttons Frame

        frameButton=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        frameButton.place(x=0,y=530,width=1530,height=57)

        btnADD=Button(frameButton,command=self.add_Data,text="Add Data",font=("arial",12,"bold"),width=24,bg="blue",fg="white")
        btnADD.grid(row=0,column=0)

        btnShow=Button(frameButton,command=self.show_data,text="Show Data",font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        btnShow.grid(row=0,column=1)

        btnUpdate=Button(frameButton,text="Update",command=self.update,font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        btnUpdate.grid(row=0,column=2)

        btnDelete=Button(frameButton,text="Delete",command=self.delete,font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        btnDelete.grid(row=0,column=3)

        btnReset=Button(frameButton,text="Reset",command=self.reset,font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        btnReset.grid(row=0,column=4)

        btnExit=Button(frameButton,text="Exit",command=self.iExit,font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        btnExit.grid(row=0,column=5)





        #Database Frame

        frameDetails=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        frameDetails.place(x=0,y=605,width=1530,height=180)

        table_Frame=Label(frameDetails,bd=6,relief=RIDGE,bg="powder blue")
        table_Frame.place(x=0,y=2,width=1460,height=150)

        xscroll=ttk.Scrollbar(table_Frame,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(table_Frame,orient=VERTICAL)



        self.rest_table=ttk.Treeview(table_Frame,column=("customertype","customerid","firstname","lastname","phoneno","orderid",
                                                        "ordername","timetoprepare","calories","date","gstcharges","servingcharges",
                                                        "totalprice"),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)

        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)

        xscroll.config(command=self.rest_table.xview)
        yscroll.config(command=self.rest_table.yview)

        self.rest_table.heading("customertype",text="Customer Type")
        self.rest_table.heading("customerid",text="Customer ID")
        self.rest_table.heading("firstname",text="First Name")
        self.rest_table.heading("lastname",text="Last Name")
        self.rest_table.heading("phoneno",text="Phone Number")
        self.rest_table.heading("orderid",text="Order ID")
        self.rest_table.heading("ordername",text="Order Name")
        self.rest_table.heading("timetoprepare",text="Time to prepare")
        self.rest_table.heading("calories",text="Calories")
        self.rest_table.heading("date",text="Date")
        self.rest_table.heading("gstcharges",text="GST Charges")
        self.rest_table.heading("servingcharges",text="Serving Charges")
        self.rest_table.heading("totalprice",text="Total Price")

        self.rest_table["show"]="headings"
        self.rest_table.pack(fill=BOTH,expand=1)

        self.rest_table.column("customertype",width=150)
        self.rest_table.column("customerid",width=150)
        self.rest_table.column("firstname",width=150)
        self.rest_table.column("lastname",width=150)
        self.rest_table.column("phoneno",width=150)
        self.rest_table.column("orderid",width=150)
        self.rest_table.column("ordername",width=150)
        self.rest_table.column("timetoprepare",width=150)
        self.rest_table.column("calories",width=150)
        self.rest_table.column("date",width=150)
        self.rest_table.column("gstcharges",width=150)
        self.rest_table.column("servingcharges",width=150)
        self.rest_table.column("totalprice",width=150)

        self.fetch_data()
        self.rest_table.bind("<ButtonRelease-1>",self.get_cursor)


    def add_Data(self):
            conn=mysql.connector.connect(host="localhost",user="root",database="rms")
            my_cursor=conn.cursor()
            my_cursor.execute("insert into restaurant values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                        self.customer_var.get(),
                                                                                                        self.id_var.get(),
                                                                                                        self.firstname_var.get(),
                                                                                                        self.lastname_var.get(),
                                                                                                        self.phoneno_var.get(),
                                                                                                        self.orderid_var.get(),
                                                                                                        self.ordername_var.get(),
                                                                                                        self.timetP_var.get(),
                                                                                                        self.calories_var.get(),
                                                                                                        self.date_var.get(),
                                                                                                        self.gst_var.get(),
                                                                                                        self.serving_var.get(),
                                                                                                        self.totPrice_var.get()
                                                                                                    ))
            conn.commit()
            self.fetch_data()
            conn.close()
            

            messagebox.showinfo("Success","Order has been placed successfully.")


    def update(self):
            conn=mysql.connector.connect(host="localhost",user="root",database="rms")
            my_cursor=conn.cursor()
            my_cursor.execute("UPDATE restaurant SET CustomerType=%s,FirstName=%s,LastName=%s,PhoneNO=%s,OrderID=%s,OrderName=%s,TimeTP=%s,Calories=%s,Date=%s,GST=%s,ServTAX=%s,TotalPrice=%s where CustomerID=%s",(
                                                                                                        self.customer_var.get(),
                                                                                                        self.firstname_var.get(),
                                                                                                        self.lastname_var.get(),
                                                                                                        self.phoneno_var.get(),
                                                                                                        self.orderid_var.get(),
                                                                                                        self.ordername_var.get(),
                                                                                                        self.timetP_var.get(),
                                                                                                        self.calories_var.get(),
                                                                                                        self.date_var.get(),
                                                                                                        self.gst_var.get(),
                                                                                                        self.serving_var.get(),
                                                                                                        self.totPrice_var.get(),
                                                                                                        self.id_var.get()
                                                                                                    ))

            conn.commit()
            self.fetch_data()
            self.reset()
            conn.close()

            messagebox.showinfo("Success","Order has been updated.")

    def fetch_data(self):
            conn=mysql.connector.connect(host="localhost",user="root",database="rms")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from restaurant")
            rows=my_cursor.fetchall()

            if len(rows)!=0:
                self.rest_table.delete(*self.rest_table.get_children())
                for i in rows:
                    self.rest_table.insert("",END,values=i)
                conn.commit()
            conn.close()

        
    def get_cursor(self,event=""):
            cursor_row=self.rest_table.focus()
            content=self.rest_table.item(cursor_row)
            row=content['values']

            self.customer_var.set(row[0])
            self.id_var.set(row[1])
            self.firstname_var.set(row[2])
            self.lastname_var.set(row[3])
            self.phoneno_var.set(row[4])
            self.orderid_var.set(row[5])
            self.ordername_var.set(row[6])
            self.timetP_var.set(row[7])
            self.calories_var.set(row[8])
            self.date_var.set(row[9])
            self.gst_var.set(row[10])
            self.serving_var.set(row[11])
            self.totPrice_var.set(row[12])

    def show_data(self):
            self.txtBox.insert(END,"Customer Type:\t\t"+self.customer_var.get() + "\n")
            self.txtBox.insert(END,"Customer ID:\t\t"+self.id_var.get()+"\n")
            self.txtBox.insert(END,"First Name:\t\t"+self.firstname_var.get()+"\n")
            self.txtBox.insert(END,"Last Name:\t\t"+self.lastname_var.get()+"\n")
            self.txtBox.insert(END,"Phone Number:\t\t"+self.phoneno_var.get()+"\n")
            self.txtBox.insert(END,"Order ID:\t\t"+self.orderid_var.get()+"\n")
            self.txtBox.insert(END,"Order Name:\t\t"+self.ordername_var.get()+"\n")
            self.txtBox.insert(END,"Time to prepare:\t\t"+self.timetP_var.get()+"\n")
            self.txtBox.insert(END,"Calories:\t\t"+self.calories_var.get()+"\n")
            self.txtBox.insert(END,"Date:\t\t"+self.date_var.get()+"\n")
            self.txtBox.insert(END,"GST Charges:\t\t"+self.gst_var.get()+"\n")
            self.txtBox.insert(END,"Serving Charges:\t\t"+self.serving_var.get()+"\n")
            self.txtBox.insert(END,"Total Price:\t\t"+self.totPrice_var.get()+"\n")


    def reset(self):
            self.customer_var.set("")
            self.id_var.set("")
            self.firstname_var.set("")
            self.lastname_var.set("")
            self.phoneno_var.set("")
            self.orderid_var.set("")
            self.ordername_var.set("")
            self.timetP_var.set("")
            self.calories_var.set("")
            self.date_var.set("")
            self.gst_var.set("")
            self.serving_var.set("")
            self.totPrice_var.set("")
            self.txtBox.delete("1.0",END)


    def delete(self):
            if self.id_var.get()=="":
                messagebox.showerror("Error","First Select the Customer")
            else:
                conn=mysql.connector.connect(host="localhost",user="root",database="rms")
                my_cursor=conn.cursor()
                query="delete from restaurant where CustomerID=%s"
                value=(self.id_var.get(),)
                my_cursor.execute(query,value)

                conn.commit()
                self.fetch_data()
                self.reset()
                conn.close()

                messagebox.showinfo("Success","Customer has been deleted.")

        
    def iExit(self):
            iExit=tkinter.messagebox.askyesno("Restaurant Management System","Confirm your exit.")
            if iExit>0:
                self.root.destroy()
                return


if __name__ == "__main__":
    root=Tk()
    obj=restaurantManagementSystem(root)
    root.mainloop
