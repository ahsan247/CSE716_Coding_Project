import Libraries.BinaryFileRead as BinaryFileRead
import Libraries.RecordToStringConvert as RecordToStringConvert
from datetime import date, datetime

file = BinaryFileRead.openFile("Storage//Data File")

object_type = {
    "students": [
        {"name": "ID", "type": int},
        {"name": "Name", "type": str},
        {"name": "BirthDate", "type": date},
        {"name": "Address", "type": str}
    ]
}

default_object_type = "students"

type_list = []
for i in object_type[default_object_type]:
    type_list.append(i["type"])

line = file.readline()
while line:
    record = RecordToStringConvert.retrieveRecordFromString(line.decode(), type_list)
    result = ''
    for i, j in enumerate(record):
        if isinstance(j, int):
            j = str(j)
        if isinstance(j, date):
            j = j.strftime('%m/%d/%Y')
        if i == 0:
            result = j
        else:
            result += ',' + j
    print(result)
    line = file.readline()

file.close()
