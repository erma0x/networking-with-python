import os
import socket
import time
import random as rnd
from datetime import datetime
from colorama import Fore, Style
from config import IP_SERVER, PORTA_SERVER, IP_PLC, PORTA_PLC

    
def testing_socket():

    try:
        while True: 
            
            # messaggio randomico per simulare il messaggio PLC
            MESSAGE = bytes('f,'+str(rnd.randint(0,5))+','+str(rnd.randint(1,100))+',' +str(rnd.randint(1,100)),'utf-8') 
            current_time = datetime.now().strftime("%H:%M:%S")
                    
            # inizializza il socket con IPv4 e straming socket
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.bind((IP_PLC, PORTA_PLC))
            sock.connect((IP_SERVER, PORTA_SERVER))
            sock.send(MESSAGE)
            sock.close()

            os.system('clear')

            print('\n\n\t Status socket: '+Fore.GREEN +'\t\t[ONLINE]\n'+ Style.RESET_ALL+'\n\t IP server: \t\t\t'+Fore.YELLOW + IP_SERVER+ ':'+str(PORTA_SERVER)+Style.RESET_ALL+'\n\n\t message from PLC: \t\t' + Fore.BLUE  +str(MESSAGE)  + Style.RESET_ALL + '\n\n\t time: \t\t\t\t'+  Fore.YELLOW  +str(current_time) + Style.RESET_ALL)
            #time.sleep(rnd.randint(minimo_intervallo_di_secondi, massimo_intervallo_di_secondi+1))
            time.sleep( 5 )


    except: 
        print('Errore 🔥',Fore.RED +current_time+Style.RESET_ALL,f'Connessione al server {IP_SERVER}:{PORTA_SERVER} non riuscita ') 
        time.sleep(5)

if __name__ == "__main__":
    testing_socket()
 
    
