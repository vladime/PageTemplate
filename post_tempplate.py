import os
import getopt
import sys

try:
    from PIL import Image
except:
    print "To use this program, you need to install Python Imaging Library - http://www.pythonware.com/products/pil/"
    sys.exit(1)

# Let's parse the arguments.
opts, args = getopt.getopt(sys.argv[1:], 'p:')

# Set some default values to the needed variables.
directory = ''

# If an argument was passed in, assign it to the correct variable.
for opt, arg in opts:
    if opt == '-p':
        directory = arg    

# We have to make sure that all of the arguments were passed.
if directory == '':
    print('Invalid command line arguments. -p [path - blah/blah/../]')
 
    # If an argument is missing exit the application.
    exit()

# Path to current *.py file
pathname = os.path.dirname(sys.argv[0])

# opent output file
f = open((pathname + '\\out.txt'), 'w')

# Set some default values to the needed variables.
directoryIN = os.path.abspath(pathname) + '\\Files'

# def width, height and counter for rows
width = -1
height = -1
i = 1

for image in os.listdir(directoryIN):

    img = Image.open(os.path.join(directoryIN, image))

    width = img.size[0]
    height = img.size[1]

    if len(str(i)) == 1:

        c = '0' + str(i)  + '. \n'

        print('!')

    else:

        c = str(i)  + '. \n'

    s = '<img class="alignnone" src="http://vladi.me/wp-content/images/places/' + directory + image + '"' + ' width="' + str(width) + '"' + ' height="' + str(height) + '" />' + '\n'  + '\n'

    print(c)
    print(s)

    f.write(c)
    f.write(s)    

    i += 1
