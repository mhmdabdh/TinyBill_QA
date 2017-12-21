from Tkinter import *
from Tkinter import Frame, Entry, Tk
import time
import datetime as dt
import ttk
from datetime import datetime
import unicodedata as u
import sqlite3
from sqlite3 import Error







#Function START
#This is the function to create a new stock item
def fn_CreateItem():
    window3 =Toplevel()
    window3.title( "Create New Stock Item")

    print "Create NEw"

    #Throw in the widgets
    lblCreateItem = Label(window3, text="SICO Create A New Item")
    lblStockItemName = Label(window3, text="Stock Item Name :")
    lblTaxExclAmount = Label(window3, text="Tax Exclusive Amount :")
    lblCgstRate= Label(window3, text="CGST Rate% :")
    lblSgstRate= Label(window3, text="SGST Rate% :")
    lblSku= Label(window3, text="SKU (If Known) :")
    txtStockItemName = Entry(window3, textvariable=vStockItemName)
    txtTaxExclAmount= Entry(window3, textvariable=vTaxExclAmt)
    txtCgstRate = Entry(window3, textvariable=vCGST)
    txtSgstRate = Entry(window3, textvariable=vSGST)
    txtSku = Entry(window3, textvariable=vSKU)
    btnSubmitCreateItem = Button(window3, text = "Submit" ,border=1, command=fn_SubmitCreateItem)


    #Bind the widgets to the grid
    lblCreateItem.grid(row=0, column=1)
    lblStockItemName.grid(row=2, column =0)
    lblTaxExclAmount.grid(row=3, column=0)
    lblCgstRate.grid(row=4, column=0)
    lblSgstRate.grid(row=5, column=0)
    lblSku.grid(row=6, column=0)
    txtStockItemName.grid(row=2, column =1)
    txtTaxExclAmount.grid(row=3, column=1)
    txtCgstRate.grid(row=4, column =1)
    txtSgstRate.grid(row=5, column =1)
    txtSku.grid(row=6, column =1)
    btnSubmitCreateItem.grid(row=8, column = 1, rowspan=2, sticky=W)
#Function END


#Function START
#This is the function for submit button to insert values into tr_inventory
def fn_SubmitCreateItem():
        print 'You clicked the button!'
        #print a.get()
        #variable = a.get()
        #print variable
        col1=vStockItemName.get()
        col2=vTaxExclAmt.get()
        col3=vCGST.get()
        col4=vSGST.get()
        col5=vSKU.get()
        #Capture the values from the textboxes to variables
        #Connect to the database and insert the values into the inventory table
        connection = sqlite3.connect('sicotrichy_qa')
        cur=connection.cursor()
        #cur.execute("select *  from tr_inventory where  stock_item_name = 'Melamine Ashtray'")
        #ohho = cur.fetchall()
        #print ohho
        #cur.execute('insert into tr_inventory (stock_item_name, tax_exclusive_amount, cgst_rate, sgst_rate, stock_keeping_unit) VALUES (?,?,?,?,?)', ('hel22lo', 123, 4 , 4 , 'Dunno'))
        #inserting Dynamic values
        cur.execute(
            'insert into tr_inventory (stock_item_name, tax_exclusive_amount, cgst_rate, sgst_rate, stock_keeping_unit) VALUES (?,?,?,?,?)',
            (col1, col2, col3, col4, col5))
        connection.commit()

#Function END












# The main function starts here starts here

root = Tk()
root.wm_attributes('-fullscreen', True)
#root.state('zoomed')
root.title ( "TinyBill SICO Trichy")



#Variables Declaration
#vTime1 is used in the function to compute dynamic time
vTime1 = ''

#vDate is used to display todays date
vDate=dt.datetime.today().strftime("%d-%b-%Y")
# The company logo image #The company logo image
vCompanyLogo=PhotoImage(file="G:\Programming\AbiePyCharmWork\SICO_Logo.gif")
#The company alphabets in Tamil
vaCompanyLetters = [ u'\u0b87' , u'\u0baa' ,u'\u0bcd'  ,u'\u0bb0' ,u'\u0bbe', u'\u0bb9' ,u'\u0bbf', u'\u0bae' ,u'\u0bcd' ]
#Concatenate the tamil letters into one word
vtCompanyName= u''.join(vaCompanyLetters)

#Variables from the window CREATE NEW ITEM
vStockItemName = StringVar()
vTaxExclAmt = StringVar()
vCGST = StringVar()
vSGST = StringVar()
vSKU = StringVar()

