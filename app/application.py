from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from forms.register import RegisterThankful


app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
bootstrap = Bootstrap(app)


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
        return render_template('thanks.html', data=data)
    return render_template('register.html', form=registerform)


if __name__ == '__main__':
    app.run(debug=True)