transliteration ={'A': 1,
'B': 2,
'C': 3,
'D': 4,
'E': 5,
'F': 6,
'G': 7,
'H': 8,
'I': 0,
'J': 1,
'K': 2,
'L': 3,
'M': 4,
'N': 5,
'O': 0,
'P': 7,
'Q': 0,
'R': 9,
'S': 2,
'T': 3,
'U': 4,
'V': 5,
'W': 6,
'X': 7,
'Y': 8,
'Z': 9,
'0': 0,
'1': 1,
'2': 2,
'3': 3,
'4': 4,
'5': 5,
'6': 6,
'7': 7,
'8': 8,
'9': 9
}

weight  = { '1': 8,
'2': 7,
'3': 6,
'4': 5,
'5': 4,
'6': 3,
'7': 2,
'8': 10,
'9': 0,
'10': 9,
'11': 8,
'12': 7,
'13': 6,
'14': 5,
'15': 4,
'16': 3,
'17': 2
}

def check_num(vin): #Finds the check number of a VIN
	vin_list = list(vin)
	place = 1
	total = 0
	for i in vin_list:
		current_value = (transliteration[i] * weight[str(place)])
		total = total + current_value
		place = place + 1
	check_num = total%11
	return check_num
	
####print check_num('5YJSA1DP0CFP01241') #test script
	
	
	
	

	