#CREATING/CONFIGURING THE WIDGETS
#Throw in  labels
lblDate_1 = Label(root,  font=(None, 20), text="Date:")
lblDate_2 = Label(root, font=(None, 20),text=vDate)
#lblShopName = Label(root, text="S. Ibrahim & Co., \n Trichy" + alist)
lblShopNameTam = Label(root, font=(None, 50), text="S. " + vtCompanyName + " & Co")
lblShopNameEng = Label(root, font=(None, 25), text="S. Ibrahim & Co., \n  23, Palakarai Maizham \n Trichy - 620008")
lblClock = Label(root,font=(None, 20))
lblCompanyLogo = Label(root, image=vCompanyLogo)
lblThankyou = Label(root,text="Thank you come again!")
lblShoestring1 = Label(root , text="shoestringapp@gmail.com")
lblShoestring1.config(fg="blue")



#throw in textboxes

#Throw in buttons
btnNewBill = Button(root, text="Create New Bill", border=1)
btnExistBill = Button(root, text = "View Existing Bill", border=1)
btnCreateItem = Button(root, text = "Create New Item",border=1 ,command= fn_CreateItem)
btnEditItem = Button(root,text="Edit Existing Item",border=1)
btnCloseWindow = Button(root, text="Exit", border=1, command=root.destroy)

#Throw in the labels, textboxes, needed in the billing form
lblBillNo= Label(root,text="Bill No")
lblBillNoValue= Label(root,text="Fetch from DB")
lblSno= Label(root,text="S.No.")
lblItemName= Label(root,text="Item Name and Description")
lblQty= Label(root,text="Qty")
lblRate= Label(root,text="Rate", width=3)
lblCGST= Label(root,text="CGST%")
lblSGST= Label(root,text="SGST%")
lblBasicAmount= Label(root,text="Basic Amount")

#Billing form entry box creation ROW1
txtBillRow1_1 = Entry(root, width=5)
txtBillRow1_1.insert(0,"   1.")
txtBillRow1_1.config(state='readonly')
txtBillRow1_2= Entry(root, width=50)
txtBillRow1_3= Entry(root, width=5)
txtBillRow1_4= Entry(root, width=5)
txtBillRow1_5= Entry(root, width=5)
txtBillRow1_6= Entry(root, width=5)
txtBillRow1_7= Entry(root)
txtBillRow1_8= Entry(root)

#PENDING ACTION Create  entry box on row 2-9 in this gap

#Billing form entry box creation Row10
txtBillRow10_1  = Entry(root, width=5)
txtBillRow10_1.insert(0,"   10.")
txtBillRow10_1.config(state='readonly')
txtBillRow10_2 = Entry(root, width=50)
txtBillRow10_3 = Entry(root, width=5)
txtBillRow10_4 = Entry(root, width=5)
txtBillRow10_5 = Entry(root, width=5)
txtBillRow10_6 = Entry(root, width=5)
txtBillRow10_7 = Entry(root)

#Billrows - 10 Serial Nos
txtBillRow2_1 = Entry(root, width=5)
txtBillRow3_1 = Entry(root, width=5)
txtBillRow4_1 = Entry(root, width=5)
txtBillRow5_1 = Entry(root, width=5)
txtBillRow6_1 = Entry(root, width=5)
txtBillRow7_1 = Entry(root, width=5)
txtBillRow8_1 = Entry(root, width=5)
txtBillRow9_1 = Entry(root, width=5)


#Create the Tax breakup, throw in textboxes

