#!/usr/bin/python



f = open('workfile1', 'w')

myList=['GEO_8245.JPG','GEO_8246.JPG','GEO_8248.JPG','GEO_8249.JPG','GEO_8252.JPG','GEO_8254.jpg','GEO_8274.jpg','GEO_8286.jpg','GEO_8287.JPG','GEO_8307.JPG','GEO_8313.JPG']



i = 0
while i < len(myList):

	print myList[i]

	fil = myList[i]

	f.write ('<td><a href="full/')
	f.write (fil)
	f.write ('"><img src="')
	f.write (fil)
	f.write ('" alt="')
	f.write (fil)
	f.write ('" /></a></td>')
	f.write ('\n')
 
	if (i+1)%5==0: f.write ('</tr><tr>\n')
	i = i + 1
f.closed