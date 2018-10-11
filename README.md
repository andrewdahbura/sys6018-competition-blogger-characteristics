# sys6018-competition-blogger-characteristics
## SYS 6018 Kaggle 3
## C2-9

**NOTE** Please consult Blogger Prediction Jupyter notebook for final code, up until the regressions.  The regressions were done in the r file called rbloggers.  The other code files were uploaded as we worked collaboratively through the assignment.

## Team Roles

* Will Gleave: Data exploration, TFIDF, LDA
* Andrew Dahbura: Model selection, data cleaning, report writing (Git Hub coordinator)
* Kanika Dawar: Feature engineering, report writing

## train.csv

* This is the given training file in the Kaggle competition

## test.csv

* This is the given test file in the Kaggle competition

## Data Exploration, Feature Extraction:
* Number of words in the text
* Average length of words
* Proportion of stopwords
* Proportion of special characters
* Proportion of numbers
* Proportion of uppercase words
* Proportion of misspelt words
* Sentiment of the text
* Number of posts by each topic
* Count of posts by each gender
* Age distribution across dataset

## Cleaning steps:
* Convert the text to lowercase
* Trim spaces and remove punctuation
* Remove stop words
* Remove commonly occuring words
* Remove rare words
* Correct the spelling of the misspelt words
* Lemmatization (preferred over Stemming): converts the word into its root word, rather than just stripping the suffices

## TF-IDF:
* After dealing with term sparsity, we cross validated to determine the ideal value of (TF-IDF features).
* We tested for a wide range of values (10, 5000) and found 2000 to be the converging point.

## Sentiment Analysis:
* We attempted to use sentiment analysis using Textblob but it was not considered as a variable in our best score.

## Feature Selection:
* We used sentiment, topic, proportioned feature extractions, derived in EDA, and TF-IDF features and found out the TF-IDF variables to be the most relevant when it came to age prediction of the blogger.

## Statistical Methods Tested:
* OLS (Final method)
* Lasso
* Ridge

## Resources:
* Text eda, data cleaning and n-gram analysis
  http://rstudio-pubs-static.s3.amazonaws.com/206183_aa3b2e5280ab4cde910612ae44a3a78a.html

* Description of N-gram text classification algorithm
  http://odur.let.rug.nl/vannoord/TextCat/textcat.pdf

* How to deal with Text Data?
  https://www.analyticsvidhya.com/blog/2018/02/the-different-methods-deal-text-data-predictive-python/
