#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      nmallow
#
# Created:     13/05/2013
# Copyright:   (c) nmallow 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------


#!/usr/bin/python

import httplib2
import pprint
import os,sys
import logging

from apiclient.discovery import build
from apiclient.http import MediaFileUpload
from oauth2client.client import OAuth2WebServerFlow
from apiclient import errors

logging.basicConfig()

#set globals

# Copy your credentials from the APIs Console
CLIENT_ID = '338832324624-uadt8tgk36nutdtchvpkjn4vis3blmc5.apps.googleusercontent.com'
CLIENT_SECRET = 'kigXZ9KXYPMRfmS8gmDOWqcn'
# Check https://developers.google.com/drive/scopes for all available scopes
OAUTH_SCOPE = 'https://www.googleapis.com/auth/drive'
# Redirect URI for installed apps
REDIRECT_URI = 'urn:ietf:wg:oauth:2.0:oob'
# Path to the file to upload
FILEID = '0AgygYNpyP57jdFR4Q05NZHI3Ml9UQ0FsYXNpWlBZR0E'


def main():

    # Run through the OAuth flow and retrieve credentials
    flow = OAuth2WebServerFlow(CLIENT_ID, CLIENT_SECRET, OAUTH_SCOPE, REDIRECT_URI)
    authorize_url = flow.step1_get_authorize_url()

    #open browser object
    if sys.platform == 'win32' or 'win64':
        os.startfile(authorize_url)
    else:
        print 'Go to the following link in your browser: \n' + authorize_url

    code = raw_input('Enter verification code: ').strip()
    credentials = flow.step2_exchange(code)

    # Create an httplib2.Http object and authorize it with our credentials
    http = httplib2.Http()
    http = credentials.authorize(http)

    drive_service = build('drive', 'v2', http=http)

    bob = print_file(drive_service, FILEID)

    cont = download_file(drive_service,bob)
    text_file = open("api.csv","w")
    text_file.writelines(str(cont))

def retrieve_all_files(service):
  """Retrieve a list of File resources.

  Args:
    service: Drive API service instance.
  Returns:
    List of File resources.
  """
  result = []
  page_token = None
  while True:
    try:
      param = {}
      if page_token:
        param['pageToken'] = page_token
      files = service.files().list(**param).execute()

      result.extend(files['items'])
      page_token = files.get('nextPageToken')
      if not page_token:
        break
    except errors.HttpError, error:
      print 'An error occurred: %s' % error
      break
  return result


def print_file(service, file_id):
  """Print a file's metadata.

  Args:
    service: Drive API service instance.
    file_id: ID of the file to print metadata for.
  """
  try:
    file = service.files().get(fileId=file_id).execute()

    #print 'Title: %s' % file['title']
    #print 'Description: %s' % file['description']
    #print 'MIME type: %s' % file['mimeType']
    #for key, val in file.iteritems():
        #print key," <<< >>> ",val
    return file
  except errors.HttpError, error:
    print 'An error occurred: %s' % error


def download_file(service, drive_file):
  """Download a file's content.

  Args:
    service: Drive API service instance.
    drive_file: Drive File instance.

  Returns:
    File's content if successful, None otherwise.
  """
  #download_url = drive_file.get('downloadUrl')
  download_url = drive_file.get('exportLinks')['application/pdf']
  print download_url,"<--"
  if download_url:
    download_url = download_url[:-4] + "=csv"
    resp, content = service._http.request(download_url)
    if resp.status == 200:
      #print 'Status: %s' % resp
      return content
    else:
      print 'An error occurred: %s' % resp
      return None
  else:
    # The file doesn't have any content stored on Drive.
    return None





