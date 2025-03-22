# Assignment #2


First, I created an empty JSON file (email_classes.json) to contain the list of classes to be used in email classification. I updated `analyze.py` to read in email classes from this file, instead of being hard coded. 
![Alt text](/screenshots/email_classes_json.png?raw=true)

Next, I added an endpoint in `app.py` that allows users to either add classes or delete classes. 
![Alt text](/screenshots/update_classes.png?raw=true) 


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
