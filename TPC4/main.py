import os
import re
import csv
import json

def csv_to_json(csv_file):
    with open(csv_file, 'r', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader)
        result = {}
        for row in reader:
            data = {}
            for i, field in enumerate(row):
                match = re.match(r'^(.+){(\d+)(,\s*(\d+))?}$', header[i])
                if match:
                    field_name, start, end = match.group(1, 2, 4)
                    if end:
                        end = int(end)
                    else:
                        end = int(start)
                    values = [x for x in row[i:i+end] if x]
                    agg_function = re.search(r'::(\w+)$', header[i])
                    if agg_function:
                        function_name = agg_function.group(1)
                        if function_name == 'sum':
                            value = sum(map(float, values))
                        elif function_name == 'media':
                            value = sum(map(float, values)) / len(values)
                    else:
                        value = values
                    data[field_name] = value
                else:
                    data[header[i]] = field
            result[row[0]] = data
        return json.dumps(result, indent=4, ensure_ascii=False)

def main():
    csv_file_name = input("Nome do arquivo CSV: ")
    csv_file = os.path.join('C://Users/Tiago Cunha/Documents/GitHub/PL/TPC4/files', csv_file_name)
    json_file = os.path.splitext(csv_file_name)[0] + ".json"
    result = csv_to_json(csv_file)
    with open(json_file, 'w', encoding='utf-8') as f:
        f.write(result)

    print("sucess")

if __name__ == '__main__':
    main()