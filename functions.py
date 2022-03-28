import json

PATH_POST = 'posts.json'


def load_posts_from_json():
    with open(PATH_POST, 'r', encoding='utf-8') as file:
        list_posts = json.load(file)
    return list_posts


def uploads_posts(list_posts):
    with open(PATH_POST, 'w', encoding='utf-8') as file:
        json.dump(list_posts, file, indent=4, ensure_ascii=False)

