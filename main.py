task 1
a=int(input("Enter a number: "))
b=int(input("Enter another number: "))
if a > b:
    print("a is greater than b")
elif a < b:
    print("a is less than b")
else:
    print("numbers are equal")

task 2
a=int(input("Enter a number: "))
if a>0:
    print("The number is positive")
elif a<0:
    print("The number is negative")
else:
    print("The number is zero")

task 3
a=int(input("Enter a number: "))
if a%2==0:
    print("The number is even")
else:
    print("The number is odd")
task 4
score=int(input("Enter your score: "))
if score >= 91:
    print("Grade: A")
elif score >= 81:
    print("Grade: B")
elif score >= 71:
    print("Grade: C")
elif score >= 61:
    print("Grade: D")
elif score >= 51:
    print("Grade: E")
elif 0<= score < 51:
    print("Grade: F")
else:
    print("Invalid score")

task 5
a=int(input("Enter a number: "))
b=int(input("Enter another number: "))
c=int(input("Enter a third number: "))
if a>b and a>c:
    print("a is the greatest number")
elif b>a and b>c:
    print("b is the greatest number")
else:
    print("c is the greatest number")

task 6
a=float(input("Enter a number: "))
b=float(input("Enter another number: "))
op=input("Enter an operator (+, -, *, /): ")
match op:
    case "+":
        print(f"The result is: {a + b}")
    case "-":
        print(f"The result is: {a - b}")
    case "*":
        print(f"The result is: {a * b}")
    case "/":
        if b != 0:
            print(f"The result is: {a / b}")
        else:
            print("Error: Division by zero")
    case "//":
        if b != 0:
            print(f"The result is: {a // b}")
        else:
            print("Error: Division by zero")
    case _:
        print("Invalid operator")

task 7
age=int(input("Enter your age: "))
if age<0:
    print("Invalid age")
elif age<13:
    print("You are a child")
elif age<18:
    print("You are a teenager")
elif age<65:
    print("You are an adult")
else:
    print("You are a senior")

task 8
amount=float(input("Enter the amount: "))
if amount<100:
    da=0
    fp=amount-da
elif amount<300:
    da=amount*0.1
    fp=amount-da
elif amount<500:
    da=amount*0.15
    fp=amount-da
else:
    da=amount*0.2
    fp=amount-da
print("original price:", amount)
print("discount amount:", da)
print("final price:", fp)

task 9
a=int(input("Enter a number: "))
b=int(input("Enter another number: "))
c=int(input("Enter a third number: "))
if a>b>c:
    print(c, b, a)
elif a>c>b:
    print(b, c, a)
elif b>a>c:
    print(c, a, b)
elif b>c>a:
    print(a, c, b)
elif c>a>b:
    print(b, a, c)
elif c>b>a:
    print(a, b, c)

task 10
wamount=int(input("Enter the amount: "))
balance=1000
if wamount>balance:
    print("Insufficient balance")
elif 0<wamount<=balance:
    balance-=wamount
    print("Remaining balance:", balance)
else:
    print("Invalid amount")

task 11
usage=int(input("Enter the electricity usage: "))
if usage<0:
    print("Invalid usage")
if usage<=100:
    rate=0.08
    bill=usage*rate
elif usage<=300:
    rate=0.12
    bill=usage*rate
else:
    rate=0.15
    bill=usage*rate
print("Electricity bill:", bill)
print("Electricity usage:", usage)
print("Rate per unit:", rate)

task 12
distance=float(input("Enter the distance in kilometers: "))
if distance<0:
    print("Invalid distance")
elif distance<=5:
    rate=0.7
    fare=distance*rate
elif distance<=15:
    rate=0.6
    fare=distance*rate
else:
    rate=0.5
    fare=distance*rate
print("Distance:", distance, "km")
print("Rate per km:", rate)
print("Total fare:", fare)

task 13
age=int(input("Enter your age: "))
salary=float(input("Enter your salary: "))
lamount=float(input("Enter the loan amount: "))
if age<0 or salary<0 or lamount<=0:
    print("Invalid input")
else:
    if age<18:
        print("decision:you are rejected")
        print("reason:you are underage")
    else:
        if salary<500:
            print("decision:you are rejected")
            print("reason:your salary is too low")
        else:
            if lamount>salary*10:
                print("decision:you are rejected")
                print("reason:loan amount exceeds limit")
            else:
                print("decision:you are approved")

task 14
a=int(input("Enter a number: "))
b=int(input("Enter another number: "))
c=int(input("Enter a third number: "))
if a<0 or b<0 or c<0:
    print("Invalid input")
else:
    if a+b>c:
        if a+c>b:
            if b+c>a:
                if a==b==c:
                    print("The triangle is equilateral")
                elif a==b or b==c or a==c:
                    print("The triangle is isosceles")
                else:
                    print("The triangle is scalene")
            else:
                print("Triangle cannot be created")
        else:
            print("Triangle cannot be created")
    else:
        print("Triangle cannot be created")

task 15
escore=int(input("Enter your exam score: "))
sscore=int(input("Enter your school score: "))
age=int(input("Enter your age: "))
if age<0 or not (0<= escore <=700) or not (0<= sscore <=100):
    print("You are rejected")
elif age<16:
    print("You are rejected, reason: you are underage")
elif 600<= escore <=700:
    print("You are accepted and scholarship: 100%")
elif 450<= escore <600:
    print("You are accepted")
elif 300<= escore <450:
    if sscore>=80:
        print("You are accepted")
    else:
        print("You are rejected, reason: your school score is too low")
