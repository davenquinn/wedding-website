from flask_wtf import Form
from wtforms import TextField, IntegerField, TextAreaField, SubmitField
from wtforms.validators import Required, Email, Length, ValidationError

def no_robots(form, field):
    if len(field.data) is not 0:
        raise ValidationError("Sorry, you're a robot.")

def required(form, field):
    if field.data is None:
        raise ValidationError("This field is required.")

class RSVPForm(Form):
      name = TextField('Name', [Required(), Length(5)])
      email = TextField('Email address',
          [Required(), Email()])
      factoid = TextField('Another form of ID', [no_robots])
      number = IntegerField(
          '# of Guests',
          [required],
          description="The number of guests in your party that will be attending.")
      message = TextAreaField('Message', description="An optional message to send with your response!")
      submit = SubmitField("RSVP")
