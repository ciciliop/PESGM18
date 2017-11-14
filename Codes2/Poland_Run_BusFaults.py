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
psspy.psseinit(200000) #need to have this high, otherwise there are not enough output channels

#These four lines suppresses the output to the terminal
psspy.report_output(6,' ', [])
psspy.progress_output(6, ' ',[])
psspy.alert_output(6,' ',[])
psspy.prompt_output(6, ' ',[])

#Create Load Bus Reduction Matrix, according to bus
#load_Bus = np.genfromtxt('poland_tenPercent_loads.csv',delimiter=',')
#load_Bus = [0.0159, 0.2838, 0.1304, 0.0211]
#print load_Bus
#load_bus_num = np.genfromtxt('poland_loadBuses.csv',delimiter=',')
#loadbus_volt = np.genfromtxt('loadbus_volt.csv',delimiter=',')
bus_volt = np.genfromtxt('poland_bus_volt.csv',delimiter=',')

#Run Case Composite
l=0
while l<len(bus_volt): # changing the P load at bus 1 #test just going to 2
	k = l+1
	#bus_num=int(load_bus_num[l])
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
	psspy.dyre_new([1,1,1,1],r"""C:\Users\psse\Desktop\Phylicia\Transmission V Distribution Study\Poland\CLM_test_2000.dyr""","","","")
	psspy.chsb(0,1,[-1,-1,-1,1,13,0])
	psspy.strt_2([0,0],r"""C:\Users\psse\Desktop\Phylicia\Transmission V Distribution Study\Poland\Channels\CLM\CLM_poland_BF_%d.outx""" % l)
	psspy.run(0, 2.0,1,1,0)
	psspy.dist_bus_fault(k,1, bus_volt[l],[0.0,-0.2E+10])
	psspy.change_channel_out_file(r"""C:\Users\psse\Desktop\Phylicia\Transmission V Distribution Study\Poland\Channels\CLM\CLM_poland_BF_%d.outx""" % l)
	psspy.run(0, 5.0,1,1,0)
	l = l+1

#Run Case ZIP
l=0
while l<len(bus_volt):# changing the P load at bus 1
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
	psspy.strt_2([0,0],r"""C:\Users\psse\Desktop\Phylicia\Transmission V Distribution Study\Poland\Channels\ZIP\ZIP_poland_%d.outx""" % l)
	psspy.run(0, 2.0,1,1,0)
	psspy.dist_bus_fault(k,1, bus_volt[l],[0.0,-0.2E+10])
	psspy.change_channel_out_file(r"""C:\Users\psse\Desktop\Phylicia\Transmission V Distribution Study\Poland\Channels\ZIP\ZIP_poland_%d.outx""" % l)
	psspy.run(0, 5.0,1,1,0)
	l = l+1
	
#Run Case 400only
l=0
while l<len(bus_volt): # changing the P load at bus 1
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
	psspy.dyre_new([1,1,1,1],r"""C:\Users\psse\Desktop\Phylicia\Transmission V Distribution Study\Poland\poland_FULLDYR_400kVCLM.dyr""","","","")
	psspy.chsb(0,1,[-1,-1,-1,1,13,0])
	psspy.strt_2([0,0],r"""C:\Users\psse\Desktop\Phylicia\Transmission V Distribution Study\Poland\Channels\CLM\CLM_400_poland_%d.outx""" % l)
	psspy.run(0, 2.0,1,1,0)
	psspy.dist_bus_fault(k,1, bus_volt[l],[0.0,-0.2E+10])
	psspy.change_channel_out_file(r"""C:\Users\psse\Desktop\Phylicia\Transmission V Distribution Study\Poland\Channels\ZIP\CLM_400_poland_%d.outx""" % l)
	psspy.run(0, 5.0,1,1,0)
	l = l+1
	
