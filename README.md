# News-ish

**Team Members :** <br>
_Emilio Bello_ <br>
_Allan Hunt_ <br>
_Alex Mogren_ <br>
_Matt Mead_

**TO RUN MODEL LOCALLY**

[CLICK HERE FOR INSTRUCTIONS ON RUNNING MODEL LOCALLY](#run-model-locally)

**Machine Learning Project Overview | Fake News Detector :**

Using natural language processing and Naive Bayes, this project will analyze a dataset of news articles that have been labeled as ‘unreliable’ or ‘reliable’ and build a model to predict **_reliability_**.

_Our project is a machine learning exercise in which we used a Naïve Bayes classification model to determine whether a news article is considered a reliable source of information. We utilized Naïve Bayes to build our model to predict these news sources as “unreliable” or “reliable”. Using Naïve Bayes, we determined which words in these articles were more commonly found in unreliable versus reliable, this was the base for our model to make predictions. Our website features a user input search bar on our home page in which you can input your own article to determine whether it is a reliable information source._

**Dataset :** 

The dataset we've selected is from an _InClass Prediction Competition_ found on [Kaggle.com](https://www.kaggle.com/c/fake-news/data) with 20k+ datapoints. The models attempted were borrowed from those submissions as well as examples from the **_University of Minnesota Data and Visualization Bootcamp 2020_**.

# Models

**Naive Bayes**

_Naïve Bayes is a supervised machine learning classifier. Naïve Bayes is noted for being a fast algorithm and being fairly accurate with predicting outcomes and works very well predicting natural language processing (NLP) problems, our project is a NLP problem. We used Naïve Bayes to predict whether or not a news article can be classified as “reliable” or “unreliable” based on certain texts pertaining to their respective “tag words”. Naïve Bayes combines both probability and Bayes’ Theorem to predict the outcome of a text, then categorizes it to a tag word. A good example of Naïve Bayes classification is categorizing emails into “Primary” or “Spam” inboxes based on the text of the email. To put Naïve Bayes simply, “tag words” is synonymous with “categories” and we are trying to decipher snippets of text that can be put into these categories. For the texts, we used the title of the article, the body of the article and a combination of both the title and body of the article to explore the different outcomes and accuracy._

# Analysis

_This is where we can add our analysis_

# Run Model Locally

To run this model on your local server follow these instructions:

1. Create your virutal environment:

    a. Open a GitBash or Terminal window
    
    b. conda create -n newsish python=3.6

    c. source activate newsish

    d. conda install pip

    e. pip install pandas

    f. pip install flask

    g. pip install joblib

    h. pip install -U scikit-learn

    i. Close the GitBash or Terminal window

    
2. Clone the news-ish repository to your computer
3. Right click the news-ish folder and Open a GitBash or Terminal window
4. source activate newsish
5. python app.py
6. Once the program is running open a Chrome browser and go to http://127.0.0.1:5000/

