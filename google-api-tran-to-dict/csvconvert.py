#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      nmallow
#
# Created:     03/04/2013
# Copyright:   (c) nmallow 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import sys, os.path, re, csv
from datetime import date


#Tell me what file to use
#Imports a csv file exports it as a dict object to file specified
#file get phase from google API
#file write phase

FILE_IN = 'api.csv'#'A3_Strings_v0.0.1 - Main.csv'
FILE_OUT = 'string_to_dict_%s.txt ' % date.today()


KEYCOL_KEY = 'tagcode'
AVAILABLE_LCID = ['en-us','en-ca','en-gb']
KEYCOL_DEFAULT = 'en-us'
KEYCOL_USE = ''


def determine_loc(rec=False,value=None):
    global KEYCOL_USE
    if rec == True:
        print 'The value you have entered was invalid, Please try again.\n'

    #build array string value
    output_str = ''
    for k,v in enumerate(AVAILABLE_LCID):
        output_str = ''.join([output_str,"[%d:%s]," % (k,v)])


    loc = raw_input("Available translations: \n%s\n Enter a number or press 'enter' to use default '%s' " % (output_str,KEYCOL_DEFAULT,))

    item = loc if loc else KEYCOL_DEFAULT


    try:
        KEYCOL_USE = AVAILABLE_LCID[int(item)]
    except IndexError:
        determine_loc(True)
    except ValueError:
        if KEYCOL_DEFAULT == item:
            KEYCOL_USE = KEYCOL_DEFAULT
        else:
            determine_loc(True)

    return

def csv_to_txt(infile, delimiter=","):

    #choose column
    determine_loc()

    #run run run
    result = {}
    reader = csv.reader(infile, delimiter=delimiter)

    #First row contains the headings
    headings = reader.next()
    headings = reader.next()
    headings = reader.next()
    headings = reader.next()

    #Remove whitespace and make lower-case
    for i, v in enumerate(headings):
        headings[i] = re.sub(r'\s', '', v.lower())
        headings[i] = headings[i].replace('#', '')

    #Create dictionaries for each row
    reader = csv.DictReader(infile, headings)

    text_file = open(FILE_OUT,"w")

    text_file.writelines('{\n')
    for row in reader:
        text_file.writelines(str('"'+row[KEYCOL_KEY]+'"="'+row[KEYCOL_USE]+ '",\n'))
        #result[row['tagcode']]=row['value']
    text_file.writelines('}')


def request_input():
    doc = raw_input("Please input the filename you wish to parse or press 'enter' to use default '%s' " % FILE_IN)
    try:
        file = doc if doc else FILE_IN
        validate_input(file)
    except KeyboardInterrupt, e:
        return
    return FILE_OUT


def validate_input(fname):
    #check to make sure file is in the root
    if os.path.isfile(fname):
        try:
            run_import(fname)
        except IOError:
            print 'IO Error'
    else:
        print fname , " Doesn't Exists"



def run_import(fname):
    f = open(fname)
    csv_to_txt(f)

    #print 'Operation finished'




