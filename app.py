from flask import Flask, render_template, request

app = Flask(__name__, static_folder='asetberharga')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    data = request.form.get('inputData')
    return render_template('result.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
