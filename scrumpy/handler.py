import re
from scrumpy import errors

VARIABLE_STORAGE = {}

def run_file(file_path):
    code_file = open(file_path, "r")
    code = code_file.read()
    check_syntax(code)

def check_syntax(code_to_check):
    operations = []
    current_operation = 0
    for line in code_to_check.split("\n"):
        line_has_ended = False
        character_count = 0
        for character in line:
            if character != ";" and line_has_ended == False:
                character_count += 1
            elif character == ";":
                line_has_ended = True
        operations.append(line[:character_count])
    parse(operations)

def get_var_value(var):
    var_name = var[1::]
    return(VARIABLE_STORAGE[var_name])

def parse_value(value):
    output = re.findall('\!s\((.*?)\)', value)
    if len(output) != 0:
        return str(output[0])
        
    output = re.findall('\!i\((.*?)\)', value)
    if len(output) != 0:
        return int(output[0])

    output = re.findall('\!f\((.*?)\)', value)
    if len(output) != 0:
        return float(output[0])

    output = re.findall('\!b\((.*?)\)', value)
    if len(output) != 0:
        return bool(output[0])
    
    raise errors.error(f"Unknown value type parsed: {value}")

def set_var_value(var, value):
    var_name = var[1::]
    value = parse_value(value)
    VARIABLE_STORAGE[var_name] = value

def get_value_of(get_value_from):
    output = re.findall('"(.*?)"', get_value_from)
    if len(output) != 0:
        return output[0]
    
    output = re.findall('\$[\s\S]*$', get_value_from)
    if len(output) != 0:
        output = get_var_value(output[0])
        return output

    return output

def process_out(operation):
    output = operation[5:]
    processed_output = get_value_of(output)
    return print(processed_output)

def parse(operations):
    for operation in operations:
        operation_segments = operation.split(" ")
        operator = operation_segments[0]
        if operator == ":out":
            process_out(operation)
        elif operator.startswith("$"):
            set_var_value(operator, operation[len(operator)+1::])