txtCGST= Entry(root, width=5)
txtCGST.insert(0,"CGST")
txtCGST.config(state='readonly')
txtSGST= Entry(root, width=5)
txtSGST.insert(0,"SGST")
txtSGST.config(state='readonly')
txtTotal= Entry(root, width=5)
txtTotal.insert(0,"Total")
txtTotal.config(state='readonly')
txtCGST_2_5= Entry(root, width=5)
txtCGST_2_5.insert(0,"2.5")
txtCGST_2_5.config(state='readonly')
txtSGST_2_5= Entry(root, width=5)
txtSGST_2_5.insert(0,"2.5")
txtSGST_2_5.config(state='readonly')
txtCGST_6_0= Entry(root, width=5)
txtCGST_6_0.insert(0,"6.0")
txtCGST_6_0.config(state='readonly')
txtSGST_6_0= Entry(root, width=5)
txtSGST_6_0.insert(0,"6.0")
txtSGST_6_0.config(state='readonly')
txtCGST_9_0= Entry(root, width=5)
txtCGST_9_0.insert(0,"9.0")
txtCGST_9_0.config(state='readonly')
txtSGST_9_0= Entry(root, width=5)
txtSGST_9_0.insert(0,"9.0")
txtSGST_9_0.config(state='readonly')
txtCGST_14_0= Entry(root, width=5)
txtCGST_14_0.insert(0,"14.0")
txtCGST_14_0.config(state='readonly')
txtSGST_14_0= Entry(root, width=5)
txtSGST_14_0.insert(0,"14.0")
txtSGST_14_0.config(state='readonly')
#Dynamic values in tax table
txtTotal_2_5= Entry(root, width=5)
txtTotal_2_5.config(state='readonly')
txtTotal_6_0= Entry(root, width=5)
txtTotal_6_0.config(state='readonly')
txtTotal_9_0= Entry(root, width=5)
txtTotal_9_0.config(state='readonly')
txtTotal_14_0= Entry(root, width=5)
txtTotal_14_0.config(state='readonly')

#Throw in labels and textboxes needed for the Totals on the bottom right
lblSubtotal=Label(root,text='Sub Total   Rs.')
lblTaxTotal=Label(root,text='Tax Total   Rs.')
lblGrandTotal=Label(root, font=(None,15), text='Grand Total  Rs.')
txtSubTotal= Entry(root, width=5)
txtSubTotal.config(state='readonly')
txtTaxTotal= Entry(root, width=5)
txtTaxTotal.config(state='readonly')
txtGrandTotal= Entry(root, width=25)
txtGrandTotal.config(state='readonly')


# L shaped reference to know row and column size, to be commented out when not in use
txtBillRowx0y12 = Entry(root)
txtBillRowx1y12 = Entry(root)
txtBillRowx2y12 = Entry(root)
txtBillRowx3y12 = Entry(root)
txtBillRowx4y12 = Entry(root)
txtBillRowx5y12 = Entry(root)
txtBillRowx6y12 = Entry(root)
txtBillRowx7y12 = Entry(root)
txtBillRowx8y12 = Entry(root)
txtBillRowx9y12 = Entry(root)
txtBillRowx10y12 = Entry(root)
txtBillRowx11y12 = Entry(root)
txtBillRowx12y12 = Entry(root)
txtBillRowx13y12 = Entry(root)
txtBillRowx14y12 = Entry(root)
txtBillRowx15y12 = Entry(root)
txtBillRowx16y12 = Entry(root)
txtBillRowx17y12 = Entry(root)
txtBillRowx18y12 = Entry(root)
txtBillRowx19y12 = Entry(root)
txtBillRowx20y12 = Entry(root)
txtBillRowx21y12 = Entry(root)
txtBillRowx22y12 = Entry(root)
txtBillRowx23y12 = Entry(root)
txtBillRowx24y12 = Entry(root)
txtBillRowx25y12 = Entry(root)
txtBillRowx26y12 = Entry(root)
txtBillColumnx260y0 = Entry(root)
txtBillColumnx261y1 = Entry(root)
txtBillColumnx262y2 = Entry(root)
txtBillColumnx263y3 = Entry(root)
txtBillColumnx264y4 = Entry(root)
txtBillColumnx265y5 = Entry(root)
txtBillColumnx266y6 = Entry(root)
txtBillColumnx267y7 = Entry(root)
txtBillColumnx268y8 = Entry(root)
txtBillColumnx269y9 = Entry(root)
txtBillColumnx2610y10 = Entry(root)
txtBillColumnx2611y11 = Entry(root)


txtBillColumnx = Entry(root)


#END OF WIDGETS


#LAYOUT OF WIDGETS ON THE GRID

# In Row 0
lblCompanyLogo.grid(row=0, column=1,sticky =W)
lblShopNameTam.grid(row=0, column=2,  columnspan=5 ,  sticky =W)
lblDate_1.grid(row=0, column=6,sticky =N)
lblDate_2.grid(row=0, column=6,sticky =S)
btnCloseWindow.grid(row=0,column=7, sticky=W)

# In Row 1
lblShopNameEng.grid(row=1, column=1, columnspan=5)
lblClock.grid(row=1,column=6, sticky=N)


# In row 2 we have only blank space


# In row 3 we have some stuff
btnNewBill.grid(row=3 , column =1)
btnExistBill.grid(row=3, column=2, sticky=W)
btnCreateItem.grid(row=3, column =4)
btnEditItem.grid(row=3, column=5,sticky=W)

