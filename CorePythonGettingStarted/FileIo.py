# writing to a file
f = open('wasteland.txt', mode='wt', encoding='utf-8')
f.write('some string that does not return a new line without "\\n"\n')
f.close()

# reading form a file
g = open('wasteland.txt', mode='rt', encoding='utf-8')
g.read(32)
g.read()
g.read()
g.seek(0)
g.readline()
g.readline()
g.seek(0)
g.readlines()
g.close()

# appending to a file
h = open('wasteland.txt', mode='at', encoding='utf-8')
h.writelines(
    ['some more text\n']
)
h.close()