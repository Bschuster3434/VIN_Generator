import itertools

### Project to create a series of VIN numbers given a final 5 digit code

def squishvin_gen():
	## Stable Digits Below. These will not change between versions
	dig_1_3 = ['5YJ'] ## WMI
	dig_4 = ['S', 'R'] #Line and Series
	dig_5 = ['A', 'B', 'C','D'] #Body Type
	dig_6 = ['1', '2'] #Restraint System
	dig_7 = ['A', 'B', 'C', 'D', 'H'] #Charger Type
	dig_8 = ['1','2','C', 'G', 'N', 'P'] #Motor/Drive Unit
	## Check digit is not used in SquishVIN
	dig_10 = ['C', 'D', 'E'] #Model Year
	dig_11 = ['F', 'P'] #Plant Manufacture
	
	#Create string list of all combinations of the possible VIN
	comb = [dig_1_3, dig_4, dig_5, dig_6, dig_7, dig_8, dig_10, dig_11]
	vin_tuples = list(itertools.product(*comb))
	vin_list = []
	for i in vin_tuples:
		joined = ''.join(i)
		vin_list.append([list(i), joined])
	
	return vin_list

