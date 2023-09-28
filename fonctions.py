def puissance(a,b):
	if not type(a) is int:
		raise TypeError("Only integers are allowed")
	if not type(b) is int:
		raise TypeError("Only integers are allowed")
	
	var = 1
	if b<0:
	 b = b*-1
	 for i in range(b):
	    var = var*a
	    print(var)
	 return 1/var
	
	   
	else:
	 for i in range(b):
	    var = var*a
	    print(var)
	 return var
	
	if not type(var) is int:
		raise TypeError("Only integers are allowed")
		
	if a == 0 and b < 0:
		raise TypeError("La puissance de 0 ne peut pas être défini par un nombre négatif")
	
	

print(puissance(2,-3))
	
	
		
	
	
	
