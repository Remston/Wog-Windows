from flask import Flask
from utils import read_file, file_path, error

app = Flask(__name__)


@app.route("/")
def score_server():
    score = read_file(file_path, error)
    if score == error:
        error_html = f'''<html>
                        <head>
                            <title>Scores Game</title>
                        </head>
                        <body>
                            <h1>
                                Houston, we have a problem: <span id="error" style="color: red">{error}</span>
                            </h1>                        
                        </body>
                    </html>'''
        return error_html
    return_html = f'''<html>
                            <head>
                                <title>Scores Game</title>
                            </head>
                            <body>
                                <h1><div class="single-line">The score is: <span id="score">{score}</span></div></h1>
                            </body>
                        </html>'''
    return return_html


if __name__ == '__main__':
    app.run(host='0.0.0.0')
    # app.run(debug=True)
