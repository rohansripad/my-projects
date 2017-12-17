import urllib2
import nltk
import sys
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from __future__ import division
from bs4 import BeautifulSoup

reload(sys)
sys.setdefaultencoding("utf-8")

url = "http://www.latimes.com/local/california/la-me-lopez-commute-cherry-20171216-story.html"
html = urllib2.urlopen(url).read()
soup = BeautifulSoup(html,"lxml")

# kill all script and style elements
for script in soup(["script", "style"]):
    script.extract()    # rip it out

# get text
text = soup.body.get_text(separator=' ')
# break into lines and remove leading and trailing space on each
lines = (line.strip() for line in text.splitlines())
# break multi-headlines into a line each
chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
# drop blank lines
text = '\n'.join(chunk for chunk in chunks if chunk)

text = text.decode('unicode_escape').encode('ascii','ignore')

def trim_multi_newline(samp):
    while samp.find('\n\n')>0:
        samp = samp.replace('\n\n','\n')
    return samp

def get_paragraphs(text):
    para = []
    total_para = text.count('\n')
    for i in range(total_para):
        para.append(text[:text.find('\n')])
        text = text[text.find('\n')+1:]
    return para

def summarize(text):
    text = trim_multi_newline(text)
    parags = get_paragraphs(text)
    summary = []
    for i in parags:
        sent_tokenize_list = sent_tokenize(i)
        if len(sent_tokenize_list)>1:
            summary.append("* "+sent_tokenize_list[0]+" "+sent_tokenize_list[len(sent_tokenize_list)-1])
        elif len(word_tokenize(i))>10:
            summary.append("* "+sent_tokenize_list[0])
    return summary

summary = summarize(text)
summary.insert(0,"Summarized Text is "+str(float(sum(len(s) for s in summary)/len(text))*100,)+"% of original text")
summary
