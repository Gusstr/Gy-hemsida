from flask import Flask, render_template, request, redirect

app = Flask(__name__)
@app.route('/', methods = ['GET'])
def input():
    return render_template('front.html')


if __name__ == '__main__':
   app.run(debug = True)


print("hello world")