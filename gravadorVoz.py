"""
Created by sudoAptIPedro
    
"""
from sounddevice import *
from scipy.io.wavfile import write

inicio = str(input("--> Do you want to start recording?\n yes(y) or no(n)\n -->"))

# procedimento que definira o tempo de duração(item 1), a captura da gravação(item 2) e o salvamento do arquivo(item 3)
def recorder():
    #1
    temp = 44122

    time_second = int(input("--> Quantos segundos deseja gravar? \n -->"))

    print("\n Iniciando a gravação...\n")

    #2
    captura_de_voz = rec(int(time_second*temp), samplerate=temp, channels = 2)
    wait()

    #3

    write("testeDeGravacao.wav", temp, captura_de_voz)

    print("\n---> GRAVAÇÃO FINALIZADA")

if(inicio == 'y'):
    recorder()
else:
    print("--> P R O G R A M A  E N C E R R A D O")

 