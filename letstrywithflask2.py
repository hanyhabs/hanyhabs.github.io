from flask import Flask, request, render_template
import openai

app = Flask(__name__)
# app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0 # naaaahhhh no use
# app.static_folder = 'static' # problem solved .... not required...

key_value_pairs = {
    "Process to Follow": "what legal process needs to be followed for the above input in Indian jursdiction. Do not write contact or consult a lawyer in the output",
    "Best Narrative": "For the above input what will be the best narrative to present the case strongly in Indian jurisdiction. what extra evidences can I add. Do not write contact or consult a lawyer in the output",
    "Case citation": "for the above input what are some similar cases that I can refer too in Indian jursidiction. Do not write contact or consult a lawyer in the output",
    "List of evidence": "for the above input what are the evidences that I can provide to make my case stronger in Indian jurisdiction. Do not write contact or consult a lawyer in the output",
    "Acts and Sections": "for the above input what are the acts and sections applicable to make my case stronger in the Indian jursidiction. Do not write contact or consult a lawyer in the output",
    "Predict result": "Can I win the case if I file a complaint for the above description in Indian jursidiction. Do not write contact or consult a lawyer in the output",
    "Time required": "Ideally what is the time needed in years for such type of cases to get final verdict from the courts, refer NJDC site data for Mumbai India. Do not write contact or consult a lawyer in the answer"
}

openai.api_key = "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"

@app.route('/')
def index():
    return render_template('index.html') #index one was simple, 2 is the latest

@app.route('/index.html')
def index2():
    return render_template('index.html')

@app.route('/main.html')
def index3():
    return render_template('main.html')

"""
@app.route('/ask', methods=['POST'])
def ask():
    text = request.form['text']
    key = request.form['key']
    prompt = text + "/n " + key_value_pairs[key]
    response = openai.Completion.create(
        engine = "text-davinci-003",
        prompt = prompt,
        temperature = 0.8,
        max_tokens = 250,
    )
    return render_template('indexandresp.html', response=response.choices[0].text)
"""

@app.route('/ask', methods=['POST'])
def ask():
    scenario_text = request.form['scenario_text']
    evidence_text = request.form['evidence_text']
    demands_text = request.form['demands_text']
    key = request.form['key']
    prompt = "Case Scenario:\n" + scenario_text + "\nEvidences:\n" + evidence_text + "\nDemands:\n" + demands_text + "\n\n" + key_value_pairs[key]
    print(prompt)
    response = openai.Completion.create(
        engine = "text-davinci-003",
        prompt = prompt,
        temperature = 0.8,
        max_tokens = 250,
    )
    return render_template('main.html', response= response.choices[0].text)
    #return render_template('main.html', response = "Filing a complaint with the police and providing the evidence of the bike number may increase the chances of recovering your stolen wallet. However, the outcome of the case will depend on various factors such as the effectiveness of the investigation, availability of witnesses, and the strength of the evidence presented. It's advisable to cooperate with the authorities and provide them with all the relevant information to assist them in their investigation.")

if __name__ == '__main__':
    app.run(debug=True)