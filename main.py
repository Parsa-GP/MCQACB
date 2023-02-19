''' Generated with ChatGPT '''
from difflib import SequenceMatcher
from ast import literal_eval
import requests as req

# Define a function that compares two strings and returns a value between 0 and 1 that indicates the degree of similarity. 
def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()
request = req.get("http://raw.githubusercontent.com/Parsa-GP/MCQACB/main/api.json", timeout=5)

if request.status_code==200:
    qa = literal_eval(request.text)
else:
    qa = {
        "What is your name?": "My name is Chatbot.", 
        "How are you?": "I'm doing well, thank you.", 
        "Is database updated?": "No, It doesn't.\n the qestion's are loaded from default database.\nplease go online and refresh the database.\nthanks a lot.", 
        "What can you do?": "I can answer questions about myself." 
    }

while True:
     # Ask the user a question. 
    question = input("? ")

     # Initialize the maximum similarity score to 0.45.
    max_similarity = 0.45

     # Initialize the best matching question to None. 
    best_match = None

     # Loop through all the questions in our dictionary. 
    for q, a in qa.items():

         # Calculate the similarity score between the user's question and the current question we're looping over. 
        similarity = similar(question, q)

         # If this similarity score is higher than the maximum we've seen so far... 
        if similarity > max_similarity:

             # Update our maximum similarity score and best matching question accordingly. 
            max_similarity = similarity  
            best_match = q

     # If we found a matching question...                (i.e., if best_match is not None)  
    if best_match:

         # Print out our answer to the user's question.   (qa[best_match] retrieves the answer from our dictionary.)  
        print(qa[best_match])
