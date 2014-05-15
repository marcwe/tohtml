#!/usr/bin/python

i = 0

fin = open('/usr/share/nginx/www/phpdata.txt', 'r')
foutlog = open('phpfileslog.txt' , 'w')
fout = open('phpfiles.txt' , 'w')
foutneedswork = open('needswork.txt' , 'w')

#line = fo.readlines()
#print "Read Line: %s" % (line)
#i = i+1
#print "i %s" % i

flist = fin.readlines()
print flist[2]

for i in range(len(flist)):
	print  "i %s" % i
	print flist[i]
	row = flist[i].split("??")
	for y in range(len(row)):
		print "write Line: %s" % row[y]
		print y; print "y \n"
		print "\n"
	print len(row); print "len \n"
	print min(row); print "min \n"
	print max(row); print "max \n"
	lenr = len(row)
#	foutlog.write (str(lenr));
	foutlog.write ("new row ")
	foutlog.write (str(i))
	foutlog.write ("\n")
	foutlog.write (str(len(row))); foutlog.write("len \n") 
	foutlog.write (str(min(row))); foutlog.write("min \n")
	foutlog.write (str(row[0])); foutlog.write("row 0 \n")
#	if len(row) == 5:
#		fout.write (str(row[0])); fout.write("row 0 \n")
#		fout.write (str(row[1])); fout.write("row 1 \n")
	if (len(row) == 5 or len(row) ==6):
		lenminus2 = len(row)-2
		fout.write (str(row[0])); fout.write("??http://mobi-1.pcom.edu/")
		fout.write (str(row[1])); fout.write("??")
		fout.write (str(row[lenminus2]))
		fout.write("\n")
	if len(row) > 2:
		foutlog.write (str(row[1])); foutlog.write("row 1 \n")
		lenminus2 = len(row)-2
		foutlog.write (str(row[lenminus2])); foutlog.write("len-2 \n")
		lenminus1 = len(row)-1
		foutlog.write (str(row[lenminus1])); foutlog.write("len-1 \n") 
		if (len(row) < 5 or len(row) >6):
			k = 0
			for k in range(len(row)):
				foutneedswork.write (str(row[k])); foutneedswork.write("\n")
	foutlog.write (str(max(row))); foutlog.write("max \n") 
#	print flist[i],
	
	

#for line in fin:
#	print line,
foutneedswork.close()
fout.close()
foutlog.close()
fin.close()
#foutlog.closed
#fin.closed

