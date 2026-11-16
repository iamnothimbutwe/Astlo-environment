
from asho import Asho
from rich.console import Console
from rich.table import Table
import os
import json
from datetime import datetime, timezone
from astlo.np_encoder import NumpyEncoder
from astlo import Contin
import time

asthor = Asho()
console = Console()
table = Table()
contin = Contin()


def talk(name: str=None,formatt: str='json'):
    '''creates the json file with the jpl state vectors and updates it every hour. if the loop is closed, astlo will not be able to the topocentric coordinates for the de440.bsp - astlohorizons - NASA JPL. if target required is moon pass moon as name.''' 
    
    if name==None:
        return 'name cannot be none'

    name = name.upper()

    if name not in contin.astlohorizons_de440_objects.keys(): #still without usimg the .keys() method attribute the dictionary would have checked correctly.
        return f'Name: {name} not supported. try astLo'


    asthor = Asho()
    now_print = datetime.now(timezone.utc) #universal timezone
    count = 0
   # moons = ('moon','luna','lunar') #not making them upper cae becaude astlo handles that and also astlojorizons handles thay..

    if (name=='MOON' or name=='LUNA' or name=='LUNAR') and formatt=='json':
       # count = 0
    #    now = datetime.now(timezone.utc)
        while True:
            try:
                now = datetime.now(timezone.utc)
                states = asthor.astlo_talk(None,'y')

                if isinstance(states,str):
                    print(states)
                    return states

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

    elif name and formatt=='json': #yes if name is moon it will check the first and also enter this statemnt becauee it all name. name==True get it..but after yhe keyboard interrupt which must be reached at the end of the lasy if statemnt..this mwhtod cannkt be reached even though they are supposed to execute both of them...ignore.
    #    count = 0
            
            
        while True:
            try:
                now = datetime.now(timezone.utc)

                states = asthor.astlo_talk(name) #methof skysolsys automatically looksup the dictioanry b4 loading the files..so just apssing the normal names is ok.

                if isinstance(states,str):
                    print(states) #fkr tge cli amd also sdk..
                    return states

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

def talk2():
    '''writes to import_states for all the objects that de440 supports. a total of '''

    asho = Asho()
    #now = datetime.now(timezone.utc)
    
    objects = {} #using name as dictionary key and value as the pos states and a utctime..
    for i in contin.astlohorizons_de440_objects.keys():
        now = datetime.now(timezone.utc)
        if i=='MOON':
            obj_states = asho.astlo_talk(None,'y')
            obj_pos_vectors = obj_states['states_list'][4] #luna relative ssb_m
        else:
            obj_states = asho.astlo_talk(i,None)
            obj_posto_m = []
            for x in obj_states['states_list'][0]:
                obj_posto_m.append(x*1000) #m
                
            obj_pos_vectors = obj_posto_m #pos vector..should later convert to m

      #  obj_pos_vectors.append(f'{now}')
        objects[i] = obj_pos_vectors
    objects['UTCtime'] = f'{now}'

    with open('import_states.json','w',encoding='utf-8') as file:

        json.dump(objects,file,cls=NumpyEncoder,indent=4)

    print(f'Completed writing to json file for all the objects supported. UTCtime: {now}')


