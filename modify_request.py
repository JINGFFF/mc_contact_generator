import os
import sys
sys.path.append('/afs/cern.ch/cms/PPD/PdmV/tools/McM/')
from rest import McM

mcm = McM(dev=False)

infile = open(sys.argv[1], "r")
lines = infile.readlines()
outdir = sys.argv[2]
os.system("mkdir -p " + outdir)

outfile_none_new              = open(outdir + '/none_new.txt' , 'w')
outfile_validation_new        = open(outdir + '/validation_new.txt' , 'w')
outfile_validation_validation = open(outdir + '/validation_validation.txt' , 'w')
outfile_define_defined        = open(outdir + '/define_defined.txt' , 'w')

    
field_to_update = 'time_event'

for i in range(0, len(lines)):
    x = lines[i].split('\n')
    request_prepid_to_update = x[0]
    #print request_prepid_to_update
    #field_to_update = 'time_event'
    request = mcm.get('requests', request_prepid_to_update)
    print str(request_prepid_to_update) + ' : ' +str(request['approval']) + ' ' + str(request['status'])

    if request['approval'] == 'none':

        #request[field_to_update] = [4.1]
        #update_response = mcm.update('requests', request)

        #request2 = mcm.get('requests', request_prepid_to_update)
        #print('Request\'s "%s" field "%s" AFTER update: %s' % (request_prepid_to_update,
        #                                                       field_to_update,
        #                                                       request2[field_to_update]))
        outfile_none_new.write(str(request_prepid_to_update)+'\n')

    if request['approval'] == 'validation' and request['status'] == 'new':
        outfile_validation_new.write(str(request_prepid_to_update)+'\n')

    if request['approval'] == 'validation' and request['status'] == 'validation':
        outfile_validation_validation.write(str(request_prepid_to_update)+'\n')

    if request['approval'] == 'define' and request['status'] == 'defined':
        outfile_define_defined.write(str(request_prepid_to_update)+'\n')

outfile_none_new.close()
outfile_validation_new.close()
outfile_validation_validation.close()
outfile_define_defined.close()
