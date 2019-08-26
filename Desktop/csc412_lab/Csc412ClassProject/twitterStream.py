# coding: utf-8
import tweepy


consumer_key = 'QZH2QH8i9Xo6arhtcgnvzfz0s'
consumer_key_secret = 'EEdjK7EuUNmDtfAxqJXzNBZddh69vSnHqANnZRLBAGYbMWTB7a'
access_token = '981607899712536576-YLXF3KfLlovkd9aNXLeWbrHXyyAemZQ'
access_token_secret = '2oGkWYBoNB2OfhkWKADkfL2toncN5G3wvMc3CDHgu3zNk'


class TweetListener(tweepy.StreamListener):
  def on_status(self, status):
    print('Tweet text: ' + status.text)
    return True

  def on_error(self, status_code):
    print('Got an error with status cod: ' + str(status_code))
    return True

  def on_timeout(self):
    print('Timeout..')
    return True

if __name__== '__main__':
  listener = TweetListener()
  auth = tweepy.OAuthHandler(consumer_key, consumer_key_secret)
  auth.set_access_token(access_token, access_token_secret)

  stream = tweepy.Stream(auth, listener)
  stream.filter(follow=[], track=['#nba'])
