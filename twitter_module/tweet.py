import tweepy
import time

auth = tweepy.OAuthHandler("chave",
                           "chave")
auth.set_access_token("chave-",
                      "chave")

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)

user = api.me()

print(user.screen_name)


def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(3.0)
    except StopIteration:
        return

for follower in limit_handler(tweepy.Cursor(api.followers).items()):
    print(follower.name)

parametro_pesquisa = "python"
numeroDeTwetts = 2
for tweet in tweepy.Cursor(api.search, parametro_pesquisa).items(numeroDeTwetts):
    try:
        tweet.retweet()
        print("Eu gostei de Tweet")
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
