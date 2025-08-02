from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, ValidationError
from wtforms.validators import Length, EqualTo, Email, DataRequired
from market.models import User

class RegistorForm(FlaskForm):
    username = StringField(label='Username',validators =[Length(min=2, max=30), DataRequired()])
    email_address = StringField(label='Email Address', validators=[Email(), DataRequired()])
    password1 = PasswordField(label='Password',validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label='Confirm Password',validators=[EqualTo('password1', message='Passwords must match!'), DataRequired()])
    submit = SubmitField(label='Create Account')

    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError(f'Username "{username_to_check.data}" is already taken! Please choose a different one.')

    def validate_email_address(self, email_to_check):
        email = User.query.filter_by(email_address=email_to_check.data).first()
        if email:
            raise ValidationError(f'Email address "{email_to_check.data}" is already in use! Please choose a different one.')
        

class LoginForm(FlaskForm):
    username = StringField(label='User Name:',validators=[DataRequired()])
    password = PasswordField(label='Password:',validators=[DataRequired()])
    submit = SubmitField(label='Login')

class PurchaseItemForm(FlaskForm):
    submit = SubmitField(label='Purchase Item')

class SellItemForm(FlaskForm):
    submit = SubmitField(label='Sell Item')