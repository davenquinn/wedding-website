from flask import Blueprint, render_template, request
from .forms import RSVPForm

wedding = Blueprint('wedding', __name__, template_folder='templates')

@wedding.route('/')
def index():
    return render_template('wedding/index.html')

@wedding.route('/details/')
def details():
    return render_template('wedding/details.html')

@wedding.route('/rsvp/', methods=['GET', 'POST'])
def rsvp():
    form = RSVPForm(request.form)
    if request.method == "POST":
        if form.validate():
            return "<p class='success'>Congratulations, you've successfully RSVPd</p>"
        else:
            return render_template('wedding/rsvp_form.html', form=form)
    return render_template('wedding/rsvp.html', form=form)
