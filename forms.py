from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError, Regexp
from models import User

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember')
    submit = SubmitField('Login')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[
        DataRequired(),
        Length(min=2, max=20),
        Regexp(r'^[\w.]+$', message='Username can only contain letters, numbers, dots and underscores')
    ])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is already registered. Please use a different one.')

class CheckoutForm(FlaskForm):
    address = StringField('Delivery Address', validators=[DataRequired()])
    phone = StringField('Phone Number', validators=[DataRequired()])
    payment_method = SelectField('Payment Method', 
                               choices=[('cash', 'Cash on Delivery'), 
                                      ('card', 'Credit/Debit Card')],
                               validators=[DataRequired()])
    submit = SubmitField('Place Order')
