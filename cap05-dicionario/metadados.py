#   5.3 - Montando o Dicionário de Metadados

# Listando arquivos de uma pasta
import os

def extract_name(name):
    return name.split('.')[0]

# recebe o caminho do arquivo e retorna uma lista de tuplas
def read_metadata(filename):
    data = open('data/meta-data/'+ filename, 'rt')
    meta_data = []
    for line in data:
        meta_data.append(tuple(line.split('\t')[:3]))
    data.close()
    return meta_data

def prompt():
    print('\nO que deseja ver?')
    print('(1) - Listar entidades')
    print('(2) - Exibir atributos de uma entidade')
    print('(3) - Exibir referencias de uma entidade')
    print('(4) - Sair do programa')
    return input('')

def main():
    # dicionario entidade -> atribuitos
    metadata = {}
    # dicionário id -> entidade
    keys = {}
    #dicionario de relacionamento
    relationships = {}
    for metadata_file in os.listdir('data/meta-data'):
        entity = extract_name(metadata_file)
        attrs = read_metadata(metadata_file)
        identified = attrs[0][0]

        metadata[entity] = attrs
        keys[identified] = entity 
    
    for key, val in metadata.items():
        for col in val:
            if col[0] in keys:
                if not col[0] == metadata[key][0][0]:
                    relationships[key] = keys[col[0]]
        
    opcao = prompt()
    while opcao != '4':
        if opcao == '1':
            for entity_name in metadata.keys():
                print(entity_name)
        elif opcao == '2':
            print('Entidades: {}'.format(''.join(name+', ' for name in metadata.keys())))
            entity_name = input('Nome da Entidade: ')
            for col in metadata[entity_name]:
                print(col)
        elif opcao == '3':
            print('Entidades: {}'.format(''.join(name+', ' for name in metadata.keys())))
            entity_name = input('Nome da Entidade: ')
            other_entity = relationships[entity_name]
            print(other_entity)
        else:
            print('Inexistente\n')
        opcao = prompt()

if __name__ == '__main__':
    main()