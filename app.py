from flask import Flask, render_template, request
import google.generativeai as genai

genai.configure(api_key="AIzaSyC1kG93_X3o2B_w6CyjAM_KxnS7dCoXoZI")
model = genai.GenerativeModel('gemini-pro')

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_text', methods=['POST'])
def process_text():
    input_text = request.form['input_text']
    enhancement_type = request.form['enhancement_type']
    
    if enhancement_type == "summarization":
        prompt = "Summarize the following text without losing details >> \n"
        request1 = prompt + " " + input_text
        response1 = model.generate_content(request1)
        #print(response1)
        enhanced_text = response1.text
    elif enhancement_type == "spelling_correction":
        prompt = "Rewrite the following text by fixing the Spelling errors in it >> \n"
        request1 = prompt + " " + input_text
        response1 = model.generate_content(request1)
        #print(response1)
        enhanced_text = response1.text
    elif enhancement_type == "sentence_correction":
        prompt = "Correct the following sentence for grammar and syntax errors >> \n"
        request1 = prompt + " " + input_text
        response1 = model.generate_content(request1)
        #print(response1)
        enhanced_text = response1.text
    elif enhancement_type == "entity_extraction":
        prompt = "Identify and list all named entities in the given passage >> \n"
        request1 = prompt + " " + input_text
        response1 = model.generate_content(request1)
        #print(response1)
        enhanced_text = response1.text
    elif enhancement_type == "text_classification":
        prompt = "Determine the intent of the following sentence or the mood of the person which ever is relavent (e.g., inquiry, statement, request, angry, sad, happy) >> \n"
        request1 = prompt + " " + input_text
        response1 = model.generate_content(request1)
        #print(response1)
        enhanced_text = response1.text
        
    return render_template('index.html', input_text=input_text, enhanced_text=enhanced_text)

if __name__ == '__main__':
    app.run(debug=True)