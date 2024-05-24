import sys
def diff():
    print("name of the file is %s and total arguments are: %d" %(sys.argv[0],len(sys.argv)))
    return int(sys.argv[1])-int(sys.argv[2])
r=diff()
print(r)