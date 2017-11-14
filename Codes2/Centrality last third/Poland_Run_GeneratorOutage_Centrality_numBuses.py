# File:"C:\Users\psse\Desktop\Phylicia\Load Placement Study\Test Systems\Poland\POLAND2383DYNP\Codes\RawLoadReductionBus10.py", generated on SUN, OCT 08 2017  19:06, PSS(R)E release 34.02.00
# Create Disturbance data for generator outages, only do one generator outage

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

#Load Bus Information 
#bus_num = np.genfromtxt('Poland_generator_buses.csv',delimiter=',')

#Change to your PSS/e Location and set up paths
#Initialize PSSE for 50 bus case
psspy.psseinit(200000) #need to have this high, otherwise there are not enough output channels

#These four lines suppresses the output to the terminal
psspy.report_output(6,' ', [])
psspy.progress_output(6, ' ',[])
psspy.alert_output(6,' ',[])
psspy.prompt_output(6, ' ',[])

#Run Cases
for i in range(2):
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
	if i ==0:
		psspy.dyre_new([1,1,1,1],r"""C:\Users\psse\Desktop\Phylicia\Transmission V Distribution Study\Poland\poland_FULLDYR_2_3_4thquartile.dyr""","","","")
	if i ==1:
		psspy.dyre_new([1,1,1,1],r"""C:\Users\psse\Desktop\Phylicia\Transmission V Distribution Study\Poland\poland_FULLDYR_3_4thquartile.dyr""","","","")
	psspy.chsb(0,1,[-1,-1,-1,1,13,0])
	psspy.strt_2([0,0],r"""C:\Users\psse\Desktop\Phylicia\Transmission V Distribution Study\Poland\Channels\Centrality\poland_45_num_%d.out""" %i)
	psspy.run(0, 1.0,1,1,0)
	psspy.machine_chng_2(45,r"""1""",[0,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f]) #45 was first, 105 next
	psspy.change_channel_out_file(r"""C:\Users\psse\Desktop\Phylicia\Transmission V Distribution Study\Poland\Channels\Centrality\poland_45_num_%d.out""" %i)
	psspy.run(0, 10.0,1,1,0)
	psspy.delete_all_plot_channels()
	
	#Gather the data
	chnfobj = dyntools.CHNF('C:\Users\psse\Desktop\Phylicia\Transmission V Distribution Study\Poland\Channels\Centrality\poland_45_num_%d.out' %i)
	d,e,z=chnfobj.get_data() #gathering data from data in dictionary format
	j=1
	while j<2383:#for j in range(2383):#key in z:	
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
	filename = "Test_45_num_%d.csv" % i #there will be an excel file for every load bus change
	np.savetxt(filename,all,delimiter=",") 		