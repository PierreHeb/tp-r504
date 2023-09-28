def puissance(a,b):
	if not type(a) is int:
		raise TypeError("Only integers are allowed")
	if not type(b) is int:
		raise TypeError("Only integers are allowed")
	if a == 0 and b < 0:
		raise ValueError("La puissance de 0 ne peut pas être défini par un nombre négatif")
		
		
	var = 1
	for i in range(b):
	    var = var*a
	    print(var)
	if b<0:
	 return 1/var
	 
	else:
	 return var
	
	
	
	

	
	
		
	
	
	
