#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-
import io
import HTMLParser
import string
from collections import Counter
import copy
import sys
#List of stopwords
stopwords=[u'i', u'me', u'my', u'myself', u'we', u'our', u'ours', u'ourselves', u'you', u'your', u'yours', u'yourself', u'yourselves', u'he', u'him', u'his', u'himself', u'she', u'her', u'hers', u'herself', u'it', u'its', u'itself', u'they', u'them', u'their', u'theirs', u'themselves', u'what', u'which', u'who', u'whom', u'this', u'that', u'these', u'those', u'am', u'is', u'are', u'was', u'were', u'be', u'been', u'being', u'have', u'has', u'had', u'having', u'do', u'does', u'did', u'doing', u'a', u'an', u'the', u'and', u'but', u'if', u'or', u'because', u'as', u'until', u'while', u'of', u'at', u'by', u'for', u'with', u'about', u'against', u'between', u'into', u'through', u'during', u'before', u'after', u'above', u'below', u'to', u'from', u'up', u'down', u'in', u'out', u'on', u'off', u'over', u'under', u'again', u'further', u'then', u'once', u'here', u'there', u'when', u'where', u'why', u'how', u'all', u'any', u'both', u'each', u'few', u'more', u'most', u'other', u'some', u'such', u'no', u'nor', u'not', u'only', u'own', u'same', u'so', u'than', u'too', u'very', u's', u't', u'can', u'will', u'just', u'don', u'should', u'now', u'd', u'll', u'm', u'o', u're', u've', u'y', u'ain', u'aren', u'couldn', u'didn', u'doesn', u'hadn', u'hasn', u'haven', u'isn', u'ma', u'mightn', u'mustn', u'needn', u'shan', u'shouldn', u'wasn', u'weren', u'won', u'wouldn']


city_f=['Los_Angeles,_CA','San_Francisco,_CA','Manhattan,_NY','Houston,_TX','Chicago,_IL','Philadelphia,_PA','Toronto,_Ontario','Atlanta,_GA','San_Diego,_CA','Orlando,_FL','Washington,_DC','Boston,_MA']
cities=['Los_A','San_F','Manha','San_D','Houst','Chica','Phila','Toron','Atlan','Washi','Bosto','Orlan']


#input file names 
train_file=sys.argv[1]
test_file=sys.argv[2]
output_file=sys.argv[3]

f=open(train_file,"rb")
lines=f.read().splitlines()
f.close()

docs=[]
 
html_parser = HTMLParser.HTMLParser()
#removing newlines in tweets plus smileys
for i in range(len(lines)) :
    temp=lines[i].split(" ")
    if temp[0] in city_f : 
        docs.append(html_parser.unescape(lines[i].decode('utf8','ignore').encode('ascii','ignore')))
    else :
        docs[-1]=docs[-1]+" "+html_parser.unescape(lines[i].decode('utf8','ignore').encode('ascii','ignore'))



#removing punctuation from training set
for i in range (len(docs)) :
    punc=set(string.punctuation)
    ftweet=""
    for char in docs[i] :
        if char not in punc:
            ftweet=ftweet+char
    docs[i]=ftweet.lower()

all_words=[]
docs_wo_city=[]
for i in range(len(docs)) :
    words=docs[i].split(" ")
    ftweet=""
    avoid_first_word=True
    for j in words :
        if j not in stopwords and j!="" :
            if avoid_first_word==False :
                all_words.append(j)
            else :
                avoid_first_word=False
            ftweet=ftweet+j+" "
    docs_wo_city.append(ftweet)

#top most frequent words
freq=Counter(all_words).most_common(1800)

best_features=[]

for i in freq :
    best_features.append(i[0])

#given a tweet return best features that occur
def find_features(document):
    temp=document.split(" ")
    city=temp[0]
    document=temp[1:]
    words=set(document)
    features={}
    for w in best_features:
        features[w]=(w in words)
    return (features,city)


featuresets=[find_features(d) for d in docs]

prob_of_label={city.lower().replace("_","").replace(",",""):0 for city in city_f}
#number of tweets in training set
total_t_count=0
labelfeat={feat:0 for feat in best_features}

#probability of features given a label
probfl={city.lower().replace("_","").replace(",",""):copy.deepcopy(labelfeat) for city in city_f}
for j in featuresets :
    prob_of_label[j[1]]+=1
    total_t_count+=1
    #p(f/label)
    for key,value in j[0].iteritems() :
        if value==True :
            probfl[j[1]][key]+=1

#probability of a label
for key,value in prob_of_label.iteritems() :
    prob_of_label[key]=float(value)/float(total_t_count)

#Calculating total number of times best_features occur for each label
sum_of_feature_occ={city.lower().replace("_","").replace(",",""):0 for city in city_f}
for c in city_f :
    p_city=c.lower().replace("_","").replace(",","")
    sum_of_feature_occ[p_city]=sum(probfl[p_city].values())

#testing data
f1=open(test_file,"rb")
lines1=f1.read().splitlines()
f1.close()
docs2=[]

#removing newlines in tweets
for i in range(len(lines1)) :
    temp=lines1[i].split(" ")
    if temp[0] in city_f : 
        docs2.append(html_parser.unescape(lines1[i].decode('utf8','ignore').encode('ascii','ignore')))
    else :
        docs2[-1]=docs2[-1]+" "+html_parser.unescape(lines1[i].decode('utf8','ignore').encode('ascii','ignore'))

original_tweets=copy.deepcopy(docs2)

#removing punctuation from testing data
for i in range (len(docs2)) :
    punc=set(string.punctuation)
    ftweet=""
    for char in docs2[i] :
        if char not in punc :
            ftweet=ftweet+char
    docs2[i]=ftweet.lower()

f3=open(output_file,"w")
twecnt=0
co_cnt=0
for t in range(len(docs2)) :
    twecnt+=1
    infeat=docs2[t].split(" ")[1:]
    all_label_prob=[]
    for city in city_f :
        feature_prob=[]
        p_city=city.lower().replace("_","").replace(",","")
        for i in infeat:
            if i in probfl[p_city].keys():
                feature_prob.append(float(probfl[p_city][i])/float(sum_of_feature_occ[p_city]))
        total_prob=1
        for j in feature_prob :
            total_prob=total_prob*j
        all_label_prob.append((total_prob)*prob_of_label[p_city])
    if city_f[all_label_prob.index(max(all_label_prob))].lower().replace("_","").replace(",","") == docs2[t].split(" ")[0] :
        co_cnt += 1
    f3.write(city_f[all_label_prob.index(max(all_label_prob))]+" "+original_tweets[t]+"\n")
f3.close()

#Accuracy    
print "Accuracy"
print (float(co_cnt)/float(twecnt))*100.0

#print top 5 features
for city in city_f :
    p_city=city.lower().replace("_","").replace(",","")
    print "Top 5 features for " + city
    v=list(probfl[p_city].values())
    k=list(probfl[p_city].keys())
    for i in range(5) :
        print k[v.index(max(v))]
        v.pop(v.index(max(v)))
        k.pop(v.index(max(v)))
