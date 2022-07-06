

import requests

import random
from tkinter import *
from tkinter import filedialog,messagebox
import time
from PIL import Image,ImageTk






def reset():
    textreciept.delete(1.0,END)
    e_dosa.set('0')
    e_bhatura.set('0')
    e_fries.set('0')
    e_bhaji.set('0')
    e_hotdog.set('0')
    e_rice.set('0')
    e_sandwich.set('0')
    e_nuggets.set('0')
    e_tikka.set('0')
    e_laasi.set('0')
    e_coffee.set('0')
    e_faluda.set('0')
    e_shikanji.set('0')
    e_jaljeera.set('0')
    e_roohafza.set('0')
    e_tea.set('0')
    e_milk.set('0')
    e_drink.set('0')
    e_oreo.set('0')
    e_apple.set('0')
    e_ktkat.set('0')
    e_vanilla.set('0')
    e_banana.set('0')
    e_brownie.set('0')
    e_pineapple.set('0')
    e_choco.set('0')
    e_forest.set('0')

    txtdosa.config(state=DISABLED)
    txtbhaji.config(state=DISABLED)
    txtbhatura.config(state=DISABLED)
    txtfries.config(state=DISABLED)
    txthotdog.config(state=DISABLED)
    txtnuggets.config(state=DISABLED)
    txtsandwich.config(state=DISABLED)
    txtrice.config(state=DISABLED)
    txttikka.config(state=DISABLED)

    txtlaasi.config(state=DISABLED)
    txtcoffee.config(state=DISABLED)
    txtfaluda.config(state=DISABLED)
    txtjaljeera.config(state=DISABLED)
    txtshikanji.config(state=DISABLED)
    txttea.config(state=DISABLED)
    txtmilk.config(state=DISABLED)
    txtroohafza.config(state=DISABLED)
    txtdrink.config(state=DISABLED)

    txtoreo.config(state=DISABLED)
    txtbanana.config(state=DISABLED)
    txtbrownie.config(state=DISABLED)
    txtchoco.config(state=DISABLED)
    txtforest.config(state=DISABLED)
    txtktkat.config(state=DISABLED)
    txtvanilla.config(state=DISABLED)
    txtpineapple.config(state=DISABLED)
    txtapple.config(state=DISABLED)

    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)
    var17.set(0)
    var18.set(0)
    var19.set(0)
    var20.set(0)
    var21.set(0)
    var22.set(0)
    var23.set(0)
    var24.set(0)
    var25.set(0)
    var26.set(0)
    var27.set(0)
    
    costoffoodvar.set('')
    costofdrinkvar.set('')
    costofcakevar.set('')
    costofttlvar.set('')
    costoftaxvar.set('')
    costofsubttlvar.set('')






















def send():
    def send_bill():
        mssg=txtarea.get(1.0,END)
        nmbr=numberfield.get()

        auth='E7A3fvlkVW3jTQSToSETImR3HOSCVQmxhAsECAI2RDPGRrk03gxkm1DNDRDx'
        url='https://www.fast2sms.com/dev/bulkV2'
        params={
            'authorisation':auth,
            'message':mssg,'numbers':nmbr,
            
            'route':'q',
            'language':'english'
        
        }
        headers={'cache-control':"no-cache"}
        response=requests.request("GET",url,params=params,headers=headers)
        print(response.text)
        dict=response.json()
        res=dict.get('return')
        if res==True:
            messagebox.showinfo('Send Successfully','Message sent succesfully')
        else:
            messagebox.showerror('ERROR','Something Went Wrong')    

                
    root2=Toplevel()

    root2.title('SEND BILL')
    root2.config(bg='red4')
    root2.geometry('480x600+50+50')


    logo=PhotoImage(file='sender.png')
    label=Label(root2,image=logo,bg='red4')
    label.pack()

    numberlbl=Label(root2,text='Mobile Number',font=('arial',18,'bold underline'),bg='red4',fg='white')
    numberlbl.pack()

    numberfield=Entry(root2,font=('helvetica',22,'bold'),bd=3,width=20)
    numberfield.pack()

    billlbl=Label(root2,text='Bill Details',font=('areial',18,'bold underline'),bg='red4',fg='white')
    billlbl.pack()

    txtarea=Text(root2,font=("arial,12,'bold"),bd=3,width=40,height=10)
    txtarea.pack()
    txtarea.insert(END,'Reciept Ref :\t'+billno+'\t\t'+date+'\n\n')
    if costoffoodvar.get()!='Rs 0':
        txtarea.insert(END,f'Cost of Snacks\t\t\tRs {pricesnacks}\n')

    if costofdrinkvar.get()!='Rs 0':
        txtarea.insert(END,f'Cost of Drinks\t\t\tRs {pricedrink}\n')

    
    if costofcakevar.get()!='Rs 0':
        txtarea.insert(END,f'Cost of Cakes\t\t\tRs {pricecakes}\n')

    
    txtarea.insert(END,f'Subtotal\t\t\tRs {subtotal}\n')    
    txtarea.insert(END,f'Service Tax\t\t\tRs {50}\n')    
    txtarea.insert(END,f'Total Cost\t\t\tRs {subtotal+50}\n')    
    

    btnsend=Button(root2,text='SEND',font=('arial',19,'bold'),bg='white',fg='red4',bd=7,relief=GROOVE,command=send_bill)
    btnsend.pack(pady=7)


    root2.mainloop()
