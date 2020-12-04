import joblib


print('***** /\/\/\/\/\ run_model.py running /\/\/\/\/\*****')

# print('loading model')
# joblib_file = open('News_ish.pkl', 'rb')
# loaded_model = pickle.load(joblib_file)

# #loading the vectorizer
# print('loading vectorizer')
# joblib_vector_file = open('vectorizer.pkl', 'rb')
# loaded_vectorizer = pickle.load(joblib_vector_file)

# loading the model
print('loading model')
joblib_file = open('News_ish.pkl', 'rb')
loaded_model = joblib.load(joblib_file)

#loading the vectorizer
print('loading vectorizer')
joblib_vector_file = open('vectorizer.pkl', 'rb')
loaded_vectorizer = joblib.load(joblib_vector_file)