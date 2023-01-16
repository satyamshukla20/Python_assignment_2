file=open('hash.txt',mode='r')
txt=file.read()
file.close()
output =""
for i in txt:
    output=output+i
    output=output+'#'
file=open('hash.txt',mode='w')
file.write(output)