# File:"C:\Users\psse\Desktop\Phylicia\Transmission V Distribution Study\Poland\Codes\raw_fullRun_load_reduction.py", generated on TUE, OCT 31 2017  14:46, PSS(R)E release 34.03.01
psspy.fdns([0,0,0,1,1,0,99,0])
psspy.cong(0)
psspy.conl(0,1,1,[0,0],[0.0, 100.0, 1.0, 1.0])
psspy.conl(0,1,2,[0,0],[0.0, 100.0, 1.0, 1.0])
psspy.conl(0,1,3,[0,0],[0.0, 100.0, 1.0, 1.0])
psspy.ordr(0)
psspy.fact()
psspy.tysl(0)
psspy.dyre_new([1,1,1,1],r"""C:\Users\psse\Desktop\Phylicia\Transmission V Distribution Study\Poland\poland_CLM_test_2000.dyr""","","","")
psspy.chsb(0,1,[-1,-1,-1,1,13,0])
psspy.bsys(1,0,[0.0,0.0],0,[],1,[10],0,[],0,[])
psspy.chsb(1,0,[-1,-1,-1,1,13,0])
psspy.strt_2([0,0],r"""C:\Users\psse\Desktop\Phylicia\Transmission V Distribution Study\Poland\Channels\CLM_verify.outx""")
psspy.run(0, 1.0,1,1,0)
psspy.load_chng_5(10,r"""1""",[_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,0.0,_f,_f,_f])
psspy.change_channel_out_file(r"""C:\Users\psse\Desktop\Phylicia\Transmission V Distribution Study\Poland\Channels\CLM_verify.outx""")
psspy.run(0, 1.5,1,1,0)
