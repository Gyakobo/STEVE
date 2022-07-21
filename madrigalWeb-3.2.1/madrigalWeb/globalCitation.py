#!python

"""This script runs a global search through Madrigal data, and returns a citation to the group of files

    This script is a stand-alone application, and can be run from anywhere with a connection to the internet.
    It runs on either unix or windows.  It requires only the MadrigalWeb python module to be installed.

$Id: globalCitation.py 7240 2020-10-02 20:05:22Z brideout $
"""

usage = """
        Usage:

        globalCitation.py  --user_fullname=<user fullname> --user_email=<user email> \
            --user_affiliation=<user affiliation> --startDate=<YYYY-MM-DD>  --endDate=<YYYY-MM-DD> \
            inst=instrument list> [options]

        where:

        --user_fullname=<user fullname> - the full user name (probably in quotes unless your name is
                                          Sting or Madonna)

        --user_email=<user email>

        --user_affiliation=<user affiliation> - user affiliation.  Use quotes if it contains spaces.

        --startDate=<YYYY-MM-DD> - start date to filter experiments before.  Defaults to allow all experiments.

        --endDate=<YYYY-MM-DD> - end date to filter experiments after.  Defaults to allow all experiments.

        --inst=<instrument list> - comma separated list of instrument codes or names.  See Madrigal documentation
                                   for this list.  Defaults to allow all instruments. If names are given, the
                                   argument must be enclosed in double quotes.  An asterick will perform matching as
                                   in glob.  Examples: (--inst=10,30 or --inst="Jicamarca IS Radar,Arecibo*")
                                   
        and options are:
        

        --expName  - filter experiments by the experiment name.  Give all or part of the experiment name. Matching
                     is case insensitive and fnmatch characters * and ? are allowed.  Default is no filtering by 
                     experiment name.
                     
        --excludeExpName - exclude experiments by the experiment name.  Give all or part of the experiment name. Matching
                     is case insensitive and fnmatch characters * and ? are allowed.  Default is no excluding experiments by 
                     experiment name.
                     
        --fileDesc - filter files by their file description string. Give all or part of the file description string. Matching
                     is case insensitive and fnmatch characters * and ? are allowed.  Default is no filtering by 
                     file description.

        --kindat=<kind of data list> - comma separated list of kind of data codes.  See Madrigal documentation
                                       for this list.  Defaults to allow all kinds of data.  If names are given, the
                                       argument must be enclosed in double quotes.  An asterick will perform matching as
                                       in glob. Examples: (--kindat=3001,13201 or 
                                       --kindat="INSCAL Basic Derived Parameters,*efwind*,2001")


        --seasonalStartDate=<MM/DD> - seasonal start date to filter experiments before.  Use this to select only part of the
                                year to collect data.  Defaults to Jan 1.  Example:
                                (--seasonalStartDate=07/01) would only allow experiments after July 1st from each year.

        
        --seasonalEndDate=<MM/DD> - seasonal end date to filter experiments after.  Use this to select only part of the
                                    year to collect data.  Defaults to Dec 31.  Example: 
                                    (--seasonalEndDate=10/31) would only allow experiments before Oct 31 of each year.

        --includeNonDefault - if given, include realtime files when there are no default.  Default is to search only default files.                            
"""

import sys
import os
import time
import traceback
import getopt
import re
import datetime
import fnmatch

import madrigalWeb.madrigalWeb


# parse command line
arglist = ''
longarglist = ['user_fullname=',
               'user_email=',
               'user_affiliation=',
               'startDate=',
               'endDate=',
               'inst=',
               'kindat=',
               'seasonalStartDate=',
               'seasonalEndDate=',
               'includeNonDefault',
               'skipVerification',
               'expName=',
               'excludeExpName=',
               'fileDesc=']

optlist, args = getopt.getopt(sys.argv[1:], arglist, longarglist)


# set default values
user_fullname=None
user_email=None
user_affiliation=None
startDate = None
endDate = None
inst = None
kindat = None
seasonalStartDate = None
seasonalEndDate = None
includeNonDefault = False
skipVerification = False
expName = None
excludeExpName = None
fileDesc = None

# check if none passed in
if len(optlist) == 0:
    print(usage)
    sys.exit(-1)
    

for opt in optlist:
    if opt[0] == '--user_fullname':
        user_fullname = opt[1]
    elif opt[0] == '--user_email':
        user_email = opt[1]
    elif opt[0] == '--user_affiliation':
        user_affiliation = opt[1]
    elif opt[0] == '--startDate':
        startDate = opt[1]
    elif opt[0] == '--endDate':
        endDate = opt[1]
    elif opt[0] == '--inst':
        inst = opt[1].split(',')
    elif opt[0] == '--expName':
        expName = opt[1]
    elif opt[0] == '--excludeExpName':
        excludeExpName = opt[1]
    elif opt[0] == '--fileDesc':
        fileDesc = opt[1]
    elif opt[0] == '--kindat':
        kindat = opt[1].split(',')
    elif opt[0] == '--seasonalStartDate':
        seasonalStartDate = opt[1]
    elif opt[0] == '--seasonalEndDate':
        seasonalEndDate = opt[1]
    elif opt[0] == '--includeNonDefault':
        includeNonDefault = True
    elif opt[0] == '--skipVerification':
        skipVerification = True

    else:
        raise ValueError('Illegal option %s\n%s' % (opt[0], usage))
    
# verify that no regular arguments were passed in
if len(args) != 0:
    print(usage)
    raise ValueError('This command does not accept any arguments without options - may be due to illegal spaces in the command')

# check that all required arguments passed in
if startDate is None:
    print(usage)
    print('--startDate argument required')
    sys.exit(-1)
else:
    try:
        startDate = datetime.datetime.strptime(startDate, '%Y-%m-%d')
    except:
        traceback.print_exc()
        print('startDate must be in format YYYY-MM-DD')
        
if endDate is None:
    print(usage)
    print('--endDate argument required')
    sys.exit(-1)
else:
    try:
        endDate = datetime.datetime.strptime(endDate, '%Y-%m-%d')
    except:
        traceback.print_exc()
        print('endDate must be in format YYYY-MM-DD')

if inst is None:
    print(usage)
    print('--inst argument required - must be a comma separated list of instrument codes or names')
    sys.exit(-1)

if user_fullname is None:
    print(usage)
    print('--user_fullname argument required - must your name')
    sys.exit(-1)

if user_email is None:
    print(usage)
    print('--user_email argument required - must your email address')
    sys.exit(-1)

if user_affiliation is None:
    print(usage)
    print('--user_affiliation argument required - must your affiliation')
    sys.exit(-1)  

# verify the url is valid
server = madrigalWeb.madrigalWeb.MadrigalData('http://cedar.openmadrigal.org')

citationList = server.getCitationListFromFilters(startDate, endDate, inst, kindat, 
                                                 seasonalStartDate, seasonalEndDate, 
                                                 includeNonDefault, expName, excludeExpName, 
                                                 fileDesc)

print('\nThe following file citations will be in this group citation:\n')
for citation in citationList:
    print(citation)
    
if not skipVerification:
    print('\nAre you sure you want to create a permanent citation to this group of files? (y/n)')
    verify = input()
    if verify.lower() != 'y':
        print('Citation not created.')
        sys.exit(-1)
        
citation = server.createCitationGroupFromList(citationList, user_fullname, user_email, user_affiliation)

print('Created group citation: %s' % (citation))
        
    





