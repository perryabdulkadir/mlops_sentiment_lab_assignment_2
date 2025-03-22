# Assignment #2

## Approach
First, I created an empty JSON file (`email_classes.json`) to contain the list of classes to be used in email classification. I updated `analyze.py` to read in email classes from this file, instead of being hard coded. 
![Alt text](/screenshots/email_classes_json.png?raw=true)

Next, I added a POST endpoint in `app.py` that allows users to either add classes or delete classes. 
![Alt text](/screenshots/update_classes.png?raw=true) 

I also added a GET endpoint that allows users to check at a glance which classes are currently in `email_classes.json`.
![Alt text](/screenshots/get_classes.png?raw=true) 

## Demo
The user begins in a state with no classes. This can be checked with a CURL request to the `get-classes` endpoint. 
![Alt text](/screenshots/get_classes.png) 






Lab 1: Sentiment Analysis

Explore flask and huggingface transformers.

To run the app:
```
python app.py
```

To install the dependencies:
```
pip install -r requirements.txt
```
