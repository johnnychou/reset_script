
string = u" 123  423          567     Test "

test_list = string.split("  ")


def strip_empty_in_list(list):
    result = []
    for entry in list:
        entry = entry.strip()
        if entry is not "":
            result.append(entry)

    return result

list = strip_empty_in_list(test_list)

print(list)
