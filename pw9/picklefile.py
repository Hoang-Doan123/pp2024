import pickle
import threading
 
def write_to_file(data, fname):
    with open(fname, "ab") as f:
        for item in data:
            pickle.dump(item, f)
def pickle_data_in_background(data, fname):
    thread = threading.Thread(target=write_to_file, args=(data, fname))
    thread.start()