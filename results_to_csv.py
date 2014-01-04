import csv
execfile('squishvin_gen.py')
execfile('check_squishvins.py')

svins = squishvin_gen()
svins_list = check_svinlist(svins)

myfile = open('squishvin_1.csv', 'wb')
wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
for i in svins_list:
	wr.writerow(i)
