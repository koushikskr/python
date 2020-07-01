from sklearn.datasets import fetch_20newsgroups

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn import metrics
from sklearn.pipeline import Pipeline
from sklearn.naive_bayes import MultinomialNB

twenty_train = fetch_20newsgroups(subset='train', shuffle=True)

#change the tfidfvectorizer to use bigram
tfidf_Vect = TfidfVectorizer()
tfidf_Vect1 = TfidfVectorizer(ngram_range=(1, 2))
tfidf_Vect2 = TfidfVectorizer(stop_words='english')

X_train_tfidf = tfidf_Vect.fit_transform(twenty_train.data)
X_train_tfidf1 = tfidf_Vect1.fit_transform(twenty_train.data)
X_train_tfidf2 = tfidf_Vect2.fit_transform(twenty_train.data)


# print(tfidf_Vect.vocabulary_)
clf = MultinomialNB()
clf.fit(X_train_tfidf, twenty_train.target)

twenty_test = fetch_20newsgroups(subset='test', shuffle=True)
X_test_tfidf = tfidf_Vect.transform(twenty_test.data)

predicted = clf.predict(X_test_tfidf)

score = metrics.accuracy_score(twenty_test.target, predicted)
print("TfidfVectorizer score: " + str(score))

#score for X_train_tfidf1
clf1 = MultinomialNB()
clf1.fit(X_train_tfidf1, twenty_train.target)

twenty_test = fetch_20newsgroups(subset='test', shuffle=True)
X_test_tfidf1 = tfidf_Vect1.transform(twenty_test.data)

predicted1 = clf1.predict(X_test_tfidf1)

score1 = metrics.accuracy_score(twenty_test.target, predicted1)
print("TfidfVectorizer score with ngram: " + str(score1))


#score for X_train_tfidf2
clf2 = MultinomialNB()
clf2.fit(X_train_tfidf2, twenty_train.target)

twenty_test = fetch_20newsgroups(subset='test', shuffle=True)
X_test_tfidf2 = tfidf_Vect2.transform(twenty_test.data)

predicted2 = clf2.predict(X_test_tfidf2)

score3 = metrics.accuracy_score(twenty_test.target, predicted2)
print("TfidfVectorizer score with english stop words: " + str(score3))