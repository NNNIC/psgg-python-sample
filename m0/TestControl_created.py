#  psggConverterLib.dll converted from TestControl.xlsx. 
# coding=utf-8
import TestControl

class TestControl_created(TestControl.TestControl) :


    #    S_START
    #
    def S_START(self,bFirst) :
        if self.HasNextState()==False :
            self.SetNextState(self.S_SAY_HELLO)
        if self.HasNextState() :
            self.GoNextState()
    #    S_END
    #
    def S_END(self,bFirst) :
        if self.HasNextState() :
            self.GoNextState()
    #    S_SAY_HELLO
    #    Say Hello!
    def S_SAY_HELLO(self,bFirst) :
        if (bFirst) :
            print("Hello")
        if self.HasNextState()==False :
            self.SetNextState(self.S_SELECT)
        if self.HasNextState() :
            self.GoNextState()
    #    S_SELECT
    #    Select Yes or NO
    def S_SELECT(self,bFirst) :
        if (bFirst) :
            self.select_yes_or_no()
        self.br_YES(self.S_YES)
        self.br_NO(self.S_NO)
        if self.HasNextState() :
            self.GoNextState()
    #    S_YES
    #    Say YES
    def S_YES(self,bFirst) :
        if (bFirst) :
            print("YES")
        if self.HasNextState()==False :
            self.SetNextState(self.S_END)
        if self.HasNextState() :
            self.GoNextState()
    #    S_NO
    #    Say NO
    def S_NO(self,bFirst) :
        if (bFirst) :
            print("NO")
        if self.HasNextState()==False :
            self.SetNextState(self.S_END)
        if self.HasNextState() :
            self.GoNextState()


    def Start(self) :
        self.Goto(self.S_START)
        return

    def IsEnd(self) :
        return self.CheckState(self.S_END)

