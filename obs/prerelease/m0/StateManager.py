# coding=utf-8

class StateManager:
    m_curfunc  = None
    m_nextfunc = None
    m_tempfunc = None

    m_noWait = False

    def Update(self) :
        while(True) :
            bFirst = False
            self.m_noWait = False;
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

    def SetNextState(self, st) :
        self.m_tempfunc = st
        return;

    def GoNextState(self) :
        self.m_nextfunc = self.m_tempfunc
        self.m_tempfunc = None
        return

    def HasNextState(self) :
        return self.m_tempfunc != None

    def NoWait(self) :
        self.m_noWait = True

