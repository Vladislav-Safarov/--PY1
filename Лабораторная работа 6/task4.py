import json

INPUT_FILE = "input1.csv"


def csv_to_list_dict(filename, delimiter=",", new_line='\n') -> list[dict]:
    with open(filename) as f:
        rows = [((''.join(row.split(new_line))).split(delimiter)) for row in f]
        first_row, *last_rows = rows
        list_dict = [{first_row[i]: row[i] for i in range(len(row))} for row in last_rows]
    return list_dict
    # TODO реализовать конвертер из csv в json


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
