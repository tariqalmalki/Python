from os import strerror

try:
    cnt = lcnt = 0
    s = open('C:\\Users\\TARIQALMALKI\\Desktop\\test.txt', "rt")
    liness = s.readlines()
    while len(liness) != 0:
        for line in liness:
            lcnt += 1
            for ch in line:
                print(ch,end='')
                cnt += 1
            
        liness = s.readlines(2)
    print('\n\n Number of Charecter = ', cnt)
    print('\n Number of Lines = ', lcnt)
except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))
