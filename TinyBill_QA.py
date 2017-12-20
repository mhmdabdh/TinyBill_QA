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
root.title ( "SICO Trichy")



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
lblQty= Label(root,text="Quantity")
lblRate= Label(root,text="Rate")
lblCGST= Label(root,text="CGST % ")
lblSGST= Label(root,text="SGST %")
lblBasicAmount= Label(root,text="Basic Amount")
txtBillRow1_1 = Entry(root, width=2)
txtBillRow1_2= Entry(root, width=50)
txtBillRow1_3= Entry(root, width=2)
txtBillRow1_4= Entry(root)
txtBillRow1_5= Entry(root, width=2)
txtBillRow1_6= Entry(root, width=2)
txtBillRow1_7= Entry(root)
txtBillRow1_8= Entry(root)

#Billrows
txtBillRow2_1 = Entry(root, width=2)
txtBillRow3_1 = Entry(root, width=2)
txtBillRow4_1 = Entry(root, width=2)
txtBillRow5_1 = Entry(root, width=2)
txtBillRow6_1 = Entry(root, width=2)
txtBillRow7_1 = Entry(root, width=2)
txtBillRow8_1 = Entry(root, width=2)
txtBillRow9_1 = Entry(root, width=2)
txtBillRow10_1 = Entry(root, width=2)


#END OF WIDGETS


#LAYOUT OF WIDGETS ON THE GRID

# In Row 0
lblCompanyLogo.grid(row=0, column=2,  sticky =N)
lblShopNameTam.grid(row=0, column=4,  columnspan=4, sticky =N)
lblDate_1.grid(row=0, column=10,sticky =N)
lblDate_2.grid(row=0, column=10,sticky =E)
btnCloseWindow.grid(row=0,column=11, sticky=N)

# In Row 1
lblShopNameEng.grid(row=1, column=5,sticky=N)
lblClock.grid(row=1,column=10, sticky=N)


# In row 2 we have only blank space


# In row 3 we have some stuff
btnNewBill.grid(row=3 , column =2)
btnExistBill.grid(row=3, column=4)
btnCreateItem.grid(row=3, column =7)
btnEditItem.grid(row=3, column=9)

# In row 4 we have only blank space

#In row 5 we display only the next bill number
lblBillNo.grid(row=5, column =2)
lblBillNoValue.grid(row=5, column =3)

# In row 6 we have only blank space

#In row 7 we display the various billing column headers
lblSno.grid(row=7, column =2)
lblItemName.grid(row=7, column =3, columnspan=2)
lblQty.grid(row=7, column =5, sticky=W)
lblRate.grid(row=7, column =6,sticky=W)
lblCGST.grid(row=7, column =7)
lblSGST.grid(row=7, column =8)
lblBasicAmount.grid(row=7, column =9)

#In  row 8 we have billing row 1
txtBillRow1_1.grid(row=8, column =2)
txtBillRow1_2.grid(row=8, column =3, columnspan=3,sticky=W)
txtBillRow1_3.grid(row=8, column =6, sticky=W)
txtBillRow1_4.grid(row=8, column =7, sticky=W)
txtBillRow1_5.grid(row=8, column =8, sticky=W)
txtBillRow1_6.grid(row=8, column =9, sticky=W)
txtBillRow1_7.grid(row=8, column =10, sticky=W)
#txtBillRow1_8.grid(row=8, column =8)


#Billrows for testing, allocate to individual rows later on for better readability
txtBillRow2_1.grid(row=9, column =2)
txtBillRow3_1.grid(row=10, column =2)
txtBillRow4_1.grid(row=11, column =2)
txtBillRow5_1.grid(row=12, column =2)
txtBillRow6_1.grid(row=13, column =2)
txtBillRow7_1.grid(row=14, column =2)
txtBillRow8_1.grid(row=15, column =2)
txtBillRow9_1.grid(row=16, column =2)
txtBillRow10_1.grid(row=17, column =2)

#In the last row
lblThankyou.grid(row=24, column= 4, columnspan = 4, sticky=S)
lblShoestring1.grid(row=25, column= 5, columnspan = 2,  sticky=S)
#END OF LAYOUT

# To fix the column and row sizes to default
col_count, row_count = root.grid_size()

for col in xrange(col_count):
    root.grid_columnconfigure(col, minsize=20)

for row in xrange(row_count):
    root.grid_rowconfigure(row, minsize=20)
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



