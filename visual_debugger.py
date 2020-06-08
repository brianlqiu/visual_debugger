import sys, tempfile

def generate_outputfile(inputfile):
    return inputfile[:inputfile.find('.py')] + "_debug.py"

def main(argv):
    if(len(argv) != 2):
        print('visual_debugger.py <inputfile>')
        sys.exit(1)
    try:
        inputfile = open(argv[1], r)
    except: 
    outputfile = open(generate_outputfile(inputfile), "w+")
    lines = inputfile.readlines()
    for line in lines:
        outputfile.write(line)
    inputfile.close()
    outputfile.close()

if __name__ == '__main__':
    main(str(sys.argv))
