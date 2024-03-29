import os

from flask import Flask, render_template, request
from ocr_implementation import getTextFromImage

UPLOAD_FOLDER = '/static/uploads/'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app = Flask(__name__)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


#Está definido como get y post para que esta misma se encargue de procesar la imagen y dar el resultado
@app.route('/', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        if 'file' not in request.files:
            return render_template('upload.html', msg='Ninguna imagen ha sido seleccionada')
        file = request.files['file']
        # opción por defecto cuando el usuario no selecciona una imagen
        if file.filename == '':
            return render_template('upload.html', msg='Ninguna imagen ha sido seleccionada')

        if file and allowed_file(file.filename):
            file.save(os.path.join(os.getcwd() + UPLOAD_FOLDER, file.filename))

            # se creó getTextFromImage  para desligar la responsabiliad del procesamiento de la imagen
            extracted_text = getTextFromImage(file)

            # Se muestra el texto de la imagen procesada
            return render_template('upload.html',
                                   msg='Imagen procesada',
                                   extracted_text=extracted_text,
                                   img_src=UPLOAD_FOLDER + file.filename)
    elif request.method == 'GET':
        return render_template('upload.html')

if __name__ == '__main__':
    app.run()
