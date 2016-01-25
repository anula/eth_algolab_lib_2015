import os

def writeFilesListFile(files, list_name):
    content = '\\newcommand*{\ListAllFiles}{%\n'
    content += ',%\n'.join(files)
    content += '\n}%\n'
    with open(list_name + '.tex', 'w') as list_file:
        list_file.write(content)

def generateFilesList(path):
    files_list = []
    for (dirpath, _, filenames) in os.walk(path):
        for fn in filenames:
            files_list.append(dirpath + '/' + fn)
    return files_list

filenames = generateFilesList('./source_files')
writeFilesListFile(filenames, 'FilesList')

