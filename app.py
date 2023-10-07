from flask import Flask, request, jsonify
from unstructured.partition.pdf import partition_pdf
from werkzeug.utils import secure_filename
import os
import uuid
import traceback
from datetime import datetime

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = '/app/'


@app.route('/', methods=['POST'])
def partition_pdf_route():
    try:
        if 'file' not in request.files:
            return jsonify({'status': 'error', 'errormsg': 'No file part in the request'})
        file = request.files['file']
        if file.filename == '':
            return jsonify({'status': 'error', 'errormsg': 'No file selected for uploading'})

        if file:
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            elements = partition_pdf(filepath)

            output = []
            for el in elements:
                output.append({
                    'text': str(el),
                    'type': el.__class__.__name__,
                    'metadata': el.metadata.to_dict()  # Adding metadata to each element
                })

            file_name, file_extension = os.path.splitext(filename)

            response = {
                'filename': filename,
                'file_extension': file_extension,
                'timestamp': datetime.utcnow().isoformat(),
                'uuid': str(uuid.uuid4()),
                'output': output,
                'status': 'ok',
                'document_metadata': {   # Add document-specific metadata here
                }
            }
            return jsonify(response)

    except Exception as e:
        return jsonify({'status': 'error', 'errormsg': str(e), 'trace': traceback.format_exc()})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
