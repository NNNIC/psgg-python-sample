# coding=utf-8

from TestControl_created import TestControl_created

sm = TestControl_created()
sm.Start();

while(sm.IsEnd()==False) :
    sm.Update()

