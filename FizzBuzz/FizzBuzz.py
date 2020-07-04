# coding=utf-8

from FizzBuzzControl import FizzBuzzControl

sm = FizzBuzzControl()
sm.Start()

while(sm.IsEnd()==False) :
    sm.Update()

