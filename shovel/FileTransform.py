import csv
import json


# TODO: Unicode support for csv
# refer: https://docs.python.org/2/library/csv.html?highlight=csv#examples
class FileTransform(object):

    @staticmethod
    def csv2json(csv_file_name, json_file_name, pretty_print=True):
        print("csv2json start, csv_file_name=%s, json_file_name=%s" %
              (csv_file_name, json_file_name))

        with open(csv_file_name, 'r') as csv_file, open(json_file_name, 'w') as json_file:
            reader = csv.DictReader(csv_file)
            rows = []
            for row in reader:
                rows.append(row)
            json.dump(rows, json_file, indent=2 if pretty_print else -1)
            json_file.write('\n')

        print("csv2json start, csv_file_name=%s, json_file_name=%s" %
              (csv_file_name, json_file_name))

    @staticmethod
    def json2csv(json_file_name, csv_file_name):
        print("json2csv start, json_file_name=%s, csv_file_name=%s" %
              (json_file_name, csv_file_name))

        # refer from: https://docs.python.org/2/library/csv.html?highlight=csv#csv.writer
        #  If csvfile is a file object, it must be opened with the ‘b’ flag on platforms where that makes a difference.

        with open(json_file_name, 'rb') as json_file, open(csv_file_name, 'wb') as csv_file:
            jsonArrays = json.load(json_file)
            firstJsonObj = jsonArrays[0]
            fieldnames = []
            for key in firstJsonObj:
                fieldnames.append(key)
            print("create header line from first json object, fieldnames=%s" % fieldnames)

            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for jsonObj in jsonArrays:
                writer.writerow(jsonObj)

        print("json2csv done, json_file_name=%s, csv_file_name=%s" %
              (json_file_name, csv_file_name))