#Run Case 220only
l=0
while l<len(bus_volt):# changing the P load at bus 1
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
	psspy.dyre_new([1,1,1,1],r"""C:\Users\psse\Desktop\Phylicia\Transmission V Distribution Study\Poland\poland_FULLDYR_220kVCLM.dyr""","","","")
	psspy.chsb(0,1,[-1,-1,-1,1,13,0])
	psspy.strt_2([0,0],r"""C:\Users\psse\Desktop\Phylicia\Transmission V Distribution Study\Poland\Channels\CLM\CLM_220_poland_%d.outx""" % l)
	psspy.run(0, 2.0,1,1,0)
	psspy.dist_bus_fault(k,1, bus_volt[l],[0.0,-0.2E+10])
	psspy.change_channel_out_file(r"""C:\Users\psse\Desktop\Phylicia\Transmission V Distribution Study\Poland\Channels\ZIP\CLM_220_poland_%d.outx""" % l)
	psspy.run(0, 5.0,1,1,0)
	l = l+1

#Run Case 110only
l=0
while l<len(bus_volt): # changing the P load at bus 1
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
	psspy.dyre_new([1,1,1,1],r"""C:\Users\psse\Desktop\Phylicia\Transmission V Distribution Study\Poland\poland_FULLDYR_110kVCLM.dyr""","","","")
	psspy.chsb(0,1,[-1,-1,-1,1,13,0])
	psspy.strt_2([0,0],r"""C:\Users\psse\Desktop\Phylicia\Transmission V Distribution Study\Poland\Channels\CLM\CLM_110_poland_%d.outx""" % l)
	psspy.run(0, 2.0,1,1,0)
	psspy.dist_bus_fault(k,1, bus_volt[l],[0.0,-0.2E+10])
	psspy.change_channel_out_file(r"""C:\Users\psse\Desktop\Phylicia\Transmission V Distribution Study\Poland\Channels\ZIP\CLM_110_poland_%d.outx""" % l)
	psspy.run(0, 5.0,1,1,0)
	l = l+1	
	
#Run Case 110-220only
l=0
while l<len(bus_volt): # changing the P load at bus 1
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
	psspy.dyre_new([1,1,1,1],r"""C:\Users\psse\Desktop\Phylicia\Transmission V Distribution Study\Poland\poland_FULLDYR_110to220kVCLM.dyr""","","","")
	psspy.chsb(0,1,[-1,-1,-1,1,13,0])
	psspy.strt_2([0,0],r"""C:\Users\psse\Desktop\Phylicia\Transmission V Distribution Study\Poland\Channels\CLM\CLM_110220_poland_%d.outx""" % l)
	psspy.run(0, 2.0,1,1,0)
	psspy.dist_bus_fault(k,1, bus_volt[l],[0.0,-0.2E+10])
	psspy.change_channel_out_file(r"""C:\Users\psse\Desktop\Phylicia\Transmission V Distribution Study\Poland\Channels\ZIP\CLM_110220_poland_%d.outx""" % l)
	psspy.run(0, 5.0,1,1,0)
	l = l+1	

	#Run Case 110-220only
l=0
while l<len(bus_volt): # changing the P load at bus 1
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
	psspy.dyre_new([1,1,1,1],r"""C:\Users\psse\Desktop\Phylicia\Transmission V Distribution Study\Poland\poland_FULLDYR_220to400kVCLM.dyr""","","","")
	psspy.chsb(0,1,[-1,-1,-1,1,13,0])
	psspy.strt_2([0,0],r"""C:\Users\psse\Desktop\Phylicia\Transmission V Distribution Study\Poland\Channels\CLM\CLM_220400_poland_%d.outx""" % l)
	psspy.run(0, 2.0,1,1,0)
	psspy.dist_bus_fault(k,1, bus_volt[l],[0.0,-0.2E+10])
	psspy.change_channel_out_file(r"""C:\Users\psse\Desktop\Phylicia\Transmission V Distribution Study\Poland\Channels\ZIP\CLM_220400_poland_%d.outx""" % l)
	psspy.run(0, 5.0,1,1,0)
	l = l+1	

