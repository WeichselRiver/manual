# example playground3


# upload
from flask import Flask, render_template, request, redirect
app = Flask(__name__)



@app.get("/")
def upload_image():

    return render_template("upload.html")

@app.post("/upload_files")
def upload_files():
    report = ""
    for f in request.files.getlist("files[]"):
        txt = f.read().decode("utf-8")
        report += txt

    print(report)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
    
"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <form enctype='multipart/form-data' method='POST' action='/upload_files'> 
        <input type='file' name='files[]' multiple/>
        <button type='submit'>Submit</button>
    </form>
    
    
</body>
</html>
"""
