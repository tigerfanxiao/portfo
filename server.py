from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
import csv

app = Flask(__name__)


@app.route('/')
def my_home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def navigate_page(page_name):
    return render_template(page_name)


def write_to_file(data):
    with open('database.csv', newline='\n', mode='a') as csvfile:
        # define a header
        fieldnames = ['email', 'subject', 'message']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        # # writer header to the csv file
        # writer.writeheader()
        writer.writerow(data)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_file(data)
        return redirect('thankyou.html')
    else:
        return 'something went wrong, try again!'


if __name__ == '__main__':
    app.run(debug=True)
