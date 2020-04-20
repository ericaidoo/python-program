
import urllib
import requests
import json

# from SendingEmail import*

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage


# set an api key
api_key = 'c345c9a3c63f4ce880492adbe2083a1e'

# define the url from where json will be retrieved
url = ('http://newsapi.org/v2/top-headlines?'
       'country=us&category=sports&'
       'apiKey=c345c9a3c63f4ce880492adbe2083a1e')

# store all the data into response variable
response = urllib.request.urlopen(url).read()
# urllib.request.urlopen(url).read()

json_obj = str(response, 'utf-8')
data = json.loads(json_obj)

# declare a string that will store all the contents such as text, buttons
html = ""
html2 = ""
# get data imported from the api file
i = 1
msgAlternate = MIMEMultipart()
msg = MIMEMultipart()
for item in data['articles']:
       # download the image
       # Download_imgs(item['urlToImage'],item['publishedAt'])

       # add title
       html += """<html>
                   <head></head>
                   <body style="background-color:#fff;">
                   <font size="5"><div class='container'>{title}
                   </div></font><br></body>""".format(title = item['title'])

       # add description
       html += """<body style="background-color:#fff;">
                  <font size="8"><p></font><br><img src="{img}" width="800" height="450 align="right""></p><div><a href={link}>{des}</a></div></body>""".format(des = item['description'], img = item['urlToImage'], link = item['url'])
       html += "<br>"
       html += "<br>"



