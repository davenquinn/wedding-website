from flask.ext.wtf import Form
from wtforms import TextField, IntegerField, TextAreaField, SubmitField
from wtforms.validators import Required, Email

class RSVPForm(Form):
      name = TextField('Name', [Required()])
      email = TextField('Email address', [Required(), Email()])
      number = IntegerField('Number of Guests')
      message = TextAreaField('Message')
      submit = SubmitField("Go!")
