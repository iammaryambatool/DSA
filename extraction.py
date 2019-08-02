import tweepy as tw
import csv

consumer_key = 'nE1gXsExmmiqLMHOkzSbcOhtk'
consumer_secret = 'JJG2nFpX1lW6PX6ctavyFrbnFKtKIAqELDtmH19lNCpFkJpIYo'
access_token = '190197768-2eYByJYUErl79UghFULOjtIX2TssfxHtikT1mpBf'
access_token_secret = 'TtJIQdgHK439r4pHRdHOgNbGWGYL6uHTI97FO6T1cOeyq'

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)
# Open/Create a file to append data
print("Enter Keyword: ")
keyword = input()
csvFile = open(keyword+'.csv', 'a', newline='')
# Use csv Writer
csvWriter = csv.writer(csvFile)


i=1
for tweet in tw.Cursor(api.search, q=keyword + '-filter:retweets', lang="en", tweet_mode="extended", compression=False,).items(10):
    print(tweet.full_text.encode('utf-8'))
    csvWriter.writerow([i,tweet.full_text.encode('utf-8')])
    i = i+1

