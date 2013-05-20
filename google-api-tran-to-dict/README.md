The purpose of this app is to import from a multi column spreadsheet from google drive is for a file that looks like this:

The spreadsheet:
col[0] : UID  
col[1] : Group (future proofing)  
col[2] : key  
col[3] : en-us (value)  
col[4] : another language local (value)  

EXPEXTED RESULTS:
{<key>: <en-us>(values based on local default en-us)} 
ie.
    {  
    "COMMON_YES": "Yes",  
    "COMMON_NO": "No",  
    "COMMON_TO": "to",  
    "COMMON_ON": "on",  
    'ERR_CRITICAL': 'System Error! Please try again later.',  
    'ERR_BID_MAIN': 'Bidding Failed! %s Please try again.',  
    'ERR_BID_GENERIC': '',  
    'ERR_LOGIN_INVALID_PASSWORD': 'Email address/password is invalid. Please try again.',  
    ...  
    }  
  
TODO: Create a user select based on the available locals   
TODO: Create a grouping output   

SETUP:  
REQ: Python 2.7  
