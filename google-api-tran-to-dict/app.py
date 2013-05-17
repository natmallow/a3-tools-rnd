#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      nmallow
#
# Created:     15/05/2013
# Copyright:   (c) nmallow 2013
# Licence:     WTFC
#-------------------------------------------------------------------------------


import csvconvert, goapi as apigo, os


def main():
    go_goapi()
    f = go_convert()
    showinnotepad(f)
"""
This is the controller
"""
#import the file
def go_goapi():
    apigo.main()
    pass

#convert the file
def go_convert():
    f = csvconvert.request_input()
    return f
    pass

#open the file
def showinnotepad(fo):
    print fo
    os.system('notepad.exe ' + fo)




if __name__ == '__main__':
    main()
