def remove_whitespace(string_list):
    cleaned_list = [s.replace(" ", "").replace("\t", "").replace("\n", "") for s in string_list]
    return cleaned_list

print(remove_whitespace(["  hello  ", "world\t", "\nnewline\n"]))