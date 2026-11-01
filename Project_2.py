'''SMART CANTEEN BILLING AND ORDR ANALYZER'''

#MENU LIST

item1='Veg Sandwich'
item1_price= 60
sandwich_qty=0
sandich_totalcost =0

item2='Masala Dosa'
item2_price=80
dosa_qty=0
dosa_totalcost=0

item3='Chole Rice'
item3_price=90
rice_qty = 0
rice_totalcost=0

item4="Paneer Roll"
item4_price=100
roll_qty=0
roll_totalcost=0

item5='Tea'
item5_price=20
tea_qty=0
tea_totalcost =0

print("\n"+"="*50)
print(f"\n{'Sl.No':<7}{'Food Items':<20}{'Price':<5}")
print("\n"+"="*50)

print(f"\n{'1.':<7}{item1:<20}{item1_price:<5}")
print(f"{'2.':<7}{item2:<20}{item2_price:<5}")
print(f"{'3.':<7}{item3:<20}{item3_price:<5}")
print(f"{'4.':<7}{item4:<20}{item4_price:<5}")
print(f"{'5.':<7}{item5:<20}{item5_price:<5}")

print("\n"+"="*50)

discount=0
subtotal=0
total_item_cost =0

finaltotal=(subtotal+discount)



while True:

    choice = int(input("\nChoose item number(1-5):"))
    
    if choice<1 or choice>5:
        print("invalid item Number!")
        continue

    quantity=int(input("Enter Quantity:"))
    
    if quantity<=0:
        print(" Please Enter quantity in positive number")
        continue
    

    if choice ==1:
        print(f"Added: {item1} X {quantity} = {item1_price*quantity}")  
        sandwich_qty+=quantity
        
    
    elif choice==2:
        print(f"Added: {item2} X {quantity} = {item2_price*quantity}") 
        dosa_qty+=quantity
        
    elif choice==3:
        print(f"Added: {item3} X {quantity} = {item3_price*quantity}") 
        rice_qty+=quantity 
        
    elif choice==4:
        print(f"Added: {item4} X {quantity} = {item4_price*quantity}")
        roll_qty+=quantity
         
    elif choice==5:
        print(f"Added: {item5} X {quantity} = {item5_price*quantity}")  
        tea_qty+=quantity
    
    else:
        print("Please select correct item Number between 1 and 5.")
        
    add_item = input("\nAdd another item?(y/n):")
    
    if add_item.lower()=='n':
        break
    
    elif add_item.lower()=='y':
        continue
    
    else :
        print("Invalid Choice.")
        
        

print("\n"+"="*30)
print("          RECEIPT")   
print("="*30,"\n")

if sandwich_qty>0:
    sandich_totalcost=item1_price*sandwich_qty
    print(f"{item1} x {sandwich_qty}: ${sandich_totalcost}")
    total_item_cost+=sandich_totalcost
    
if dosa_qty>0:
    dosa_totalcost=item2_price*dosa_qty
    print(f"{item2} x {dosa_qty}: ${dosa_totalcost}")
    total_item_cost+=dosa_totalcost
    
if rice_qty>0:
    rice_totalcost=item3_price*rice_qty
    print(f"{item3} x {rice_qty}: ${rice_totalcost}")
    total_item_cost+=rice_totalcost
    
if roll_qty>0:
    roll_totalcost=item4_price*roll_qty
    print(f"{item4} x {roll_qty}: ${roll_totalcost}")
    total_item_cost+=roll_totalcost
    
if tea_qty>0:
    tea_totalcost=item5_price*tea_qty
    print(f"{item5} x {tea_qty}: ${tea_totalcost}")
    total_item_cost+=tea_totalcost
    

subtotal=subtotal+total_item_cost

if subtotal>=500:
    discount=subtotal*(10/100)
    
elif 250<=subtotal<=499.99:
    discount=subtotal*(5/100)
    
else:
    discount=0    
    
final_total = (subtotal-discount)

print(f"Subtotal: ${subtotal}")
print(f"Dicount:  ${discount}")
print(f"Final Total: ${final_total}")

print("\n\nThank You! Visit Again")

