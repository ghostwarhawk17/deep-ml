import numpy as np
from collections import Counter
import math

def compute_tf_idf(corpus, query):
	"""
	Compute TF-IDF scores for a query against a corpus of documents.
    
	:param corpus: List of documents, where each document is a list of words
	:param query: List of words in the query
	:return: List of lists containing TF-IDF scores for the query words in each document
	"""
	if not corpus:
		return []
	ans = []
	N = len(corpus)
	df = Counter()
	for doc in corpus:
		for word in doc:
			df[word]+=1

	for doc in corpus:
		doc_len = len(doc)
		word_count = Counter(doc)
		row = []
		for word in query:
			if doc_len == 0:
				tf == 0
			else:
				tf = word_count[word] / doc_len


			idf = math.log((N + 1)/(df[word] + 1)) + 1
			tfid = tf * idf

			row.append(np.round(tfid,5))
		
		ans.append(row)

	return ans

	

