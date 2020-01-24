import json
import glob
import datetime


def write(path, fields_to_write, output_file):
    header = f"# Extracted from Hatebase on {datetime.date.today()} \n"
    input_files = glob.glob(path+'/*.txt')

    print(f'writing results to {output_file}')

    with open(output_file, "w") as out_file:
        out_file.write(header)
        for f in input_files:
            with open(f) as json_file:
                data =  json.load(json_file)
                for r in data['result']:
                    fields = [f"{x}={r[x]}" for x in fields_to_write]
                    for i, _ in enumerate(fields):
                        #Must replace all colons for gazetteer to be read correctly
                        fields[i]=fields[i].replace(":"," -")
                    fields_string = ":".join(fields)
                    #Add term to the beginning of the line
                    line = f"{r['term']}:{fields_string}"
                    out_file.write(line+'\n')

    print('done!')

