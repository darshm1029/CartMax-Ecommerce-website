from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError
from market.models import User

class RegisterForm(FlaskForm):

    def validate_username(self, username_to_check):
        user= User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('Username already exists')
    
    def validate_email_address(self, email_address_to_check):
        user= User.query.filter_by(email_address=email_address_to_check.data).first()
        if user:
            raise ValidationError('Email address already exists')


    username = StringField(label='User Name:', validators=[DataRequired(), Length(min=2, max=20)])
    email_address = StringField(label='Email Address:',validators=[DataRequired(), Email(message='Invalid Email Address')])
    password1 = PasswordField(label='Password:', validators=[DataRequired(), Length(min=6)])
    password2 = PasswordField(label='Confirm Password:', validators=[DataRequired(), EqualTo('password1')])
    submit = SubmitField(label='Create Account')

class LoginForm(FlaskForm):
    username = StringField(label='User Name:', validators=[DataRequired()])
    password = PasswordField(label='Password:', validators=[DataRequired()])
    submit = SubmitField(label='Sign In')

class PurchaseItemForm(FlaskForm):
    submit = SubmitField(label='Purchase item!')

class SellItemForm(FlaskForm):
    submit = SubmitField(label='Sell item!')