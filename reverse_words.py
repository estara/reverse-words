def rev_word(str, start, end):
    return str[start:end][::-1]


def rev_string(str):
    start = 0
    idx = 0
    out = ""
    if len(str) == 0 or str.isspace():
        return "Please give me good input"
    for char in str:
        if char == " ":
            end = idx
            out += rev_word(str, start, end) + " "
            start = idx
        idx += 1
    out = out[0:len(out)-1]
    out += rev_word(str, end+1, len(str))
    if out == "":
        return str[::-1]
    return out

