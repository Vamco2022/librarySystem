def writeLine(file,data):
    with open(file,'a') as writer:
        writer.writelines(str(data))