from flask import Blueprint

github_view = Blueprint('github_view', __name__, url_prefix='/github')

@github_view.route('/')
def github_commits():
    print('registered')
    return 'commits'
