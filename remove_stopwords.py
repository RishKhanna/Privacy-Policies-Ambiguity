from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
  
stop_words = set(stopwords.words('english')) 

def count_without_stopwords(input):
	count = 0
	for i in input:
		final = word_tokenize(i)
		filtered_sentence = [w for w in final if not w in stop_words]
		count += len(filtered_sentence) 
	return count