def save():
    if textreciept.get(1.0,END)=='\n':
        pass
    else:
        

        url=filedialog.asksaveasfile(mode='w',defaultextension='.txt')
        if url==None:

          bill_data=textreciept.get(1.0,END)
          url.write(bill_data)
          url.close()
          messagebox.showinfo('Information','You Bill is Succesfully Saved')


def reciept():
    global billno,date
    if costofcakevar.get()!='' or costofdrinkvar.get()!='' or costoffoodvar.get()!='':

        textreciept.delete(1.0,END)
        x=random.randint(100,10000)
        billno='BILL '+str(x)
        date=time.strftime('%d/%m/%Y')
        textreciept.insert(END,'Receipt Ref:\t\t'+billno+'\t\t'+date+'\n')
        textreciept.insert(END,'***************************************************************\n')
        textreciept.insert(END,'Items:\t\t Cost of Items(Rs)\n')
        textreciept.insert(END,'***************************************************************\n')
        if e_dosa.get()!='0':
          textreciept.insert(END,f'Dosa\t\t\t{int(e_dosa.get())*60}\n\n')
        if e_fries.get()!='0':
          textreciept.insert(END,f'French Fries\t\t\t{int(e_fries.get())*60}\n\n')  
        if e_bhatura.get()!='0':
          textreciept.insert(END,f'Chole Bhature\t\t\t{int(e_bhatura.get())*40}\n\n')       
        if e_bhaji.get()!='0':
          textreciept.insert(END,f'Pav BHaji\t\t\t{int(e_bhaji.get())*65}\n\n')
        if e_hotdog.get()!='0':
          textreciept.insert(END,f'HotDog\t\t\t{int(e_hotdog.get())*45}\n\n')
        if e_sandwich.get()!='0':
           textreciept.insert(END,f'Sandwich\t\t\t{int(e_sandwich.get())*35}\n\n')
        if e_nuggets.get()!='0':
           textreciept.insert(END,f'Chicken Nuggets\t\t\t{int(e_nuggets.get())*75}\n\n')
        if e_tikka.get()!='0':
           textreciept.insert(END,f'Chicken Tikka\t\t\t{int(e_tikka.get())*120}\n\n')
        if e_rice.get()!='0':
           textreciept.insert(END,f'Egg Fried Rice\t\t\t{int(e_rice.get())*80}\n\n')


        if e_forest.get()!='0':
           textreciept.insert(END,f'Black Forest\t\t\t{int(e_forest.get())*600}\n\n')       
        if e_oreo.get()!='0':
           textreciept.insert(END,f'Oreo Cake\t\t\t{int(e_oreo.get())*300}\n\n')
        if e_apple.get()!='0':
           textreciept.insert(END,f'Apple Cake\t\t\t{int(e_apple.get())*500}\n\n')
        if e_ktkat.get()!='0':
           textreciept.insert(END,f'Kitkat Cake\t\t\t{int(e_ktkat.get())*550}\n\n')
        if e_choco.get()!='0':
           textreciept.insert(END,f'Chocolate Cake\t\t\t{int(e_choco.get())*450}\n\n')
        if e_vanilla.get()!='0':
           textreciept.insert(END,f'Vanilla Cake\t\t\t{int(e_vanilla.get())*800}\n\n')
        if e_banana.get()!='0':
           textreciept.insert(END,f'Banana Cake\t\t\t{int(e_banana.get())*620}\n\n')  
        if e_brownie.get()!='0':
           textreciept.insert(END,f'Brownie\t\t\t{int(e_brownie.get())*700}\n\n')       
        if e_pineapple.get()!='0':
           textreciept.insert(END,f'Pine apple Cake\t\t\t{int(e_pineapple.get())*550}\n\n')


        if e_laasi.get()!='0':
          textreciept.insert(END,f'Laasi\t\t\t{int(e_laasi.get())*45}\n\n')
        if e_coffee.get()!='0':
          textreciept.insert(END,f'Coffee\t\t\t{int(e_coffee.get())*40}\n\n')
        if e_faluda.get()!='0':
          textreciept.insert(END,f'Faluda\t\t\t{int(e_faluda.get())*60}\n\n')
        if e_shikanji.get()!='0':
          textreciept.insert(END,f'Shikanji\t\t\t{int(e_shikanji.get())*30}\n\n')
        if e_jaljeera.get()!='0':
          textreciept.insert(END,f'Jaljeera\t\t\t{int(e_jaljeera.get())*30}\n\n')
        if e_roohafza.get()!='0':
          textreciept.insert(END,f'Roohafza\t\t\t{int(e_roohafza.get())*40}\n\n')
        if e_tea.get()!='0':
          textreciept.insert(END,f'Masala Tea\t\t\t{int(e_tea.get())*25}\n\n')
        if e_milk.get()!='0':
          textreciept.insert(END,f'Badam Milk\t\t\t{int(e_milk.get())*50}\n\n')  
        if e_drink.get()!='0':
          textreciept.insert(END,f'Cold Drink\t\t\t{int(e_drink.get())*80}\n\n') 

        textreciept.insert(END,'*************************************************************\n')     


        if costoffoodvar.get()!='Rs 0':
          textreciept.insert(END,f'Cost of Snacks\t\t\tRs {pricesnacks}\n\n')

        if costofdrinkvar.get()!='Rs 0':
          textreciept.insert(END,f'Cost of Drinks\t\t\tRs {pricedrink}\n\n')

    
        if costofcakevar.get()!='Rs 0':
          textreciept.insert(END,f'Cost of Cakes\t\t\tRs {pricecakes}\n\n')

    
        textreciept.insert(END,f'Subtotal\t\t\tRs {subtotal}\n\n')    
        textreciept.insert(END,f'Service Tax\t\t\tRs {50}\n\n')    
        textreciept.insert(END,f'Total Cost\t\t\tRs {subtotal+50}\n\n')    
        textreciept.insert(END,'********************THANK YOU****************************\n')

    










