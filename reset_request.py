import os
import sys
sys.path.append('/afs/cern.ch/cms/PPD/PdmV/tools/McM/')
from rest import McM

mcm = McM(dev=False)

infile = open(sys.argv[1], "r")
lines = infile.readlines()

for i in range(0, len(lines)):
    x = lines[i].split('\n')
    request_prepid_to_update = x[0]
    print request_prepid_to_update
    #field_to_update = 'time_event'
    request = mcm.get('requests', request_prepid_to_update)
    mcm.approve('requests', request_prepid_to_update, 0)
    print str(request_prepid_to_update) + ' : ' + str(request['dataset_name']) + ' ' + str(request['approval']) + ' ' + str(request['status'])

