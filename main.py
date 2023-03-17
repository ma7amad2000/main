from tkinter import *
from tkinter import ttk, messagebox
import time
import pymysql
from db import Database
#from db2 import Database1

db = Database('MARTHA.db')

#db2 = Database1('d0ct0rs.db')





class martha:
    def __init__(self,root):
    #=======النافذه
    
        self.date = time.ctime()  
        self.root = root
        self.root.geometry('1350x715+0+0')
        self.root.title('[استقبال مرضى]')
        
        self.root.configure(background='silver')
        self.root.resizable(False,False)
        title=  Label(self.root,text='نـــــظام استقبـــــال',
        bg='#62fabb',font=('calibri',16,'bold'),fg='black').pack(fill=X)
        btn_help= Button(self.root,text='مساعده',font=('calibri',16,'bold'),fg='black',bg='white',command=self.help1).place(x=10,y=5,width=70,height=20)
       #============== طبقات الادخال==========
      #==============المتغيرات=============
        
        self.name = StringVar()
        self.email_mr = StringVar()
        self.phone_mr = StringVar() 
        self.mstawa = StringVar()
        self.mkhtas = StringVar()
        self.mrajaa= StringVar()
        self.dawa = StringVar()
        self.date_out= StringVar()
        self.name_mr= StringVar()
        self.date_in= StringVar()
        self.nw3 = StringVar()
        self.qasm =StringVar()
        self.age =StringVar()  
        self.se_py = StringVar()
        self.se_var =StringVar()

        self.user = StringVar()
        self.password =StringVar()
        self.name_doc_1=StringVar()
        self.takhss_1= StringVar()
        self.dawam_1 = StringVar()
        self.addres_1 = StringVar()
        self.phone_doc_1 =StringVar()
        self.nationality_1 = StringVar()    
       


 



        ent_frame = Frame(self.root,bg='white',bd=4)
        ent_frame.place(x=1130,y=34,width=220,height=714)
        lblName =Label(ent_frame,text='الاســــم',bg='white',bd=4,font=('calibri',10,'bold')).pack()
        ent_name = Entry(ent_frame,highlightthickness=2,highlightbackground="white",highlightcolor="#62fabb",justify='center',textvariable=self.name,font=('calibri',10,'bold'))
        ent_name.pack()
        lblage =Label(ent_frame,text='العمر',bg='white',bd=4,font=('calibri',10,'bold')).pack()
        ent_age = Entry(ent_frame,highlightthickness=2,highlightbackground="white",highlightcolor="#62fabb",justify='center',textvariable=self.age,font=('calibri',10,'bold'))
        ent_age.pack()
        
        lblphone =Label(ent_frame,text='هاتف المرافق',bg='white',bd=4,font=('calibri',10,'bold')).pack()
        ent_phone = Entry(ent_frame,highlightthickness=2,highlightbackground="white",highlightcolor="#62fabb",justify='center',textvariable=self.phone_mr,font=('calibri',10,'bold'))
        ent_phone.pack()

        lblemail =Label(ent_frame,text='بريد المرافق',bg='white',bd=4,font=('calibri',10,'bold')).pack()
        ent_email = Entry(ent_frame,highlightthickness=2,highlightbackground="white",highlightcolor="#62fabb",justify='center',textvariable=self.email_mr,font=('calibri',10,'bold'))
        ent_email.pack()

        lblName =Label(ent_frame,text='التحاليل',bg='white',bd=4,font=('calibri',10,'bold')).pack()
        combo_nw3 = ttk.Combobox(ent_frame, width=15,textvariable=self.mstawa, font=(
        'calibri', 14, 'bold'), justify='center')
        combo_nw3['value'] = ('TSH', 'CBC','BRCs','HCT','MCV','MCHC','PLT','W.B.C','ESR','LDL','HDL','TG')
        combo_nw3.pack()


        lblName =Label(ent_frame,text='موعد المراجعه',bg='white',bd=4,font=('calibri',10,'bold')).pack()
        ent_mrajaa = Entry(ent_frame,highlightthickness=2,highlightbackground="white",highlightcolor="#62fabb",justify='center',textvariable=self.mrajaa,font=('calibri',10,'bold'))
        ent_mrajaa.pack()
 
        lblName =Label(ent_frame,text='تاريخ الدخول',bg='white',bd=4,font=('calibri',10,'bold')).pack()
        ent_date = Entry(ent_frame,highlightthickness=2,highlightbackground="white",highlightcolor="#62fabb",justify='center',textvariable=self.date_in,font=('calibri',10,'bold'))
        ent_date.pack()

        lblName =Label(ent_frame,text='متابع الحاله',bg='white',bd=4,font=('calibri',10,'bold')).pack()
        ent_mkhtas = Entry(ent_frame,highlightthickness=2,highlightbackground="white",highlightcolor="#62fabb",justify='center',textvariable=self.mkhtas,font=('calibri',10,'bold'))
        ent_mkhtas.pack()

        lblName =Label(ent_frame,text='جنس المريض',bg='white',bd=4,font=('calibri',10,'bold')).pack()
        combo_nw3 = ttk.Combobox(ent_frame, width=15, state='readonly',textvariable=self.nw3, font=(
        'calibri', 14, 'bold'), justify='center')
        combo_nw3['value'] = ('ذكر', 'انثى')
        combo_nw3.pack()
        lblName_mr =Label(ent_frame,text='اسم المرافق',bg='white',bd=4,font=('calibri',10,'bold')).pack()
        ent_Name_mr = Entry(ent_frame,highlightthickness=2,highlightbackground="white",highlightcolor="#62fabb",textvariable=self.name_mr,justify='center',font=('calibri',10,'bold')).pack()
        lbldawa =Label(ent_frame,text='الدواء',bg='white',bd=4,font=('calibri',10,'bold')).pack()
        ent_dawa = Entry(ent_frame,highlightthickness=2,highlightbackground="white",highlightcolor="#62fabb",justify='center',textvariable=self.dawa,font=('calibri',10,'bold')).pack()
        lblout =Label(ent_frame,text='تاريخ الخروج',bg='white',bd=4,font=('calibri',10,'bold')).pack()
        ent_out = Entry(ent_frame,highlightthickness=2,highlightbackground="white",highlightcolor="#62fabb",justify='center',textvariable=self.date_out,font=('calibri',10,'bold')).pack()
        lblqasm =Label(ent_frame,text='القسم',bg='white',bd=4,font=('calibri',10,'bold')).pack()
        ent_qasm = Entry(ent_frame,highlightthickness=2,highlightbackground="white",highlightcolor="#62fabb",justify='center',textvariable=self.qasm,font=('calibri',10,'bold')).pack()
        #======= الازرار=====
      
        btn_frame = Frame(self.root,bg='white',bd=4)
        btn_frame.place(x=1,y=34,width=1125,height=70)
        btn_add = Button(btn_frame,text='اضافه مريض',fg='black',command=self.Add_Martha,bg='#62fabb',bd=4,font=('calibri',12,'bold'))
        btn_add.place(x=1000,y=2,width=100,height=50)

        btn_update = Button(btn_frame,text='تعديل بيانات',fg='black',bg='#62fabb',bd=4,font=('calibri',12,'bold'))
        btn_update.place(x=880,y=2,width=100,height=50)

        btn_del = Button(btn_frame,text='حدف مريض',fg='black',bg='#62fabb',bd=4,font=('calibri',12,'bold'))
        btn_del.place(x=760,y=2,width=100,height=50)

        btn_show = Button(btn_frame,text='عرض تقرير',fg='black',command=self.show_tq,bg='#62fabb',bd=4,font=('calibri',12,'bold'))
        btn_show.place(x=640,y=2,width=100,height=50)

        btn_print = Button(btn_frame,text='اضافة تقرير',fg='black',bg='#62fabb',command=self.inesrt_tahlel,bd=4,font=('calibri',12,'bold'))
        btn_print.place(x=520,y=2,width=100,height=50)

        btn_Add_doc = Button(btn_frame,text='اضافة دكتور',fg='black',command=self.addDoc,bg='#62fabb',bd=4,font=('calibri',12,'bold'))
        btn_Add_doc.place(x=400,y=2,width=100,height=50)
        
        btn_search = Button(btn_frame,text='بحث',fg='black',bg='#62fabb',bd=4,font=('calibri',12,'bold'))
        btn_search.place(x=280,y=2,width=100,height=50)
        
        lblsearch_py =Label(btn_frame,text='فلتره',bg='white',bd=4,font=('calibri',16,'bold')).place(x=20,y=5)
        combo_search = ttk.Combobox(btn_frame, width=15, state='readonly', font=(
        'calibri', 14, 'bold'), justify='center',textvariable=self.se_py)
        combo_search['value'] = ('الاسم', 'القسم','الهاتف','رقم التسلسلي')
        combo_search.place(x=16,y=9)
        ent_search = Entry(btn_frame,font=('calibri',12,'bold'),textvariable=self.se_var).place(x=5,y=9)
       
        datamarth= Frame(self.root,bg='white')
        datamarth.place(x=1,y=130 ,width=1125,height=570)
    
        scrol1_x =Scrollbar(datamarth,orient=HORIZONTAL)
        scrol1_y= Scrollbar(datamarth,orient=VERTICAL)




      
        #try vw doc
        Lb_title1 = Label(self.root,text='المرضى',bg='#62fabb',fg='black',font=('calibri',14,'bold'))
        Lb_title1.place(x=1,y=92,width=1125,height=40)
        self.martha_table = ttk.Treeview(datamarth,
        columns=('id','name','email_mr','phone','name_mr','nw3','age','date_in','date_out','mrajaa','dawa','mkhtas','mstawa','qasm'),
        xscrollcommand=scrol1_x.set,
        yscrollcommand=scrol1_y.set)
        self.martha_table.place(x=1,y=0,width=1110,height=550,)
      
        scrol1_x.pack(side=BOTTOM,fill=X)
        scrol1_y.pack(side=RIGHT,fill=Y)
        scrol1_x.config(command=self.martha_table.xview)
        scrol1_y.config(command=self.martha_table.yview)

        self.martha_table['show']='headings'
        self.martha_table.heading('id',text='رقم التسلسلي')
        self.martha_table.heading('name',text='اسم المريض')
        self.martha_table.heading('email_mr',text='بريد المرافق')
        self.martha_table.heading('phone',text='هاتف المرافق')
        self.martha_table.heading('name_mr',text='اسم المرافق')
        self.martha_table.heading('nw3',text='جنس المريض')
        self.martha_table.heading('age',text='العمر')
        self.martha_table.heading('date_in',text='تاريخ الدخول')
        self.martha_table.heading('date_out',text='تاريخ الخروج')
        self.martha_table.heading('mrajaa',text='المراجعه')
        self.martha_table.heading('dawa',text='الدواء')
        self.martha_table.heading('mkhtas',text='متابع الحاله')
        self.martha_table.heading('mstawa',text='التحايل')
        self.martha_table.heading('qasm',text='القسم \ الغرفه')
        

        self.martha_table.column('id',width=80)
        self.martha_table.column('name',width=150)
        self.martha_table.column('email_mr',width=150)
        self.martha_table.column('phone',width=90)
        self.martha_table.column('name_mr',width=150)
        self.martha_table.column('nw3',width=90)
        self.martha_table.column('age',width=30)
        self.martha_table.column('date_in',width=150)
        self.martha_table.column('date_out',width=150)
        self.martha_table.column('mrajaa',width=70)
        self.martha_table.column('dawa',width=100)
        self.martha_table.column('mkhtas',width=150)
        self.martha_table.column('mstawa',width=160)
        self.martha_table.column('qasm',width=150)
        self.martha_table.bind("<ButtonRelease-1>",self.get_data)
        self.fatch_martha()
       #  self.fatch_doctors()
    def get_data(self,event):
          selected_row =self.martha_table.focus()
          data = self.martha_table.item(selected_row)
          global row 
          row = data["values"]
          self.name.set(row[1])
          self.email_mr.set(row[2])
          self.phone_mr.set(row[3]) 
          self.name_mr.set(row[4])
          self.nw3.set(row[5])
          self.age.set(row[6])
          self.date_in.set(row[7])
          self.date_out.set(row[8])
          self.mrajaa.set(row[9])
          self.dawa.set(row[10])
          self.mkhtas.set(row[11])
          self.mstawa.set(row[12])
          self.qasm.set(row[13])
          
          
          
    
    def get_data_doc(self):
          selected_row =self.doctors_table.focus()
          data = self.doctors_table.item(selected_row)
          global row 
          row = data["values"]
          self.name_doc_1.set(row[1])
          self.takhss_1.set(row[2])
          self.phone_doc_1.set(row[3]) 
          self.dawam_1.set(row[4])
          self.addres_1.set(row[5])
          self.nationality_1.set(row[6])
           
   
        


    def fatch_martha(self):
          self.martha_table.delete(*self.martha_table.get_children())
          for row in db.fetch():
                self.martha_table.insert("",END,values=row)       
          
