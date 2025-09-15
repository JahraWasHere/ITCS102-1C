temperature = eval(input("Hello! What's the temperature outside? --> "))

if temperature <=0 :
	print("You must be a block of ice by now, it's Freezing")
elif temperature >= 1 and temperature <=20 :
	print("Wow, That's Extremely Cold bro")
elif temperature >= 21 and temperature <=30 :
	print("It's getting Moderately Cold in there")
elif temperature >=31 and temperature <=37 :
	print("Eh, It's Normal, I'd say Lukewarm")
elif temperature >=38 and temperature <=45 :
	print("It's getting a bit Hot in there, huh?")
elif temperature >=46 and temperature <=50 :
	print("Try cooking an Egg in there, It's Boiling Hot")
elif temperature >=51 :
	print("HOW ARE YOU ALIVE?!")
	
else :
	print("Bruh")
