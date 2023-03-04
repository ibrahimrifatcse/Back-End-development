#in python there are two type of control flow
# if/else/elif 
# for loop / while loop
# What is control flow? Control flow refers to the order in which the instructions in a program are executed. 

total_bill = 95
discount = 10
discount_bill = total_bill - discount
if total_bill > 100 :
   print("Total bill greather than 100")  
   print("totat bill is " + discount_bill)  
elif total_bill > 500 :
    print("total bill greather than 500")
else :
   print("total bill is less than 100")
   print(str(discount_bill) + " is the discount bill") # str() is for typecusting

print(discount_bill - 10)

# other example 

#Light is currently off
current = False

if current:
    current = False
    print('Turning light off')

if not current:
    current = True
    print('Turning light on')
   
   # output is : Turning light on because first 'if' is false
   
   # IF ELSE The above code works fine but it can be rewritten more effectively by using another condition called else. The following code is an example:
   current = False

if current:
    current = False
    print('Turning light off')
else: 
    current = True
    print('Turning light on')
   
   #output : Turning light on
   
   # else if 
   
   loyalty_customer = True
total_bill = 124

if loyalty_customer and total_bill > 100:
    #give 20% discount
    total_bill = total_bill - (float(total_bill)/ 100) * 20
elif total_bill > 100:
    #give 10% discount
    total_bill = total_bill - (float(total_bill)/ 100) * 10
else:
    #sorry no discount, 5% service charge applied.
    print('Sorry, no discount ...')

print('Total Bill: ', float(total_bill))




   
   
   
