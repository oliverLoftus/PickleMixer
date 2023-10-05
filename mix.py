def mix(V,T):
	#V=Volume
	#T=Target Concentration
	
	tl = 3 #Tolerance
	a = 24 #Stronger Concentration
	b = 5  #Weaker Concentration
	
	c = a-b #Range
	x = (T-b)/c #Solve
	y = round(V*x,tl) #Amount of a
	z = round(V-y,tl) #Amount of b

	print(f'{V}ml at {T}% strength is:')
	print(f'{y}ml of {a}% acid,')
	print(f'and {z}ml of {b}% vinegar.')
		
#start
mix(1000,7) #enter desired volume (ml) and concentration (%) here.
