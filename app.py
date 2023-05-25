from flask import Flask,render_template

app = Flask(__name__)
jobs = [
    {
        'id':1,
        'title':'Data Analyst',
        'location':'Ontario,Canada',
        'Salary':'$ 80,000 '
    },
    {
        'id':2,
        'title':'ML Dev',
        'location':'Victoria,Canada',
        'Salary':'$ 120,000 '
    },
    {
        'id':3,
        'title':'Web Developer',
        'location':'Ontario,Canada',
        'Salary':'$ 75,000 '
    },
    {
        'id':4,
        'title':'Game Developer',
        'location':'Los Angeles, USA',
        'Salary':'$ 110,000 '
    }
]
@app.route("/")
def hello_world():
    # return "<p>Hello, Woasdasd!</p>"
    return render_template('home.html',
                           jobs=jobs,
                           company_name='Jovia')

# @app.rout("/home.html")
# def html():
#     return render_template('home.html')

# if __name__ == "__main__":
#     app.run(host='0.0.0.0',debug=True)