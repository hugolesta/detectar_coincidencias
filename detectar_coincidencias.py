import os
import glob
import filecmp

path = 'directorio de los archivos'
extension = '*.txt'

def comparar_linea(file1, file2):
    data1 = [line.strip() for line in file1.readlines()]
    data2 = [line.strip() for line in file2.readlines()]
    same = set(data1).intersection(data2)
    return same

def buscarCoincidencias(path, extension):
    with open('some_output_file.txt', 'w') as file_out:
        os.chdir(path)
        files = glob.glob(extension)
        for i in range(len(files)):
            for j in range(i+1, len(files)):
                with open(files[i]) as file1:
                    with open(files[j], 'r') as file2:
                        same = comparar_linea(file1, file2)
                        file_out.write(files[i] + "-"+ files[j] + ": "+str(same)+"\n")


buscarCoincidencias(path, extension)