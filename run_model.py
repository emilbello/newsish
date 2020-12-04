import joblib

# loading the model
print('loading model')
joblib_file = "News_ish.pkl"
loaded_model = joblib.load(joblib_file)

#loading the vectorizer
print('loading vectorizer')
joblib_vector_file = "vectorizer.pkl"
loaded_vectorizer = joblib.load(joblib_vector_file)