def cel_to_fahr(C):
	F = ((5/9.0)*C)+32
	return F
def fahr_to_cel(F):
	C = (F-32)/(5/9.0)
	return C
def checkConverter(F):
	if a==cel_to_fahr(fahr_to_cel(F)):
		print ("True")
	else:
		print ("False")
a=float(raw_input("Give Fahrenheit \n"))
checkConverter(a)
