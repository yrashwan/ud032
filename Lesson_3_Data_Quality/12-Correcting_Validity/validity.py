"""
Your task is to check the "productionStartYear" of the DBPedia autos datafile for valid values.
The following things should be done:
- check if the field "productionStartYear" contains a year
- check if the year is in range 1886-2014
- convert the value of the field to be just a year (not full datetime)
- the rest of the fields and values should stay the same
- if the value of the field is a valid year in range, as described above,
  write that line to the output_good file
- if the value of the field is not a valid year,
  write that line to the output_bad file
- discard rows (neither write to good nor bad) if the URI is not from dbpedia.org
- you should use the provided way of reading and writing data (DictReader and DictWriter)
  They will take care of dealing with the header.

You can write helper functions for checking the data and writing the files, but we will call only the
'process_file' with 3 arguments (inputfile, output_good, output_bad).
"""
import csv
import re

INPUT_FILE = 'autos.csv'
OUTPUT_GOOD = 'autos-valid.csv'
OUTPUT_BAD = 'FIXME-autos.csv'


def writeCSVFile(fileName, header, rowList):
    with open(fileName, "w") as f:
        writer = csv.DictWriter(f, delimiter=",", fieldnames=header, lineterminator='\n')
        writer.writeheader()
        for row in rowList:
            writer.writerow(row)


def extractYear(year):
    m = re.match('[0-9]+', year)
    if m is None:
        return -1
    return m.group(0)


def isValidYear(year):
    return year >= 1886 and year <= 2014


def isValidURI(uri):
    return re.match('(http:\/\/)?(www.)?(dbpedia.org)', uri) is not None


def process_file(input_file, output_good, output_bad):

    with open(input_file, "r") as f:
        reader = csv.DictReader(f)
        header = reader.fieldnames
        goodRows = []
        badRows = []

        #COMPLETE THIS FUNCTION
        for row in reader:
            yearField = row["productionStartYear"]
            if not isValidURI(row["URI"]):
                continue
            year = int(extractYear(yearField))
            if isValidYear(year):
                row["productionStartYear"] = str(year)
                goodRows.append(row)
            else:
                badRows.append(row)

    writeCSVFile(output_good, header, goodRows)
    writeCSVFile(output_bad, header, badRows)


def test():

    process_file(INPUT_FILE, OUTPUT_GOOD, OUTPUT_BAD)


if __name__ == "__main__":
    test()