# In row 4 we have only blank space

#In row 5 we display only the next bill number
lblBillNo.grid(row=5, column =1)
lblBillNoValue.grid(row=5, column =2,sticky=W)

# In row 6 we have only blank space

#In row 7 we display the various billing column headers
lblSno.grid(row=7, column =1, sticky=E)
lblItemName.grid(row=7, column =2 , sticky=W)
lblQty.grid(row=7, column =3, sticky=W,padx=(5))
lblRate.grid(row=7, column =3,padx=(5))
lblCGST.grid(row=7, column =3, sticky=E)
lblSGST.grid(row=7, column =4, sticky=W)
lblBasicAmount.grid(row=7, column =4, sticky=W,padx=(45))



#In  row 8 we have billing row 1
txtBillRow1_1.grid(row=8, column =1,sticky=E)
txtBillRow1_2.grid(row=8, column =2  , sticky=W,padx=(5))
txtBillRow1_3.grid(row=8, column =3, sticky=W,padx=(5))
txtBillRow1_4.grid(row=8, column =3 ,padx=(5))
txtBillRow1_5.grid(row=8, column =3, sticky=E,padx=(5))
txtBillRow1_6.grid(row=8, column =4, sticky=W,padx=(5))
txtBillRow1_7.grid(row=8, column =4, sticky=W,padx=(45))
#txtBillRow1_8.grid(row=8, column =8)





#Billrows for testing, allocate to individual rows later on for better readability
txtBillRow2_1.grid(row=9, column =1,sticky=E)
txtBillRow3_1.grid(row=10, column =1,sticky=E)
txtBillRow4_1.grid(row=11, column =1,sticky=E)
txtBillRow5_1.grid(row=12, column =1,sticky=E)
txtBillRow6_1.grid(row=13, column =1,sticky=E)
txtBillRow7_1.grid(row=14, column =1,sticky=E)
txtBillRow8_1.grid(row=15, column =1,sticky=E)
txtBillRow9_1.grid(row=16, column =1,sticky=E)



#In row 17 we have the 10th billing row
txtBillRow10_1.grid(row=17, column =1,sticky=E)
txtBillRow10_2.grid(row=17, column =2  , sticky=W,padx=(5))
txtBillRow10_3.grid(row=17, column =3, sticky=W,padx=(5))
txtBillRow10_4.grid(row=17, column =3 ,padx=(5))
txtBillRow10_5.grid(row=17, column =3, sticky=E,padx=(5))
txtBillRow10_6.grid(row=17, column =4, sticky=W,padx=(5))
txtBillRow10_7.grid(row=17, column =4, sticky=W,padx=(45))


#In Row 19 we have the tax table, sub total
txtCGST.grid(row=19, column =1,sticky=E)
txtSGST.grid(row=19, column =2,sticky=W,padx=(5))
txtTotal.grid(row=19, column =2 ,sticky=W,padx=(45))
lblSubtotal.grid(row=19, column=4,sticky=W)
txtSubTotal.grid(row=19, column=4,sticky=W,padx=(80))

#In Row 20 we have the tax table, tax total
txtCGST_2_5.grid(row=20, column=1,sticky=E)
txtSGST_2_5.grid(row=20, column=2,sticky=W,padx=(5))
txtTotal_2_5.grid(row=20, column =2 ,sticky=W,padx=(45))
lblTaxTotal.grid(row=20,column=4,sticky=W)
txtTaxTotal.grid(row=20, column=4, sticky=W,padx=(80))

#In Row 21 we have the tax table
txtCGST_6_0.grid(row=21, column =1,sticky=E )
txtSGST_6_0.grid(row=21, column=2,sticky=W,padx=(5))
txtTotal_6_0.grid(row=21, column =2 ,sticky=W,padx=(45))
#In Row 22 we have the tax table , grand total
txtCGST_9_0.grid(row=22, column=1,sticky=E)
txtSGST_9_0.grid(row=22, column=2,sticky=W,padx=(5))
txtTotal_9_0.grid(row=22, column =2 ,sticky=W,padx=(45))
lblGrandTotal.grid(row=22,column=3,rowspan=2, sticky=E)
txtGrandTotal.grid(row=22, column=4, rowspan=2,sticky=W,padx=(25))

#In Row 23 we have the tax table , grand total
txtCGST_14_0.grid(row=23, column=1,sticky=E)
txtSGST_14_0.grid(row=23, column=2,sticky=W,padx=(5))
txtTotal_14_0.grid(row=23, column =2 ,sticky=W,padx=(45))



