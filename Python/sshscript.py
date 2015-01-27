#!/usr/bin/python 

from subprocess import call 

machinesList = []
propertyDictTemplate = {'machineName' : None,
'externalHostName' : None,
'keyDepth' : None,
'dmgPassphrase' : None}

print(propertyDictTemplate)

while True:
    propertyList = propertyDictTemplate.copy()
    propertyList['machineName'] = raw_input('Please enter a unique name for the remote box. ')
    propertyList['externalHostName'] = raw_input('Enter the DNS hostname or IP address of the remote server e.g., derp.derping.org, or 10.15.20.25 ')
    propertyList['keydepth'] = raw_input('Enter the key size, in bits, of the key to be generated, in the range between 1024 and 4096. ')
    propertyList['dmgPassphrase'] = raw_input('Enter a password to be used to encrypt the DMG file containing your generated SSH keypairs. ')
    machinesList.append(propertyList)
    call('clear')
    
    print(machinesList)


