from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

app = Flask(__name__)


class LoginForm(FlaskForm):
    email = StringField(label='Email',
                        validators=[DataRequired(),
                                    Email(message="Invalid Email Address",
                                          check_deliverability=True)])
    password = PasswordField(label='Password',
                             validators=[DataRequired(),
                                         Length(min=8,
                                                message="Password Should Be Between 8-30 Characters")])
    login = SubmitField(label="Login")

app.secret_key = "hi"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login_page():
    login_form = LoginForm(app.secret_key)
    if request.method == "POST":
        print(f"{request.method}")
        print(f"{login_form.validate_on_submit()}")
        print(f"{login_form.email.data} ")
        print(f"{login_form.password.data} ")
        print("im editing this")
    return render_template('login.html', form=login_form)


if __name__ == '__main__':
    app.run(debug=True)
