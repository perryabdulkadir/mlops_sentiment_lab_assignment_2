# Assignment #2
Perry Abdulkadir

SEIS 765 - ML Ops

## Approach
First, I created an empty JSON file (`email_classes.json`) to contain the list of classes to be used in email classification. I updated `analyze.py` to read in email classes from this file, instead of being hard coded. 
![Alt text](/screenshots/email_classes_json.png?raw=true)

Next, I added a POST endpoint in `app.py` that allows users to either add classes or delete classes. 
![Alt text](/screenshots/update_classes.png?raw=true) 

I also added a GET endpoint that allows users to check at a glance which classes are currently in `email_classes.json`.
![Alt text](/screenshots/get_classes.png?raw=true) 

## Demo
First, the user must  install dependencies. 
```
pip install -r requirements.txt
```
Next, to start, the app: 
```
python app.py
```
The user begins in a state with no classes. This can be checked with a CURL request to the `get-classes` endpoint. 
![Alt text](screenshots/get_classes_1.png) 

Next, the user sends the classes they wish to use in email classification to the `update-classes` endpoint. In this case, animals, sports, food, art, politics, and advertisements.
![Alt text](/screenshots/add_classes.png) 

When the user sends a request to `get-classes` again, we see that the JSON has been updated. 
![Alt text](/screenshots/get_classes_2.png) 

Running the `classify` endpoint, the user inputs the text "Elephant". We can see the resulting probability of belonging to each category. Unsurprisingly, the category with the highest similarity is "Animals". 
![Alt text](/screenshots/classify_1.png) 

We can also use the `update-classes` endpoint to delete classes from the JSON file. Say, for example, we want to remove "Advertisements" and "Sports" as categories.
![Alt text](/screenshots/classes_deleted.png) 

When we check the classes in the JSON, we see that "Advertisements" and "Sports" have been removed, as expected. 
![Alt text](/screenshots/get_classes_3.png) 

With this updated set of classes, the user can run another piece of text to be classified. Now, we'll try "My favorite thing to eat is cheese." As expected, "Food" is the category with the highest similarity. 
![Alt text](/screenshots/classify_2.png) 

With this system, a user can extend to as many classification categories as they like. 
