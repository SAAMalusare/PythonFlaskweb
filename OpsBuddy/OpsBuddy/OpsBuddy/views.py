"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import request, flash, url_for, redirect, render_template
from OpsBuddy import app
from OpsBuddy.forms import UserOpsForm, GetNodesForm, GetRMSForm, GetUserMapForm
from OpsBuddy.db import logonstats
from flask_login import login_user, current_user, logout_user, login_required


@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/userops')
def userops():
    form = UserOpsForm()
    return render_template('userops.html', title='User Administration', form=form, year=datetime.now().year)

@app.route("/getnodes", methods=['GET','POST'])
def getnodes():
    form = GetNodesForm()
    return render_template('getnodes.html', title='Get last accessed nodes', nodedata = logonstats.query.filter_by(acname=form.username.data).order_by("datetime desc"), username=form.username.data, form=form)

@app.route("/getrms", methods=['GET', 'POST'])
def getrms():
    form = GetRMSForm()
    return render_template('getrms.html', title='Get last accessed nodes', form=form)

@app.route("/getusermap", methods=['GET', 'POST'])
def getusermap():
    form = GetUserMapForm()
    return render_template('getusermap.html', title='Get last accessed nodes', form=form)

@app.route('/showall')
def show_all():
   return render_template('showall.html', nodedata = logonstats.query.all() )