#     def fatch_doctors(self):
#         self.doctors_table.delete(*self.doctors_table.get_children())
#         for row in db2.fetch_doc():
#               self.doctors_table.insert("",END,values=row)           
    def addDoc(self):
        self.doc = Tk()
       

        self.doc.title("اضافة اطباء")
        self.doc.geometry('1350x715+0+0')
        self.doc.resizable(False,False)
        frame_doc = Frame(self.doc)
        frame_doc.pack()
       
        userinfo_frame = LabelFrame(frame_doc,text='معلومات الدكتور')
        userinfo_frame.grid(row=0 , column=0)

        fist_name_lbl = Label(userinfo_frame,text='الاسم')
        fist_name_lbl.grid(row=0,column=0,padx=20,pady=20)
        la_nm_lbl = Label(userinfo_frame, text='التخصص')
        la_nm_lbl.grid(row=0, column=1)


        

        Ent_firt_name1 = Entry(userinfo_frame,textvariable=self.name_doc_1)
        Ent_last_name1 = Entry(userinfo_frame,textvariable=self.takhss_1)
        Ent_firt_name1.grid(row=1,column=0)
        Ent_last_name1.grid(row=1,column=1)



        title = Label(userinfo_frame,text='رقم الهاتف')
        title.grid(row=0, column=2)
        titl_ent = Entry(userinfo_frame,textvariable=self.phone_doc_1)
        titl_ent.grid(row=1,column=2)
        



        age_lbl = Label(userinfo_frame, text= 'الدوام')
        age_span1 = Entry(userinfo_frame,textvariable=self.dawam_1)
        age_lbl.grid(row=2,column=0)
        age_span1.grid(row=3,column=0) 

        nationaliye_lbl = Label(userinfo_frame,text='nationality')
        nationaliye_commbo = ttk.Combobox(userinfo_frame,values=["libya","Iraq","Egypt","syria"],textvariable=self.nationality_1)
        nationaliye_commbo.grid(row=3,column=1)
        nationaliye_lbl.grid(row=2, column=1)
        
        
        self.dataDoc= Frame(self.doc,bg='white')
        self.dataDoc.place(x=460,y=150 ,width=830,height=550)
       
        
        scrol_x1 =Scrollbar(self.dataDoc,orient=HORIZONTAL)
        scrol_y1= Scrollbar(self.dataDoc,orient=VERTICAL)
        self.doctors_table = ttk.Treeview(self.doc,
        columns=('id_doc','name_doc','takhss','phone_doc','dawam','addres','nationality'),
        xscrollcommand=scrol_x1.set,
        yscrollcommand=scrol_y1.set)
        self.doctors_table.place(x=440,y=150,width=830,height=530,)

        scrol_x1.pack(side=BOTTOM,fill=X,)
        scrol_y1.pack(side=RIGHT,fill=Y)
        scrol_x1.config(command=self.doctors_table.xview)
        scrol_y1.config(command=self.doctors_table.yview)

        
        self.doctors_table['show']='headings'
        self.doctors_table.heading('id_doc',text='الايدي')
        self.doctors_table.heading('name_doc',text='الدكتور')
        self.doctors_table.heading('takhss',text='الاختصاص')
        self.doctors_table.heading('phone_doc',text='هاتف الدكتور')
        self.doctors_table.heading('dawam',text='الدوام')
        self.doctors_table.heading('addres',text='العنوان')
        self.doctors_table.heading('nationality',text='الجنسيه')


        self.doctors_table.column('id_doc',width=50)
        self.doctors_table.column('name_doc',width=150)
        self.doctors_table.column('takhss',width=150)
        self.doctors_table.column('phone_doc',width=90)
        self.doctors_table.column('dawam',width=150)
        self.doctors_table.column('addres',width=90)
        self.doctors_table.column('nationality',width=60)
        
        
        
        
        
        
        
        
        
        
        
        
        
        def add_doc1():
          con= pymysql.connect(host= 'localhost', user ='root', password ='', database = 'receptions1')
          cur = con.cursor()
          cur.execute("insert into d0ct0rs values(NULL,%s,%s,%s,%s,%s,%s)",(
                                                               self.name_doc_1.get(),
                                                               self.takhss_1.get(),
                                                               self.phone_doc_1.get(),
                                                               self.dawam_1.get(),
                                                               self.addres_1.get(),
                                                               self.nationality_1.get()
                                                            
          ))   
          con.commit()
         
          con.close()
        
        
        for widget in userinfo_frame.winfo_children():
                  widget.grid_configure(padx=10,pady=5)
        

        tahlel_Lbl= Label(self.doc,text=' العنوان')
        tahlel_Lbl.place(x=10,y=140)

        ent_tahlel1 = Entry(self.doc,textvariable=self.addres_1)
        ent_tahlel1.place(x=10,y=180,width=400,height=80) 
           
        tahlel1_Lbl= Label(self.doc,text='ـــــــــــــــــــــــــــــــــــــــــــــــــــــــــــ')
        tahlel1_Lbl.place(x=10,y=260,width=380)
       
       
        btn_print_taq = Button(self.doc,text='اضافة طبيب',fg='black',command=add_doc1,bg='#62fabb',bd=4,font=('calibri',12,'bold'))
        btn_print_taq.place(x=1,y=450,width=100,height=50)

        btn_clear = Button(self.doc,text='مسح الحقول',fg='black',command=self.clear,bg='#62fabb',bd=4,font=('calibri',12,'bold'))
        btn_clear.place(x=115,y=450,width=100,height=50)

        btn_clear = Button(self.doc,text='مسح طبيب',fg='black',bg='#62fabb',bd=4,font=('calibri',12,'bold'))
        btn_clear.place(x=225,y=450,width=100,height=50)
           
        tahlel2_Lbl= Label(self.doc,text='تحقق الادمن')
        tahlel2_Lbl.place(x=15,y=263)

        user_ad = Entry(self.doc,textvariable=self.user)
        user_ad.place(x=20,y=300)
       
        pass_ad = Entry(self.doc,textvariable=self.password)
        pass_ad.place(x=20,y=340)
        
        
    

    
       
        
        
        
        
        
        
        
        
        
      
           
      
        
                         
          
            
    def clear1(self):
            
          self.name.set("")
          self.email_mr.set("")
          self.phone_mr.set("")
          self.name_mr.set("")
          self.nw3.set("")
          self.age.set("")
          self.date_in.set("")
          self.date_out.set("")
          self.mrajaa.set("")
          self.dawa.set("")
          self.mkhtas.set("")
          self.mstawa.set("")
          self.qasm.set("")

                
    def clear(self):
          self.name_doc_1.set("")
          self.phone_doc_1.set("")
          self.takhss_1.set("")
          self.user.set("")
          self.password.set("")
          self.addres_1.set("")
          self.dawam_1.set("")
          self.nationality_1.set("")
         
        
  #=====الاتصال ====
    
    def Add_Martha(self):
            if self.name.get() == "" or self.age.get() == "" or self.phone_mr.get() =="" or self.nw3.get()=="":
                
                messagebox.showerror("خطأ","املئ الحقول المطلوبه")
                return
   
                    
    
           
            db.insert(
                        self.name.get(),
                        self.email_mr.get(),
                        self.phone_mr.get(),
                        self.name_mr.get(),
                        self.nw3.get(),
                        self.age.get(),
                        self.date_in.get(),
                        self.date_out.get(),
                        self.mrajaa.get(),
                        self.dawa.get(),
                        self.mkhtas.get(),
                        self.mstawa.get(),
                        self.qasm.get()
                )
            messagebox.showinfo('اضافة دكتور','تمت اضافة دكتور جديد')
        


        
    def help1(self):
      messagebox.showinfo('تعليمات','اولا السلام عليكم اخي \اختي المستخدم اليك \n التعليمات البسيطه لطريقة الاستخدام لاضافة مريض اضف البيانات في الحقول ثم اضغط على اضافه وللحذف اضغط على الاسم المراد حذفه واضغط حذف \n وكذالك للتعديل هذا يعتبر الاصدار الاول من المنظومه ولازال هناك افكار \n في حال واجهتك مشكله اتصل بي \n0912896101')
        
 
    
    
   
        #=====vz7tKn56UWMyn5qS كلمة المرور   
    def inesrt_tahlel(self):
           self.tqarer = Tk()
          
           self.tqarer.title("اضافة تقارير")
           self.tqarer.geometry('500x500+100+100')
           self.tqarer.resizable(False,False)
           frame_tqarer = Frame(self.tqarer)
           frame_tqarer.pack()

           userinfo_frame = LabelFrame(frame_tqarer,text='معلومات المستخدم')
           userinfo_frame.grid(row=0 , column=0)

           fist_name_lbl = Label(userinfo_frame,text='First_Name')
           fist_name_lbl.grid(row=0,column=0,padx=20,pady=20)
           la_nm_lbl = Label(userinfo_frame, text='last name')
           la_nm_lbl.grid(row=0, column=1)


        

           Ent_firt_name = Entry(userinfo_frame)
           Ent_last_name = Entry(userinfo_frame)
           Ent_firt_name.grid(row=1,column=0)
           Ent_last_name.grid(row=1,column=1)



           title = Label(userinfo_frame,text='gendery')

           titl_commbo = ttk.Combobox(userinfo_frame, values=["male","female"])
           title.grid(row=0, column=2)
           titl_commbo.grid(row=1,column=2) 



           age_lbl = Label(userinfo_frame, text= 'Age')
           age_span = Spinbox(userinfo_frame,state='readonly',from_=1, to=100)
           age_lbl.grid(row=2,column=0)
           age_span.grid(row=3,column=0) 

           nationaliye_lbl = Label(userinfo_frame,text='nationality')
           nationaliye_commbo = ttk.Combobox(userinfo_frame,values=["libya","Iraq","Egypt","syria"])
           nationaliye_commbo.grid(row=3,column=1)
           nationaliye_lbl.grid(row=2, column=1)

           for widget in userinfo_frame.winfo_children():
                  widget.grid_configure(padx=10,pady=5)
           

           tahlel_Lbl= Label(self.tqarer,text='تقرير طبي')
           tahlel_Lbl.place(x=10,y=140)

           ent_tahlel = Text(self.tqarer)
           ent_tahlel.place(x=10,y=180,width=400,height=80) 
           
           tahlel1_Lbl= Label(self.tqarer,text='ـــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــ')
           tahlel1_Lbl.place(x=10,y=260,width=480)
           
           
           tahlel2_Lbl= Label(self.tqarer,text='تحاليل مطلوبه ')
           tahlel2_Lbl.place(x=15,y=263)

           combo_nw3 = ttk.Combobox(self.tqarer, width=15, font=(
        'calibri', 14, 'bold'), justify='center')
           combo_nw3['value'] = ('TSH', 'CBC','BRCs','HCT','MCV','MCHC','PLT','W.B.C','ESR','LDL','HDL','TG','ACTH','ALT(SGPT)','Abunim','Aldolase','Ca','Ca CSF','CA 125','CA 15-3','CEA','Ca lonized')
           combo_nw3.place(x=20,y=300)

           
           btn_Add_taq = Button(self.tqarer,text='اضافة تقرير',fg='black',bg='#62fabb',bd=4,font=('calibri',12,'bold'))
           btn_Add_taq.place(x=1,y=450,width=100,height=50)

           btn_print_taq = Button(self.tqarer,text='طباعة تقرير',fg='black',bg='#62fabb',bd=4,font=('calibri',12,'bold'))
           btn_print_taq.place(x=115,y=450,width=100,height=50)

           btn_clear = Button(self.tqarer,text='افراغ تقرير',fg='black',bg='#62fabb',bd=4,font=('calibri',12,'bold'))
           btn_clear.place(x=225,y=450,width=100,height=50)


    def show_tq(self):
          self.show = Tk()
          self.show.title('عرض التقارير')
          self.show.geometry('890x515+100+100') 
          self.show.resizable(False,False)
          scrol_x =Scrollbar(self.show,orient=HORIZONTAL)
          scrol_y= Scrollbar(self.show,orient=VERTICAL)
          self.taq_table = ttk.Treeview(self.show,
          columns=('first_name','last_name','gendery','age','nationality','txt_taq','tahlel'),
          xscrollcommand=scrol_x.set,
          yscrollcommand=scrol_y.set)
          self.taq_table.place(x=1,y=1,width=870,height=380,)

          scrol_x.pack(side=BOTTOM,fill=X,)
          scrol_y.pack(side=RIGHT,fill=Y)
          scrol_x.config(command=self.doctors_table.xview)
          scrol_y.config(command=self.doctors_table.yview)

        
          self.taq_table['show']='headings'
          self.taq_table.heading('first_name',text='الاسم الاول')
          self.taq_table.heading('last_name',text='اسم العائله')
          self.taq_table.heading('gendery',text='جنس المريض')
          self.taq_table.heading('age',text='العمر')
          self.taq_table.heading('nationality',text='الجنسيه')
          self.taq_table.heading('txt_taq',text='تقرير طبي')
          self.taq_table.heading('tahlel',text='التحاليل المطلوبه')


        
          self.taq_table.column('first_name',width=150)
          self.taq_table.column('last_name',width=150)
          self.taq_table.column('gendery',width=90)
          self.taq_table.column('age',width=70)
          self.taq_table.column('nationality',width=70)
          self.taq_table.column('txt_taq',width=200)
          self.taq_table.column('tahlel',width=150)


          btn_updaet = Button(self.show,text='تعديل تقرير',bg='#62fabb',fg='black',font=('calibri',12,'bold'))
          btn_updaet.place(x=1,y=460,width=90,height=40)

          btn_se = Button(self.show,text='بحث عن تقرير',bg='#62fabb',fg='black',font=('calibri',12,'bold'))
          btn_se.place(x=90,y=460,width=90,height=40)


          ent_se = Entry(self.show,bg='#62fabb',fg='black',font=('calibri',12,'bold'))
          ent_se.place(x=1,y=420)
          

          
          

          
           

         
                    
root= Tk()
main = martha(root)


root.mainloop()