from flask import render_template, request, Blueprint
from functions import load_posts_from_json

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')


@main_blueprint.route("/")
def page_index():
    return render_template("index.html")


@main_blueprint.route("/search/")
def search_posts():
    search = request.args['s']
    list_posts = [x for x in load_posts_from_json() if search.lower() in x['content'].lower()]
    return render_template("post_list.html", search=search, list_posts=list_posts)
