from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from diagnosis_model import get_diagnosis_and_treatment

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class DiagnosisLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    symptoms = db.Column(db.String(200))
    diagnosis = db.Column(db.String(100))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/diagnose', methods=['POST'])
def diagnose():
    symptoms = request.json.get('symptoms', [])
    diagnosis, treatments = get_diagnosis_and_treatment(symptoms)
    log = DiagnosisLog(symptoms=",".join(symptoms), diagnosis=diagnosis)
    db.session.add(log)
    db.session.commit()
    return jsonify({'diagnosis': diagnosis, 'treatments': treatments})

if __name__ == '__main__':
    with app.app_context():
       db.create_all()
    app.run(debug=True)
