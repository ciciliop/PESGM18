# File:"C:\Users\psse\Desktop\Phylicia\Load Placement Study\Test Systems\Poland\POLAND2383DYNP\Codes\RawLoadReductionBus10.py", generated on SUN, OCT 08 2017  19:06, PSS(R)E release 34.02.00
# Run a case and dynamic file to verify that it works
# Also adjust method for data collection so all is contained in the same file

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
psspy.psseinit(300000) #need to have this high, otherwise there are not enough output channels

#These four lines suppresses the output to the terminal
psspy.report_output(6,' ', [])
psspy.progress_output(6, ' ',[])
psspy.alert_output(6,' ',[])
psspy.prompt_output(6, ' ',[])

#Run Case Composite
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
psspy.dyre_new([1,1,1,1],r"""C:\Users\psse\Desktop\Phylicia\Transmission V Distribution Study\Poland\poland_CLM_full.dyr""","","","")
psspy.chsb(0,1,[-1,-1,-1,1,13,0])
psspy.strt_2([0,0],r"""C:\Users\psse\Desktop\Phylicia\Transmission V Distribution Study\Poland\Channels\CLM_verify_3.outx""")
psspy.run(0, 2.0,1,1,0)
psspy.load_chng_5(10,r"""1""",[_i,_i,_i,_i,_i,_i,_i],[_f,_f, 0.2,_f,_f,_f,_f,_f])
psspy.change_channel_out_file(r"""C:\Users\psse\Desktop\Phylicia\Transmission V Distribution Study\Poland\Channels\CLM_verify_3.outx""")
psspy.run(0, 5.0,1,1,0)