def total():
    global pricecakes,pricedrink,pricesnacks,subtotal
    if var1.get()!=0 or var2.get()!=0 or var3.get()!=0 or var4.get()!=0 or var5.get()!=0 or var6.get()!=0 or var7.get()!=0 or var8.get()!=0 or var9.get()!=0 or \
         var10.get()!=0 or var11.get()!=0 or var12.get()!=0 or var13.get()!=0 or var14.get()!=0 or var15.get()!=0 or var16.get()!=0 or var17.get()!=0 or var18.get()!=0 or \
         var19.get()!=0 or var20.get()!=0 or var21.get()!=0 or var22.get()!=0 or var23.get()!=0 or var24.get()!=0 or var25.get()!=0 or var26.get()!=0 or var27.get()!=0 :
         item1=int(e_dosa.get())
         item2=int(e_fries.get())
         item3=int(e_bhatura.get())
         item4=int(e_bhaji.get())
         item5=int(e_hotdog.get())
         item6=int(e_sandwich.get())
         item7=int(e_nuggets.get())
         item8=int(e_tikka.get())
         item9=int(e_rice.get())

         item10=int(e_laasi.get())
         item11=int(e_coffee.get())
         item12=int(e_faluda.get())
         item13=int(e_shikanji.get())
         item14=int(e_jaljeera.get())
         item15=int(e_roohafza.get())
         item16=int(e_tea.get())
         item17=int(e_milk.get())
         item18=int(e_drink.get())

         item19=int(e_forest.get())
         item20=int(e_oreo.get())
         item21=int(e_apple.get())
         item22=int(e_ktkat.get())
         item23=int(e_choco.get())
         item24=int(e_vanilla.get())
         item25=int(e_banana.get())
         item26=int(e_brownie.get())
         item27=int(e_pineapple.get())

         pricesnacks=item1*60+item2*60+item3*40+item4*65+item5*45+item6*35+item7*75+item8*120+item9*80
         pricedrink=item10*45+item11*40+item12*60+item13*30+item14*30+item15*40+item16*25+item17*50+item18*80
         pricecakes=item19*600+item20*300+item21*500+item22*550+item23*450+item24*800+item25*620+item26*700+item27*550

         costoffoodvar.set('Rs'+str(pricesnacks))
         costofdrinkvar.set('Rs'+str(pricedrink))
         costofcakevar.set('Rs'+str(pricecakes))
         subtotal=pricesnacks+pricedrink+pricecakes
         costofsubttlvar.set('Rs'+str(subtotal))

         costoftaxvar.set('Rs 50')

         ttlcost=subtotal+50
         costofttlvar.set('Rs'+str(ttlcost))

    else:
        messagebox.showerror('Error',"NO Item Selected")


    
def dosa():
    if var1.get()==1:
        txtdosa.config(state=NORMAL)
        txtdosa.delete(0,END)
        txtdosa.focus()
    else:
        txtdosa.config(state=DISABLED)
        e_dosa.set('0') 

def bhatura():
    if var3.get()==1:
        txtbhatura.config(state=NORMAL)
        txtbhatura.delete(0,END)
        txtbhatura.focus()
    else:
        txtbhatura.config(state=DISABLED)
        e_bhatura.set('0')     

def french():
    if var2.get()==1:
        txtfries.config(state=NORMAL)
        txtfries.delete(0,END)
        txtfries.focus()
    else:
        txtfries.config(state=DISABLED)
        e_fries.set('0')     

def bhaji():
    if var4.get()==1:
        txtbhaji.config(state=NORMAL)
        txtbhaji.delete(0,END)
        txtbhaji.focus()
    else:
        txtbhaji.config(state=DISABLED)
        e_bhaji.set('0')     

def hotdog():
    if var5.get()==1:
        txthotdog.config(state=NORMAL)
        txthotdog.delete(0,END)
        txthotdog.focus()
    else:
        txthotdog.config(state=DISABLED)
        e_hotdog.set('0')     

def sandwich():
    if var6.get()==1:
        txtsandwich.config(state=NORMAL)
        txtsandwich.delete(0,END)
        txtsandwich.focus()
    else:
        txtsandwich.config(state=DISABLED)
        e_sandwich.set('0')     

