
from asho import Asho
from rich.console import Console
from rich.table import Table
import os
import json
from datetime import datetime, timezone
from astlo.np_encoder import NumpyEncoder
import time

asthor = Asho()
console = Console()
table = Table()

def talk(name: str=None,formatt: str='json'):
    '''creates the json file with the jpl state vectors and updates it every hour. if the loop is closed, astlo will not be able to the topocentric coordinates for the de440.bsp - astlohorizons - NASA JPL.''' 
    
    if name==None:
        return 'name cannot be none'
    
    asthor = Asho()
    now_print = datetime.now(timezone.utc) #universal timezone
    count = 0

    if (name=='moon' or name=='luna' or name=='lunar') and formatt=='json':
       # count = 0
    #    now = datetime.now(timezone.utc)
        while True:
            try:
                now = datetime.now(timezone.utc)
                states = asthor.astlo_talk(None,'y')
                states['UTCtime'] = f'{now}'

                with open('import_states.json','w',encoding='utf-8') as file: #utf-8 ensures cross platform fole compatibility, indent=4 Pretty-prints the JSON file with 4-space indentation instead of a single compact line., cls=NumpyEncoder Automatically converts NumPy scalars and arrays to serializable lists/floats from astlo the core engine.
                #   file.write(f'{states['states_list'][0]}\n{states['states_list'][1]}\n{states['states_list'][2]}\n{states['states_list'][3]}\n{states['name']}\n{states['time_unix']}\n{states['time_simple']}\n{states['explanation']}') #with a separator of ','..the comma acts as the separato...no \n is the perfect separator..
             ###json i love you##
                    json.dump(states, file, cls=NumpyEncoder, indent=4)

                
            
                print(f'frequency at which file updated since UTC={now_print} /: UTCstated + {count} 1-minute-interval', end='\r') #

                time.sleep(60) #sleeps for onenhour then updates the json file.
                count += 1
            except KeyboardInterrupt:
                raise KeyboardInterrupt('keyboard interrupt')

    elif name and formatt=='json':
    #    count = 0
    
            
        while True:
            try:
                now = datetime.now(timezone.utc)

                states = asthor.astlo_talk(name)
                states['UTCtime'] = f'{now}'

                with open('import_states.json','w',encoding='utf-8') as file:
            #     file.write(f'{states['states_list'][0]}\n{states['states_list'][1]}\n{states['name']}\n{states['time_unix']}\n{states['time_simple']}\n{states['explanation']}')
                    json.dump(states, file, cls=NumpyEncoder, indent=4)

                print(f'frequency at which file updated since UTC={now_print} /: UTCstated + {count} 1-minute-interval', end='\r')

                time.sleep(60)
                count += 1

            except KeyboardInterrupt:
                raise KeyboardInterrupt('keyboard interrupt')

        

  #  elif (name=='moon' or name=='luna' or name=='lunar') and formatt=='txt':
 #       pass
#
    #    states = asthor.astlo_talk(None,'y')

  #      with open('states.json') as file:
   #         pass


   ##json fknish         

#####STICK WITH JSOJ FIL only because txt files require string files and jaon files any data type can be passed



