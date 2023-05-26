from flask import Flask,render_template,jsonify

app = Flask(__name__)
jobs = [
    {
        'id':1,
        'title':'Data Analyst',
        'location':'Ontario,Canada',
        'salary':'$ 80,000 '
    },
    {
        'id':2,
        'title':'ML Dev',
        'location':'Victoria,Canada',
        'salary':'$ 120,000 '
    },
    {
        'id':3,
        'title':'Web Developer',
        'location':'Ontario,Canada',
        'salary':'$ 75,000 '
    },
    {
        'id':4,
        'title':'Game Developer',
        'location':'Los Angeles, USA',
        # 'salary':'$ 110,000 '
    }
]
@app.route("/")
def hello_world():
    return render_template('home.html',
                           jobs=jobs,
                           company_name='Jovian')
@app.route("/api/jobs")
def list_jobs():
    return jsonify(jobs)

if __name__ == "__main__":
     app.run(host='0.0.0.0',debug=True)