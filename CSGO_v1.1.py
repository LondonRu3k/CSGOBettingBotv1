import re
import traceback
import time
import datetime
from datetime import datetime, timedelta
import sqlite3
import praw # simple interface to the reddit API, also handles rate limiting of requests
'''USER CONFIGURATION'''

USERNAME  = "WeatherReportBot"
#This is the bot's Username. In order to send mail, he must have some amount of Karma.
PASSWORD  = "woodeye"
#This is the bot's Password. 
USERAGENT = "Flair For CSGOBETTING"
#This is a short description of what the bot does. For example "/u/GoldenSights' Newsletter bot"
SUBREDDIT = "CSGOBETTING"
#This is the sub or list of subs to scan for new posts. For a single sub, use "sub1". For multiple subreddits, use "sub1+sub2+sub3+..."
REPLYSTRING = ['[Here is your Weather Report](www.thefuckingweather.com/?where=)']
#This is the word you want to put in reply
MAXPOSTS = 100
#This is how many posts you want to retrieve all at once. PRAW can download 100 at a time.
WAIT = 20
#This is how many seconds you will wait between cycles. The bot is completely inactive during this time.


'''All done!'''
r = praw.Reddit(user_agent=USERAGENT)
try:
    import bot #This is a file in my python library which contains my Bot's username and password. I can push code to Git without showing credentials
    USERNAME = bot.getu()
    PASSWORD = bot.getp()
    USERAGENT = bot.geta()
except ImportError:
    pass


def main():
	subreddit = r.get_subreddit('CSGOBETTING')
	for submission in subreddit.get_new(limit=20):
		pbody = submission.selftext.lower()
		print submission.link_flair_text
		ptitle = submission.title.lower()
	#	print ptitle
		dateObj= re.search(r'(\d\d[^\d\w]\d\d[^\d\w]\d\d)', ptitle)
		if dateObj:
			timeObj = re.search( r'(\d\d:\d\d)', pbody)
			if timeObj:
				found = timeObj
				pStrDate = (dateObj.group(1) +':'+ found.group(1))
				timeNow = datetime.utcnow()
				timeNowP = timeNow + timedelta(hours=4)
				ptime = datetime.strptime(pStrDate, "%d.%m.%y:%H:%M")
				if timeNowP > ptime:
					print True
				else:
					print False
while True:
	try:
		main()
	except Exception as e:
		traceback.print_exc()
	print('Running again in %d seconds \n' % WAIT)
	time.sleep(WAIT)


