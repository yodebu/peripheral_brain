#!/usr/bin/python3

# coding: utf-8

# In[1]:

# Import required modules
import requests
from bs4 import BeautifulSoup
import pandas as pd
from time import gmtime, strftime


# In[2]:

yesterday_df = pd.read_csv('yesterday.csv')


# In[3]:

# Create a variable with the url
url = 'http://chrisralbon.com'

# Use requests to get the contents
r = requests.get(url)

# Get the text of the contents
html_content = r.text

# Convert the html content into a beautiful soup object
soup = BeautifulSoup(html_content)


# In[4]:

header = soup.title.string
title = header.split(' - ')[0]
description = header.split(' - ')[1]
todays_date = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())


# In[5]:

link = []
title = []

for i in soup.find_all('li'):
    i = i.a
    try: 
        relative_url = i.get('href')
        base_url = url+'/'
        link_url = str(base_url)+str(relative_url)
        link.append(link_url)
        
        title.append(i.string)
    except:
        continue


# In[6]:

title = pd.Series(title, name='title')
link = pd.Series(link, name='link')

today_df = pd.concat([title, link], axis=1)


# In[7]:

today_df.to_csv('yesterday.csv', index=False)


# In[8]:

today_df['new'] = (today_df['title'] != yesterday_df['title'])


# In[9]:

diff = today_df[today_df['new'] == True]


# In[10]:

post_items = []

for index, row in diff.iterrows():
    post_title = row[0]
    post_url = row[1]
    post_items.append('<item><title>'+post_title+'</title><link>'+post_url+'</link><pubDate>'+todays_date+'</pubDate><description></description> </item>')


# In[11]:

rss_items = str(post_items)

rss_items = rss_items.strip("['")
rss_items = rss_items.replace("', '", " ")
rss_items = rss_items.strip("']")


# In[12]:

rss_header = '<?xml version="1.0" encoding="UTF-8"?> <rss version="2.0" xmlns:content="http://purl.org/rss/1.0/modules/content/" xmlns:wfw="http://wellformedweb.org/CommentAPI/" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:atom="http://www.w3.org/2005/Atom"><channel><title>Chris Albon</title><link>http://chrisalbon.com/</link><atom:link href="http://chrisalbon.pythonanywhere.com/feed.xml" rel="self" type="application/rss+xml" /><description>Political Science And Data Science</description><language>en</language>' 


# In[13]:

rss_footer = '</channel></rss>'


# In[14]:

if len(rss_items) > 1:
    rss_full = rss_header + rss_items + rss_footer
    text_file = open("feed.xml", "w")
    text_file.write(rss_full)
    text_file.close()

