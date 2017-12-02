import random
import re
def riddle():


    list_riddle=[{"answer":"I see!"},{"answer":"Oh o:"},{"answer":"okay!"},{"answer":"Hmm"},{"answer":"Mhmm?"},{"answer":"Hmm?"},{"answer":"o_o"},{"answer":"Ah, I see"},{"answer":"No"},{"answer":"Yes"},{"answer":"okay!"},{"answer":"Hahahah"},{"answer":"That's alright"},{"answer":"kay!"},{"answer":"Alright"},{"answer":"O:"},{"answer":"Bored"},{"answer":"Hahahah"},{"answer":"xD"},{"answer":"*sushhh*"}]
    random_riddle = random.choice(list_riddle)
    
    return random_riddle["answer"]
   


def talk(stuff):
   if 'hi' in stuff: return 'Hello'
   elif 'hello' in stuff: return 'hi'
   elif 'hey' in stuff: return 'hey!'
   elif 'how are you' in stuff: return 'I am doing good :)'
   elif 'noob' in stuff: return 'ya thats you xD'
   elif 'morning' in stuff: return 'Good Morning'
   elif 'night' in stuff: return 'Good Night'
   elif 'sleepy' in stuff: return 'https://i.imgur.com/H9F8Enm.gif'
   elif 'hmm' in stuff: return 'mhm?'
   elif 'bored' in stuff: return 'o: I am random , talk to me!'
   elif 'lol' in stuff: return 'xD'
   elif 'lmao' in stuff: return 'LMAO'
   elif 'lel' in stuff: return 'lol'
   elif 'bye' in stuff: return 'bye'
   elif 'hibiki' in stuff: return 'Hello I am Hibiki :)'
   elif 'slap' in stuff: return 'slap you'
   elif 'idk' in stuff: return 'https://media1.tenor.com/images/cdfa5ab16e71a6a8fae89164873bebc6/tenor.gif?itemid=5729174'
   elif 'hug' in stuff: return '(づ￣ ³￣)づ'
   elif 'angry' in stuff: return '（▼へ▼メ）'
   elif 'flip' in stuff: return '(╯°□°）╯︵ ┻━┻'
   elif 'sorry' in stuff: return '๑•́ㅿ•̀๑) ᔆᵒʳʳᵞ'
   elif 'pat' in stuff: return 'http://cloud-3.steamusercontent.com/ugc/646628994017635190/693C4B830CA27AF08FC87CE736892135F3C69510/'
   elif 'aww' in stuff: return '<@https://media.giphy.com/media/xXDuw08XyIg1y/giphy.gif'
   elif 'top song' in stuff: return 'http://www.youtube.com/playlist?list=PLw-VjHDlEOgstyQx-bOfTg-S-aDV_D_Ot'
   else:return riddle()
