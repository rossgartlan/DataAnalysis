import ast

ftweets = []
tweets_file = []
def read_ftweets():
	with open('C:/Users/Rossco/desktop/twitter.txt', 'r' , encoding= 'ISO-8859-1') as f:	
		for line in f:
			ftweets.append((line))

def convert_ftweets_to_dict(count):
	for i in range(0, count):
		tweets_file.append(ast.literal_eval(ftweets[i]))
#
#
read_ftweets()
convert_ftweets_to_dict(len(ftweets))
#converted_tweets = convert_ftweets_to_dict(len(ftweets))
#print(tweets_file)