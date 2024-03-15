import pickle
 
def write_to_file(data, fname):
    with open(fname, "ab") as f:
        for item in data:
            pickle.dump(item, f)