from flask import Flask, render_template

app = Flask(__name__,template_folder='project')

@app.route('/')
def index():
    return 'Hi!'

@app.route('/main/')
def main():
    content = {'title': 'Главная'}
    return render_template('main.html', **content)

@app.route('/data/')
def data():
    content = {'title': 'Обувь'}
    return render_template('data.html', **content)

@app.route('/jacket/')
def data():
    content = {'title': 'Куртка'}
    return render_template('jacket.html', **content)

if __name__ == '__main__':
    app.run(debug=True)