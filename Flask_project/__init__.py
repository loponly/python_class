from flask import Flask, request, render_template
from Flask_project.unegui_scrap import Unegui

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route('/',  methods=('GET', 'POST'))
def index():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        print(list(request.form.keys()))
        return render_template('index.html', data=request.form)
    return 'Now Allowed'

# some data


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/unegui')
@app.route('/unegui/<index>')
def unegui(index=None):
    for i, obj in enumerate([Unegui('/l-hdlh/l-hdlh-zarna/')]):
        obj.filename = f'output_{i}.csv'
        data = obj.run()
    if index:
        return render_template('unegui.html', data=data[int(index)])
    return render_template('unegui.html', data=data[0])


@app.route('/data_enter')
def data_enter():
    return render_template('data_enter.html')


@app.route('/api/get_data')
def get_data():
    return {
        'data': 'data1'
    }


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.before_first_request
def logggin():
    print('loggin')
    print(request)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('not_found.html'), 404
