water= 1000;
milk =1000
coffee = 1000

while True:
	global flavour
	flavour = input("What would you like? (espresso-$2.50(Or)latte-$3.0(Or)cappuccino-$1.90):")
	if  flavour == "off" :
		break
	a = input("U can check the resources values and the cost of the flavoured coffee by entering yes/ no:")
	def report():
		if flavour == "espresso" :
			print(" Water : 100 ml")
			print( "Milk : 50 ml  ")
			print(" Coffee : 76 g")
			print( " Money : $ 2.5")
		elif flavour == "latte" :
			print(" Water : 80 ml")
			print( "Milk : 70 ml  ")
			print(" Coffee : 80 g")
			print( " Money : $ 3.0")
		else :
			print(" Water : 90 ml")
			print( "Milk : 65 ml  ")
			print(" Coffee :  55 g")
			print( " Money : $ 1.9")
	
	if  a ==  "yes" :
			report ()	
	def resourcessufficient():
		global water
		global milk 
		global coffee
		if  (water >100  and milk> 100 and coffee > 100 ):
			if flavour == "espresso":
				water = water -100
				milk = milk -50
				coffee = coffee - 76
			elif flavour == "latte" :
				water = water -80
				milk = milk -70
				coffee = coffee - 80		
			else :
				water = water -90
				milk = milk -65 
				coffee = coffee - 55		
		elif water <100 :
			print("Sorry there is no enough water")
		elif milk <100:
			print("Sorry there is no enough milk")
		elif coffee< 100:
			print("Sorry there is no enough coffee")
		else:
			print("Resources are not enough to prepare the coffee!!")
	resourcessufficient()
	def coins():
		global cost
		print("Please insert the coins for the payment !!!")
		quaters = 0.25; dimes = 0.10 ; nickles = 0.05 ; pennies = 0.01 
		p= int(input("Enter the number of quater coins :"))
		q =int(input("Enter the num of dimes coins :"))
		r= int(input("Enter the number of nickles coins:"))
		s= int(input("Enter the number of pennies coins:"))
		cost = quaters * p + dimes * q + nickles * r + pennies * s
	coins()
	def ingredientscheck():
		if (flavour == "espresso" or flavour == "latte" or flavour == " cappuccino"):
				print(f"Water : {water} ml")
				print (f"Milk : {milk} ml")
				print(f"Coffee :{coffee}g")
				if (flavour=="espresso"):
					print("Money : $2.50")
					if (flavour == "latte"):
						print("Money : $3.0")
						if(flavour == "cappuccino"):
							print("Money : $1.90")
				print(f" Here is your {flavour}.Enjoy!!")
	def moneycheck():
		if (  flavour == "espresso" and cost == 2.50 ):
			print("your payment has been succesful")
			ingredientscheck()
		elif(flavour == "espresso" and cost <2.50 ):
			print("Sorry thats not enough money,Money Refunded...Try again")
			coins()
			while( cost < 2.50):
				print("Sorry thats not enough money,Money Refunded...Try again")
				coins()
			if(cost >2.50):
				moneycheck()
		elif(flavour == "espresso" and cost >2.50 ):
			amount = round(cost - 2.50,2) 
			print(f" Here is ${amount} dollars in change .")
			ingredientscheck()
		elif (  flavour == "latte" and cost ==  3.0 ):
			print("your payment has been succesful")
			ingredientscheck()
		elif(flavour == "latte" and cost < 3.0):
			print("Sorry thats not enough money,Money Refunded....Try again")
			coins()
			while( cost < 3.0):
				print("Sorry thats not enough money,Money Refunded...Try again")
				coins()		
			if(cost >3.0):
				moneycheck()
		elif(flavour == "latte" and cost >3.0):
			amount = round(cost - 3.00,2) 
			print(f" Here is ${amount} dollars in change .")
			ingredientscheck()
		elif(flavour == "cappuccino" and cost == 1.90):
			print("your payment has been succesful")
			ingredientscheck()
		elif(flavour == "cappuccino" and cost < 1.90):
			print("Sorry thats not enough money,Money Refunded...Try again")
			coins()
			while(cost< 3.0):
				print("Sorry thats not enough money,Money Refunded...Try again")
				coins()
			if(cost >1.90):
				moneycheck()
		elif(flavour == "cappuccino" and cost > 1.90):
			amount = round(cost - 1.90,2) 
			print(f" Here is ${amount} dollars in change .")
			print(f"Water : {water} ml")
			print (f"Milk : {milk} ml")
			print(f"Coffee :{coffee}g")
			print("Money : $1.90")
			print(f" Here is your {flavour}.Enjoy!!")
	moneycheck()


