"# cmpe130_group1_spam_classifier"

Python Version: Python 3.6.1

The following python packages are required:
    beautifulsoup4==4.6.0
    bs4==0.0.1
    click==6.7
    cycler==0.10.0
    Flask==0.12.2
    itsdangerous==0.24
    Jinja2==2.10
    MarkupSafe==1.0
    matplotlib==2.1.0
    nltk==3.2.5
    numpy==1.13.3
    olefile==0.44
    pandas==0.21.0
    Pillow==4.3.0
    pyparsing==2.2.0
    python-dateutil==2.6.1
    pytz==2017.3
    six==1.11.0
    Werkzeug==0.13
    wordcloud==1.3.1

Jupyter Notebook
1. Jupyter Notebook is required to run the "Spam Detection.ipynb"
2. The cells can be run one-by-one, but can also be ran all at once.
3. Output is shown in below in their respective cells.

In order to run Flask app,
1. Clone Repo
2. Run command 
    1. if using Linux: "export FLASK_APP=app.py"
        1. Code may require certain packages be downloaded in order to run 
    2. if using Windows: "set FLACK_APP=app.py"
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
        3. Ham Word Frequency: displays top 100 words used in legitimate comments and how many times they appeared
        4. Spam Word Frequency: displays top 100 words used in spam comments and how many times they appeared.

The site can also be accessed at:
    https://youtube-spam-classifier.herokuapp.com/
