from flask import Flask, request, render_template
from AI_interaction import answer_question

app = Flask(__name__)

@app.route('/ask', methods = ["POST"])
def do_ask() -> "html":
    title = "Here are your answers!"
    input_string = request.form['input_string']
    results = answer_question(input_string)
    return render_template('results.html', 
                           the_title = title,
                           the_input_string = input_string,
                           the_results = results,)
@app.route('/')
@app.route('/entrypage')
def entry_page() -> "html":
    return render_template('entry.html', the_title = "Welcome to our lame Q&A")

app.run(debug = True) 