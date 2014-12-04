import sys, os
import re

def read_file(ds, res_file):
    ifile = open(res_file, "r")
    
    for line in ifile:
        if not ">" in line:
            continue
        split_array = line.split(">")
        if "construct" in split_array[1]:
            if split_array[0] in ds.keys():
                ds[split_array[0]] += 1
            else:
                ds[split_array[0]] = 0
        
        if "release" in split_array[1]:
            if split_array[0] in ds.keys():
                ds[split_array[0]] -= 1
            else:
                ds[split_array[0]] = -1


file_paths = ["C:/Users/admin/AppData/Local/Temp/log_sfsemmodels.txt", "C:/Users/admin/AppData/Local/Temp/log_AmadaSemFw00_Models.txt", "C:/Users/admin/AppData/Local/Temp/log_modeler.txt", "C:/Users/admin/AppData/Local/Temp/log_SEMViewer.txt"]
def start_prog(file_paths):
    for file_path in file_paths:
        if not os.path.exists(file_path):
            continue
        ds = {}
        print("############# {} ################".format(file_path))
        read_file(ds, file_path)
        show_result(ds);


def show_result(ds):
    total = 0
    for k in ds:
        if ds[k] >= 0:
            print ("{} leaks = {}".format(k, ds[k]+1))
            total = total + (ds[k] + 1)

    print (" total leaks = {} ".format(total))



