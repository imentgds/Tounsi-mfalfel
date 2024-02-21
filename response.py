import lgtn as long
import re
from datetime import datetime

import test
import asyncio

n = 0

#message_probability y7wel ytl3 message mt3 usrer
#recognised word : hiya kalimet mo3tarf biha
#  required_word : el kalimet matloouba

def message_probability(user_message , recognised_words , required_words=[],signal_response =False):
    message_certainty=0
    has_required_words=True
    #nbda bil kelma bi kelma
    for word in user_message :
        #itha kelma mwjuda  fil message mt3 user nzyd 1 ma3na daqiq
        if word in recognised_words:
            
            message_certainty+=1
    #besh ne7seb porcentage ed9a
    percentage= float(message_certainty)/float(len(recognised_words))
    
    #besh ntthabet fi required word
    for word in required_words :
        if word not in user_message:
            #ken 9ithech yaani ne9setni kelma
            has_required_words=False
            break
    if has_required_words  or signal_response :
        return int(percentage*100)
    else :
        #yaani hata kelma mahi metchebha 
        return 0
        

#fonction eli besh ncheki beha el message t3 user
async def check_all_messages(user_message):
    global n
    highest_prob_list={}
    #naaml fonction response fi westha
    def response (bot_response , list_of_words , signal_response=False,required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response]=message_probability(user_message , list_of_words , required_words,signal_response )       
    #response
    response('Asleeemaa !',['ahla','selem','aslemaa','bnjr','hi','marhbe'],signal_response=True,required_words=['ahla','selem','aslemaa','bnjr','hi','marhbe'])

    response('Hta enii!', ['eni','nheb', 'barsha', 'lklem','tv','net'],signal_response=True, required_words=['nheb'])
    response('Hamdulh aa shaybi wink nty', ['chnhwelk', 'kifnk', 'chaaml', 'hru','?'], signal_response=True,required_words=['chnhwelk', 'kifnk', 'chaaml', 'hru','?'])
    response('Hay bhy chfama jdid ?', ['hmd', 'hani', 'hamdulh', 'cv',], signal_response=True,required_words=['hmd','cv'])
    response(long.dbara(), ['chntayb', 'dbara', 'daber aaliya', 'chbechnatyb',"chnaamel mekla"], signal_response=True,required_words=['dbara','chntayb'])
    response(long.R_EATING, ['mekla', 'tekl', 'chtekl'],signal_response=True, required_words=[ 'mekla','chtekl'])
    response(long.wzyr(), ['chkun jey', 'Lyum','chfama','lyoum'],signal_response=True, required_words=[ 'lyum','chkun jey'])
    response("Tounsy mfalfel Chat Bot tounsi a 100 pour 100 sahaybi", ['chkunk', 'chesmk', 'man anta','wru','??'],signal_response=True, required_words=[ 'chkunk','chesmk'])
    response("°C", ['takes', 'chnoi takes', 'kif','weather','ta9es'],signal_response=True, required_words=[ 'takes','weather'])
    response("Imen Gueddes (Moon) future ingenieure genie logiciel <3 ", ['chkun san3ek', 'creator', 'Moulek'],signal_response=True, required_words=[ 'Moulek','creator'])
    response("Cyber Processing Robot est un club de robotique dont le prinicpal objectif est de de produire une génération capable de travailler dans plusieurs domaines technologiques ", ['cpu', 'club', 'dev','robotique'],signal_response=True, required_words=[ 'club','cpu'])
    
    response(datetime.now(), ['waket', 'kadeh', 'elwaket'],signal_response=True, required_words=[ 'waket'])
    
    
    best_match = max(highest_prob_list, key=highest_prob_list.get)
    if(best_match == '.'):
        n = 1
     
    if highest_prob_list[best_match] < 1 :
        
        return long.unknown()
    else :
        return best_match




async def get_reponse(message, user_input):
    global n
    #message lkollu fi lowercase
    split_message = re.split(r'\s[!?.,\-;]\s*', user_input.lower())
    #chnaaml check lil msg
    response= await check_all_messages(split_message)
    if(n==1):
        n = 0
        await test.wt(message)
    #nraj3 erponse eli sna3tha
    return response
    
