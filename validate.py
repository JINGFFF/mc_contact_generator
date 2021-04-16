import os
import sys
sys.path.append('/afs/cern.ch/cms/PPD/PdmV/tools/McM/')
from rest import McM
from json import dumps
mcm = McM(dev=False)

infile = open(sys.argv[1], "r")
lines = infile.readlines()
#outdir = sys.argv[2]
#os.system("mkdir -p " + outdir)

#outfile_none_new              = open(outdir + '/none_new.txt' , 'w')
#outfile_validation_new        = open(outdir + '/validation_new.txt' , 'w')
#outfile_validation_validation = open(outdir + '/validation_validation.txt' , 'w')
#outfile_define_defined        = open(outdir + '/define_defined.txt' , 'w')

    
field_to_update = 'time_event'
ii = 0
for i in range(0, len(lines)):
    x = lines[i].split('\n')
    request_prepid_to_update = x[0]
    #print request_prepid_to_update
    #field_to_update = 'time_event'
    request = mcm.get('requests', request_prepid_to_update)
    print str(request_prepid_to_update) + ' : ' +str(request['approval']) + ' ' + str(request['status'])

    if request['approval'] == 'none':
        mcm.approve('requests', request_prepid_to_update)
        ii = ii + 1
        print ii
    if request['approval'] == 'validation':
        mcm.approve('requests',request_prepid_to_update)
    
    if ii > 50 : 
        break
