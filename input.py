from flask import Flask, render_template, request
from others import calculation
app = Flask(__name__)
@app.route('/')
def input():
    return render_template('front.html')

@app.route('/', methods = ['POST', 'POST'])
def input_handle():
    #if request.method == 'POST':
        V1 = request.form['A1']
        V2 = request.form['A2']
        #V1 = int(V1)
        #V2 = int(V2)

        print(V1)

        #result = 5
        #result = calculation.result_calc(V1calculation.result_calc(V1, V2), V2)
        return render_template('front.html', m1 = V1, m2 = V2)

@app.route('/info')
def info():
    return render_template('front2.html')



if __name__ == '__main__':
   app.run(debug = True)


