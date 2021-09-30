from os import strerror

try:
    cnt = lcnt = 0
    s = open('C:\\Users\\TARIQALMALKI\\Desktop\\test.txt', "rt")
    line = s.readline()
    while line != '':
        lcnt += 1
        for ch in line:
            print(ch,end='')
            cnt += 1
            
        line = s.readline()
    print('\n\n Number of Charecter = ', cnt)
    print('\n Number of Lines = ', lcnt)
except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))
