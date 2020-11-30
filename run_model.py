import joblib
from nltk.corpus import stopwords

# loading the model
joblib_file = "News_ish.pkl"
loaded_model = joblib.load(joblib_file)
#loading the vectorizer
joblib_vector_file = "vectorizer.pkl"
loaded_vectorizer = joblib.load(joblib_vector_file)


# message from get.js is preprocessed and classified in this function
# input_message = something from get.js

# message from get.js is preprocessed in this function
def get_reliability(input_message):
    
    # if loaded model exist, don't load it again, if not, load it?????
    
    
    # variable, characters to be removed
    bad_char = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~', '—']
    
    message = input_message.lower()
    # removing possesives and contractions
    message = message.replace("'s","")
    # replacing '\n' with blank space
    message = message.replace('\n',' ')
    # removing special characters (regex)
    message_nochar = ''.join((filter(lambda i: i not in bad_char, message)))
    # # removing leading and trailing spaces
    message_nospace = message_nochar.strip()
    # # split (tokenization)
    message_pp = message_nospace.split()
    # remove stopwords and join back into string space-separated
    stop_words = [w for w in message_pp if w not in stopwords.words('english')]
    message_stop_words_removed = ' '.join(stop_words)
    # convert the whole text to list
    list_test = [message_stop_words_removed]
    # classify reliable or unreliable
    result = loaded_model.predict(loaded_vectorizer.transform(list_test))

    return result