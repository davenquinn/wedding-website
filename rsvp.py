from flask import render_template
from pathlib import Path
from datetime import datetime
from functools import partial
from flask.ext.mail import Mail, Message

def send_mail(app, form):
    """
    Send email confirmation of an RSVP response,
    both to myself and to the guest. If DEBUG
    is enabled, send responses to a testing
    address instead.
    """
    mail = Mail(app)

    msg = Message("Thanks for your RSVP!",
        sender="mailer-daemon@davenquinn.com",
        reply_to="Daven and Beth <wedding@davenquinn.com>",
        extra_headers={"From":"Daven and Beth via davenquinn.com <mail@davenquinn.com>"})

    if app.config["DEBUG"]:
        msg.recipients = ['test@davenquinn.com']
    else:
        msg.recipients = [form["email"]]
        msg.bcc = ["wedding@davenquinn.com"]

    _ = partial(render_template,
        form=form,
        attending=int(form["number"]) > 0)

    msg.body = _("wedding/email/thanks.txt")
    msg.html = _("wedding/email/thanks.html")
    mail.send(msg)

def save_file(app, form):
    """
    Save a file containing the response (if we have
    a STORAGE_BASE directory path defined in our
    configuration) because email is unreliable and
    I'm likely to make mistakes.
    """
    path = app.config.get("STORAGE_BASE", None)
    if path is None: return

    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    fn = "{0} {1}.txt".format(form["name"],time)
    directory = Path(path)/"wedding-responses"

    try:
        directory.mkdir()
    except FileExistsError:
        pass

    with (directory/fn).open("w") as f:
        w = lambda s: print(s,file=f)
        w("Name: "+form["name"])
        w("Email:"+form["email"])
        w("No. attending: "+str(form["number"]))
        w("Message:")
        w(form["message"])

def complete_rsvp(app, form):
    save_file(app, form)
    send_mail(app, form)

