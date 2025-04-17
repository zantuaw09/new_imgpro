from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = '''
<!doctype html>
<html>
    <head>
        <title>Leap Year Checker</title>
    </head>
    <body>
        <h1>Leap Year Checker</h1>
        <form method="post">
            <label for="year">Enter a year:</label>
            <input type="number" id="year" name="year" required>
            <button type="submit">Check</button>
        </form>
        {% if result %}
            <p><strong>{{ result }}</strong></p>
        {% endif %}
    </body>
</html>
'''

def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

@app.route('/', methods=['GET', 'POST'])
def home():
    result = ''
    if request.method == 'POST':
        try:
            year = int(request.form['year'])
            if is_leap_year(year):
                result = f"Year {year} is a leap year."
            else:
                result = f"Year {year} is not a leap year."
        except ValueError:
            result = "Invalid input. Please enter a valid year."
    return render_template_string(HTML_TEMPLATE, result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
