from nltk import word_tokenize
from collections import Counter
from nltk import WordNetLemmatizer
lemmatize = WordNetLemmatizer()

with open('JOBDES.txt','rb') as f:
	A = f.readlines()
#print(A)
from nltk.corpus import stopwords

a = ''

for x in A:
	a += str(x)
# ...
A =a.replace('.','').replace(',','').replace(':','').replace('%','').replace('&','').replace("\n",'').replace('the','').replace('then','').replace('it', '').replace("'\n'",'').replace("Job",'').replace("Description",'')
word_list = word_tokenize(A)
A = [lemmatize.lemmatize(n) for n in word_list]
A = [word for word in A if word not in stopwords.words('english')]

print(Counter(A))