from flask import Flask, render_template, request

app = Flask(__name__)

from classifier import *

@app.route('/', methods = ['GET', 'POST'])
def welcome():
    if request.method == 'POST':
        comment = request.form['comment']
        label = 'Spam' if classifier(comment) else 'Ham'
        return render_template('home.html',
                                comment=comment,
                                label=label,
                                results=True)
    return render_template('home.html',
                            results=False)

if __name__ == "__main__":
        app.run(port=5000)
