def read():
    path = './repositories.json' 
    file = open(path)
    content = file.read()
    file.close()
    return json.loads(content)

read()