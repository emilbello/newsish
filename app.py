# Import the functions we need from flask
from flask import Flask
from flask import render_template 
from flask import jsonify
from flask import request
import joblib
import run_model #Testing running model from another .py

# Show a start-up message
print('This is app.py')

# # loading the model
# print('loading model')
# joblib_file = "News_ish.pkl"
# loaded_model = joblib.load(joblib_file)

# #loading the vectorizer
# print('loading vectorizer')
# joblib_vector_file = "vectorizer.pkl"
# loaded_vectorizer = joblib.load(joblib_vector_file)



# Instantiate the Flask application. (Chocolate cake recipe.)
# This statement is required for Flask to do its job. 
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0 # Effectively disables page caching


# DEFINE APP ROUTES TO SPECIFIC PAGES

@app.route("/")
def IndexRoute():
    ''' This function runs when the browser loads the index route. 
        Note that the html file must be located in a folder called templates. '''
     # Open a session, run the query, and then close the session again
    gifpath = "../static/assets/meter-centered.gif"
    webpage = render_template("index.html", gifpath = gifpath)

    return webpage

@app.route('/run_model', methods=['POST'])
def run_model():

    input_message = request.form['user_input']
    print('User Input:')
    print(input_message)
    
    # final_message = 'Minnesota is reporting 45 new COVID-19 deaths and more than 9,000 coronavirus cases in an unusual release Saturday that covers two days worth of data. The latest figures cap a week when the number of COVID-19 deaths reported by the state each day fluctuated greatly. The Minnesota Department of Health reported 72 deaths for the 24-hour period ending at 4 p.m. on Tuesday, and a record 101 deaths reported for the 24-hour period ending at 4 p.m. Wednesday. For the 48-hour period ending Friday afternoon, the state reported fewer than 50 deaths. Funeral home directors and medical examiners need to file reports within five days of death, according to the Health Department. It’s possible they pushed to file reports before Thanksgiving, so they wouldn’t have to do so on the holiday weekend, said Kris Ehresmann, the state’s director for infectious diseases. It’s harder to say why the two-day totals released Saturday for new cases and completed tests were low, Ehresmann said, but the holiday could have influenced decisions about whether people sought testing. Throughout the pandemic, COVID numbers released on Mondays have tended to be lower due to reduced testing and reporting activity on weekends. With the latest figures, Minnesota has now seen 304,023 positive cases, 16,423 hospitalizations and 3,521 deaths since the pandemic arrived here in March. Residents of long-term care and assisted-living facilities accounted for 23 of the newly announced deaths, and 2,378 deaths since the start of the pandemic. The state’s two-day count of 9,040 new cases came on a low volume of 36,601 newly completed tests, according to the Star Tribune’s coronavirus tracker. Minnesota did not plan to update its dashboard for hospital capacity on Saturday, but the Star Tribune tracker shows 380 new admissions reported over the two-day period. The one-day figures on each of the last three Saturdays were 283, 271 and 201 new admissions. Daily reports of new admissions typically include patients who have entered the hospital at some point over the last several days — not just on the most recent day. Numbers released Saturday show health care workers have accounted for 22,292 positive cases — up by more than 200 cases from last week. More than 257,000 people who were infected no longer need to be isolated. COVID-19 is a viral respiratory illness caused by a new coronavirus that surfaced late last year. People at greatest risk include those 65 and older, residents of long-term care facilities and those with underlying medical conditions. Those health problems range from lung disease and serious heart conditions to severe obesity and diabetes. People undergoing treatment for failing kidneys also run a greater risk, as do those with cancer and other conditions where treatments suppress immune systems. Most patients with COVID-19 don’t need to be hospitalized. Most illnesses involve mild or moderate symptoms; many cases are asymptomatic.'
    
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

    # Tokenization and stop-words removal are now handled by the 
    # saved vectorizer. The following blocks can be removed.

    # # # split (tokenization)
    # message_pp = message_nospace.split()

    # # remove stopwords and join back into string space-separated
    # stop_words = [w for w in message_pp if w not in stopwords.words('english')]
    # message_stop_words_removed = ' '.join(stop_words)

    # convert the whole text to list
    list_test = [message_nospace] # Changed this because we no longer need to tokenize or remove stop words. 

    # classify reliable or unreliable
    vectorized_text = loaded_vectorizer.transform(list_test)
    result = loaded_model.predict(vectorized_text)
    # result = [0]

    reliability = " "
    gifpath = " "
    
    if result == [0]: 
        reliability = "Reliable"
        gifpath = "../static/assets/meter-reliable.gif"
    else :
        reliability = "Unreliable"
        gifpath = "../static/assets/meter-unreliable.gif"


    # Run the ML model 
    # article_status = run_model.get_reliablitiy()
    return render_template('index.html', reliability = reliability, gifpath = gifpath)

    
@app.route("/about")
def ChartsRoute():
    ''' This function runs when the browser loads the index route. 
        Note that the html file must be located in a folder called templates. '''
     # Open a session, run the query, and then close the session again

    webpage = render_template("about.html")

    return webpage

@app.route("/team")
def TeamRoute():
    ''' This function runs when the browser loads the index route. 
        Note that the html file must be located in a folder called templates. '''
     # Open a session, run the query, and then close the session again

    webpage = render_template("team.html")

    return webpage 

# This statement is required for Flask to do its job. 
# Think of it as chocolate cake recipe. 
if __name__ == '__main__':
    app.run(debug=True)