@echo off

echo Activating Virtual Environment...

call ..\myselenium\Scripts\activate

echo Running DemoBlaze Test File...

pytest Tests/test_demo.py -v -s

pause