from flask import render_template
from pathlib import Path
from datetime import datetime
from functools import partial
from flask.ext.mail import Mail, Message

def send_mail(app, form):
    debug = app.config["DEBUG"]
    test_recipients = ['test@davenquinn.com']

    mail = Mail(app)

    msg = Message("Thanks for your RSVP!",
        sender="mailer-daemon@davenquinn.com",
        reply_to="Daven and Beth <wedding@davenquinn.com>",
        extra_headers={"From":"Daven and Beth via davenquinn.com <mail@davenquinn.com>"})

    if debug:
        msg.recipients = test_recipients
    else:
        msg.recipients = [form["email"]]
        msg.bcc = test_recipients+["wedding@davenquinn.com"]

    _ = partial(render_template,
        form=form,
        attending=int(form["number"]) > 0)

    msg.body = _("wedding/email/thanks.txt")
    msg.html = _("wedding/email/thanks.html")
    mail.send(msg)

def complete_rsvp(app, form):
    send_mail(app, form)

    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    fn = "{0} {1}.txt".format(form["name"],time)
    directory = Path(app.config["STORAGE_BASE"])/"wedding-responses"

    try:
        directory.mkdir()
    except FileExistsError:
        pass
    p = directory/fn

    with p.open("w") as f:
        w = lambda s: print(s,file=f)
        w("Name: "+form["name"])
        w("Email:"+form["email"])
        w("No. attending: "+str(form["number"]))
        w("Message:")
        w(form["message"])
