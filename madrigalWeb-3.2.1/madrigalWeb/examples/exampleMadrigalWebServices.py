"""exampleMadrigalWebServices.py runs an example of the Madrigal Web Services interface
   for a given Madrigal server.

   usage:

   python exampleMadrigalWebServices.py <optional url>

"""
import sys, os.path

# $Id: exampleMadrigalWebServices.py 7404 2021-12-17 15:52:40Z brideout $

import madrigalWeb.madrigalWeb

# constants
user_fullname = 'Bill Rideout - automated test'
user_email = 'brideout@haystack.mit.edu'
user_affiliation = 'MIT Haystack'

if len(sys.argv) > 1:
    madrigalUrl = sys.argv[1]
else:
    madrigalUrl = 'http://madrigal.haystack.mit.edu'


testData = madrigalWeb.madrigalWeb.MadrigalData(madrigalUrl)



print('Example of call to getAllInstruments')
instList = testData.getAllInstruments()
# print out Millstone
for inst in instList:
    if inst.code == 30:
        print((str(inst) + '\n'))
        

print('Example of call to getExperiments')
expList = testData.getExperiments(30, 1998,1,19,0,0,0,1998,1,22,0,0,0)
for exp in expList:
    # should be only one
    print((str(exp) + '\n'))


print('Example of call to getExperimentFiles')
fileList = testData.getExperimentFiles(expList[0].id)
for thisFile in fileList:
    if thisFile.category == 1:
        print((str(thisFile) + '\n'))
        thisFilename = thisFile.name
        break
    
print('Example of downloadFile - simple and hdf5 formats:')
result = testData.downloadFile(thisFilename, "/tmp/test.txt", 
                               user_fullname, user_email, user_affiliation, "simple")
result = testData.downloadFile(thisFilename, "/tmp/test.hdf5", 
                               user_fullname, user_email, user_affiliation, "simple")

print('Example of simplePrint - only first 1000 characters printed')
result = testData.simplePrint(thisFilename, user_fullname, user_email, user_affiliation)
print(result[:1000])
print()

print('Example of call to getExperimentFileParameters - only first 10 printed')
fileParms = testData.getExperimentFileParameters(thisFilename)
for i in range(10):
    print(fileParms[i])
print()


print('Example of call to isprint (prints data)')
print((testData.isprint(thisFilename,
                       'gdalt,ti',
                       'filter=gdalt,500,600 filter=ti,1900,2000',
                       user_fullname, user_email, user_affiliation)))

print('Example of call to listFileTimes')
expDir = os.path.dirname(thisFilename)
fileTimes = testData.listFileTimes(expDir)
epsFile = None
for i, fileTime in enumerate(fileTimes):
    if i > 5:
        print(fileTime)
    if epsFile is None:
        if fileTime[0].find('.eps') != -1:
            epsFile = fileTime[0]
            
print('example of call to getVersion')
version = testData.getVersion()
print('Madrigal version is %s' % (str(version)))

if not testData.compareVersions(version, '2.9'):
    print('Not a Madrigal 3 server - skipping Madrigal 3 tests')
    isMad3 = False
else:
    print('Is a Madrigal 3 server - including Madrigal 3 tests')
    isMad3 = True
            
if not epsFile is None and isMad3:
    print('Example of call to downloadWebFile')
    tmpFile = os.path.join('/tmp', os.path.basename(epsFile))
    try:
        os.remove(tmpFile)
    except:
        pass
    testData.downloadWebFile(epsFile, tmpFile)
    try:
        os.remove(tmpFile)
    except:
        pass


print('Example of call to madCalculator (gets derived data at any time)')
result = testData.madCalculator(1999,2,15,12,30,0,45,55,5,-170,-150,10,200,200,0,'sdwht,kp,ne_iri')
for line in result:
    for value in line:
        print(('%8.2e ' % (value)))
    print('\n')

print('Example of searching all Madrigal sites for an experiment - here we search for PFISR data')
expList = testData.getExperiments(61,2008,4,1,0,0,0,2008,4,30,0,0,0,local=0)
print(expList[0])

print('Since this experiment is not local (note the experiment id = -1), we need to create a new MadrigalData object to get it')
testData2 = madrigalWeb.madrigalWeb.MadrigalData(expList[0].madrigalUrl)

print('Now repeat the same calls as above to get PFISR data from the SRI site')
expList2 = testData2.getExperiments(61,2008,4,1,0,0,0,2008,4,30,0,0,0,local=1)
print('This is a PFISR experiment')
print(expList2[0])
