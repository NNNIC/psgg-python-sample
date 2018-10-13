# coding=utf-8
import StateManager
import random

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
        return

    def select_yes_or_no(self) :
        i = random.randrange(10)
        print(i)
        self.m_bYesNo = i % 2 == 0