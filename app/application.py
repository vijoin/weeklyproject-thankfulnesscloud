import os
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_pymongo import PyMongo
from forms.register import RegisterThankful


app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
bootstrap = Bootstrap(app)

app.config['MONGO_URI'] = os.environ.get('MONGO_URI')
mongo = PyMongo(app)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    registerform = RegisterThankful()
    if registerform.validate_on_submit():
        data = {
            'name': registerform.name.data,
            'age': registerform.age.data,
            'description': registerform.description.data,
        }
        mongo.db.thankfulness.insert_one(data)
        return render_template('thanks.html', data=data)
    return render_template('register.html', form=registerform)

@app.route('/results')
def results():
    thankfulness_descriptions = mongo.db.thankfulness.find({})
    return render_template('results.html', data=thankfulness_descriptions)

if __name__ == '__main__':
    app.run(debug=True)