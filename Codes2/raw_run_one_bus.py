# File:"C:\Users\psse\Desktop\Phylicia\Transmission V Distribution Study\Poland\Codes2\raw_run_one_bus.py", generated on TUE, NOV 14 2017  10:00, PSS(R)E release 34.03.01
psspy.case(r"""C:\Users\psse\Desktop\Phylicia\Transmission V Distribution Study\Poland\POLAND2383DYNP.sav""")
psspy.fdns([0,0,0,1,1,0,99,0])
psspy.cong(0)
psspy.conl(0,1,1,[0,0],[0.0, 100.0, 1.0, 1.0])
psspy.conl(0,1,2,[0,0],[0.0, 100.0, 1.0, 1.0])
psspy.conl(0,1,3,[0,0],[0.0, 100.0, 1.0, 1.0])
psspy.ordr(1)
psspy.fact()
psspy.tysl(1)
psspy.dyre_new([1,1,1,1],r"""C:\Users\psse\Desktop\Phylicia\Transmission V Distribution Study\Poland\poland_ZIP.dyr""","","","")
psspy.bsys(1,0,[0.0,0.0],0,[],1,[10],0,[],0,[])
psspy.chsb(1,0,[-1,-1,-1,1,13,0])
psspy.chsb(1,0,[-1,-1,-1,1,16,0])