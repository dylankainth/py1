from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])

def index():
  if request.method == 'POST':
    contents = request.form['content']
    with open('messages.csv', 'w', newline='') as file:
      writer = csv.writer(file)
      writer.writerow(contents)
    file.close()
    return redirect('/')
  else:
    return render_template('update.html')


if __name__ == "__main__":
    app.run(debug=True)
