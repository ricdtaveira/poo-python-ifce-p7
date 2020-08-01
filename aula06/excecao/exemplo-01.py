import sys

print ("argv[0]=" + sys.argv[0])
print ("argv[1]=" + sys.argv[1])
print ("argv[2]=" + sys.argv[2])

for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except OSError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()