#In the last row
lblThankyou.grid(row=24, column= 3,  sticky=S)
lblShoestring1.grid(row=25, column= 3,  sticky=S)

# L shaped reference to know row and column size, to be commented out when not in use
#These will display  textboxes on the right side
txtBillRowx0y12.grid(row=0, column=8, sticky=W)
txtBillRowx1y12.grid(row=1, column=8, sticky=W)
txtBillRowx2y12.grid(row=2, column=8, sticky=NSEW)
txtBillRowx3y12.grid(row=3, column=8, sticky=NSEW)
txtBillRowx4y12.grid(row=4, column=8, sticky=NSEW)
txtBillRowx5y12.grid(row=5, column=8, sticky=NSEW)
txtBillRowx6y12.grid(row=6, column=8, sticky=NSEW)
txtBillRowx7y12.grid(row=7, column=8, sticky=NSEW)
txtBillRowx8y12.grid(row=8, column=8, sticky=NSEW)
txtBillRowx9y12.grid(row=9, column=8, sticky=NSEW)
txtBillRowx10y12.grid(row=10 , column=8, sticky=NSEW)
txtBillRowx11y12.grid(row= 11, column=8, sticky=NSEW)
txtBillRowx12y12.grid(row=12 , column=8, sticky=NSEW)
txtBillRowx13y12.grid(row=13 , column=8, sticky=NSEW)
txtBillRowx14y12.grid(row=14 , column=8, sticky=NSEW)
txtBillRowx15y12.grid(row=15 , column=8, sticky=NSEW)
txtBillRowx16y12.grid(row=16 , column=8, sticky=NSEW)
txtBillRowx17y12.grid(row=17 , column=8, sticky=NSEW)
txtBillRowx18y12.grid(row=18 , column=8, sticky=NSEW)
txtBillRowx19y12.grid(row=19 , column=8, sticky=NSEW)
txtBillRowx20y12.grid(row=20 , column=8, sticky=NSEW)
txtBillRowx21y12.grid(row=21 , column=8, sticky=NSEW)
txtBillRowx22y12.grid(row=22 , column=8, sticky=NSEW)
txtBillRowx23y12.grid(row=23 , column=8, sticky=NSEW)
txtBillRowx24y12.grid(row=24 , column=8, sticky=NSEW)
txtBillRowx25y12.grid(row=25 , column=8, sticky=NSEW)
txtBillRowx26y12.grid(row=26 , column=8, sticky=NSEW)
#These will display textboxes on the last row of the page
txtBillColumnx260y0.grid(row=26 , column=0 , sticky=NSEW)
txtBillColumnx261y1.grid(row=26 , column=1 , sticky=NSEW)
txtBillColumnx262y2.grid(row=26 , column=2, sticky=NSEW)
txtBillColumnx263y3.grid(row=26 , column=3 , sticky=NSEW)
txtBillColumnx264y4.grid(row=26 , column=4 , sticky=NSEW)
txtBillColumnx265y5.grid(row=26 , column=5 , sticky=NSEW)
txtBillColumnx266y6.grid(row=26 , column=6 , sticky=NSEW)
txtBillColumnx267y7.grid(row=26 , column=7 , sticky=NSEW)
txtBillColumnx268y8.grid(row=26 , column=8 , sticky=NSEW)
txtBillColumnx269y9.grid(row=26 , column=9 , sticky=NSEW)
txtBillColumnx2610y10.grid(row=26  , column=10 , sticky=NSEW)
txtBillColumnx2611y11.grid(row=26 ,  column=11 , sticky=NSEW)



#END OF LAYOUT

# To fix the column and row sizes to default
col_count, row_count = root.grid_size()

for col in xrange(col_count):
    root.grid_columnconfigure(col, minsize=10)

for row in xrange(row_count):
    root.grid_rowconfigure(row, minsize=10)
# END of fixing the column and row sizez

#Setup the clock timer to display
def fn_tick():
    global vTime1
    # get the current local time from the PC
    vTime2 = time.strftime("%I:%M:%S %p")
    # if time string has changed, update it
    if vTime2 != vTime1:
        vTime1 = vTime2
        lblClock.config(text=vTime2)
    # calls itself every 200 milliseconds
    # to update the time display as needed
    # could use >200 ms, but display gets jerky
    lblClock.after(200, fn_tick)
    #END OF CLOCK TICKER


#Call the clock ticker on initialization
fn_tick()





root.mainloop()



