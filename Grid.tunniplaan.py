from tkinter import*
from tkinter.messagebox import*

Lessons={}
with open("TextFile.txt","r") as f:
	for i in f: # создаем цикл по кол-ву строк
		k,v=i.strip().split(" -") # отделяем слова на строчке в строчке по знаку " - "
		Lessons[k.strip()]=v.strip() # добавляем в словарь

def newwind():
	text=esttug2.get("text")
	showinfo("tunni informatsioon",Lessons.get(text) )
	newwd=Toplevel() #tk()

wind=Tk()

Label(wind,text=" ").grid(row=0,column=0)
Label(wind,text="0\n7.40-8.25",borderwidth=1,relief="solid").grid(row=0,column=2,sticky=W+E+N+S)
Label(wind,text="1\n8.30-9.15",borderwidth=1,relief="solid").grid(row=0,column=3,sticky=W+E+N+S)
Label(wind,text="2\n9.20-10.05",borderwidth=1,relief="solid").grid(row=0,column=4,sticky=W+E+N+S)
Label(wind,text="3\n10.10-10.55",borderwidth=1,relief="solid").grid(row=0,column=5,sticky=W+E+N+S)
Label(wind,text="4\n11.00-11.45",borderwidth=1,relief="solid").grid(row=0,column=6,sticky=W+E+N+S)
Label(wind,text="5\n11.50-12.35",borderwidth=1,relief="solid").grid(row=0,column=7,sticky=W+E+N+S)
Label(wind,text="6\n12.40-13.25",borderwidth=1,relief="solid").grid(row=0,column=8,sticky=W+E+N+S)
Label(wind,text="7\n13.30-14.15",borderwidth=1,relief="solid").grid(row=0,column=9,sticky=W+E+N+S)
Label(wind,text="8\n14.20-15.05",borderwidth=1,relief="solid").grid(row=0,column=10,sticky=W+E+N+S)
Label(wind,text="9\n15.10-15.55",borderwidth=1,relief="solid").grid(row=0,column=11,sticky=W+E+N+S)
Label(wind,text="10\n16.00-16.45",borderwidth=1,relief="solid").grid(row=0,column=12,sticky=W+E+N+S)

esm=Label(wind,text="Esmaspäev",borderwidth=1,relief="solid").grid(row=1,rowspan=2,column=0,columnspan=2,sticky=W+E+N+S)
teis=Label(wind,text="Teisipäev",borderwidth=1,relief="solid").grid(row=3,rowspan=2,column=0,columnspan=2,sticky=W+E+N+S)
kolm=Label(wind,text="Kolmapäev",borderwidth=1,relief="solid").grid(row=5,rowspan=2,column=0,columnspan=2,sticky=W+E+N+S)
nelj=Label(wind,text="Neljapäev",borderwidth=1,relief="solid").grid(row=7,rowspan=2,column=0,columnspan=2,sticky=W+E+N+S)
reede=Label(wind,text="Reede",borderwidth=1,relief="solid").grid(row=9,rowspan=2,column=0,columnspan=2,sticky=W+E+N+S)

Label(wind,text=" ",borderwidth=1,relief="solid").grid(row=1,column=3,sticky=W+E+N+S)

esttug2=Button(wind,text="Tugiõpe Eesti keel \n 2 grupp",bg="#9d7a73",borderwidth=1,relief="solid",command=newwind).grid(row=2,column=3,sticky=W+E+N+S)

esmLogist=Button(wind,text="Logistikateenused ja \n varude juhtmine",bg="lightgreen",borderwidth=1,relief="solid").grid(row=1,rowspan=2,column=4,columnspan=2,sticky=W+E+N+S)
mat=Button(wind,text="Matemaatika",bg="pink",borderwidth=1,relief="solid").grid(row=1,rowspan=2,column=6,columnspan=2,sticky=W+E+N+S)
Label(wind,text=" Перерыв ",borderwidth=1,relief="solid").grid(row=1,rowspan=2,column=8,sticky=W+E+N+S)
keel=Button(wind,text="Keel ja kirjandus",bg="#32F224",borderwidth=1,relief="solid").grid(row=1,rowspan=2,column=9,columnspan=2,sticky=W+E+N+S)
tugmat=Button(wind,text="Tugiõpe \n Matemaatika",bg="pink",borderwidth=1,relief="solid").grid(row=1,rowspan=2,column=11,sticky=W+E+N+S)

