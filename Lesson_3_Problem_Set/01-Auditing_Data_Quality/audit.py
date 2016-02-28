#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
In this problem set you work with cities infobox data, audit it, come up with a cleaning idea and then clean it up.
In the first exercise we want you to audit the datatypes that can be found in some particular fields in the dataset.
The possible types of values can be:
- 'NoneType' if the value is a string "NULL" or an empty string ""
- 'list', if the value starts with "{"
- 'int', if the value can be cast to int
- 'float', if the value can be cast to float, but is not an int
- 'str', for all other values

The audit_file function should return a dictionary containing fieldnames and the datatypes that can be found in the field.
All the data initially is a string, so you have to do some checks on the values first.

"""
import csv
import pprint
import re


CITIES = 'cities.csv'

FIELDS = ["name", "timeZone_label", "utcOffset", "homepage", "governmentType_label", "isPartOf_label", "areaCode", "populationTotal",
          "elevation", "maximumElevation", "minimumElevation", "populationDensity", "wgs84_pos#lat", "wgs84_pos#long",
          "areaLand", "areaMetro", "areaUrban"]


def getType(value):
    if value is None or len(str(value)) == 0 or str(value) == "NULL":
        return type(None)
    if str(value)[0] == '{':
        return type([])
    if re.match('[0-9]+$', value):
        return type(1)
    try:
        float(value)
        return type(1.1)
    except Exception:
        pass
    return type("")


def audit_file(filename, fields):
    fieldtypes = {}
    for key in FIELDS:
        fieldtypes.update({key: set([])})
    areaValues = set([])
    toSkip = 3
    cnt = 0
    with open(filename, "r") as f:
        reader = csv.DictReader(f, delimiter=",")
        for row in reader:
            if cnt < toSkip:
                cnt += 1
                continue
            areaValues.add(row["areaMetro"])
            for field in FIELDS:
                fieldtypes[field].add(getType(row[field]))

    return fieldtypes


def test():
    fieldtypes = audit_file(CITIES, FIELDS)

    pprint.pprint(fieldtypes)

    assert fieldtypes["areaLand"] == set([type(1.1), type([]), type(None)])
    assert fieldtypes['areaMetro'] == set([type(1.1), type(None)])

if __name__ == "__main__":
    test()
