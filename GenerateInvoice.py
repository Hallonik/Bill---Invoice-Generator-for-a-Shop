#invoice generator using tkinter and fpdf modules

from tkinter import *#tkinter module to build the interface of the app
from fpdf import FPDF#to generate the pdf

window=Tk()#name the windows object anything

window.title(" INVOICE GENERATOR ")#to add window title



# insertion of list of medicines with its prices using dictionary
#since dictionary has key value pair
medicines={
    "Medicine A : " : 10,
    "Medicine B : " : 30,
    "Medicine C : " : 45,
    "Medicine D : " : 67,
    "Medicine E : " : 35,

}


#adding medicines to the shopping cart
invoice_items=[]#a vacant list is created 


#func. to add the selected medicines to generate invoice on screen
def add_medicine():
    selected_medicine=medicine_listbox.get(ANCHOR)#Anchor means the item selected,gives access to the item selected
    quantity=int(quantity_entry.get())#since quantity entry type is str we need to convert it in int
    price=medicines[selected_medicine]#to get the price of the selected medicine
    item_total=price*quantity#to calculate the total price for each medicine
    invoice_items.append((selected_medicine,quantity,item_total))#this tuple stores the medicine , quantity and total price
    total_amount_entry.delete(0,END)#to clear the txt in the total amount txt box
    total_amount_entry.insert(END,str(calculate_total()))#since calculate total returns an int convert it to strings    
    update_invoice_text()

#to calculate the total amount
def calculate_total():
    total=0.0
    for item in invoice_items:
        total=total+item[2]
    return total
#after calculating the total amount we have to pass it to total_amount _entry widget





#func. to update the list displayed for every time a new item added in the txt box
def update_invoice_text():
    invoice_text.delete(1.0,END)#1- row 0- colmn, delete all txt frm 1st row 0th colmn to end
    for item in invoice_items:#to access each item in invoice_item
        invoice_text.insert(END,f"Medicine : {item[0]},Quantity : {item[1]},Total : {item[2]}\n")


#func. to build the pdf  doc.
def generate_invoice():
    customer_name=customer_entry.get()#to add customer name 

    #creation of pdf 
    pdf=FPDF()
    pdf.add_page()
    pdf.set_font("Times",size=14)

    pdf.cell(0,10,txt="Invoice",new_x="LMARGIN",new_y="NEXT",align="C")#for the heding
    pdf.cell(0,10,txt="Customer : "+customer_name,
             new_x="LMARGIN",new_y="NEXT",align="L")#for customer name
    pdf.cell(0,10,txt="",new_x="LMARGIN",new_y="NEXT")
    
    for item in invoice_items:
        medicine_name,quantity,item_total=item
        pdf.cell(0,10,txt=f"Medicine : {medicine_name},Quantity : {quantity},Total : {item_total}",new_x="LMARGIN",new_y="NEXT",align="L")
    pdf.cell(0,10,txt="Total Amount : "+str(calculate_total()),
             new_x="LMARGIN",new_y="NEXT",align="L")
    pdf.output("invoice.pdf")





#layout

#create label
medicine_label=Label(window,text=" Medicine : ")#label created

medicine_label.pack()#adds the label to the tkinter window

#display list of medicines

medicine_listbox=Listbox(window,selectmode=SINGLE)#BOX IN TKINTER INTERFACE 
for medicine in medicines:#to access each medicine individually
    medicine_listbox.insert(END,medicine)#END is the index where the medicine is to be inserted
 #to display the list of medicines and select any one
medicine_listbox.pack()

#quantity of medicine
quantity_label=Label(window,text=" Quantity ")#to add lable for quantity
quantity_label.pack()

quantity_entry=Entry(window)#to enter the quantity of a medicine
quantity_entry.pack()

#adding buttons to add medicine to the cart or some other window

add_button=Button(window,text=" Add Medicine ",command=add_medicine)#add_medicine func. is called
add_button.pack()#buttons to add the medicines selected

#calculation of total amount

total_amount_label=Label(window,text=" Total Amount ")#label for total amount
total_amount_label.pack()

total_amount_entry=Entry(window)#to display the total amount
total_amount_entry.pack()#here the user dont have to enter anything , 
#the total amount automatically calculated through logic developed



 #customer's details

customer_lable=Label(window,text=" Customer Name ")#label for customer name
customer_lable.pack()

customer_entry=Entry(window)#to enter the customer name
customer_entry.pack()


#generate invoice

generate_button=Button(window,text=" Generate Invoice ",command=generate_invoice)
generate_button.pack()

# display of all the medicine that are selected

invoice_text=Text(window,height=10,width=60)#text box to display all the medicines selected
invoice_text.pack()





window.mainloop()#to generate a window loop for this layout


