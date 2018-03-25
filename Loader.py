import os
import time
import subprocess
folder_secure = "F:\Extractor\secure"
folder_update = "F:\Extractor\update"
folder_normal = "F:\Extractor\ormal"
folder_output = "F:\Extractor\Extracted"
hactool_location = "F:\Extractor\Hactool\hactool.exe"


def file_found(path_input):
    filename = os.listdir(path_input)
    return filename


def create_folder(folder_location): #Not making a folder but a file
    if not os.path.isdir(folder_location):
        os.mkdir(folder_location)



def file_remover(unsorted):
    unwanted_script = [s for s in unsorted if not ".cnmt" in s]
    return unwanted_script


def hactool_run(file_list, output_folder, hactool, input_folder):
    loop_counter = 1
    loop_counters = 1
    while len(file_list) >= loop_counter:
        with open(output_folder, 'w') as extract_folder : # Not opening folder as write so permission denied
            file_name = file_list[loop_counter]
            loop_counter = loop_counter + 1
            cmd = (hactool + " -k keys.dat --plaintext " + input_folder + "/" + file_name + " " + extract_folder + "/")
            subprocess.call(cmd)
            time.sleep(20)
            loop_counters = loop_counters + 1





secure_files = file_found(path_input=folder_secure)
update_files = file_found(path_input=folder_update)
normal_files = file_found(path_input=folder_normal)
secure_purged_files = file_remover(unsorted=secure_files)
update_purged_files = file_remover(unsorted=update_files)
normal_purged_files = file_remover(unsorted=normal_files)
create_folder = create_folder(folder_location = folder_output)
hactool_run(file_list=secure_purged_files,output_folder = folder_output,hactool=hactool_location,input_folder=folder_secure)
hactool_run(file_list=update_purged_files,output_folder = folder_output,hactool=hactool_location,input_folder=folder_update)
hactool_run(file_list=normal_purged_files,output_folder = folder_output,hactool=hactool_location,input_folder=folder_normal)
