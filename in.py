import os

cwd = os.getcwd()

full_list = os.listdir(cwd)

files_list = [i for i in full_list if os.path.isfile(i) and '.py' not in i]
types = list(set([i.split('.')[1] for i in files_list]))

for file_type in types:
    os.mkdir(file_type)

for file in files_list:
    from_path =  os.path.join(cwd, file)
    to_path = os.path.join(cwd, file.split('.')[-1], file)

     # Adiciona uma verificação se o arquivo de origem existe
    if os.path.exists(from_path):
        try:
            os.replace(from_path, to_path)
        except Exception as e:
            print(f"Erro ao substituir {from_path} para {to_path}: {e}")
    else:
        print(f"Arquivo de origem {from_path} não encontrado. A substituição não foi realizada.")