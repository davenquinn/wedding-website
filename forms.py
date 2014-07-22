from flask.ext.wtf import Form
from wtforms import TextField, IntegerField, TextAreaField, SubmitField
from wtforms.validators import Required, Email, Length, ValidationError

def no_robots(form, field):
    if len(field.data) is not 0:
        raise ValidationError("Sorry, you're a robot.")

class RSVPForm(Form):
      name = TextField('Name', [Required(), Length(5)])
      email = TextField('Email address',
          [Required(), Email()])
      factoid = TextField('Another form of ID', [no_robots])
      number = IntegerField(
          '# of Guests',
          [Required()],
          description="The number of guests in your party that plan to attend.")
      message = TextAreaField('Message', description="An optional message to send with your response!")
      submit = SubmitField("RSVP")
