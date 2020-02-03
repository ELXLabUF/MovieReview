
# coding: utf-8

# In[21]:


#URL
#1. Twitter API - https://developer.twitter.com/apps
#2. Access token: 860552192968712192-GUj7zPoOhLNa2SiAbZBjhP3zgR3jI2t
#3. Access token secret: PY3Osvw6roExUh22MCs0K8fWHom3834WIctJSET8M7PGC
#4. API key: oOOLEPPMTs7vcmqOeXKUEHJG0
#5. API secret key: a8OT9BwDfQtwYxCY6zDHydQb21mNXmGUJPCDplQcKJQFpgfYSg


# In[22]:


# import pandas as pd

# # Search tweets
# dict_ = {'user': [], 'date': [], 'text': [], 'favorite_count': []}
# for status in python_tweets.search(**query)['statuses']:
#     dict_['user'].append(status['user']['screen_name'])
#     dict_['date'].append(status['created_at'])
#     dict_['text'].append(status['text'])
#     dict_['favorite_count'].append(status['favorite_count'])

# # Structure data in a pandas DataFrame for easier manipulation
# df = pd.DataFrame(dict_)
# df.sort_values(by='favorite_count', inplace=True, ascending=False)
# df.head(5)


# In[1]:


from twython import Twython

TWITTER_APP_KEY = 'oOOLEPPMTs7vcmqOeXKUEHJG0'  #supply the appropriate value
TWITTER_APP_KEY_SECRET = 'a8OT9BwDfQtwYxCY6zDHydQb21mNXmGUJPCDplQcKJQFpgfYSg' 
TWITTER_ACCESS_TOKEN = '860552192968712192-GUj7zPoOhLNa2SiAbZBjhP3zgR3jI2t'
TWITTER_ACCESS_TOKEN_SECRET = 'PY3Osvw6roExUh22MCs0K8fWHom3834WIctJSET8M7PGC'


# In[2]:


t = Twython(app_key=TWITTER_APP_KEY, 
            app_secret=TWITTER_APP_KEY_SECRET, 
            oauth_token=TWITTER_ACCESS_TOKEN, 
            oauth_token_secret=TWITTER_ACCESS_TOKEN_SECRET)

search = t.search(q='#DepressionIsReal',count=1)
# search


# In[3]:


tweets = search['statuses']
# tweets


# In[4]:


for tweet in tweets:
  print(tweet['id_str'], '\n', tweet['text'])


# In[5]:


#create own keyword dataset from scratch - https://towardsdatascience.com/extracting-keywords-from-short-text-fce39157166b
#keyword extraction existing module - RAKE short for Rapid Automatic Keyword Extraction algorithm
#processing for custom dataset - https://medium.com/analytics-vidhya/automated-keyword-extraction-from-articles-using-nlp-bfd864f41b34
from rake_nltk import Rake

r = Rake() # Uses stopwords for english from NLTK, and all puntuation characters.


# In[16]:


#to do - clean text data
import re
text = "I like kitty and puppy while developing on systems"
# text = tweets[0]['text']
text = re.sub(r'http\S+', '', text)


# In[17]:


r.extract_keywords_from_text(text)


# In[18]:


r.get_ranked_phrases() # To get keyword phrases ranked highest to lowest.


# In[51]:


#to build hierarchical classifier from scratch - https://github.com/richliao/textClassifier
#to find the main idea/root word - https://www.kdnuggets.com/2018/08/understanding-language-syntax-and-structure-practitioners-guide-nlp-3.html
#textClassification using Word2Vec - https://github.com/richliao/textClassifier
#text classification - https://github.com/brightmart/text_classification


# In[52]:


#to try - https://github.com/sloria/www/blob/master/content/2013-09-30-tutorial-wordnet-textblob.md


# In[ ]:


#scratch
#remove stopword 
#steming
#find sentiment - remove sentiment words
#parent category - https://stackoverflow.com/questions/54625493/how-to-group-wikipedia-categories-in-python

