from flask import Flask, redirect, url_for, jsonify
app = Flask(__name__)

#static routing
@app.route("/hello")
def hello_world():
    return "Hello World"


#dynamic routing
@app.route("/user/<username>")
def user(username):
    return f"Welcome {username}!!"

@app.route("/post/<int:post_id>")
def post_number(post_id):
    return f"This is a post number: {post_id}"

#url rule handler
def contact():
    return f"This is a contact page"

app.add_url_rule('/conatct', view_func=contact)

@app.route("/new-home")
def new_home():
    return redirect(url_for('home'))

@app.errorhandler(404)
def not_found(e):
    return jsonify({
        "error": "404 not found",
        "message": "The requested url not found"
    })

@app.errorhandler
def internal_server_error(e):
    return jsonify({
        "error": "Internal server error",
        "message": "Something went wrong"
    })

if __name__ == "__main__":
    app.run(debug=True)