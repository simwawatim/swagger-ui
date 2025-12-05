from flask import Flask, jsonify, render_template
from openapi_spec.custom_swagger import custom_swagger

app = Flask(__name__, template_folder="templates")

@app.route("/custom-swagger.json")
def swagger_json():
    return jsonify(custom_swagger)

@app.route("/swagger")
def swagger_ui():
    return render_template("swagger.html")

if __name__ == "__main__":
    app.run(debug=True)
