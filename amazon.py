import pandas as pd
import nltk 
import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
lematizer=WordNetLemmatizer() 


df=pd.read_excel('Amazon_reviews.xlsx',header=None,)
df.columns=['reviews','label']
#print(df)
## to print first 5rows:
print(df.head(10))
## to print last 5rows:
# print(df.tail(5))
# ## to print total columns:
# for col in df.columns:
#     print(col)
# ## to print total rows:
# pd.set_option('display.max_rows',None)
# print(df)
# ##to print inedx:
# print(df.index)
# ## to print dimensions:
# print(df.ndim)
## to print only reviews column:
#print(df.reviews)
## to remove special characters
df['reviews']=df['reviews'].str.replace('[&@#$]+','',regex=True)
print(df)
##Remove digits:
df['reviews']=df['reviews'].str.replace('[0-9]+','',regex=True)
print(df.head(10))
## Remove multiple spaces.
df['reviews']=df['reviews'].str.replace('[\s]+',' ',regex=True).str.strip()
print(df.tail(10))
## Remove html tags.
df['reviews']=df['reviews'].str.replace('[<>]+','',regex=True)
print(df.tail(5))
## lower()
df['reviews']=df['reviews'].str.lower()
print(df.tail(5))

# import nltk
# from nltk.corpus import stopwords

# # Download stopwords (only first time)
# nltk.download('stopwords')

# # Get the list of English stopwords
# stop_words = stopwords.words('english')

# # Print the total count and all stopwords
# print("Total Stopwords:", len(stop_words))
# print(stop_words)

## slpit()
df['reviews']=df['reviews'].str.split()
print(df.tail(5))
## stop words
stop_words=set(stopwords.words('english'))
cleaned_reviews=[]
for words in df['reviews']:
    filtered_words=[word for word in words if word not in stop_words]
    cleaned_reviews.append(filtered_words)
df['reviews']=cleaned_reviews
print(df.tail(5))
## Lemmatization
import nltk
nltk.download('wordnet')
lemmatized_reviews = []
for words in df['reviews']:
    lemmatized = [lematizer.lemmatize(word) for word in words]
    lemmatized_reviews.append(lemmatized)
df['reviews'] = lemmatized_reviews
print(df.tail(5))
##join
joined_reviews=[]
for words in df['reviews']:
    joined_reviews.append(' '.join(words))
df['reviews']=joined_reviews
print(df.tail(5))



