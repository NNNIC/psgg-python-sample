@echo off
echo : 
echo : del doc\*.* and src\*.* then copy ref\test.py to src
echo :
echo : continue?
pause
del /q doc\*.*
del /q src\*.*
copy ref\Test.py src\*.*
pause
