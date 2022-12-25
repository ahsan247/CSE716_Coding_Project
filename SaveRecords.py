from datetime import datetime, date
import Libraries.BinaryFileAppend as BinaryFileAppend
import Libraries.RecordToStringConvert as RecordToStringConvert
from collections import namedtuple

ObjectType = namedtuple('ObjectType', ['name', 'datatype'])

default_object_type = "students"

object_type = {
    "students": [
        ObjectType("ID", int),
        ObjectType("Name", str),
        ObjectType("BirthDate", date),
        ObjectType("Address", str)
    ]
}

def check_record(record):
    record = record.split(",")
    if len(record) == len(object_type[default_object_type]):
        for i, j in enumerate(record):
            if isinstance(object_type[default_object_type][i].datatype, int):
                record[i] = int(j, default=0)
            elif isinstance(object_type[default_object_type][i].datatype, date):
                record[i] = datetime.strptime(j, '%m/%d/%Y').date()
        return {"Data": RecordToStringConvert.stringifyRecord(record), "Param": True}
    else:
        return {"Param": False}

exit_command = "E"
file = BinaryFileAppend.createOrOpenFileForAppend("Storage//Data File")

while True:
    data_input = input("Input a record or type E to Exit: \n")
    if data_input == exit_command:
        print("Successfully exited.")
        break

    flag = check_record(data_input)
    if flag["Param"] != True:
        print("Something wrong! Try Again. Format is: int,str,date,str")
    else:
        BinaryFileAppend.appendToFile(file, '\n'.join([flag["Data"], '']))

file.close()