from avro import schema, datafile, io
import pprint
import json
import sys

out = str(sys.argv[1])
OUTFILE_NAME = out
rec_reader = io.DatumReader()
 
df_reader = datafile.DataFileReader(
    open(OUTFILE_NAME,"rb"),
    rec_reader
)

pp = pprint.PrettyPrinter()
with open('{0}.json'.format(out),'w') as outfile:
    data = []

    for record in df_reader:
        data.append(record)
        
    json.dump(data, outfile, indent=4, sort_keys=True)
    print("file printed to {0}.json".format(out))