#!/usr/local/bin/python3.4

# Import required modules
import requests
from bs4 import BeautifulSoup
import pandas as pd
from time import gmtime, strftime

# Load yesterday's version of the site
yesterday_df = pd.read_csv('/home/chrisalbon/web/yesterday.csv')

# Create today's version of the site
url = 'http://chrisalbon.com'
r = requests.get(url)
html_content = r.text
soup = BeautifulSoup(html_content)

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

title = pd.Series(title, name='title')
link = pd.Series(link, name='link')

today_df = pd.concat([title, link], axis=1)

today_df.to_csv('/home/chrisalbon/web/yesterday.csv', index=False)

# Compare today's version and yesterday's version
new_posts = today_df.loc[~today_df['link'].isin(yesterday_df['link'])]

todays_date = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
new_posts['published'] = todays_date

# Save new posts to csv for later retrieval
old_posts = pd.read_csv('/home/chrisalbon/web/all_posts.csv')
all_posts = pd.concat([new_posts, old_posts], axis=0)
all_posts.to_csv('/home/chrisalbon/web/all_posts.csv', index=False)

# Construct and save the RSS feed
header = soup.title.string
title = header.split(' - ')[0]
description = header.split(' - ')[1]

post_items = []

for index, row in all_posts[0:9].iterrows():
    post_title = row[0]
    post_url = row[1]
    post_date = str(row[2])
    post_items.append('<item><title>'+post_title+'</title><link>'+post_url+'</link><pubDate>'+post_date+'</pubDate><description></description> </item>')

rss_items = str(post_items)

rss_items = rss_items.strip("['")
rss_items = rss_items.replace("', '", " ")
rss_items = rss_items.strip("']")

rss_header = '<?xml version="1.0" encoding="UTF-8"?> <rss version="2.0" xmlns:content="http://purl.org/rss/1.0/modules/content/" xmlns:wfw="http://wellformedweb.org/CommentAPI/" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:atom="http://www.w3.org/2005/Atom"><channel><title>Chris Albon</title><link>http://chrisalbon.com/</link><atom:link href="http://chrisalbon.pythonanywhere.com/feed.xml" rel="self" type="application/rss+xml" /><description>Political Science And Data Science</description><language>en</language>'
rss_footer = '</channel></rss>'

rss_full = rss_header + rss_items + rss_footer
text_file = open("/home/chrisalbon/web/feed.xml", "w")
text_file.write(rss_full)
text_file.close()
print(rss_full)
print('Script done!')