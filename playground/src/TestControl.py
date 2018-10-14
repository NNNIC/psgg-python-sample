# coding=utf-8
from time import sleep

class TestControl :

    # public
    def Start(self) :
        self.Goto(self.S_START)
        return
    
    def IsEnd(self) :
        return self.CheckState(self.S_END)

    # Manager
    m_curfunc  = None
    m_nextfunc = None

    m_noWait = False

    def Update(self) :
        while(True) :
            bFirst = False
            self.m_noWait = False
            if self.m_nextfunc != None :
                self.m_curfunc = self.m_nextfunc
                self.m_nextfunc = None
                bFirst = True

            if self.m_curfunc != None :
                self.m_curfunc(bFirst)
            
            if self.m_noWait == False :
                return

    def Goto(self,st) :
        self.m_nextfunc = st
        return

    def CheckState(self, st) :
        return self.m_curfunc == st

    def HasNextState(self) :
        return self.m_nextfunc != None

    def NoWait(self) :
        self.m_noWait = True

    # [SYN-G-GEN OUTPUT START] indent(4) $/./$
#  psggConverterLib.dll converted from TestControl.xlsx. 
    #    E_0005
    #
    counter=0
    #    S_0001
    #
    def S_0001(self,bFirst) :
        a=3
        if a==1 :
            self.Goto( self.S_0002 )
        elif a==2 :
            self.Goto( self.S_0003 )
        else :
            self.Goto( self.S_0004 )
        return
    #    S_0002
    #
    def S_0002(self,bFirst) :
        if (bFirst) :
            print('S_0002')
        if self.HasNextState()==False :
            self.Goto(self.S_NEXTPROC)
        return
    #    S_0003
    #
    def S_0003(self,bFirst) :
        if (bFirst) :
            print('S_0003')
        if self.HasNextState()==False :
            self.Goto(self.S_NEXTPROC)
        return
    #    S_0004
    #
    def S_0004(self,bFirst) :
        if (bFirst) :
            print('S_0004')
        if self.HasNextState()==False :
            self.Goto(self.S_NEXTPROC)
        return
    #    S_0006
    #    Count 10
    def S_0006(self,bFirst) :
        if (bFirst) :
            self.counter = 0
        sleep(0.1)
        self.counter += 1
        print(self.counter)
        if self.counter < 10 :
            return
        if self.HasNextState()==False :
            self.Goto(self.S_0007)
        return
    #    S_0007
    #
    def S_0007(self,bFirst) :
        if (bFirst) :
            print('1 sec elapsed.')
        if self.HasNextState()==False :
            self.Goto(self.S_END)
        return
    #    S_END
    #
    def S_END(self,bFirst) :
        return
    #    S_NEXTPROC
    #
    def S_NEXTPROC(self,bFirst) :
        if self.HasNextState()==False :
            self.Goto(self.S_0006)
        return
    #    S_START
    #
    def S_START(self,bFirst) :
        if self.HasNextState()==False :
            self.Goto(self.S_0001)
        return


    # [SYN-G-GEN OUTPUT END]

    m_bYesNo = False
    def br_YES(self,st) :
        if self.HasNextState()==False :
            if self.m_bYesNo==True :
                self.Goto(st)
        return

    def br_NO(self,st) :
        if self.HasNextState()==False :
            if self.m_bYesNo==False :
                self.Goto(st)

