#!/usr/bin/python

i = 1

for i in xrange(10):

	name = i
	ff = open("file_{0:02d}.dat".format(i),'w')
	f = open('%s.csv' % name, 'wb')
	print i
	s= str(i)
	f.write(s)
	f.write("text")
	ff.write(s)
	ff.write("text")
f.close()
ff.close()