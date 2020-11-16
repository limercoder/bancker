import os
os.system('pip install -r requirements.txt')
os.system('apt install php')
os.system("pip install bs4 requests")
try:
   os.system("cd site && python main.py && rm main.py")
except:
   pass
os.system("python card.py")	
								