def nuggets():
    if var7.get()==1:
        txtnuggets.config(state=NORMAL)
        txtnuggets.delete(0,END)
        txtnuggets.focus()
    else:
        txtnuggets.config(state=DISABLED)
        e_nuggets.set('0')     

def tikka():
    if var8.get()==1:
        txttikka.config(state=NORMAL)
        txttikka.delete(0,END)
        txttikka.focus()
    else:
        txttikka.config(state=DISABLED)
        e_tikka.set('0')     

def rice():
    if var9.get()==1:
        txtrice.config(state=NORMAL)
        txtrice.delete(0,END)
        txtrice.focus()
    else:
        txtrice.config(state=DISABLED)
        e_rice.set('0')     



def laasi():
    if var10.get()==1:
        txtlaasi.config(state=NORMAL)
        txtlaasi.delete(0,END)
        txtlaasi.focus()
    else:
        txtlaasi.config(state=DISABLED)
        e_laasi.set('0') 

def coffee():
    if var11.get()==1:
        txtcoffee.config(state=NORMAL)
        txtcoffee.delete(0,END)
        txtcoffee.focus()
    else:
        txtcoffee.config(state=DISABLED)
        e_coffee.set('0')     


def roohafza():
    if var12.get()==1:
        txtroohafza.config(state=NORMAL)
        txtroohafza.delete(0,END)
        txtroohafza.focus()
    else:
        txtroohafza.config(state=DISABLED)
        e_roohafza.set('0')             

def faluda():
    if var13.get()==1:
        txtfaluda.config(state=NORMAL)
        txtfaluda.delete(0,END)
        txtfaluda.focus()
    else:
        txtfaluda.config(state=DISABLED)
        e_faluda.set('0')     


def jaljeera():
    if var14.get()==1:
        txtjaljeera.config(state=NORMAL)
        txtjaljeera.delete(0,END)
        txtjaljeera.focus()
    else:
        txtjaljeera.config(state=DISABLED)
        e_jaljeera.set('0')   

def badam():
    if var15.get()==1:
        txtmilk.config(state=NORMAL)
        txtmilk.delete(0,END)
        txtmilk.focus()
    else:
        txtmilk.config(state=DISABLED)
        e_milk.set('0')     

def tea():
    if var16.get()==1:
        txttea.config(state=NORMAL)
        txttea.delete(0,END)
        txttea.focus()
    else:
        txttea.config(state=DISABLED)
        e_tea.set('0')     



def sikanji():
    if var17.get()==1:
        txtshikanji.config(state=NORMAL)
        txtshikanji.delete(0,END)
        txtshikanji.focus()
    else:
        txtshikanji.config(state=DISABLED)
        e_shikanji.set('0')     
  
def drink():
    if var18.get()==1:
        txtdrink.config(state=NORMAL)
        txtdrink.delete(0,END)
        txtdrink.focus()
    else:
        txtdrink.config(state=DISABLED)
        e_drink.set('0')    


def forest():
    if var19.get()==1:
        txtforest.config(state=NORMAL)
        txtforest.delete(0,END)
        txtforest.focus()
    else:
        txtforest.config(state=DISABLED)
        e_forest.set('0') 

def oreo():
    if var20.get()==1:
        txtoreo.config(state=NORMAL)
        txtoreo.delete(0,END)
        txtoreo.focus()
    else:
        txtoreo.config(state=DISABLED)
        e_oreo.set('0')     

def apple():
    if var21.get()==1:
        txtapple.config(state=NORMAL)
        txtapple.delete(0,END)
        txtapple.focus()
    else:
        txtapple.config(state=DISABLED)
        e_apple.set('0')     

def kitkat():
    if var22.get()==1:
        txtktkat.config(state=NORMAL)
        txtktkat.delete(0,END)
        txtktkat.focus()
    else:
        txtktkat.config(state=DISABLED)
        e_ktkat.set('0')     

def choco():
    if var23.get()==1:
        txtchoco.config(state=NORMAL)
        txtchoco.delete(0,END)
        txtchoco.focus()
    else:
        txtchoco.config(state=DISABLED)
        e_choco.set('0')     

def vanilla():
    if var24.get()==1:
        txtvanilla.config(state=NORMAL)
        txtvanilla.delete(0,END)
        txtvanilla.focus()
    else:
        txtvanilla.config(state=DISABLED)
        e_vanilla.set('0')     

def banana():
    if var25.get()==1:
        txtbanana.config(state=NORMAL)
        txtbanana.delete(0,END)
        txtbanana.focus()
    else:
        txtbanana.config(state=DISABLED)
        e_banana.set('0')     

def brownie():
    if var26.get()==1:
        txtbrownie.config(state=NORMAL)
        txtbrownie.delete(0,END)
        txtbrownie.focus()
    else:
        txtbrownie.config(state=DISABLED)
        e_brownie.set('0')     

def pineapple():
    if var27.get()==1:
        txtpineapple.config(state=NORMAL)
        txtpineapple.delete(0,END)
        txtpineapple.focus()
    else:
        txtpineapple.config(state=DISABLED)
        e_pineapple.set('0')     









