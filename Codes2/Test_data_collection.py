# File:"C:\Users\psse\Desktop\Phylicia\Load Placement Study\Test Systems\Poland\POLAND2383DYNP\Codes\RawLoadReductionBus10.py", generated on SUN, OCT 08 2017  19:06, PSS(R)E release 34.02.00
# Test data collection methods

from __future__ import division
from collections import defaultdict
import os,sys

#Change to your PSS/e Location and set up paths
sys.path.append(r"C:\Program Files (x86)\PTI\PSSE34\PSSPY27") #Give the path to PSSBIN to imoport psspy
sys.path.append(r"C:\Program Files (x86)\PTI\PSSE34\PSSBIN")
sys.path.append(r"C:\Program Files (x86)\PTI\PSSE34\PSSLIB")
sys.path.append(r"C:\Program Files (x86)\PTI\PSSE34\EXAMPLE")
os.environ['PATH'] = (r"C:\Program Files (x86)\PTI\PSSE34\PSSPY27;" + r"C:\Program Files (x86)\PTI\PSSE34\PSSBIN;" + r"C:\Program Files (x86)\PTI\PSSE34EXAMPLE;" + os.environ['PATH'])
import psse34 #addition necessary for new version 34
import psspy
import pssarrays
import redirect
import dyntools
import pssplot
#import pssexcel
import random
import copy
import math
import multiprocessing
import time
import sys
import csv
import numpy as np
#import matplotlib
_i=psspy.getdefaultint()
_f=psspy.getdefaultreal()
_s=psspy.getdefaultchar()
redirect.psse2py()


#Gather the data
chnfobj = dyntools.CHNF('C:\Users\psse\Desktop\Phylicia\Transmission V Distribution Study\Poland\Channels\ZIP\poland_test.out' )
d,e,z=chnfobj.get_data() #gathering data from data in dictionary format
j=1
while j<2384: #This makes sure it is all indexed by 1 and there is no time recorded			#for j in range(2383):#key in z:	
	v = z[j]
	new_v = ", ".join(str(i) for i in v) #this removes the brackets at the beginning and end of the list so can be processed in matlab 
	a = np.matrix(new_v)#try to make it into a matrix in python
	if j ==1:
		all = a
	elif j<2384: #changed from else so time is not included
		all = np.concatenate((all,a),axis=0)#concatenates vertically
	j = j+1
#Output to CSV
#Data Key: |Load Change Bus|All Data...|	concatenates vertically for each load change bus
filename = "Test_timeorder.csv"  #there will be an excel file for every load bus change
np.savetxt(filename,all,delimiter=",") 
	

#Gather the data
#chnfobj = dyntools.CHNF('C:\Users\psse\Desktop\Phylicia\Transmission V Distribution Study\Poland\Channels\ZIP\poland_1.out')
#d,e,z=chnfobj.get_data() #gathering data from data in dictionary format
#print(d) # title
#print(e)
#keys
##j=1
##for key in z:
##	v = z[key]
##	new_v = ", ".join(str(i) for i in v) #this removes the brackets at the beginning and end of the list so can be processed in matlab 
##	a = np.matrix(new_v)#try to make it into a matrix in python
##	if j ==1:
##		all = a
##	elif j<2384: #changed from else so time is not included
##		all = np.concatenate((all,a),axis=0)#concatenates vertically
##	j = j+1
	#Output to CSV
	#Data Key: |Load Change Bus|All Data...|	concatenates vertically for each load change bus
##	j = j+1

##filename = "Test_%d.csv" % j #there will be an excel file for every load bus change
##np.savetxt(filename,all,delimiter=",") 	
	
#outfile = 'C:\Users\psse\Desktop\Phylicia\Transmission V Distribution Study\Poland\Channels\ZIP\ZIP_poland_1.out'
#channels = 0
#show = True
#xlsfile = 'test.xlsx'
#chnfobj.xlsout(outfile,channels,show,xlsfile)	