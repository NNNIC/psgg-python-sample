# coding=utf-8
import StateManager

class TestControl(StateManager.StateManager) :
    m_bYesNo = False
    def br_YES(self,st) :
        if self.HasNextState()==False :
            if self.m_bYesNo==True :
                self.SetNextState(st)
        return

    def br_NO(self,st) :
        if self.HasNextState()==False :
            if self.m_bYesNo==False :
                self.SetNextState(st)

#write your code here