root=Tk()
root.geometry('1370x670+0+0')
root.resizable(0,0)
root.title('laure restaurent')
root.config(bg='skyblue')

topframe=Frame(root,bd=10,relief=RIDGE,bg='#4A7A8C')
topframe.pack(side=TOP)
img1=Image.open("images.jpg")
img1=img1.resize((300,57),Image.ANTIALIAS)
photoimg1=ImageTk.PhotoImage(img1)
labeltitle=Label(topframe,bg='skyblue',text='  Restaurent Billing System',font=('areial',30,'bold'),image=photoimg1,width=900,compound='left')
labeltitle.grid(row=0,column=0)



#frames
menuframe=Frame(root,bd=10,relief=RIDGE,bg='skyblue')
menuframe.pack(side=LEFT)
costframe=Frame(menuframe,bd=4,relief=RIDGE,bg='skyblue',pady=10)
costframe.pack(side=BOTTOM)
foodframe=LabelFrame(menuframe,text='Snacks',bd=10,relief=RIDGE,font=('areial',19,'bold'),fg='#4A7A8C')
foodframe.pack(side=LEFT)
drinkframe=LabelFrame(menuframe,text='Drinks',bd=10,relief=RIDGE,font=('areial',19,'bold'),fg='#4A7A8C')
drinkframe.pack(side=LEFT)
cakeframe=LabelFrame(menuframe,bd=10,text='Cakes',font=('areial',19,'bold'),relief=RIDGE,fg='#4A7A8C')
cakeframe.pack(side=LEFT)

rightframe=Frame(root,bd=10,relief=RIDGE,bg='skyblue')
rightframe.pack(side=RIGHT)
calcframe=Frame(rightframe,bd=1,relief=RIDGE)
calcframe.pack()
recieptframe=Frame(rightframe,bd=4,relief=RIDGE)
recieptframe.pack()
btnframe=Frame(rightframe,bd=3,relief=RIDGE)
btnframe.pack()

#variables
var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
var7=IntVar()
var8=IntVar()
var9=IntVar()
var10=IntVar()
var11=IntVar()
var12=IntVar()
var13=IntVar()
var14=IntVar()
var15=IntVar()
var16=IntVar()
var17=IntVar()
var18=IntVar()
var19=IntVar()
var20=IntVar()
var21=IntVar()
var22=IntVar()
var23=IntVar()
var24=IntVar()
var25=IntVar()
var26=IntVar()
var27=IntVar()

e_dosa=StringVar()
e_fries=StringVar()
e_bhatura=StringVar()
e_bhaji=StringVar()
e_hotdog=StringVar()
e_sandwich=StringVar()
e_nuggets=StringVar()
e_tikka=StringVar()
e_rice=StringVar()
e_laasi=StringVar()
e_coffee=StringVar()
e_faluda=StringVar()
e_shikanji=StringVar()
e_jaljeera=StringVar()
e_roohafza=StringVar()
e_tea=StringVar()
e_milk=StringVar()
e_drink=StringVar()
e_oreo=StringVar()
e_apple=StringVar()
e_ktkat=StringVar()
e_vanilla=StringVar()
e_banana=StringVar()
e_brownie=StringVar()
e_pineapple=StringVar()
e_choco=StringVar()
e_forest=StringVar()


costoffoodvar=StringVar()
costofdrinkvar=StringVar()
costofcakevar=StringVar()
costofsubttlvar=StringVar()
costoftaxvar=StringVar()
costofttlvar=StringVar()



e_dosa.set('0')
e_bhatura.set('0')
e_fries.set('0')
e_bhaji.set('0')
e_hotdog.set('0')
e_rice.set('0')
e_sandwich.set('0')
e_nuggets.set('0')
e_tikka.set('0')
e_laasi.set('0')
e_coffee.set('0')
e_faluda.set('0')
e_shikanji.set('0')
e_jaljeera.set('0')
e_roohafza.set('0')
e_tea.set('0')
e_milk.set('0')
e_drink.set('0')
e_oreo.set('0')
e_apple.set('0')
e_ktkat.set('0')
e_vanilla.set('0')
e_banana.set('0')
e_brownie.set('0')
e_pineapple.set('0')
e_choco.set('0')
e_forest.set('0')

#food items
Dosa=Checkbutton(foodframe,text='Masala Dosa',font=('areial',18,'bold'),onvalue=1,offvalue=0,variable=var1,command=dosa)
Dosa.grid(row=0,column=0,sticky=W)

frenchfries=Checkbutton(foodframe,text='French Fries',font=('areial',18,'bold'),onvalue=1,offvalue=0,variable=var2,command=french)
frenchfries.grid(row=1,column=0,sticky=W)

batura=Checkbutton(foodframe,text='Chole Bhature',font=('areial',18,'bold'),onvalue=1,offvalue=0,variable=var3,command=bhatura)
batura.grid(row=2,column=0,sticky=W)

bhaji=Checkbutton(foodframe,text='Pav Bhaji',font=('areial',18,'bold'),onvalue=1,offvalue=0,variable=var4,command=bhaji)
bhaji.grid(row=3,column=0,sticky=W)

