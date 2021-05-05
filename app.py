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
        V1 = float(V1)
        V2 = float(V2)

        print(V1)

        #result = 5
        result = calculation.result_calc(V1, V2)
        if result > 0:
            if result == 3:
                rec = "Buy"
            elif result == 2:
                rec = "Neutral"
            elif result == 1:
                rec = "No buy signal"
                

            return render_template('front.html', m1 = rec)
        else:
            render_tamplate('front.html')

@app.route('/info')
def info():
    return render_template('front2.html')



if __name__ == '__main__':
   app.run(host='0.0.0.0')


