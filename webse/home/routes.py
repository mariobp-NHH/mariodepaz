from flask import render_template, url_for, Blueprint
from webse import application
home= Blueprint('home', __name__)


###########################
####   Block 0. Home   ####
###########################
@home.route('/home')
@home.route('/')
def home_main():
    return render_template('home.html', title='Home')
