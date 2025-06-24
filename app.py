from flask import Flask, render_template, request
import joblib
import os

app = Flask(__name__)
model = joblib.load(os.path.join('model', 'spam_model.pkl'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    message = request.form.get('message')
    
    if not message:
        return render_template('result.html', prediction="⚠️ No message provided!", label_class="spam")
    
    prediction = model.predict([message])[0]
    
    if prediction == 1:
        result = "🔴 This is a SPAM message!"
        label_class = "spam"
    else:
        result = "🟢 This is NOT a spam message."
        label_class = "ham"
    
    return render_template('result.html', prediction=result, label_class=label_class)

if __name__ == '__main__':
    app.run(debug=True)
