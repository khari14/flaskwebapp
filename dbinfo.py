from flask import Flask, render_template

app = Flask(__name__)

posts = [

    {
        'Name': 'Hari Kommineni',
        'Heading': 'Reference 1',
        'Content Type': 'Books',
        'Date': 'March 23,2029'

    },

    {
        'Name': 'Madhavi Boyapati',
        'Heading': 'Reference 2',
        'Content Type': 'Sheets',
        'Date': 'March 23,2012'

    }
]


@app.route('/')
@app.route('/home')
def hello_world():
    return render_template('layout.html')


@app.route('/about')
def about():
    return render_template('about.html', title='About')


if __name__ == "__main__":
    app.run(debug=True)
