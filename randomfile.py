#!/usr/bin/env python3

# Little script to create one or multiple files with random content of a
# specified size
# Written by Sebastian Varga

import os, sys, getopt

filesize = 153600
fileamount = 24
fileprefix = 'outputfile_'

# def main(argv):
#    filesize = 1024
#    fileamount = 1
#    fileprefix = 'outputfile'
#    try:
#        opts, args = getopt.getopt(argv,"hs:a:p:",["fsize=","famount=","prefix="])
#    except getopt.GetoptError:
#        print("usage: randomfile.py -s <filesize_in_Byte> -a <amount_of_files> -p <fileprefix>")
#        sys.exit(2)
#    for opt, arg in opts:
#       if opt == '-h':
#          print('usage: randomfile.py -s <filesize_in_Byte> -a <amount_of_files> -p <fileprefix>')
#          sys.exit()
#       elif opt in ("-s", "--fsize"):
#          filesize = opt
#       elif opt in ("-a", "--afiles"):
#          fileamount = opt
#       elif arg in ("-p", "--prefix"):
#          fileprefix = arg


# if __name__ == "__main__":
#    main(sys.argv[1:])

   # filesize = argv[1]
   # fileamount = argv[2]
   # fileprefix = argv[3]
print ('Filesize is', filesize)
print ('amount of generated files:', fileamount)
print ('fileprefix is:', fileprefix)

for i in range (0, fileamount):
    filename = fileprefix+str(i+1)
    print(filename)
    with open(filename, 'wb') as fout:
        fout.write(os.urandom(filesize))
