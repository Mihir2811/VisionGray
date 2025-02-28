from flask import Flask, render_template, request
import cv2
import os

app = Flask(__name__)

UPLOAD_FOLDER = "Project 1/static/uploads"
GRAYSCALE_FOLDER = "Project 1/static/grayscale"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(GRAYSCALE_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    uploaded_image = None
    grayscale_image = None

    if request.method == "POST":
        file = request.files["image"]
        if file:
            filepath = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(filepath)

            # Convert to Grayscale
            image = cv2.imread(filepath)
            gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            grayscale_path = os.path.join(GRAYSCALE_FOLDER, "gray_" + file.filename)
            cv2.imwrite(grayscale_path, gray_image)

            uploaded_image = filepath
            grayscale_image = grayscale_path

    return render_template("index.html", uploaded_image=uploaded_image, grayscale_image=grayscale_image)

if __name__ == "__main__":
    app.run(debug=True)
