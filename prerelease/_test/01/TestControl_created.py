# coding=utf-8
import TestControl

class TestControl_created(TestControl.TestControl) :
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
