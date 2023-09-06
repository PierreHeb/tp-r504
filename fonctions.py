def puissance(a,b):
	var = a
	for i in range(b):
	   var = var *(a*b)
	return var
	if not type(var) is int:
		raise TypeError("Only integers are allowed")
	
	
	