Label(wind,text=" ",borderwidth=1,relief="solid").grid(row=6,column=3,sticky=W+E+N+S)
tugkeem=Button(wind,text="Tugiõpe Keemia",borderwidth=1,relief="solid",bg="#C929CB").grid(row=3,rowspan=2,column=3,sticky=W+E+N+S)
teisprog=Button(wind,text="Programmeerimise alused \n (eesti keeles)",bg="lightblue",borderwidth=1,relief="solid").grid(row=3,rowspan=2,column=4,columnspan=3,sticky=W+E+N+S)
Label(wind,text=" Перерыв ",borderwidth=1,relief="solid").grid(row=3,rowspan=2,column=7,sticky=W+E+N+S)
fuusika=Button(wind,text="Füüsika",bg="pink",borderwidth=1,relief="solid").grid(row=3,rowspan=2,column=8,columnspan=2,sticky=W+E+N+S)

esttug1=Button(wind,text="Tugiõpe Eesti keel \n 1 grupp",borderwidth=1,relief="solid",bg="#F335F6").grid(row=5,column=3,sticky=W+E+N+S)
kunst=Button(wind,text="Kunstiained",borderwidth=1,relief="solid",bg="#C929CB").grid(row=5,rowspan=2,column=4,columnspan=2,sticky=W+E+N+S)
Label(wind,text=" Перерыв ",borderwidth=1,relief="solid").grid(row=5,rowspan=2,column=6,sticky=W+E+N+S)
kehalinekasv=Button(wind,text="Kehaline Kasvatus",borderwidth=1,relief="solid",bg="#C929CB").grid(row=5,rowspan=2,column=7,columnspan=2,sticky=W+E+N+S)

neljLogist=Button(wind,text="Logistikateenused ja \n varude juhtmine",borderwidth=1,relief="solid",bg="lightgreen").grid(row=7,rowspan=2,column=3,columnspan=2,sticky=W+E+N+S)
Label(wind,text=" Перерыв ",borderwidth=1,relief="solid").grid(row=7,rowspan=2,column=5,sticky=W+E+N+S)
neljprog=Button(wind,text="Programmeerimise alused \n (eesti keeles)",bg="lightblue",borderwidth=1,relief="solid").grid(row=7,rowspan=2,column=6,columnspan=2,sticky=W+E+N+S)
ingl1=Button(wind,text="Inglise keel \n 1 grupp",borderwidth=1,relief="solid",bg="#E0E4C0").grid(row=7,column=8,columnspan=2,sticky=W+E+N+S)
merk2=Button(wind,text="Rakendustarkvara ja \n arenduskeskkonna loomine \n (IT valdkonna alusteadmised)",borderwidth=1,relief="solid",bg="#CF4141").grid(row=8,column=8,columnspan=2,sticky=W+E+N+S)
merk1=Button(wind,text="Rakendustarkvara ja \n arenduskeskkonna loomine \n (IT valdkonna alusteadmised)",borderwidth=1,relief="solid",bg="#CF4141").grid(row=7,column=10,columnspan=2,sticky=W+E+N+S)
est2=Button(wind,text="Eesti keel \n 2 grupp",borderwidth=1,relief="solid",bg="#9d7a73").grid(row=8,column=10,columnspan=2,sticky=W+E+N+S)
ruhm=Button(wind,text="Rühmajuhataja \n tund",borderwidth=1,relief="solid",bg="#F335F6").grid(row=7,rowspan=2,column=12,sticky=W+E+N+S)

est1=Button(wind,text="Eesti keel \n 1 grupp",borderwidth=1,relief="solid",bg="#F335F6").grid(row=9,column=3,columnspan=2,sticky=W+E+N+S)
merkul2=Button(wind,text="Rakendustarkvara ja \n arenduskeskkonna loomine \n (IT valdkonna alusteadmised)",borderwidth=1,relief="solid",bg="#CF4141").grid(row=10,column=3,columnspan=2,sticky=W+E+N+S)
redprogram=Button(wind,text="Programmeerimise alused \n (eesti keeles)",bg="lightblue",borderwidth=1,relief="solid").grid(row=9,rowspan=2,column=5,columnspan=5,sticky=W+E+N+S)
merkul1=Button(wind,text="Rakendustarkvara ja \n arenduskeskkonna loomine \n (IT valdkonna alusteadmised)",borderwidth=1,relief="solid",bg="#CF4141").grid(row=9,column=10,columnspan=2,sticky=W+E+N+S)
ingl2=Button(wind,text="Inglise keel \n 2 grupp",borderwidth=1,relief="solid",bg="#32F224").grid(row=10,column=10,columnspan=2,sticky=W+E+N+S)

wind.mainloop()