hotdog=Checkbutton(foodframe,text='Hot Dog',font=('areial',18,'bold'),onvalue=1,offvalue=0,variable=var5,command=hotdog)
hotdog.grid(row=4,column=0,sticky=W)

sandwich=Checkbutton(foodframe,text='Cheese Sandwich',font=('areial',18,'bold'),onvalue=1,offvalue=0,variable=var6,command=sandwich)
sandwich.grid(row=5,column=0,sticky=W)

nuggets=Checkbutton(foodframe,text='Chicken Nuggets',font=('areial',18,'bold'),onvalue=1,offvalue=0,variable=var7,command=nuggets)
nuggets.grid(row=6,column=0,sticky=W)

tikka=Checkbutton(foodframe,text='Chicken Tikka',font=('areial',18,'bold'),onvalue=1,offvalue=0,variable=var8,command=tikka)
tikka.grid(row=7,column=0,sticky=W)

rice=Checkbutton(foodframe,text='Egg Fried Rice',font=('areial',18,'bold'),onvalue=1,offvalue=0,variable=var9,command=rice)
rice.grid(row=8,column=0,sticky=W)

#entry field for food item
txtdosa=Entry(foodframe,font=('areial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_dosa)
txtdosa.grid(row=0,column=1)

txtfries=Entry(foodframe,font=('areial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_fries)
txtfries.grid(row=1,column=1)

txtbhatura=Entry(foodframe,font=('areial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_bhatura)
txtbhatura.grid(row=2,column=1)

txtbhaji=Entry(foodframe,font=('areial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_bhaji)
txtbhaji.grid(row=3,column=1)

txthotdog=Entry(foodframe,font=('areial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_hotdog)
txthotdog.grid(row=4,column=1)

txtsandwich=Entry(foodframe,font=('areial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_sandwich)
txtsandwich.grid(row=5,column=1)

txtnuggets=Entry(foodframe,font=('areial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_nuggets)
txtnuggets.grid(row=6,column=1)

txttikka=Entry(foodframe,font=('areial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_tikka)
txttikka.grid(row=7,column=1)

txtrice=Entry(foodframe,font=('areial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_rice)
txtrice.grid(row=8,column=1)


#drinks

laasi=Checkbutton(drinkframe,text='Laasi',font=('areial',18,'bold'),onvalue=1,offvalue=0,variable=var10,command=laasi)
laasi.grid(row=0,column=0,sticky=W)

coffee=Checkbutton(drinkframe,text='Cold Coffee',font=('areial',18,'bold'),onvalue=1,offvalue=0,variable=var11,command=coffee)
coffee.grid(row=1,column=0,sticky=W)

roohafza=Checkbutton(drinkframe,text='Roohafza',font=('areial',18,'bold'),onvalue=1,offvalue=0,variable=var12,command=roohafza)
roohafza.grid(row=5,column=0,sticky=W)

faluda=Checkbutton(drinkframe,text='Faluda',font=('areial',18,'bold'),onvalue=1,offvalue=0,variable=var13,command=faluda)
faluda.grid(row=2,column=0,sticky=W)

jaljeera=Checkbutton(drinkframe,text='Jal-Jeera',font=('areial',18,'bold'),onvalue=1,offvalue=0,variable=var14,command=jaljeera)
jaljeera.grid(row=4,column=0,sticky=W)

badam=Checkbutton(drinkframe,text='Badam Milk',font=('areial',18,'bold'),onvalue=1,offvalue=0,variable=var15,command=badam)
badam.grid(row=7,column=0,sticky=W)

masala=Checkbutton(drinkframe,text='Masala Tea',font=('areial',18,'bold'),onvalue=1,offvalue=0,variable=var16,command=tea)
masala.grid(row=6,column=0,sticky=W)

shikanji=Checkbutton(drinkframe,text='Shikanji',font=('areial',18,'bold'),onvalue=1,offvalue=0,variable=var17,command=sikanji)
shikanji.grid(row=3,column=0,sticky=W)

colddrinks=Checkbutton(drinkframe,text='Cold Drinks',font=('areial',18,'bold'),onvalue=1,offvalue=0,variable=var18,command=drink)
colddrinks.grid(row=8,column=0,sticky=W)

#entry fields for drink

txtlaasi=Entry(drinkframe,font=('areial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_laasi)
txtlaasi.grid(row=0,column=1)

txtcoffee=Entry(drinkframe,font=('areial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_coffee)
txtcoffee.grid(row=1,column=1)

txtfaluda=Entry(drinkframe,font=('areial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_faluda)
txtfaluda.grid(row=2,column=1)

txtshikanji=Entry(drinkframe,font=('areial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_shikanji)
txtshikanji.grid(row=3,column=1)

txtjaljeera=Entry(drinkframe,font=('areial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_jaljeera)
txtjaljeera.grid(row=4,column=1)

txtroohafza=Entry(drinkframe,font=('areial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_roohafza)
txtroohafza.grid(row=5,column=1)

txttea=Entry(drinkframe,font=('areial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_tea)
txttea.grid(row=6,column=1)

txtmilk=Entry(drinkframe,font=('areial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_milk)
txtmilk.grid(row=7,column=1)

txtdrink=Entry(drinkframe,font=('areial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_drink)
txtdrink.grid(row=8,column=1)

#cakes

blackforest=Checkbutton(cakeframe,text='Black Forest',font=('areial',18,'bold'),onvalue=1,offvalue=0,variable=var19,command=forest)
blackforest.grid(row=0,column=0,sticky=W)
oreocake=Checkbutton(cakeframe,text='Oreo',font=('areial',18,'bold'),onvalue=1,offvalue=0,variable=var20,command=oreo)
oreocake.grid(row=1,column=0,sticky=W)
applecake=Checkbutton(cakeframe,text='Apple',font=('areial',18,'bold'),onvalue=1,offvalue=0,variable=var21,command=apple)
applecake.grid(row=2,column=0,sticky=W)
ktkat=Checkbutton(cakeframe,text='Kitkat',font=('areial',18,'bold'),onvalue=1,offvalue=0,variable=var22,command=kitkat)
ktkat.grid(row=3,column=0,sticky=W)
chocl=Checkbutton(cakeframe,text='chocolate',font=('areial',18,'bold'),onvalue=1,offvalue=0,variable=var23,command=choco)
chocl.grid(row=4,column=0,sticky=W)
vanlla=Checkbutton(cakeframe,text='Vanilla',font=('areial',18,'bold'),onvalue=1,offvalue=0,variable=var24,command=vanilla)
vanlla.grid(row=5,column=0,sticky=W)
banana=Checkbutton(cakeframe,text='Banana',font=('areial',18,'bold'),onvalue=1,offvalue=0,variable=var25,command=banana)
banana.grid(row=6,column=0,sticky=W)
brownie=Checkbutton(cakeframe,text='Brownie',font=('areial',18,'bold'),onvalue=1,offvalue=0,variable=var26,command=brownie)
brownie.grid(row=7,column=0,sticky=W)
pappl=Checkbutton(cakeframe,text='Pineapple',font=('areial',18,'bold'),onvalue=1,offvalue=0,variable=var27,command=pineapple)
pappl.grid(row=8,column=0,sticky=W)


# entry field for cakes
txtoreo=Entry(cakeframe,font=('areial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_oreo)
txtoreo.grid(row=1,column=1)

txtapple=Entry(cakeframe,font=('areial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_apple)
txtapple.grid(row=2,column=1)

txtktkat=Entry(cakeframe,font=('areial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_ktkat)
txtktkat.grid(row=3,column=1)

txtvanilla=Entry(cakeframe,font=('areial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_vanilla)
txtvanilla.grid(row=5,column=1)

txtbanana=Entry(cakeframe,font=('areial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_banana)
txtbanana.grid(row=6,column=1)

txtbrownie=Entry(cakeframe,font=('areial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_brownie)
txtbrownie.grid(row=7,column=1)

txtpineapple=Entry(cakeframe,font=('areial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_pineapple)
txtpineapple.grid(row=8,column=1)

txtchoco=Entry(cakeframe,font=('areial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_choco)
txtchoco.grid(row=4,column=1)

txtforest=Entry(cakeframe,font=('areial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_forest)
txtforest.grid(row=0,column=1)


#cost frame

lblcostfood=Label(costframe,text='Cost Of Foods',font=('arial',16,'bold'),fg='white',bg='#4A7A8C')
lblcostfood.grid(row=0,column=0)

txtcostfood=Entry(costframe,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=costoffoodvar)
txtcostfood.grid(row=0,column=1,padx=49)

lblcostdrink=Label(costframe,text='Cost Of Drinks',font=('arial',16,'bold'),fg='white',bg='#4A7A8C')
lblcostdrink.grid(row=1,column=0)

txtcostdrink=Entry(costframe,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=costofdrinkvar)
txtcostdrink.grid(row=1,column=1,padx=49)

lblcostcake=Label(costframe,text='Cost Of Cakes',font=('arial',16,'bold'),fg='white',bg='#4A7A8C')
lblcostcake.grid(row=2,column=0)

txtcostcake=Entry(costframe,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=costofcakevar)
txtcostcake.grid(row=2,column=1,padx=49)

lblsubttl=Label(costframe,text='Sub-Total',font=('arial',16,'bold'),fg='white',bg='#4A7A8C')
lblsubttl.grid(row=0,column=2)

txtsubttl=Entry(costframe,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=costofsubttlvar)
txtsubttl.grid(row=0,column=3,padx=49)

lbltax=Label(costframe,text='Service tax',font=('arial',16,'bold'),fg='white',bg='#4A7A8C')
lbltax.grid(row=1,column=2)

txtsubttl=Entry(costframe,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=costoftaxvar)
txtsubttl.grid(row=1,column=3,padx=49)

lblttl=Label(costframe,text='Total Cost',font=('arial',16,'bold'),fg='white',bg='#4A7A8C')
lblttl.grid(row=2,column=2)

txtttl=Entry(costframe,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=costofttlvar)
txtttl.grid(row=2,column=3,padx=49)

#BUTTONS
buttonTotal=Button(btnframe,text='Total',font=('arial',14,'bold'),fg='white',bg='#4A7A8C',bd=3,padx=5,command=total)
buttonTotal.grid(row=0,column=0)

buttonreciept=Button(btnframe,text='Reciept',font=('arial',14,'bold'),fg='white',bg='#4A7A8C',bd=3,padx=5,command=reciept)
buttonreciept.grid(row=0,column=1)

buttonSave=Button(btnframe,text='Save',font=('arial',14,'bold'),fg='white',bg='#4A7A8C',bd=3,padx=5,command=save)
buttonSave.grid(row=0,column=2)

#buttonsend=Button(btnframe,text='Send',font=('arial',14,'bold'),fg='white',bg='red4',bd=3,padx=5,command=send)
#buttonsend.grid(row=0,column=3)

buttonreset=Button(btnframe,text='Reset',font=('arial',14,'bold'),fg='white',bg='#4A7A8C',bd=3,padx=5,command=reset)
buttonreset.grid(row=0,column=4)

#textarea for receipt
textreciept=Text(recieptframe,font=('arial',12,'bold'),bd=3,width=42,height=14)
textreciept.grid(row=0,column=0)

#calculator
operator=''
def btnclick(num):
    global operator
    calcifield.delete(0,END)
   
    operator=operator+num
    calcifield.insert(END,operator)

def clear():
    global operator
    operator=''
    calcifield.delete(0,END)

def answer():
    global operator
    result=str(eval(operator))
    calcifield.delete(0,END)
    calcifield.insert(0,result)
    operator=''




calcifield=Entry(calcframe,font=('arial',16,'bold'),bd=4,width=32)
calcifield.grid(row=0,column=0,columnspan=4)

btn7=Button(calcframe,text='7',font=('arial',16,'bold'),fg='yellow',bg='#4A7A8C',bd=6,width=6,command=lambda:btnclick('7'))
btn7.grid(row=1,column=0)

btn8=Button(calcframe,text='8',font=('arial',16,'bold'),fg='yellow',bg='#4A7A8C',bd=6,width=6,command=lambda:btnclick('8'))
btn8.grid(row=1,column=1)

btn9=Button(calcframe,text='9',font=('arial',16,'bold'),fg='yellow',bg='#4A7A8C',bd=6,width=6,command=lambda:btnclick('9'))
btn9.grid(row=1,column=2)

btnplus=Button(calcframe,text='+',font=('arial',16,'bold'),fg='yellow',bg='#4A7A8C',bd=6,width=6,command=lambda:btnclick('+'))
btnplus.grid(row=1,column=3)

btn4=Button(calcframe,text='4',font=('arial',16,'bold'),fg='yellow',bg='#4A7A8C',bd=6,width=6,command=lambda:btnclick('4'))
btn4.grid(row=2,column=0)

btn5=Button(calcframe,text='5',font=('arial',16,'bold'),fg='yellow',bg='#4A7A8C',bd=6,width=6,command=lambda:btnclick('5'))
btn5.grid(row=2,column=1)

btn6=Button(calcframe,text='6',font=('arial',16,'bold'),fg='yellow',bg='#4A7A8C',bd=6,width=6,command=lambda:btnclick('6'))
btn6.grid(row=2,column=2)

btnminus=Button(calcframe,text='-',font=('arial',16,'bold'),fg='yellow',bg='#4A7A8C',bd=6,width=6,command=lambda:btnclick('-'))
btnminus.grid(row=2,column=3)

btn1=Button(calcframe,text='1',font=('arial',16,'bold'),fg='yellow',bg='#4A7A8C',bd=6,width=6,command=lambda:btnclick('1'))
btn1.grid(row=3,column=0)

btn2=Button(calcframe,text='2',font=('arial',16,'bold'),fg='yellow',bg='#4A7A8C',bd=6,width=6,command=lambda:btnclick('2'))
btn2.grid(row=3,column=1)

btn3=Button(calcframe,text='3',font=('arial',16,'bold'),fg='yellow',bg='#4A7A8C',bd=6,width=6,command=lambda:btnclick('3'))
btn3.grid(row=3,column=2)

btnmult=Button(calcframe,text='*',font=('arial',16,'bold'),fg='yellow',bg='#4A7A8C',bd=6,width=6,command=lambda:btnclick('*'))
btnmult.grid(row=3,column=3)

btnans=Button(calcframe,text='Ans',font=('arial',16,'bold'),fg='yellow',bg='#4A7A8C',bd=6,width=6,command=lambda:answer())
btnans.grid(row=4,column=0)

btnclear=Button(calcframe,text='Clear',font=('arial',16,'bold'),fg='yellow',bg='#4A7A8C',bd=6,width=6,command=lambda:clear())
btnclear.grid(row=4,column=1)

btn0=Button(calcframe,text='0',font=('arial',16,'bold'),fg='yellow',bg='#4A7A8C',bd=6,width=6,command=lambda:btnclick('0'))
btn0.grid(row=4,column=2)

btnminus=Button(calcframe,text='/',font=('arial',16,'bold'),fg='yellow',bg='#4A7A8C',bd=6,width=6,command=lambda:btnclick('/'))
btnminus.grid(row=4,column=3)



root.mainloop()