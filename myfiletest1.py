#!/usr/bin/python

i = 1

#	f = open("file_{0:02d}.dat".format(i),'w')

for i in xrange(10):
   with open('file_{0}.dat'.format(i),'w') as f:
   	   f.write ("file")
#      f.write(str(i))
       f.close()
	