from flask import Blueprint, render_template, request, current_app, flash
from .forms import RSVPForm
from .rsvp import complete_rsvp

wedding = Blueprint('wedding', __name__,
        template_folder='templates',
        static_folder='static')

@wedding.route('/')
def index():
    return render_template('wedding/index.html')

@wedding.route('/details/')
def details():
    return render_template('wedding/details.html', active='.details')

@wedding.route('/story/')
def story():
    return render_template('wedding/story.html', active='.story')

@wedding.route('/rsvp/', methods=['GET', 'POST'])
def rsvp():
    form = RSVPForm(request.form)
    if request.method == "POST":
        if form.validate():
            try:
                complete_rsvp(current_app, request.form)
            except Exception as err:
                flash("There was an error submitting the form: "+str(err), "error")
            else:
                msg = """Your response was successfully processed!
                 You should receive an email confirmation at
                 {0}.""".format(request.form["email"])
                flash(msg,"success")
                return render_template('wedding/rsvp_form.html')
        return render_template('wedding/rsvp_form.html', form=form, active='.rsvp')
    else:
        return render_template('wedding/rsvp.html', form=form, active='.rsvp')
