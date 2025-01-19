from flask import Flask, request, send_file

app = Flask(__name__)

# Endpoint para upload de arquivos
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return {"error": "No file provided"}, 400
    file = request.files['file']
    file.save(f"./uploads/{file.filename}")
    return {"message": "File uploaded successfully", "filename": file.filename}, 200

# Endpoint para download de arquivos
@app.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    try:
        return send_file(f"./uploads/{filename}", as_attachment=True)
    except FileNotFoundError:
        return {"error": "File not found"}, 404

if __name__ == '__main__':
    app.run(debug=True)