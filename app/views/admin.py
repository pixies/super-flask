from flask import Blueprint, render_template

admin = Blueprint('admin', __name__)

@admin.route('/admin')
def manager():
    return render_template('admin/index.html')
