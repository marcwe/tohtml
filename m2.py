#!/usr/bin/python

#Created by Erin Bailey, 7/8/2013 for Marc Wertheimer, both members of the Philadelphia College of Osteopathic Medicine MIS department.

f = open('workfile', 'w')

j=0
i=0
fullrow = ''

links = raw_input('Enter data here:') 
splitlinks = links.split('", "')
print splitlinks

k=0
for i in splitlinks:
	k = k + 1
	print k
	f.write(k/n)
#	f.write('/n')
	print '<td><a href="full/', i, '"><img src="', i, '" alt="', i, '" /></a></td>'
	
	f.write('hi')
	f.write ('<td><a href="full/')
	f.write (i)
	f.write ('"><img src="')
	f.write (i)
	f.write ('" alt="')
	f.write (i)
	f.write ('" /></a></td>'/n)
	
	
	if j == 5:
		print '</tr>'
		print '<tr>'
		j = 0
	j = j + 1	
	f.closed