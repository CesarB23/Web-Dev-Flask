from flask import Flask, render_template, jsonify, request
from db import load_jobs_fromdb, load_job_fromdb, add_application_to_db

app = Flask(__name__)

@app.route("/")
def hello_world():
    jobs = load_jobs_fromdb()
    return render_template("home.html",
                           jobs=jobs, 
                           company_name="Computer Science")


@app.route("/api/jobs")
def list_jobs():
    jobs = load_jobs_fromdb()
    return jsonify(jobs)

@app.route("/jobs/<id>")
def show_jobs(id):
    job = load_job_fromdb(id)
    # return jsonify(job)
    if not job:
        return "Not Found", 404
    return render_template('jobpage.html',
                           job=job)
    
@app.route("/job/<id>/apply", methods=['post'])
def apply_to_job(id):
    data = request.form
    # return jsonify(data)
    job = load_job_fromdb(id)
    add_application_to_db(id,data)
    return render_template('application_submited.html',
                           application=data,
                           job=job)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
