# coding=utf-8

class StateManager:
    m_curfunc  = None
    m_nextfunc = None

    def Update(self) :
        bFirst = False
        if self.m_nextfunc != None :
            self.m_curfunc = self.m_nextfunc
            self.m_nextfunc = None
            bFirst = True

        if self.m_curfunc != None :
            self.m_curfunc(bFirst)
        return

    def Goto(self,st) :
        self.m_nextfunc = st
        return

    def CheckState(self, st) :
        return self.m_curfunc == st


class TestControl(StateManager) :
    def br_YES(self,st) :
        return
    
        
class TestControl_created(TestControl) :

    def S_START(self,bFirst) :
        if (bFirst) :
            print("S_START")
            self.Goto(self.S_END)
        return


    def S_END(self,bFirst) :
        if (bFirst) :
            print("S_END")
        return

    def Start(self) :
        self.Goto(self.S_START)
        return
    
    def IsEnd(self) :
        return self.CheckState(self.S_END)

print("Hello!")

sm = TestControl_created()
sm.Start()
while(sm.IsEnd()==False) :
    sm.Update()

print("Bye")

        
    
        
