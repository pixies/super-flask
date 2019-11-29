from flask import Blueprint, render_template
from forms.account import NewUserForm

account = Blueprint('accounts', __name__)

@account.route('/new')
def new_account():
    form = NewUserForm()
    return render_template('account/new_user.html')