temp = input("what is the temp in celcius")
temp = float(temp)
isfreezing = temp <= 0.0
isnormal = temp < 100.0 and temp > 0.0
isgas = temp > 100.0
if(isfreezing):
	print("ice")
elif(isnormal):
	print("water")
elif(isgas):
	print("gas")
