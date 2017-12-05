"# cmpe130_group1_spam_classifier"

In order to run Flask app,
1. Clone Repo
2. Run command "export FLASK_APP=app.py"
    2a. Code may require certain packages be downloaded in order to run 
3. flask run
4. Open browser and go to http://localhost:5000/
5. Once web app opens,
    1. Enter a comment
    2. Click "Submit" to test comment
    3. Result will be displayed as "Spam" or "Ham"
       where "Spam" means it is considered a Spam comment and
        "Ham" means it is a legitimate comment.
    4. You may observe:
        1. Ham Word Cloud: displays words often used in legitimate comments. 
        2. Spam Word Cloud: displays words often used in spam comments
        3. Ham Word Frequency: displays all words used in legitimate comments and how many times they appeared
        4. Spam Word Frequency: displays all words used in spam comments and how many times they appeared.