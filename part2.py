import json
import re

bus_data = input()
tf_data = json.loads(bus_data)

errors = {"bus_id": 0, "stop_id": 0, "stop_name": 0,"next_stop": 0, "stop_type": 0, "a_time": 0}
regex_errors = {"stop_name": 0, "stop_type": 0, "a_time": 0}

def check_data(data,id,type=None,req='y'):
    error_count = 0
    for x in data:
        value = x[id]
        if not value and value != 0 and req == 'n':
            pass
        elif not value and value != 0 and req == 'y': 
            error_count += 1
        elif type == 'char':
            error_count += int(not (isinstance(value, str) and len(value) == 1))
        elif type:
            error_count += int(not isinstance(value, type))
    return error_count

def regex_data(data,id,template):
    error_count = 0
    for x in data:
        value = x[id]
        match = re.match(template,value)
        if not value:
            pass
        elif match:
            pass
        elif not match: 
            error_count += 1
    return error_count

errors['bus_id'] = check_data(tf_data,"bus_id",int)
errors['stop_id'] = check_data(tf_data,"stop_id",int)
errors['stop_name'] = check_data(tf_data,"stop_name",str)
errors['next_stop'] = check_data(tf_data,"next_stop",int)
errors['stop_type'] = check_data(tf_data,"stop_type",'char',req='n')
errors['a_time'] = check_data(tf_data,"a_time",str)

# print(f'Type and required field validation: {sum(errors.values())} errors')
# for key, value in errors.items():
#     print(f"{key}: {value}")

regex_errors['stop_name'] = regex_data(tf_data,"stop_name",r"[A-Z](\w|\s)+(Road|Avenue|Boulevard|Street)$")
regex_errors['stop_type'] = regex_data(tf_data,"stop_type",r"(S|O|F)$")
regex_errors['a_time'] = regex_data(tf_data,"a_time",r"[0-1][\d]:[0-5][\d]$")

print(f'Format validation: {sum(regex_errors.values())} errors')
for key, value in regex_errors.items():
    print(f"{key}: {value}")
