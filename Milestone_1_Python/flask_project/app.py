#  python -m venv myenv --> Add environment
# . myenv/Scripts/activate --> Activate environment
# pip list --> see all the installed packages
# pip freeze > requirements.txt --> Lists everything in requirements.txt



from flask import Flask, render_template, jsonify
import analysis

app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template('index.html')


@app.route('/get_player_name')
def get_player_name():
    a = analysis.analyze_data()
    return jsonify(a.tolist())


if __name__ == "__main__":
    app.run(debug=True)