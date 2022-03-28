from flask import render_template, request, Blueprint
from functions import load_posts_from_json, uploads_posts

loader_blueprint = Blueprint('loader_blueprint', __name__, url_prefix='/post', static_folder='static', template_folder='templates')


@loader_blueprint.route("/form/")
def page_form():
    return render_template("post_form.html")


@loader_blueprint.route("/upload/", methods=["GET", "POST"])
def upload():
    try:
        file = request.files['picture']
        filename = file.filename
        content = request.values['content']
        list_posts = load_posts_from_json()
        list_posts.append({
            'pic': f'/uploads/images/{filename}',
            'content': content
        })
        uploads_posts(list_posts)
        file.save(f'uploads/images/{filename}')
    except FileNotFoundError:
        return "<h1> Файл не найден </h1>"
    else:
        return render_template('post_uploaded.html', pic=f'/uploads/images/{filename}', content=content)
