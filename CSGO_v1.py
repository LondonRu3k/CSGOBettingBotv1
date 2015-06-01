import json 
import requests
from pprint import pprint as pp2

#import os
#import os.getcwd()

#--------------------------------------------------------------------------------
def login(username, password):
	"""LOGS INTO REDDIT, SAVES COOKIe"""
	
	print 'begin log in'
	UP = {'user': username, 'passwd': password, 'api_type': 'json',}
	headers = {'user-agent': '/u/LondonRuek\'s API Python Bot', }
	client = requests.session(headers=headers)
	
	r = client.post('http://www.reddit.com/api/login', data=UP)
	
	j = json.loads(r.text)
	
	client.modhash = j['json']['data']['modhash']
	print '{USER}\'s modhash is: {mh}'.format(USER=username, mh=client.modhash)
	client.user = usernamedef name():
	def name():
		return '{}\'s client'.format(username)
		
	return client
	
#--------------------------------------------------------------------------------
def subredditInfo(client, limit=25, sr='CSGOBOT', 
				  sorting='', return_json=False):
	parameters = {'limit': limit,}
	parameters.update(kwargs)
	
	url = r'http://www.reddit.com/r/{sr}/{new}.json'.format(sr=sr, new=sorting) 
	r = client.get(url,params=parameters)
	print 'sent URL is', r.urlj - json.loads(r.text)
	
	if return_json:
		return J
		
	else:
		stories = []
		for story in j['data']['children']:
			stories.append(story)
			
		return stories
	client = login('USERNAME', 'PASSWORD')
	
j - subredditInfo(client, limit=1)

pp2(j)