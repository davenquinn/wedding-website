from flask import Blueprint, render_template, request, current_app, flash
from pathlib import Path
from datetime import datetime
from .forms import RSVPForm

wedding = Blueprint('wedding', __name__, template_folder='templates')

def complete_rsvp(app, form):
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    fn = "{0} {1}.txt".format(form["name"],time)
    p = Path(app.config["STORAGE_BASE"])/"wedding-responses"/fn
    with p.open("w") as f:
        w = lambda s: print(s,file=f)
        w("Name: "+form["name"])
        w("Email:"+form["email"])
        w("No. attending: "+str(form["number"]))
        w("Message:")
        w(form["message"])

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
            try:
                complete_rsvp(current_app, request.form)
            except Exception as err:
                flash("There was an error submitting the form: "+str(err), "error")
            else:
                flash("Congratulations, you've successfully RSVPd","success")
                return render_template('wedding/rsvp_form.html')
        return render_template('wedding/rsvp_form.html', form=form)
    else:
        return render_template('wedding/rsvp.html', form=form)
