def write_to_file(fname, data):
    f = open(fname, "a")
    for item in data:
        f.write(str(item) + "\n")
    f.close()