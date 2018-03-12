#Train
import pandas as pd
from sklearn import cross_validation
from sklearn.linear_model import SGDClassifier
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB

#Import Data
data = pd.read_csv('/Users/.../data.csv')
data = data.dropna()

#Init Train and Test Samples
X = data.comment
y = data.sub_class_number
X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size = 0.2)

#Build Pipeline - SVM
text_clf = Pipeline([('vect', CountVectorizer(stop_words='english')),
                         ('tfidf', TfidfTransformer()),
                         ('clf', SGDClassifier(loss='hinge', penalty='l2',
                                               alpha=1e-3, random_state=42,
                                               max_iter=10, tol=None))])

#Fit the model
text_clf.fit(X_train, y_train)

#Calculate Accuracy
accuracy = text_clf.score(X_test, y_test)
print (accuracy)

#Prediction
data_all = pd.read_csv("/Users/.../six_months_data.csv")
data_all = data_all.dropna()

#Remove Non-ASCII Charecters
strings = data_all.comment
modified_comments = []
import string
printable = set(string.printable)
for s in strings:
    modified_comments.append(filter(lambda x: x in printable, s))
    
#Predict - Classify on Test data
predicted = text_clf.predict(modified_comments)

#Export to CSV
cols = ['comment','predicted']
df = pd.DataFrame(columns=cols)
for i in range(len(modified_comments)):
    df.loc[i] = [modified_comments[i], predicted[i]]
df.to_csv("Output.csv")
