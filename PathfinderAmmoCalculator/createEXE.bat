@echo off
cd C:\Users\Adamm\.spyder-py3\Projects\DND\Ammo_Calc
echo running command pyinstaller AmmoCalculator.py -F -w
pyinstaller AmmoCalculator.py -F -w
echo Success!
pause