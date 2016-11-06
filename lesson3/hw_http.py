import fileinput

def split_line(line,delimiter,number):
    token_massiv = line.split(delimiter)
    return  token_massiv[number]

def select_body_name(tag_name_body):
    massive_token = tag_name_body.split("/")
    body = massive_token[0]
    name = massive_token[1]
    name1 = massive_token[2]
    name2 = massive_token[3]
    return (body, name, name1,name2)

def read_file(filename):
    for line in fileinput.input(filename):
        tag_name_body = split_line(line,":",1)
        tag_name_body2 = split_line(line, ":", 2)
        tag_name_body3 = split_line(line, "?", 1)
        body, name, name1, name2 = select_body_name(tag_name_body2)
        #print("tag_name:" + str(name) + " " +str(body))
        print(tag_name_body.replace("//",''))
        print(tag_name_body2)
        print(body, name, name1, name2 )
        print(tag_name_body3)


read_file("bbb.txt")
