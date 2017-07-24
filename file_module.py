import os
import pickle

directory = "contacts"


def save(contact):
    if not os.path.exists(directory):
        os.makedirs(directory)
    pickle.dump(contact, open(directory+"/"+contact.first_name + '_' + contact.last_name+'.dat', "wb"))


def load_all():
    files = []
    for filename in os.listdir(directory):
        files.append(pickle.load(open(directory+"/"+filename, "rb")))
    return files
