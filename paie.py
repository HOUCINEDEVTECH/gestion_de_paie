from tkinter import *
from tkinter import  messagebox ,ttk
from tkcalendar import *
import sqlite3 
import os
import tempfile
class Payement :
    def __init__(self,root) :
          self.root =  root
          self.root.title(" Gestion de paie")
          self.root.geometry("1300x1000+0+0")
          title = Label( self.root, text =" Gestion de Paie Proffesseur",bd=20, relief= RAISED , font= (' Algerian', 45),bg= 'cyan', fg= 'black')
          title.pack( side =TOP, fill= X)
         ################################################# FRAME1




          Frame1 = Frame(self.root ,bd= 2 , relief=RIDGE)
          Frame1.place( x=10 , y= 120 , width= 675 , height= 675)
          
          title2  = Label ( Frame1, text=" Information Proffesseur" , bd= 20 , relief= RAISED , font=( " Algerian" , 30 ), bg="lightgray" , fg= "black")
          title2.pack( side= TOP , fill= X)

          Label.code = Label( Frame1, text = "Code professeur" , font =("times new roman", 20 )).place(  x = 120, y = 95 )
          self.txt_code= Entry ( Frame1, font=( ' times new roman', 25) , bg = "lightyellow" , fg = "black")
          self.txt_code.place(x= 320,y= 95, width = 150)
          btn_recher= Button(Frame1 ,text ="Recherche", font=("times new roman" , 16," bold"),bg= "gray").place(x=500, y= 95,width= 150)

          Label.etblissement = Label( Frame1, text = "Etablissement" , font =("times new roman", 20 )).place(  x = 10, y = 170 )
          Label.Nom= Label( Frame1, text = "Nom" , font =("times new roman", 20 )).place(  x = 10, y = 230 )
          Label.Prenom= Label( Frame1, text = "Prenom" , font =("times new roman", 20 )).place(  x = 10, y = 290)

          Label.Sex= Label( Frame1, text = "Sex" , font =("times new roman", 20 )).place(  x = 10, y = 350) 
          Label.Email= Label( Frame1, text = "E_mail" , font =("times new roman", 20 )).place(  x = 10, y = 400)
          Label.Nationnalite= Label( Frame1, text = "Nationnalite" , font =("times new roman", 20 )).place(  x = 10, y = 450 )
          Label.Adress= Label( Frame1, text = "Adresse" , font =("times new roman", 20 )).place(  x = 10, y = 500 )
          Label.Anne_Acad= Label( Frame1, text = "Anne Academique" , font =("times new roman", 20 )).place(  x = 320, y = 170 )
          Label.Date_naiss= Label( Frame1, text = "Date de naissance" , font =("times new roman", 20 )).place(  x = 320, y = 230 )
          Label.EXPER= Label( Frame1, text = "Experience" , font =("times new roman", 20 )).place(  x = 320, y = 290)
          Label.identification= Label( Frame1, text = "Identification" , font =("times new roman", 20 )).place(  x = 320, y = 350)
          Label.Tel= Label( Frame1, text = "Tel " , font =("times new roman", 20 )).place(  x = 420 , y = 400)
          Label.Stat= Label( Frame1, text = "Statut" , font =("times new roman", 20 )).place(  x = 400, y = 450)
          

          self.etablissement= Entry ( Frame1, font=( ' times new roman', 25) , bg = "lightyellow" , fg = "black")
          self.etablissement.place(x= 170,y= 170, width = 150)
          self.Nom= Entry ( Frame1, font=( ' times new roman', 25) , bg = "lightyellow" , fg = "black")
          self.Nom.place(x= 170,y= 230 , width = 150)
          self.Prenom= Entry ( Frame1, font=( ' times new roman', 25) , bg = "lightyellow" , fg = "black")
          self.Prenom.place(x= 170,y= 290 , width = 150)
          self.ecri_sexe= ttk.Combobox(Frame1,font=("times new roman",15 ), state = "readonly")
          self.ecri_sexe["values"] = (" Homme"," Femme")
          self.ecri_sexe.place(x = 170  , y = 355  , width= 140 )
          self.ecri_sexe.current(0)
          self.Email= Entry ( Frame1, font=( ' times new roman', 16) , bg = "lightyellow" , fg = "black")
          self.Email.place( x=170 ,y = 410  ,width=250 )
          self.Nationanalite= Entry ( Frame1, font=( ' times new roman', 20) , bg = "lightyellow" , fg = "black")
          self.Nationanalite.place( x=170 ,y =  450   ,width= 220 )
          self.Adress= Entry ( Frame1, font=( ' times new roman', 20) , bg = "lightyellow" , fg = "black")
          self.Adress.place( x=170 ,y =  500   ,width= 600 )
          self.EXPER= Entry ( Frame1, font=( ' times new roman', 20) , bg = "lightyellow" , fg = "black")
          self.EXPER.place( x= 500  ,y =  290 ,width= 150 )

          self.Identification = Entry(Frame1, font=(' times new roman', 20), bg="lightyellow", fg="black")
          self.Identification.place(x=500, y=350, width=150)

          self.Tel = Entry(Frame1, font=(' times new roman', 16), bg="lightyellow", fg="black")
          self.Tel.place(x=500, y=400, width=150)
          self.ecri_statut= ttk.Combobox(Frame1, font=("times new roman", 15), state="readonly")
          self.ecri_statut["values"] = (" celebataire ", " marie ", " Divorse")
          self.ecri_statut.place(x=500, y=450 , width=140)

          self.Anne_Acad = ttk.Combobox(Frame1, font=("times new roman", 15), state="readonly")
          self.Anne_Acad["values"] = (" 2019/2020 ", " 2020/2021 ", " 2021/2022","2022/2023 ")
          self.Anne_Acad.place(x=530, y=170, width=140)
          self.Anne_Acad.current(0)
          self.ecri_date= DateEntry(Frame1 , font=( "time new roman" , 15 ) ,bg = "lightgray" ,state = "readonly", date_pattern ='dd/mm/yy' )
          self.ecri_date.place(x=530, y=230, width=140)
          ######################################### CONSTRUCTION FRAME 2
          Frame2 = Frame(self.root, bd=2, relief=RIDGE)
          Frame2.place(x=700, y=120, width=575, height=575)

          title3 = Label(Frame2, text=" Salaire Professeur ", bd=20, relief=RAISED, font=(" Algerian", 22), bg="lightgray", fg="black")
          title3.pack(side= TOP, fill=X)
          Label.Mois = Label(Frame2, text="Mois", font=("times new roman", 15)).place(x=20 , y=95)
          Label.anne = Label(Frame2, text="Année", font=("times new roman", 15)).place(x=350 , y=95)
          Label.mode_payment = Label(Frame2, text="Mode de payment", font=("times new roman", 15)).place(x=20, y=140)
          Label.matière = Label(Frame2, text="Matière", font=("times new roman", 15)).place(x=350, y=140)
          Label.nombre_heure = Label(Frame2, text="Nombre d'Heure", font=("times new roman", 15)).place(x=20, y=180)
          Label.tarif_Horaire = Label(Frame2, text="Tarif Horaire", font=("times new roman", 15)).place(x=20, y=220)
          Label.Salaire_Net = Label(Frame2, text=" Salaire Net ", font=("times new roman", 15, " bold")).place(x=310, y=220)

          self.ADJ_Mois = ttk.Combobox(Frame2, font=("times new roman", 15), state="readonly")
          self.ADJ_Mois["values"] = (" Jan ", " Fev ", " Mars" , " Avr ", "Mai", "Juin", "Juill", "Aout", "Sept", "Oct", "Nouv","Dec")
          self.ADJ_Mois.place(x=150 , y=95, width=140)
          self.ADJ_Mois.current(0)
          self.ADJ_anne = ttk.Combobox(Frame2, font=("times new roman", 15), state="readonly")
          self.ADJ_anne["values"] = (" 2019", " 2020" ,"2021" ,"2022" )
          self.ADJ_anne.place(x= 426, y=95, width=140)
          self.ADJ_anne.current(0)
          self.matière = Entry(Frame2, font=(' times new roman',15), bg="lightyellow", fg="black")
          self.matière.place(x=420, y=140, width=140)
          self.Salaire_net = Entry(Frame2, font=(' times new roman', 15), bg="lightyellow", fg="black")
          self.Salaire_net.place(x=420, y=220, width=140)
          self.Nombre_Heure = Entry(Frame2, font=(' times new roman', 15), bg="lightyellow", fg="black")
          self.Nombre_Heure.place(x= 170, y=180, width=140)
          self.Tarif_Heure = Entry(Frame2, font=(' times new roman', 15), bg="lightyellow", fg="black")
          self.Tarif_Heure.place(x=170, y=220, width=140)

          self.Selectpay = ttk.Combobox(Frame2, font=("times new roman", 15), state="readonly")
          self.Selectpay["values"] = ( " Selection" ," Espece ", " Cheque ", " Virment")
          self.Selectpay.place(x=170, y=140, width=140)
          self.Selectpay.current(0)
          self.btn_calcul= Button(Frame2 ,  text= " Calculer "  , font=("times new roman", 15, " bold") , bg= 'orange')
          self.btn_calcul.place(x=10, y= 300, width= 160 )

          self.sauvegarde = Button(Frame2, text=" Sauvegarder ", font=("times new roman", 15, " bold"), bg='GREEN')
          self.sauvegarde.place(x=200, y=300, width=160)

          self.Res= Button(Frame2, text=" Resiter", font=("times new roman", 15, " bold"), bg='GREEN')
          self.Res.place(x=400, y=300, width=160)

          self.modifier = Button(Frame2, text=" Modifier ", font=("times new roman", 15, " bold"), bg='YELLOW')
          self.modifier.place(x=10, y=350, width=160)

          self.sup = Button(Frame2, text=" Supprimer", font=("times new roman", 15, " bold"), bg='RED')
          self.sup.place(x=300, y=350, width=160)
          ######################################## FRAME 3


          ###########################FRAME3

          Frame3 = Frame(self.root, bd=2, relief=RIDGE)
          Frame3.place(x=700, y=525, width=900, height=400)
          ####CALCULATRICE
          Cal_Frame =Frame( Frame3, bd = 2 ,relief = RIDGE)
          Cal_Frame.place( x= 5 , y = 5, width =  285, height = 334)
          self.var_txt= StringVar()
          self.var_operation=""


          def btn_click(nombre):
                self.var_operation= self.var_operation+str(nombre)
                self.var_txt.set(self.var_operation)

          def resulat():
              resulat= str(eval( self.var_operation))
              self.var_txt.set( resulat)
              self.var_operation = ""

          def clear():
                self.var_txt.set("")
                self.var_operation=""





          txt_resultat = Entry( Cal_Frame , textvariable=self.var_txt,state= "readonly" , font=(" times new roman", 20, "bold"), justify=RIGHT).place( x = -59, y = 9, relheight= 1, height=50)


          btn_7 = Button(Cal_Frame, text = "7",command= lambda : btn_click(7),font =("times new roman",20," bold")).place ( x= 5 , y= 10, height=40, width= 30)
          btn_8 = Button(Cal_Frame,text="8", command= lambda : btn_click(8),font=("times new roman", 20, " bold")).place(x=40, y=10,height=40, width=30)
          btn_9 = Button(Cal_Frame,text="9", command= lambda : btn_click(9),font=("times new roman", 20, " bold")).place(x=75, y=10,height=40, width=30)
          btn_DIV = Button(Cal_Frame,text="/", command= lambda : btn_click("/"),font=("times new roman", 20, " bold")).place(x=110, y=10,height=40, width=30)
          btn_4 = Button(Cal_Frame,text="4", command= lambda : btn_click(4),font=("times new roman", 20, " bold")).place(x=5, y= 50,height=40, width=30)
          btn_5 = Button(Cal_Frame,text="5", command= lambda : btn_click(5),font=("times new roman", 20, " bold")).place(x=40, y= 50,height=40, width=30)
          btn_6 = Button(Cal_Frame,text="6", command= lambda : btn_click(6),font=("times new roman", 20, " bold")).place(x=75, y= 50,height=40, width=30)
          btn_MULTI = Button(Cal_Frame,text="*",command= lambda : btn_click("*"),font=("times new roman", 20, " bold")).place(x=110, y= 50,height=40, width=30)
          btn_1 = Button(Cal_Frame,text="1",command= lambda : btn_click(1),font=("times new roman", 20, " bold")).place(x=5, y=90,height=40, width=30)
          btn_2 = Button(Cal_Frame,text="2",command= lambda : btn_click(2),font=("times new roman", 20, " bold")).place(x=40, y=90,height=40, width=30)
          btn_3 = Button(Cal_Frame,text="3",command= lambda : btn_click(3),font=("times new roman", 20, " bold")).place(x=75, y=90,height=40, width=30)
          btn_ADD = Button(Cal_Frame,text="+",command= lambda : btn_click("+"),font=("times new roman", 20, " bold")).place(x=110, y=90,height=40, width=30)
          btn_ZERO= Button(Cal_Frame,text="0",command= lambda : btn_click(0),font=("times new roman", 20, " bold")).place(x=5, y=140,height=40, width=30)
          btn_INIT = Button(Cal_Frame,text="C",command= clear,font=("times new roman", 20, " bold")).place(x=40, y=140,height=40, width=30)
          btn_SOUS = Button(Cal_Frame,text="-",command= lambda : btn_click("-"),font=("times new roman", 20, " bold")).place(x=75, y=140,height=40, width=30)
          btn_EGALE = Button(Cal_Frame,text="=", command= resulat,font=("times new roman", 20, " bold")).place(x=110, y=140,height=40, width=30)






root = Tk()
obj  = Payement(root)
root.mainloop()