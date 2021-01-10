from flask import redirect, g, request, Blueprint, render_template, url_for, abort, flash

from . import auth
from . import db
bp = Blueprint('blog', __name__)


@bp.route('/')
@auth.login_required
def index():
    db_ = db.get_db()
    rv = db_.execute(
        'SELECT * FROM blog INNER JOIN user on blog.author_id=user.id').fetchall()

    return render_template('blog/index.html', datas=rv)


@bp.route('/create', methods=('GET', 'POST'))
@auth.login_required
def create():
    error = None
    if request.method == 'POST':
        titile = request.form['title']
        body = request.form['body']

        if titile is None:
            error = 'Title is empty'
        elif body is None:
            error = 'Body is empty'

        db_ = db.get_db()
        db_.execute(
            "INSERT INTO blog(author_id,title,body) VALUES (?,?,?);", (g.user['id'], titile, body))
        db_.commit()
        return redirect(url_for('blog.index'))
    flash(error)
    return render_template('blog/create.html')


@bp.route('/edit/<int:id>', methods=('GET', 'POST'))
@auth.login_required
def edit(id):
    blog = get_blog(id)
    error = None
    if request.method == 'POST':
        titile = request.form['title'].strip()
        body = request.form['body'].strip()

        if titile is None:
            error = 'Title is none'
        elif body is None:
            error = 'Body is empty'
        elif titile == '':
            error = 'Title is empty'

        if error is None:
            db_ = db.get_db()
            db_.execute(
                "UPDATE blog SET title=?, body=? WHERE id=?;", (titile, body, id))
            db_.commit()
            return redirect(url_for('blog.index'))

        flash(error)
    return render_template('blog/edit.html', data=blog)


def get_blog(id):
    blog = db.get_db().execute(
        "SELECT BLOG.* FROM blog INNER JOIN user on blog.author_id=user.id WHERE blog.id=?", (id,)).fetchone()

    if blog is None:
        abort(404, 'Blog is not found')

    return blog


@bp.route('/delete/<int:id>', methods=('GET', 'POST'))
@auth.login_required
def delete(id):
    blog = get_blog(id)

    db_ = db.get_db()
    db_.execute(
        "DELETE FROM blog WHERE id= ?;", (int(id),))
    db_.commit()

    return redirect(url_for('blog.index'))
