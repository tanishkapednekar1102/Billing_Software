from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk  #pip install pillow
import random,os
from tkinter import messagebox
import tempfile
from time import strftime
import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders



class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1500x800+0+0")
        self.root.title("Billing Software")


        #=============================Variables===========================
        self.c_name=StringVar()
        self.c_phone=StringVar()
        self.bill_no=StringVar()
        z=random.randint(1000,9999)
        self.bill_no.set(z)
        self.c_email=StringVar()
        self.search_bill=StringVar()
        self.product=StringVar()
        self.prices=IntVar()
        self.qty=IntVar()
        self.sub_total=StringVar()
        self.tax_input=StringVar()
        self.total=StringVar()


        #product Categories list
        self.Category=["Select Option","Clothing","LifeStyle","Mobiles"]

        #SubCatClothing
        self.subCatClothing=["pant","T-Shirt","Shirt"]
        self.pant=["Levis","Mufti","Spykar"]
        self.price_levis=5000
        self.price_mufti=7000
        self.price_spaykar=8000

        self.T_Shirt=['polo','Roadster','Jack&Jones']
        self.price_polo=1500
        self.price_Roadster=1800
        self.price_JackJones=1700

        self.Shirt=['peter England','Louis Phillipe','Park Avenue']
        self.price_peter=2100
        self.price_Louis=2700
        self.price_Park=1740

        #SubcatLifStyle
        self.SubCatLifStyle=['Bath Soap','Face Creame','Hair Oil']
        self.Bath_Soap=['LifeBuy','Lux','Santoor','Pearl']
        self.price_life=20
        self.price_lux=20
        self.price_Santoor=20
        self.price_pearl=30

        self.Face_Creame=['Fair&Lovely','Ponds','Olay','Garnier']
        self.price_fair=20
        self.price_ponds=20
        self.price_olay=20
        self.price_garnier=30

        self.Hair_oil=['Parachute','Jashmin','Bajaj']
        self.price_para=25
        self.price_jashmin=22
        self.price_bajaj=30

        #SubCatMobiles
        self.SubCatMobiles=['Iphone','Samsung','Xiome','Realme',"One+"]
        self.Iphone=['Iphone_X','Iphone_11','Iphone_12']
        self.price_ix=40000
        self.price_i11=60000
        self.price_i12=85000

        self.Samsung=['Samsung M16','Samsung M12','Samsung M21']
        self.price_sm16=16000
        self.price_sm12=12000
        self.price_sm21=21000

        self.Xiome=['Red11','Redme-12','Redmepro']
        self.price_r11=11000
        self.price_r12=12000
        self.price_rpro=9000

        self.Realme=['Realme 12','Realme 13','Realme pro']
        self.price_rel12=25000
        self.price_rel13=22000
        self.price_relpro=30000

        self.Oneplus=['Oneplus','Onepluse2','Oneplus3']
        self.price_one1=45000
        self.price_one12=60000
        self.price_one3=45000




        # #image1
        img=Image.open("Images/good.jpg")
        img = img.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        lbl_img=Label(self.root,image=self.photoimg)
        lbl_img.place(x=0,y=0,width=500,height=130)

        #image2
        img_1=Image.open("Images/girls.jpg")
        img_1= img_1.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg_1=ImageTk.PhotoImage(img_1)

        lbl_img_1=Label(self.root,image=self.photoimg_1)
        lbl_img_1.place(x=500,y=0,width=500,height=130)

        #image3
        img_2=Image.open("Images/girl1.jpg")
        img_2= img_2.resize((380, 130), Image.Resampling.LANCZOS)
        self.photoimg_2=ImageTk.PhotoImage(img_2)

        lbl_img_2=Label(self.root,image=self.photoimg_2)
        lbl_img_2.place(x=1000,y=0,width=380,height=130)

        lbl_title=Label(self.root,text="BILLING SOFTWARE USING PYTHON",font=("times new roman",35,"bold"),bg="white",fg="red")
        lbl_title.place(x=0,y=130,width=1500,height=45)

        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text = string)
            lbl.after(1000, time)

        lbl = Label(lbl_title, font=('times new roman',16,'bold'),background='white',foreground='black')
        lbl.place(x=0,y=0,width=120,height=45)
        time()

        Main_Frame=Frame(self.root,bd=5,relief=GROOVE,bg="white")
        Main_Frame.place(x=0,y=175,width=1500,height=620)

        # Customer LableFrame
        #Mobile
        Cust_Frame=LabelFrame(Main_Frame,text="Customer",font=("times new roman",12,"bold"),bg="white",fg="red")
        Cust_Frame.place(x=10,y=5,width=330,height=140)

        self.lbl_mob=Label(Cust_Frame,text="Mobile No.",font=("times new roman",12,"bold"),bg="white")
        self.lbl_mob.grid(row=0,column=0,stick=W,padx=5,pady=2)

        # Mobile number validation - only digits, max 10
        vcmd_mob = (self.root.register(self.validate_mobile), '%S', '%d')
        self.entry_mob=ttk.Entry(Cust_Frame,textvariable=self.c_phone,font=("times new roman",12,"bold"),width=22,validate='key',validatecommand=vcmd_mob)
        self.entry_mob.grid(row=0,column=1)

        #customer
        self.lblCustName=Label(Cust_Frame,font=("times new roman",12,"bold"),bg="white",text="Customer Name",bd=4)
        self.lblCustName.grid(row=1,column=0,stick=W,padx=5,pady=2)

        self.txtCustName=ttk.Entry(Cust_Frame,textvariable=self.c_name,font=("times new roman",12,"bold"),width=22)
        self.txtCustName.grid(row=1,column=1,stick=W,padx=5,pady=2)

        #Email
        self.lblEmail=Label(Cust_Frame,font=("times new roman",12,"bold"),bg="white",text="Email",bd=4)
        self.lblEmail.grid(row=2,column=0,stick=W,padx=5,pady=2)

        # Email validation - basic email format
        vcmd_email = (self.root.register(self.validate_email), '%S', '%d')
        self.txtEmail=ttk.Entry(Cust_Frame,textvariable=self.c_email,font=("times new roman",12,"bold"),width=22,validate='key',validatecommand=vcmd_email)
        self.txtEmail.grid(row=2,column=1,stick=W,padx=5,pady=2)

        #Product LabelFrame
        product_Frame=LabelFrame(Main_Frame,text="Product",font=("times new roman",12,"bold"),bg="white",fg="red")
        product_Frame.place(x=350,y=5,width=610,height=140)

        #category
        self.lblCategory=Label(product_Frame,font=("times new roman",12,"bold"),bg="white",text="Select Categories",bd=4)
        self.lblCategory.grid(row=0,column=0,stick=W,padx=5,pady=2)

        self.Combo_Category=ttk.Combobox(product_Frame,values=self.Category,font=("times new roman",12,"bold"),width=22,state="readonly")
        self.Combo_Category.current(0)
        self.Combo_Category.grid(row=0,column=1,stick=W,padx=5,pady=2)
        self.Combo_Category.bind("<<ComboboxSelected>>", self.Categories)

        #subcategory
        self.lblSubCategory=Label(product_Frame,font=("times new roman",12,"bold"),bg="white",text="SubCategory",bd=4)
        self.lblSubCategory.grid(row=1,column=0,stick=W,padx=5,pady=2)

        self.ComboSubCategory=ttk.Combobox(product_Frame,values=[""],state="readonly",font=("times new roman",12,"bold"),width=22)
        self.ComboSubCategory.grid(row=1,column=1,stick=W,padx=5,pady=2)
        self.ComboSubCategory.bind("<<ComboboxSelected>>",self.Product_add)

        #product Name
        self.lblproduct=Label(product_Frame,font=("times new roman",12,"bold"),bg="white",text="Product Name",bd=4)
        self.lblproduct.grid(row=2,column=0,stick=W,padx=5,pady=2)

        self.Comboproduct=ttk.Combobox(product_Frame,textvariable=self.product,state="readonly",font=("times new roman",12,"bold"),width=22)
        self.Comboproduct.grid(row=2,column=1,stick=W,padx=5,pady=2)
        self.Comboproduct.bind("<<ComboboxSelected>>",self.price)

        #price
        self.lblprice=Label(product_Frame,font=("times new roman",12,"bold"),bg="white",text="Price",bd=4)
        self.lblprice.grid(row=0,column=2,stick=W,padx=5,pady=2)

        self.Comboprice=ttk.Combobox(product_Frame,state="readonly",textvariable=self.prices,font=("times new roman",12,"bold"),width=20)
        self.Comboprice.grid(row=0,column=3,stick=W,padx=5,pady=2)

        #Qty
        self.lblQty=Label(product_Frame,font=("times new roman",12,"bold"),bg="white",text="Qty",bd=4)
        self.lblQty.grid(row=1,column=2,stick=W,padx=5,pady=2)

        self.ComboQty=ttk.Entry(product_Frame,textvariable=self.qty,font=("times new roman",12,"bold"),width=22)
        self.ComboQty.grid(row=1,column=3,stick=W,padx=5,pady=2)


        #middle Frame
        MiddleFrame=Frame(Main_Frame,bd=10)
        MiddleFrame.place(x=10,y=150,width=950,height=340)

        #search
        Search_Frame=LabelFrame(Main_Frame,text="Search Bill",font=("times new roman",12,"bold"),bg="white",fg="red",bd=2,relief=GROOVE)
        Search_Frame.place(x=950,y=10,width=560,height=55)

        self.lblBill=Label(Search_Frame,font=("times new roman",12,"bold"),fg="black",bg="white",text="Bill Number")
        self.lblBill.grid(row=0,column=0,sticky=W,padx=5,pady=5)

        self.txt_Entry_Search=ttk.Entry(Search_Frame,textvariable=self.search_bill,font=("times new roman",12,"bold"),width=20)
        self.txt_Entry_Search.grid(row=0,column=1,sticky=W,padx=5,pady=5)

        self.BtnSearch=Button(Search_Frame,command=self.find_bill,text="Search",font=("times new roman",10,"bold"),bg="orangered",fg="white",width=12,cursor="hand2")
        self.BtnSearch.grid(row=0,column=2,padx=5,pady=5)

        # Rightframe Bill Aria
        RightLabelFrame=LabelFrame(Main_Frame,text="Bill Aria",font=("times new roman",12,"bold"),bg="White",fg="red")
        RightLabelFrame.place(x=970,y=80,width=370,height=340)

        scroll_y=Scrollbar(RightLabelFrame,orient=VERTICAL)
        self.textarea=Text(RightLabelFrame,yscrollcommand=scroll_y.set,bg="White",fg="blue",font=("times new roman",12,"bold"))
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)


        #Bill Counter LabelFrame
        Bottom_Frame=LabelFrame(Main_Frame,text="Bill Counter",font=("times new roman",12,"bold"),bg="white",fg="red")
        Bottom_Frame.place(x=0,y=390,width=1350,height=125)


        self.lblSubTotal=Label(Bottom_Frame,font=("times new roman",12,"bold"),bg="white",text="Sub Total",bd=4)
        self.lblSubTotal.grid(row=0,column=0,stick=W,padx=5,pady=2)

        self.EntySubTotal=ttk.Entry(Bottom_Frame,textvariable=self.sub_total,font=("times new roman",12,"bold"),width=22)
        self.EntySubTotal.grid(row=0,column=1,stick=W,padx=5,pady=2)

        #txt bill
        self.lbl_tax=Label(Bottom_Frame,font=("times new roman",12,"bold"),bg="white",text="Gov Tax",bd=4)
        self.lbl_tax.grid(row=1,column=0,stick=W,padx=5,pady=2)

        self.txt_tax=ttk.Entry(Bottom_Frame,textvariable=self.tax_input,font=("times new roman",12,"bold"),width=22)
        self.txt_tax.grid(row=1,column=1,stick=W,padx=5,pady=2)

        #Amount
        self.lblAmountTotal=Label(Bottom_Frame,font=("times new roman",12,"bold"),bg="white",text="Total",bd=4)
        self.lblAmountTotal.grid(row=2,column=0,stick=W,padx=5,pady=2)

        self.txtAmountTotal=ttk.Entry(Bottom_Frame,textvariable=self.total,font=("times new roman",12,"bold"),width=22)
        self.txtAmountTotal.grid(row=2,column=1,stick=W,padx=5,pady=2)

        #Button Frame
        Btn_Frame=Frame(Bottom_Frame,bd=2,bg="white")
        Btn_Frame.place(x=320,y=0)

        self.BtnAddToCart=Button(Btn_Frame,command=self.AddItem,height=2,text="Add To Cart",font=("times new roman",15,"bold"),bg="orangered",fg="white",width=12,cursor="hand2")
        self.BtnAddToCart.grid(row=0,column=0)


        self.Btngenerate_bill=Button(Btn_Frame,command=self.gen_bill,height=2,text="Generate Bill",font=("times new roman",15,"bold"),bg="orangered",fg="white",width=12,cursor="hand2")
        self.Btngenerate_bill.grid(row=0,column=1)


        self.BtnSave=Button(Btn_Frame,command=self.save_bill,height=2,text="Save Bill",font=("times new roman",15,"bold"),bg="orangered",fg="white",width=12,cursor="hand2")
        self.BtnSave.grid(row=0,column=2)

        self.BtnPrint=Button(Btn_Frame,command=self.iprint,height=2,text="Print",font=("times new roman",15,"bold"),bg="orangered",fg="white",width=12,cursor="hand2")
        self.BtnPrint.grid(row=0,column=3)

        self.BtnClear=Button(Btn_Frame,command=self.clear,height=2,text="Clear",font=("times new roman",15,"bold"),bg="orangered",fg="white",width=12,cursor="hand2")
        self.BtnClear.grid(row=0,column=4)

        self.BtnExit=Button(Btn_Frame,command=self.root.destroy,height=2,text="Exit",font=("times new roman",15,"bold"),bg="orangered",fg="white",width=12,cursor="hand2")
        self.BtnExit.grid(row=0,column=5)
        self.Welcome()



        self.l=[]
        self.products_list=[]  # Store product details: [product_name, qty, price]
    #==========================Function Declaration===========================
    def Welcome(Self):
        Self.textarea.delete(1.0,END)    
        Self.textarea.insert(END,"\t Welcome  TO  Mini Mall")
        Self.textarea.insert(END,f"\n Bill Number :{Self.bill_no.get()}")
        Self.textarea.insert(END,f"\n Customer Name:{Self.c_name.get()}")
        Self.textarea.insert(END,f"\n Phone Number:{Self.c_phone.get()} ")
        Self.textarea.insert(END,f"\n Customer Email:{Self.c_email.get()}")

    def send_bill(self):
        try:
            self.Email_sender = "put your email here"
            self.Email_password ="create google App password and put here"
            self.Email_reciever = self.c_email.get()



            # File information
            filename = self.bill_no.get()
            filepath = "C:\\Users\\Administrator\\OneDrive\\Desktop\\codes\\backend\\Billing_Software_1\\bills\\" + filename + ".txt"
            
            print(self.Email_reciever, self.Email_sender, self.Email_password)

            self.subject = 'GENERATED GST BILL'
            self.body = '''Thank You for visiting Our Store,
            We will wait for your next visit.
            please Find the GST bill attached
            '''
            #self.body= font=("times new roman",15,"bold")
            

            em = MIMEMultipart()
            em['From'] = self.Email_sender
            em['To'] = self.Email_reciever
            em['subject'] =self.subject
            

            # Attach body
            em.attach(MIMEText(self.body, 'plain'))

            # Attach file
            with open(filepath, 'rb') as f:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(f.read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', f'attachment; filename="{filename}"')
                em.attach(part)

    
            
            context = ssl.create_default_context()
            
            with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
                    server.login(self.Email_sender,self.Email_password)
                    server.sendmail(self.Email_sender,self. Email_reciever, em.as_string())
            
                    
        except Exception as e:
            print(e)
            print("Email failed to send")

    def validate_mobile(self, input_char, action):
        """Validate mobile number - only digits, maximum 10 characters"""
        if action == '1':  # '1' means insertion, '0' means deletion
            # Check if input is a digit
            if input_char.isdigit():
                # Check current length + new character doesn't exceed 10
                current_length = len(self.c_phone.get())
                if current_length < 10:
                    return True
                else:
                    return False
            else:
                # Non-digit character, reject it
                return False
        return True  # Allow deletion
    
    def validate_email(self, input_char, action):
        """Validate email - block spaces and obviously invalid characters"""
        if action == '1':  # '1' means insertion
            # Reject spaces and some obviously invalid email characters
            invalid_chars = ' '
            if input_char not in invalid_chars:
                return True
            else:
                return False
        return True  # Allow deletion
    
    def is_valid_email_format(self, email):
        """Check if email has valid format (contains @ and domain)"""
        import re
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None

    def AddItem(self):
        if self.product.get()=="":
            messagebox.showerror("Error","Please Select the Product Name")
        else:
            Tax=5  # Tax rate is 5%
            self.n=self.prices.get()
            self.m=self.qty.get()*self.n
            self.l.append(self.m)
            # Store product details: [product_name, qty, unit_price, total_price]
            self.products_list.append({
                'name': self.product.get(),
                'qty': self.qty.get(),
                'price': self.n,
                'total': self.m
            })
            self.textarea.insert(END,f"\n {self.product.get()}\t\t{self.qty.get()}\t\t{self.m}")
            subtotal = sum(self.l)
            tax_amount = (subtotal * Tax) / 100
            total_amount = subtotal + tax_amount
            self.sub_total.set(str('Rs.%.2f'%(subtotal)))
            self.tax_input.set(str('Rs.%.2f'%(tax_amount)))
            self.total.set(str('Rs.%.2f'%(total_amount)))


    
    def gen_bill(self):
        if self.product.get()=="":
            messagebox.showerror("Error","Please Add To Cart Product")
        elif self.c_name.get()=="":
            messagebox.showerror("Error","Please Enter Customer Name")
        elif self.c_phone.get()=="":
            messagebox.showerror("Error","Please Enter Phone Number")
        elif len(self.c_phone.get()) != 10:
            messagebox.showerror("Error","Phone Number must be exactly 10 digits")
        elif self.c_email.get()=="":
            messagebox.showerror("Error","Please Enter Email Address")
        elif not self.is_valid_email_format(self.c_email.get()):
            messagebox.showerror("Error","Please Enter Valid Email Address (e.g., user@example.com)")
        else:
            self.Welcome()
            self.textarea.insert(END,f"\n==================================================\n")
            self.textarea.insert(END,f"\nProducts\t\tQty\t\tPrice\t\tTotal")
            self.textarea.insert(END,"\n=========================================\n")
            
            # Display all products from the products_list
            for product in self.products_list:
                self.textarea.insert(END,f"\n {product['name']}\t\t{product['qty']}\t\t{product['price']}\t\tRs.{product['total']:.2f}")
            
            self.textarea.insert(END,"\n ==========================================\n")
            self.textarea.insert(END,f"\n Sub Amount:\t\t\t{self.sub_total.get()}")
            self.textarea.insert(END,f"\n Tax Amount:\t\t\t{self.tax_input.get()}")
            self.textarea.insert(END,f"\n Total Amount:\t\t\t{self.total.get()}")
            self.textarea.insert(END,"\n ==========================================\n")

    def save_bill(self):
        Op=messagebox.askyesno("Save Bill","Do you want to save the bill")
        if Op>0:
            self.bill_data=self.textarea.get(1.0,END)
            f1=open('bills/'+str(self.bill_no.get())+".txt",'w')
            f1.write(self.bill_data)
            Op=messagebox.showinfo("Saved",f"Bill, No:{self.bill_no.get()} saved successfully")
            f1.close()
            self.send_bill()


    def iprint(self):
        q=self.textarea.get(1.0,"end-1c")
        filename=tempfile.mktemp('.txt')
        open(filename,'w').write(q)
        os.startfile(filename,"print")

    def find_bill(self):
        found="no"
        for i in os.listdir("bills/"):
            if i.split('.')[0]==self.search_bill.get():
                f1=open(f'bills/{i}','r')
                self.textarea.delete(1.0,END)
                for d in f1:
                    self.textarea.insert(END,d)
                f1.close()
                found="yes"
        if found=="no":
            messagebox.showerror("Error","Invalid Bill No.")


    def clear (self):
        self.textarea.delete(1.0,END)
        self.c_name.set("")
        self.c_phone.set("")
        self.c_email.set("")
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.search_bill.set("")
        self.product.set("")
        self.prices.set(0)
        self.qty.set(0)
        self.l=[0]
        self.products_list=[]  # Clear products list for new bill
        self.total.set("")
        self.sub_total.set("")
        self.tax_input.set('')
        self.Welcome()

    


    def Categories(self,event=""):
        if self.Combo_Category.get()=="Clothing":
            self.ComboSubCategory.config(value=self.subCatClothing)
            self.ComboSubCategory.current(0)

        if self.Combo_Category.get()=="LifeStyle":
            self.ComboSubCategory.config(value=self.SubCatLifStyle)
            self.ComboSubCategory.current(0)

        if self.Combo_Category.get()=="Mobiles":
            self.ComboSubCategory.config(value=self.SubCatMobiles)
            self.ComboSubCategory.current(0)


    def Product_add(self,event=""):
        if self.ComboSubCategory.get()=="pant":
            self.Comboproduct.config(values=self.pant)
            self.Comboproduct.current(0)

        if self.ComboSubCategory.get()=="T-Shirt":
            self.Comboproduct.config(values=self.T_Shirt)
            self.Comboproduct.current(0)

        if self.ComboSubCategory.get()=="Shirt":
            self.Comboproduct.config(values=self.Shirt)
            self.Comboproduct.current(0)

        #LifeStyle
        if self.ComboSubCategory.get()=="Bath Soap":
            self.Comboproduct.config(values=self.Bath_Soap)
            self.Comboproduct.current(0)

        if self.ComboSubCategory.get()=="Face Creame":
            self.Comboproduct.config(values=self.Face_Creame)
            self.Comboproduct.current(0)

        if self.ComboSubCategory.get()=="Hair Oil":
            self.Comboproduct.config(values=self.Hair_oil)
            self.Comboproduct.current(0)
        #Mobile
        if self.ComboSubCategory.get()=="Iphone":
            self.Comboproduct.config(values=self.Iphone)
            self.Comboproduct.current(0)

        if self.ComboSubCategory.get()=="Samsung":
            self.Comboproduct.config(values=self.Samsung)
            self.Comboproduct.current(0)

        if self.ComboSubCategory.get()=="Xiome":
            self.Comboproduct.config(values=self.Xiome)
            self.Comboproduct.current(0)

        if self.ComboSubCategory.get()=="Realme":
            self.Comboproduct.config(values=self.Realme)
            self.Comboproduct.current(0)

        if self.ComboSubCategory.get()=="One+":
            self.Comboproduct.config(values=self.Oneplus)
            self.Comboproduct.current(0)

    def price(self,event=""):
        #pant
        if self.Comboproduct.get()=="Levis":
            self.Comboprice.config(values=self.price_levis)
            self.Comboprice.current(0)
            self.qty.set(1)   

        if self.Comboproduct.get()=="Mufti":
            self.Comboprice.config(values=self.price_mufti)
            self.Comboprice.current(0)
            self.qty.set(1)  

        if self.Comboproduct.get()=="Spykar":
            self.Comboprice.config(values=self.price_spaykar)
            self.Comboprice.current(0)
            self.qty.set(1) 

        #Tshirt
        if self.Comboproduct.get()=="polo":
            self.Comboprice.config(values=self.price_polo)
            self.Comboprice.current(0)
            self.qty.set(1)   

        if self.Comboproduct.get()=="Roadster":
            self.Comboprice.config(values=self.price_Roadster)
            self.Comboprice.current(0)
            self.qty.set(1)

        if self.Comboproduct.get()=="Jack&Jones":
            self.Comboprice.config(values=self.price_JackJones)
            self.Comboprice.current(0)
            self.qty.set(1)
        
        #shirt
        if self.Comboproduct.get()=="peter England":
            self.Comboprice.config(values=self.price_peter)
            self.Comboprice.current(0)
            self.qty.set(1)  
         
        if self.Comboproduct.get()=="Louis Phillipe":
            self.Comboprice.config(values=self.price_Louis)
            self.Comboprice.current(0)
            self.qty.set(1)  
       
        if self.Comboproduct.get()=="Park Avenue":
            self.Comboprice.config(values=self.price_Park)
            self.Comboprice.current(0)
            self.qty.set(1)  
        
        #Bath Soap
        if self.Comboproduct.get()=="LifeBuy":
            self.Comboprice.config(values=self.price_life)
            self.Comboprice.current(0)
            self.qty.set(1) 

        if self.Comboproduct.get()=="Lux":
            self.Comboprice.config(values=self.price_lux)
            self.Comboprice.current(0)
            self.qty.set(1)   
        
        if self.Comboproduct.get()=="Santoor":
            self.Comboprice.config(values=self.price_Santoor)
            self.Comboprice.current(0)
            self.qty.set(1)  

        if self.Comboproduct.get()=="Pearl":
            self.Comboprice.config(values=self.price_pearl)
            self.Comboprice.current(0)
            self.qty.set(1)  

        if self.Comboproduct.get()=="Fair&Lovely":
            self.Comboprice.config(values=self.price_fair)
            self.Comboprice.current(0)
            self.qty.set(1)  

        if self.Comboproduct.get()=="Ponds":
            self.Comboprice.config(values=self.price_ponds)
            self.Comboprice.current(0)
            self.qty.set(1)  

        if self.Comboproduct.get()=="Olay":
            self.Comboprice.config(values=self.price_olay)
            self.Comboprice.current(0)
            self.qty.set(1)  

        if self.Comboproduct.get()=="Garnier":
            self.Comboprice.config(values=self.price_garnier)
            self.Comboprice.current(0)
            self.qty.set(1)  

        if self.Comboproduct.get()=="parachute":
            self.Comboprice.config(values=self.price_levis)
            self.Comboprice.current(0)
            self.qty.set(1)  

        if self.Comboproduct.get()=="Parachute":
            self.Comboprice.config(values=self.price_para)
            self.Comboprice.current(0)
            self.qty.set(1)  

        if self.Comboproduct.get()=="Jashmin":
            self.Comboprice.config(values=self.price_jashmin)
            self.Comboprice.current(0)
            self.qty.set(1)  

        if self.Comboproduct.get()=="Bajaj":
            self.Comboprice.config(values=self.price_bajaj)
            self.Comboprice.current(0)
            self.qty.set(1)  

        if self.Comboproduct.get()=="Iphone_X":
            self.Comboprice.config(values=self.price_ix)
            self.Comboprice.current(0)
            self.qty.set(1) 

        if self.Comboproduct.get()=="Iphone_11":
            self.Comboprice.config(values=self.price_i11)
            self.Comboprice.current(0)
            self.qty.set(1)   

        if self.Comboproduct.get()=="Iphone_12":
            self.Comboprice.config(values=self.price_i12)
            self.Comboprice.current(0)
            self.qty.set(1)  

        if self.Comboproduct.get()=="Samsung M16":
            self.Comboprice.config(values=self.price_sm16)
            self.Comboprice.current(0)
            self.qty.set(1)  

        if self.Comboproduct.get()=="Samsung M12":
            self.Comboprice.config(values=self.price_sm12)
            self.Comboprice.current(0)
            self.qty.set(1)  

        if self.Comboproduct.get()=="Samsung M21":
            self.Comboprice.config(values=self.price_sm21)
            self.Comboprice.current(0)
            self.qty.set(1)  

        if self.Comboproduct.get()=="Red11":
            self.Comboprice.config(values=self.price_r11)
            self.Comboprice.current(0)
            self.qty.set(1)  

        if self.Comboproduct.get()=="Redme-12":
            self.Comboprice.config(values=self.price_r12)
            self.Comboprice.current(0)
            self.qty.set(1)  

        if self.Comboproduct.get()=="Redmepro":
            self.Comboprice.config(values=self.price_rpro)
            self.Comboprice.current(0)
            self.qty.set(1)  

        if self.Comboproduct.get()=="Realme 12":
            self.Comboprice.config(values=self.price_rel12)
            self.Comboprice.current(0)
            self.qty.set(1)  

        if self.Comboproduct.get()=="Realme 13":
            self.Comboprice.config(values=self.price_rel13)
            self.Comboprice.current(0)
            self.qty.set(1) 

        if self.Comboproduct.get()=="Realme pro":
            self.Comboprice.config(values=self.price_relpro)
            self.Comboprice.current(0)
            self.qty.set(1) 

        if self.Comboproduct.get()=="Oneplus":
            self.Comboprice.config(values=self.price_one1)
            self.Comboprice.current(0)
            self.qty.set(1) 

        if self.Comboproduct.get()=="Onepluse2":
            self.Comboprice.config(values=self.price_one12)
            self.Comboprice.current(0)
            self.qty.set(1) 

        if self.Comboproduct.get()=="Oneplus3":
            self.Comboprice.config(values=self.price_one3)
            self.Comboprice.current(0)
            self.qty.set(1)



if __name__ == '__main__':
    root=Tk()
    obj=Bill_App(root)
    root.mainloop()




# ===== TEST SMTP CONNECTION (RUNS WHEN SCRIPT STARTS) =====