else:
    print("You are rejected, reason: your exam score is too low")

task 16
score=int(input("Enter your score: "))
if 0<= score <= 100:
    result = "Pass" if score >= 51 else "Fail"
    print(result)
else:
    print("Invalid score")

task 17
total = float(input("Sifariş məbləği (AZN): "))
membership = input("Üzvlük var? (yes/no): ")
if total < 0:
    print("Xəta: məbləğ mənfi ola bilməz")
elif membership != "yes" and membership != "no":
    print("Xəta: üzvlük cavabi yalniz 'yes' və ya 'no' ola bilər")
else:
    fee = 0 if total >= 50 or membership == "yes" else 5
    final_amount = total + fee
print("fee:", fee)
print("final amount:", final_amount)

task 18
day=input("Enter a day of the week: ")
match day:
    case 1:
        print("Monday")
        print("Study day")
    case 2:
        print("Tuesday")
        print("Study day")
    case 3:
        print("Wednesday")
        print("Study day")
    case 4:
        print("Thursday")
        print("Study day")
    case 5:
        print("Friday")
        print("Study day")  
    case 6:
        print("Saturday")
        print("Weekend")    
    case 7:
        print("Sunday")
        print("Weekend")
    case _:
        print("Invalid day")

task 19
code=input("Enter a product code: ")
quantity=int(input("Enter the quantity: "))
match code:
    case "T":
        drink="tea"
        price=2
    case "C":
        drink="coffee"
        price=4
    case "J":
        drink="juice"
        price=3
    case _:
        drink="unknown"
        price=0
if drink == "unknown":
    print("Invalid product code")
elif not  (1 <= quantity <= 10):
    print("Invalid quantity")
else:
    total_price = price * quantity
    order="large order" if total_price >= 20 else "regular order"
    print(f"Product: {drink}")
    print(f"Quantity: {quantity}")
    print(f"Total price: {total_price} AZN")

task 20
a="0123456789"
id=(input("Enter your ID: "))
if len(id)==0:
    print("Rejected: ID cannot be empty")
elif len(id)!=8:
    print("Rejected: ID must be 8 characters long")
for i in id:
    if i not in a:
        print("Rejected: ID must contain only digits")
        break
else:
    print("Accepted")

task 21
pin=input("Enter your PIN: ")
a="0123456789"
stored_pin="0427"
if len(pin)==0:
    print("PIN is required")
elif len(pin)!=4:
    print("PIN must have 4 digits")
for i in pin:
    if i not in a:
        print("Digits only")
        break
elif pin==stored_pin:
    print("Access granted")
else:
    print("Incorrect PIN")

task 22
number=input("Enter phone number: ")
a="0123456789"
if number='':
    print("Phone number is required")
for i in number:
    if i not in a:
        print("Phone number must contain only digits")
        break
elif len(number)!=10:
    print("Phone number must be 10 digits long")
elif number[0]!='0':
    print("Phone number must start with 0")
else:
    match number[:3]:
    case "050" | "051" | "055" | "070" | "077" | "099":
            print("Phone number accepted")
    case _:
            print("Invalid operator")

task 23
pin=input("Enter your PIN: ")
wamount=input("Enter withdrawal amount: ")
a="0123456789"
if len(pin)!=4 or len(wamount)==0:
    print("PIN must have 4 digits and withdrawal amount cannot be empty")
for i in pin:
    if i not in a:
        print("PIN must contain only digits")
        break
for i in wamount:
    if i not in a:
        print("Withdrawal amount must contain only digits")
        break
elif pin!="0427":
    print("Incorrect PIN")
else:
    if int(wamount)<10 or int(wamount)>500:
        print("Withdrawal amount must be between 10 and 500")
    elif int(wamount)%10!=0:
        print("Withdrawal amount must be a multiple of 10")
    else:
        fee=0 if int(wamount)<=200 else 2
        if int(wamount)+fee>balance:
            print("Insufficient balance")
        else:
            balance-=int(wamount)-fee
            print("Withdrawal successful")
            print("Remaining balance:", balance)

task 24
pcode=input("Enter product code: ")
quantity=input("Enter quantity: ") 
ccode=input("Enter coupon code: ")
dcode=input("Enter delivery code: ")
a="0123456789"
match pcode:
    case "K":
        product="Keyboard"
        price=40  
    case "M":
        product="Mouse" 
        price=20
    case "H":
        product="Headphones" 
        price=60
    case _:
        product="unknown"  
        price=0
if product=="unknown":
    print("Invalid product code")
for i in quantity:
    if i not in a and (int(quantity)<1 or int(quantity)>5):
        print("Invalid quantity")
        break
elif ccode not in("NONE","SAVE10"):
    print("Invalid coupon code")
else:
    quantity=int(quantity)
    subtotal=price*quantity
    if ccode=="SAVE10" and subtotal<100:
        print("Coupon code SAVE10 is not applicable for orders below 100 AZN")
    else:
        discount=subtotal*0.1 if ccode=="SAVE10" else 0
        discounted=subtotal-discount
        match dcode:
            case "P":
                fee=0
            case "S":
                 fee=0 if discounted>=80 else 5
            case _:
                 fee=None
        if fee is None:
            print("Invalid delivery code")
        else:
            total=discounted+fee
            print("Product:", product)
            print("Quantity:", quantity)
            print("Subtotal:", subtotal, "AZN")
            print("Discount:", discount, "AZN")
            print("Delivery fee:", fee, "AZN")
            print("Total amount to pay:", total, "AZN")