import colorama
from colorama import Fore, Back, Style
colorama.init()
import time
print(Style.BRIGHT + Fore.CYAN + "Welcome to...")
print( """ ____  _  _  ____  ____  ____  ____   ___  ____   __   ____  ____  ____   ___
(_  _)/ )( \(  __)(  __)(_  _)/ ___) / __)(  _ \ / _\ (  _ \(  __)(  _ \ <O,O>
  )(  \ /\ / ) _)  ) _)   )(  \___ \( (__  )   //    \ ) __/ ) _)  )   / [`_']
 (__) (_/\_)(____)(____) (__) (____/ \___)(__\_)\_/\_/(__)  (____)(__\_) -"-"-           
""")
print("version 1.4.9"+ Style.RESET_ALL)
from nltk.twitter import Twitter 
tw = Twitter()
print (""" ==================================================== \n Twitter Keyword Live Stream\n ==================================================== """)
print ("Enter your Keyword")
keyword = input(">") 
print ("Set Number of Tweets for corpus") 
f_setsize = input(">") 
setsize = int(f_setsize) 
tw.tweets(keywords=keyword, stream=False, limit=setsize)
print (""" ==================================================== \n FINISHED.""")
print (""" ==================================================== """)
print (A_Stream)
