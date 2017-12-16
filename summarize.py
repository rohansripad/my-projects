import nltk
from nltk.tokenize import sent_tokenize
from __future__ import division
f = open("/Users/rattravanam/Desktop/Sample_text.txt","r")
text = f.read()
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
        else:
            summary.append("* "+sent_tokenize_list[0])
    return summary

summary = summarize(text)
summary.insert(0,"Summarized Text is "+str(float(sum(len(s) for s in summary)/len(text))*100,)+"% of original text")
summary
