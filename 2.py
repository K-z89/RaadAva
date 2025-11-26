import requests
import json
import time
import random
import sys
import os




def make():
	
	for i in range(1000):
		sok = 'qwertyuiopasdfghjklzxcvbnm'
		so="qwertyuiopasdfghjklzxcvbnm_0123456789"
		s = random.choice(sok)
		d = random.choice(so)
		f = random.choice(so)
		t = random.choice(so)
		k = random.choice(so)
		user = s+d+f+t+k
		kota = requests.get('https://t.me/'+user)
		reba = (kota.text)
		if ('name="robots"') in reba:
			print('\033[32m OK: '+user)
		else:
			print('\033[31m NO: '+user)

make()
