import fileinput

def split_line(line,delimiter):
    token_massiv = line.split(delimiter)
    return  token_massiv[0]

def select_body_name(tag_name_body):
    massive_token = tag_name_body.split(">")
    body = massive_token[1]
    name = massive_token[0][1:]
    return (name, body)

def read_file(filename):
    for line in fileinput.input(filename):
        tag_name_body = split_line(line,"</")
        name, body = select_body_name(tag_name_body)
        print("tag_name:" + str(name) + " " +str(body))

read_file("aaa.txt")
