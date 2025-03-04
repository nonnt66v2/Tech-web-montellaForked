from flask import Flask

app = Flask(__name__)


@app.route("/")
def root():
    html = '''
        <!doctype html>
        <html lang="en">
        <head>
            <meta charset="utf-8">
            <title>Hello World</title>
            <link rel="stylesheet" href="css/style.css">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <link rel="manifest" href="manifest.json">
            <meta name="theme-color" content="white"/>
        </head>
        <body class="fullscreen">
        <div class="container">
            <h1 class="title">Hello World!</h1>
        </div>
        <script src="js/main.js"></script>
        </body>
        </html>'''
    return html
