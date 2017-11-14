# File:"C:\Users\psse\Desktop\Phylicia\Load Placement Study\Test Systems\Poland\POLAND2383DYNP\Codes\RawLoadReductionBus10.py", generated on SUN, OCT 08 2017  19:06, PSS(R)E release 34.02.00
# Collect disturbance data for load reduction at all buses in the system when using ZIP and composite load models

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


#Change to your PSS/e Location and set up paths
#Initialize PSSE for 50 bus case
psspy.psseinit(150000) #need to have this high, otherwise there are not enough output channels

#These four lines suppresses the output to the terminal
psspy.report_output(6,' ', [])
psspy.progress_output(6, ' ',[])
psspy.alert_output(6,' ',[])
psspy.prompt_output(6, ' ',[])

#Create Load Bus Reduction Matrix, according to bus
load_Bus = np.genfromtxt('poland_tenPercent_loads.csv',delimiter=',')
#load_Bus = [0.0159, 0.2838, 0.1304, 0.0211]
#print load_Bus

#Run Case Composite
l=0
while l<len(load_Bus): # changing the P load at bus 1
	k = l+1
	psspy.case(r"""C:\Users\psse\Desktop\Phylicia\Transmission V Distribution Study\Poland\POLAND2383DYNP.sav""")
	psspy.fdns([0,0,0,1,1,0,99,0])
	psspy.cong(0)
	psspy.conl(0,1,1,[0,0],[ 100.0,0.0,0.0, 100.0])
	psspy.conl(0,1,2,[0,0],[ 100.0,0.0,0.0, 100.0])
	psspy.conl(0,1,3,[0,0],[ 100.0,0.0,0.0, 100.0])
	psspy.fact()
	psspy.ordr(0)
	psspy.fact()
	psspy.tysl(0)
	psspy.dyre_new([1,1,1,1],r"""C:\Users\psse\Desktop\Phylicia\Transmission V Distribution Study\Poland\poland_CLM_test_2000.dyr""","","","")
	psspy.chsb(0,1,[-1,-1,-1,1,13,0])
	psspy.strt_2([0,0],r"""C:\Users\psse\Desktop\Phylicia\Transmission V Distribution Study\Poland\Channels\CLM_poland_%d.outx""" % l)
	psspy.run(0, 2.0,1,1,0)
	psspy.load_chng_5(k,r"""1""",[_i,_i,_i,_i,_i,_i,_i],[_f,_f, load_Bus[l],_f,_f,_f,_f,_f])
	psspy.change_channel_out_file(r"""C:\Users\psse\Desktop\Phylicia\Transmission V Distribution Study\Poland\Channels\CLM_poland_%d.outx""" % l)
	psspy.run(0, 5.0,1,1,0)

	#Gather the data
	data = dyntools.CHNF(r"C:\Users\psse\Desktop\Phylicia\Transmission V Distribution Study\Poland\Channels\CLM_poland_%d.outx" % l) #getting data from channel.out file
	d,e,z=data.get_data() #gathering data from data in dictionary format
	j=1
	for key in z:
		v = z[key]
		new_v = ", ".join(str(i) for i in v) #this removes the brackets at the beginning and end of the list so can be processed in matlab 
		a = np.matrix(new_v)#try to make it into a matrix in python
		if j ==1:
			all = a
		elif j<2384: #changed from else so time is not included
			all = np.concatenate((all,a),axis=1)#concatenates horizontally
		j = j+1
	#Add together to one giant matrix
	if l==0:
		total=all
	else:
		total = np.concatenate((total,all),axis=0) #concatenate vertically
	l=l+1				
	psspy.delete_all_plot_channels()
	
#Output to CSV
#Data Key: |Load Change Bus|All Data...|	concatenates vertically for each load change bus
filename = "LoadReduction_CLM_poland.csv"
np.savetxt(filename,total,delimiter=",") 

	
#Run Case ZIP
l=0
while l<len(load_Bus): # changing the P load at bus 1
	k = l+1
	psspy.case(r"""C:\Users\psse\Desktop\Phylicia\Transmission V Distribution Study\Poland\POLAND2383DYNP.sav""")
	psspy.fdns([0,0,0,1,1,0,99,0])
	psspy.cong(0)
	psspy.conl(0,1,1,[0,0],[ 100.0,0.0,0.0, 100.0])
	psspy.conl(0,1,2,[0,0],[ 100.0,0.0,0.0, 100.0])
	psspy.conl(0,1,3,[0,0],[ 100.0,0.0,0.0, 100.0])
	psspy.fact()
	psspy.ordr(0)
	psspy.fact()
	psspy.tysl(0)
	psspy.dyre_new([1,1,1,1],r"""C:\Users\psse\Desktop\Phylicia\Transmission V Distribution Study\Poland\poland_ZIP.dyr""","","","")
	psspy.chsb(0,1,[-1,-1,-1,1,13,0])
	psspy.strt_2([0,0],r"""C:\Users\psse\Desktop\Phylicia\Transmission V Distribution Study\Poland\Channels\ZIP_poland_%d.outx""" % l)
	psspy.run(0, 2.0,1,1,0)
	psspy.load_chng_5(k,r"""1""",[_i,_i,_i,_i,_i,_i,_i],[_f,_f, load_Bus[l],_f,_f,_f,_f,_f])
	psspy.change_channel_out_file(r"""C:\Users\psse\Desktop\Phylicia\Transmission V Distribution Study\Poland\Channels\ZIP_poland_%d.outx""" % l)
	psspy.run(0, 5.0,1,1,0)

	#Gather the data
	data = dyntools.CHNF(r"C:\Users\psse\Desktop\Phylicia\Transmission V Distribution Study\Poland\Channels\ZIP_poland_%d.outx" % l) #getting data from channel.out file
	d,e,z=data.get_data() #gathering data from data in dictionary format
	j=1
	for key in z:
		v = z[key]
		new_v = ", ".join(str(i) for i in v) #this removes the brackets at the beginning and end of the list so can be processed in matlab 
		a = np.matrix(new_v)#try to make it into a matrix in python
		if j ==1:
			all = a
		elif j<2384: #changed from else so time is not included
			all = np.concatenate((all,a),axis=1)#concatenates horizontally
		j = j+1
	#Add together to one giant matrix
	if l==0:
		total=all
	else:
		total = np.concatenate((total,all),axis=0) #concatenate vertically
	l=l+1				
	psspy.delete_all_plot_channels()
	
#Output to CSV
#Data Key: |Load Change Bus|All Data...|	concatenates vertically for each load change bus
filename = "LoadReduction_ZIP_poland.csv"
np.savetxt(filename,total,delimiter=",") 


