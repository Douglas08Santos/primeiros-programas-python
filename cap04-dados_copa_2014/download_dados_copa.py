import io
import sys
from urllib import response
import urllib.request as request

BUFF_SIZE = 1024
#Fonte: http://livropython.com.br/dados.zip
def download_length(response, output, length):
    times = length // BUFF_SIZE
    if length % BUFF_SIZE > 0:
        times += 1
    for time in range(times):
        output.write(response.read(BUFF_SIZE))
        print('Baixando... {:.2f} %'.format(((time*BUFF_SIZE)/length)*100))

def download(response, output):
    total_download = 0
    while True:
        data = response.read(BUFF_SIZE)
        total_download += len(data)
        if not data:
            break
        output.write(data)
        print('Baixando... {} bytes'.format(total_download))

# main só é executada quando esse módulo é o utilizado na linha de comando
# Quando ele é importado, a função main não é executada
def main():
    response = request.urlopen(sys.argv[1])
    out_file = io.FileIO('saida.zip', mode='w')

    content_length = response.getheader('Content-Length')
    print(content_length)
    if content_length:
        length = int(content_length)
        download_length(response, out_file, length)
    else:
        download(response, out_file)
    
    response.close()
    out_file.close()
    print('Completado!!')

if __name__ == '__main__':
    main()