from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk

root=Tk()
root.geometry("400x300")
root.minsize(200,100)
root.title('criminal management system')



p=Label(text='CRIMINAL MANAGEMENT SYSTEM',font=('time new roman',40),bg='brown',fg='gold')
p.place(x=0,y=0,width=1530,height=70)

p1=Label(text='Our criminal justice system treats you better if you are rich and guilty than if you are poor and innocent',font=('Comic Sans MS',20),bg='white',fg='black')
p1.place(x=0,y=100,width=1530,height=70)

#main frame
f1=Frame(root,bd=2,relief=RIDGE,bg='white')
f1.place(x=10,y=200,width=1500,height=560)

#subframe
f2=LabelFrame(f1,bd=2,relief=RIDGE,text='Crime Record',font=('time new roman',15),fg='black',bg='white')
f2.place(x=10,y=20,width=1359,height=280)

frame = Frame(f2,height=280)
frame.place(x=1080,y=0,anchor='w',width=300)

# Create an object of tkinter ImageTk
img = ImageTk.PhotoImage(Image.open("sss.png"))

# Create a Label Widget to display the text or Image
label = Label(frame, image = img)
label.pack(padx=3,pady=3)

id=Label(f2,text="CASE_ID" ,font=('arial',11),bg='white',pady=5).grid(row=0,column=0,padx=2)
name=Label(f2,text="CRIMINAL NAME",font=('arial',11),bg='white',pady=5).grid(row=0,column=2,padx=2)
mark=Label(f2,text="BIRTH MARK",font=('arial',11),bg='white',pady=5).grid(row=0,column=4,padx=2)
date=Label(f2,text="ARREST DATE",font=('arial',11),bg='white',pady=5).grid(row=2)
address=Label(f2,text="ADDRESS",font=('arial',11),bg='white',pady=5).grid(row=6)
criminalno=Label(f2,text="CRIMINAL NO",font=('arial',11),bg='white',pady=5).grid(row=8)
age=Label(f2,text="AGE",font=('arial',11),bg='white',pady=5).grid(row=10)
sex=Label(f2,text="SEX",font=('arial',11),bg='white',pady=5).grid(row=12)
dateofcrime=Label(f2,text='DATE OF CRIME',font=('arial',11),bg='white',pady=5).grid(row=2,column=2,padx=2)
crime=Label(f2,text='CRIME DESCRIPTION',font=('arial',11),bg='white',pady=5).grid(row=2,column=4,padx=2)



#variable class in tkinter

id_value=StringVar()
name_value=StringVar()
mark_value=StringVar()
date_value=StringVar()
address_value=StringVar()
criminalno_value=StringVar()
age_value=StringVar()
sex_value=StringVar()
dateofcrime_value=StringVar()
crime_value=StringVar()

identry=Entry(f2,textvariable=id_value,font=('arial')).grid(row=0,column=1,padx=2,sticky=W)
nameentry=Entry(f2,textvariable=name_value,font=('arial')).grid(row=0,column=3,padx=2,sticky=W)
markentry=Entry(f2,textvariable=mark_value,font=('arial')).grid(row=0,column=5,padx=2)
dateentry=Entry(f2,textvariable=date_value,font=('arial')).grid(row=2,column=1,padx=2,sticky=W)
addressentry=Entry(f2,textvariable=address_value,font=('arial')).grid(row=6,column=1,padx=2,sticky=W)
criminalnoentry=Entry(f2,textvariable=criminalno_value,font=('arial')).grid(row=8,column=1,padx=2,sticky=W)
ageentry=Entry(f2,textvariable=age_value,font=('arial')).grid(row=10,column=1,padx=2,sticky=W)
sexentry=Entry(f2,textvariable=sex_value,font=('arial',)).grid(row=12,column=1,padx=2,sticky=W)
dateofcrimeentry=Entry(f2,textvariable=dateofcrime_value,font=('arial')).grid(row=2,column=3,padx=2,sticky=W)
crimeentry=Entry(f2,textvariable=dateofcrime_value,font=('arial')).grid(row=2,column=5,padx=2,sticky=W)

#button
buttonframe=Frame(f2,bd=2,relief=RIDGE,bg='white')
buttonframe.place(x=5,y=200,width=470,height=35)

#addbutton
b1=Button(buttonframe,text='SAVE',font=('arial',13,'bold'),width=14,bg='blue',fg='white').grid(row=0,column=0,padx=5)
b2=Button(buttonframe,text='DELETE',font=('arial',13,'bold'),width=14,bg='blue',fg='white').grid(row=0,column=1,padx=5)
b3=Button(buttonframe,text='UPDATE',font=('arial',13,'bold'),width=14,bg='blue',fg='white').grid(row=0,column=2,padx=5)


f3=LabelFrame(f1,bd=2,relief=RIDGE,text='Criminal Record',font=('time new roman',15),fg='red',bg='white')
f3.place(x=10,y=300,width=1480,height=400)

search=LabelFrame(f3,bd=2,relief=RIDGE,text='Search criminal record',font=('time new roman',15),fg='blue',bg='white')
search.place(x=0,y=0,width=1470,height=50)

search_by=Label(search,font=('arial',11,'bold'),text='Search',bg='blue',fg='white')
search_by.grid(row=0,column=0,sticky=W)

search_box=ttk.Combobox(search,font=('arial',11,'bold'),width=20)
search_box['value']=('select option :','case_id','criminal_name')
search_box.set(0)
search_box.grid(row=0,column=1,sticky=W,padx=2)

table_frame=Frame(f3,bd=2,relief=RIDGE,bg='white')
table_frame.place(x=0,y=55,width=1500,height=180)

scrollx=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
scrolly=ttk.Scrollbar(table_frame,orient=VERTICAL)
criminaltable=ttk.Treeview(table_frame,columns=('1','2','3','4','5','6','7','8','9'))
xscrollcommand=scrollx.set
yscrollcommand=scrolly.set
scrollx.pack(side=BOTTOM,fill=X)
scrolly.pack(side=RIGHT,fill=Y)

criminaltable.heading('1',text='case_id')
criminaltable.heading('2',text='criminal name')
criminaltable.heading('3',text='birth mark')
criminaltable.heading('4',text='arrest date')
criminaltable.heading('5',text='date of crime')
criminaltable.heading('6',text='crime desc')
criminaltable.heading('7',text='criminal no')
criminaltable.heading('8',text='age')
criminaltable.heading('9',text='sex')

criminaltable.pack(fill=BOTH)


root.mainloop()
