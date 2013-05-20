* **Overview**
  - Google-api-tran-to-dict: Imports a shared spreadsheet doc as a dictionary.

* **Getting Started**
  - 
  -
* **Example Usage**
* **Design Goals**
* **Detailed Usage**
* **Developer info**
* **Colophon**  
 


The spreadsheet:
col[0] : UID  
col[1] : Group (future proofing)  
col[2] : key  
col[3] : en-us (value)  
col[4] : another language local (value)  

EXPECTED RESULTS:
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
REQ:  
<a href="http://http://www.python.org/getit/releases/2.7/" target="_blank">Python 2.7 `External Link`</a>,  
<a href="https://code.google.com/p/httplib2/" target="_blank">httplib2 External Link</a>, <a href="https://github.com/natmallow/a3-tools-rnd/blob/master/libs/httplib2-0.8.zip" target="_blank">httplib2 (httplib2-0.8.zip)</a>,  
<a href="https://code.google.com/p/google-api-python-client/" target="_blank">google-api-python-client External Link</a>, <a href="https://github.com/natmallow/a3-tools-rnd/blob/master/libs/google-api-python-client-1.1.zip" target="_blank">google-api-python-client-1.1</a>,  
<a href="http://www.lfd.uci.edu/~gohlke/pythonlibs/" target="_blank">setuptools External Link</a>, <a href="https://github.com/natmallow/a3-tools-rnd/blob/master/libs/distribute-0.6.40.win-amd64-py2.7.exe" target="_blank">setuptools distribute-0.6.40.win-amd64-py2.7</a>,  

  


