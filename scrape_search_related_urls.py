import json
import string
import requests
import lxml
from lxml import html
from bs4 import BeautifulSoup
from requests_html import HTMLSession

# no tbm


def find_related(chiave):
  
 '''
 The function takes in input a json like the following one
 and returns in output the same object with the related links for each key 
 
 {
"host": "www.google.it",
"language": "it",
"keys": {
"guida a big query": [],
"come diventare ricchi senza lavorare": [],
"come creare siti senza programmare": []
}
}

'''


	fac_sim= "http://www.google.{}/search?&q={}"
	session = HTMLSession()
	host = chiave['host']
	lang = chiave['language']

	related={}

	related['host'] = chiave['host']

	related['language'] = chiave['language']

	ll = []
	d = {}

	for key in chiave['keys']:
	    key = key.replace(' ', '+')
	    r = session.get((fac_sim.format(lang, key))).text    
	    tree = BeautifulSoup(r)    
	    l = []
	    
	    for i in tree.find_all("p", attrs={ "class" : "nVcaUb"}):
	        try:
	            l.append(str(i).split('q=')[1].split('&amp')[0].replace('+', ' '))
	        except not l:
	            l.append(['void'])
	        
	        d[key.replace('+', ' ')] = l
	    
	    related['keys'] = d
	   
	    print('url {} processed'.format(fac_sim.format(lang, key)))

	return related