## Introduction

This project showcases the implementation of a high-level document processing API using Flask, a popular Python web framework. It leverages the `unstructured-io` machine learning library for processing and analyzing documents in a variety of formats.

The API follows a service-oriented architecture and runs inside a Docker container for increased portability and easier deployment. Furthermore, it employs Gunicorn ('Green Unicorn'), a Python WSGI HTTP Server for UNIX, which offers superior load balancing and increased performance compared to Flask's default server when serving multiple simultaneous requests.

To sum up, the core components of the project are:

1. **Flask** - It acts as our web framework, enabling us to define routes/endpoints for our service and handle requests/responses.
    
2. **unstructured-io** - A library that uses machine learning techniques to process, analyze and extract valuable insights from unstructured documents.
    
3. **Docker** - Aims for simplifying deployment by creating a standardized unit (referred to as a container) for our software including all dependencies it needs to run.
    
4. **Gunicorn** - Used as our WSGI HTTP Server in place of the default Flask server for handling multiple simultaneous requests more efficiently.
    

Through this project, we aim to expose a high-level, easy-to-use API endpoint for document processing. This can be utilized in a range of applications, from information retrieval systems and chatbots to data mining and information extraction workflows.

## A Brief Summary of the Main Features of the Application

The application we've created serves as an automated document processing tool, supporting various types of unstructured files such as text, PDFs, and images. Its main features include:

1. **File Uploading**: The application provides a straightforward mechanism for a user to upload their document file. This is done through a simple API interface that accepts file uploads.
    
2. **Document Processing**: Once a document is uploaded, the application leverages the unstructured-io library's abilities to analyze the document. Elements within the document are processed and categorized using machine learning, providing structured and useful data.
    
3. **Data Extraction**: The application doesn't just analyze the document; it extracts useful data from it. This includes text, metadata, and classifications (like titles, headings, body text, etc.).
    
4. **Response Formatting**: After the analysis and extraction, the application formats the results into a user-friendly JSON format. This includes both the extracted structured data and the metadata of the document and elements in a well-organized manner.
    
5. **Error Handling**: The application is designed to handle potential errors gracefully. In the event of an invalid file upload or a processing failure, the application will return a helpful error message to the user.
    
6. **Concurrent Request Handling**: Thanks to Gunicorn, our Flask application can handle multiple requests at the same time, which enhances the user experience and ensures the application remains responsive even under high usage.
    

By combining these features, we provide a full-fledged document processing service that is accessible, usable, and scalable for various use cases.

## Technology Stack

The technology stack for our project consists of several components each with its own purpose and functionality. Let's take a closer look at each of them.

### Python

Python serves as the backbone of our application. It's a versatile programming language known for its simplicity and wide range of libraries and frameworks. In our project, it allows us to implement the server-side logic of our web application.

### Flask

Flask is a Python web framework used to develop the server-side of our application. It is micro, yet powerful and can easily be extended with a wide variety of plugins. Flask was chosen for its simplicity and flexibility, and it is responsible for routing and handling client requests in our project.

### Docker

Docker is an open-source platform that automates deployment, scaling, and management of applications. It does this by containerizing the applications, encapsulating them along with their environment and dependencies. This not only ensures that our application works uniformly regardless of the environment, but also simplifies the deployment process.

### Gunicorn

Gunicorn 'Green Unicorn' is a Python Web Server Gateway Interface (WSGI) HTTP server. It's a pre-fork worker model, which means it forks multiple worker processes to handle incoming requests. We use it in our project to serve our Flask application, making it ready to handle multiple requests concurrently.

### unstructured-io

unstructured-io is a powerful library used for document processing and text extraction. It tracks a variety of metadata about elements extracted from documents and allows users to filter document elements based on metadata of interest. In our application, we use unstructured-io to process the documents uploaded by the user.

## Python: Brief language overview and relevance for the project

Python is an interpreted, high-level, general-purpose programming language that emphasizes readability and simplicity. Created by Guido van Rossum and first released in 1991, Python has grown in popularity due to its ease of learning and flexibility, making it commonly used for a wide range of tasks, including but not limited to web development, data analysis, machine learning, and artificial intelligence.

For our project, Python plays a critical role for several reasons:

1. **Simplicity and readability:** Python's clean syntax allows for clear and maintainable code, which is crucial for any application, especially when it integrates multiple components such as our project.
    
2. **Extensive Standard Library:** Python has a rich library that has been extended by packages developed by its active community. This project utilizes a number of these, including Flask for creating the web server and [Unstructured.io](http://Unstructured.io) for document processing.
    
3. **Integration with Web Frameworks:** Python integrates seamlessly with web frameworks such as Flask, which we use to expose our document-processing functionality via a REST API.
    
4. **Popularity in the ML/AI Community:** Python is a popular choice in the machine learning and AI community because of the availability of cutting-edge libraries and frameworks. The [Unstructured.io](http://Unstructured.io) library we are using in this project is a Python package, allowing comprehensive document processing functionalities.
    
5. **Interoperability with Docker:** Python applications are easy to containerize using Docker which simplifies deployment and scaling in different environments.
    

In sum, Python, with its extensive ecosystem and straightforward syntax, proves to be a productive language choice for our project that carries out document processing via a flask API.

## Flask: Introduction, benefits, and its role in the project.

Flask is a lightweight WSGI web application framework designed with simplicity, flexibility and fine-grained control in mind. It provides a robust foundation for web applications, enabling developers to build applications that can scale from small, simple single-file projects to large, complex web services.

### Introduction

Flask was developed in Python and is known for its relatively low learning curve, high adaptability, and elegant, straightforward syntax. This makes it a fantastic choice for beginners and advanced developers alike who want to develop web applications in Python.

### Benefits

Some benefits of Flask include:

* **Simple and Easy-to-Use**: Flask is designed to be simple, easy to understand and use. Flask allows developers to build web applications quickly, with a minimum amount of setup and boilerplate code.
    
* **Flexible and Fine-Grained Control**: Unlike other web frameworks, which come with a predetermined way of doing things, Flask leaves the organization of your application up to you, giving you the flexibility to structure your application in the way that makes the most sense for your project.
    
* **Extensible**: Flask can be easily extended with a wide range of extensions available for tasks like form validation, upload handling, various open authentication technologies, and several common framework related tools.
    
* **Lightweight**: Flask is a "micro" framework that’s designed to keep the core simple but extensible. It doesn't make many decisions for you, such as what database to use, keeping the framework light.
    

### Role in the Project

In this project, Flask serves as the backbone for our web application, acting as the intermediary between the client's requests and the system's responses. It takes uploaded documents, processes the upload, hands it off for processing by the `unstructured` Python library and then structures and returns a response containing the document's metadata. Flask allows us to do all this in a simple and efficient manner.

The chosen structure of Flask, its extension capabilities along with its easy nature, helped us focus on the project's logic rather than the technicalities of the web server infrastructure. This facilitated an efficient completion of the project, providing a reliable and scalable web server for our document processing application.

## Docker's Role in Deployment and Dependency Management

One of the main technologies used in this project is Docker, a popular platform that enables developers to automate the deployment, scaling, and management of applications within containers.

In the context of our Flask application, Docker plays a key role for several reasons:

**Deployment**

Docker containers encapsulate everything an application needs to run (including libraries, system tools, code, and runtime). With Docker, you can rest assured that the application will run on any other Linux machine regardless of any customized settings in the machine that could differ from those used for writing and testing the code.

Docker Compose is a tool that is used for defining and managing multi-container Docker applications. It uses a YAML file (`docker-compose.yml`) to define the services and with a single command, all the services (our web application) can be set up.

In our case, we have a simple service – our web application, required configurations are mentioned like:

* Building from Dockerfile
    
* Port to be exposed
    
* Volumes for mapping
    
* Command to be run when the Docker container is up
    

**Dependency management**

One of the main advantages of using Docker is its ability to manage dependencies effectively. Each Docker image contains only the bare minimum software that is needed to run a particular application.

This helps in eliminating any issues due to differences in OS, system libraries or any additional software that might be present when the product is deployed on different environments.

In our case, we have specified our dependencies (`flask`, `gunicorn` and anything from unstructured-io) through a `Dockerfile`. Docker builds images by reading instructions from this Dockerfile.

With the powerful combination of Flask, Docker, and unstructured-io, the application is not only able to process documents with a high level of precision, but it also achieves high portability and scalabilty.

#### Why Gunicorn was chosen over the default Flask server.

Gunicorn, or 'Green Unicorn', is a Python Web Server Gateway Interface (WSGI) HTTP server. It's a pre-fork worker model, which means it forks multiple worker processes to handle incoming requests. This process management allows Gunicorn to handle multiple simultaneous connections, making it much more suitable for production environments compared to Flask’s built-in server.

Flask’s built-in server is intended for development use. While it's easy to use and good for testing, it isn’t meant to handle production traffic. The server is single-threaded and can only handle one request at a time. This is fine for development because you're likely the only one communicating with the server. However, in a production environment, this becomes a major issue where numerous clients may be trying to communicate with your server simultaneously.

Gunicorn also has several configuration options that are beneficial for a production level application. For example, you can specify the number of worker processes, control the logging, and define server hooks for various events.

Using Gunicorn also allows the application to be decoupled from the HTTP server, meaning you can swap it out for a different WSGI HTTP server (like uWSGI or mod\_wsgi) if desired, with minimal modifications to your codebase.

Therefore, for the robustness, effectiveness and scalability it offers, Gunicorn was chosen to serve our Flask application over Flask's default server.

## unstructured-io

unstructured-io is a powerful library designed for efficiently extracting and processing information from unstructured documents. It uses machine learning algorithms to power its core capabilities, enabling it to reliably and accurately identify, categorize, and extract the information present in a range of file types such as PDFs, Word Documents, and more.

The fundamental object in unstructured-io is the `Element`, which represents a discrete unit of information extracted from the document. This can be a phrase, sentence, paragraph, or any other identifiable unit of text. Each `Element` includes metadata regarding its origins, type, and other detail characteristics.

In our application, we primarily use the `partition_pdf` function provided by unstructured-io to extract content from uploaded PDF files. The function breaks down a PDF document into a list of elements.

Each element returned by `partition_pdf` provides a robust set of metadata that provides granular detail about the element. This risk metadata can include coordinates locating the element within the document, the page number where the element is found, attributes such as whether the text is emphasized, the language of the text, and more.

By leveraging the capabilities of unstructured-io, we're able to provide an API endpoint that accepts PDF files and returns a detailed breakdown of the contents of the uploaded documents.

## Application Design

Our project uses a Flask application to provide an API endpoint for document processing. The structure of the Flask application is kept straightforward and easy to comprehend.

Below is the overall structure of the Flask application:

```python
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
	# logic to handle incoming files and processing them

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
```

## Docker Setup

Docker is a significant part of this project as it provides a way to bundle the application along with its environment. Docker uses a special file called `Dockerfile` to automatically build images, or snapshots of our container — which include our application, the environment it runs in, and its dependencies.

### Dockerfile

Here is the Dockerfile used in this project:

```Dockerfile
FROM downloads.unstructured.io/unstructured-io/unstructured:latest

RUN pip install flask gunicorn

ENV PYTHONPATH /app:$PYTHONPATH
```

The Dockerfile starts with a base image obtained from [downloads.unstructured.io/unstructured-io/unstructured:latest](http://downloads.unstructured.io/unstructured-io/unstructured:latest). This base image already has Python and some necessary libraries installed which help us to run our Flask application.

Then we install flask and gunicorn using pip. This step prepares our Docker image with all the necessary Python libraries needed for our Flask application.

Finally, an ENV command is used to set the PYTHONPATH environment variable.

### Docker Compose

Docker Compose simplifies the process of working with multiple containers in Docker. In this project, we use Docker Compose to define our services and their relationships in a docker-compose.yml file.

Here is the Docker Compose file used in this project:

```yaml
version: '3.8'
services:
  app:
    build: .
    volumes:
      - .:/app
    ports:
      - '5000:5000'
    command: ["python3", "-m", "gunicorn", "-b", ":5000", "app:app", "-w", "4"]
```

In this file, we define a single service called app. The build command tells Docker to build an image from the Dockerfile in the current directory. We map the current directory on the host to /app in the container using the volumes key. And we map port 5000 in the host to port 5000 in the container using the ports key.

The command key tells Docker how to start our application. In this case, it starts the server using gunicorn, binding to port 5000 and using app:app as the WSGI application object. The -w 4 option starts four worker processes to serve requests.

Note that you can handle much more complex multi-container setups using Docker Compose, but for the scope of our Flask application, this simple setup works well.

## Explanation of the Makefile and its Convenience Methods for Docker

A Makefile aims to organize code compilation more quickly and flexibly. This project contains a `Makefile` that contains shortcut commands to manage Docker containers.

Our `Makefile` in this project contains the following commands:

```makefile
build:
	docker build -t my_flask_app .

up:
	docker compose up --build -d

down:
	docker compose down

test:
	curl -F 'file=@article.pdf' http://localhost:5000/
```

Let's break it down:

build: This command runs docker build to create a Docker image from the Dockerfile. The -t flag tags the image with the name my\_flask\_app.

up: The up command is an instruction to Docker Compose. The --build flag ensures that the image used is up-to-date. If the image isn't up-to-date, it will build it using the provided Dockerfile. The -d flag means that the containers will run in the detached mode. This runs the containers in the background and leaves them running.

down: This command tells Docker Compose to stop and remove all the containers described in the docker-compose.yml file.

test: The test task is a simple curl command that sends a POST request to the web application with a file.

The advantage of these commands is that you don't have to remember or write out the entire Docker command each time, and it enhances consistency across development, staging, and production environments. Instead of entering the long Docker commands, you can just type make up or make down in your terminal.

### Details on How the Application Handles File Upload, Processing, and Return of Results

In the Python file the core of this Flask application, a single route is defined that accepts POST requests for document processing. This endpoint acts as the handler for incoming requests, and more specifically, it handles and processes document files contained in the requests.

When a client sends a POST request to the server, the endpoint first checks if there is a file in the request. If there is no file in the request or if no file is selected for uploading (filename is empty), an error message is sent back to the client.

Once a file is confirmed to be present in the request, the filename is secured using the `secure_filename` function from `werkzeug.utils`. The file is then saved to an '/app/' directory located inside the Docker container.

After the file is saved, the application proceeds to process the document using the `partition_pdf` function from the `unstructured.partition.pdf` package. This function reads the file and partitions the data into several `Elements` which are crucial pieces of the document. These can vary from titles to paragraphs to tables, etc.

Each element is then processed further to extract important data such as the element's text and type. If available, metadata is also extracted for each individual element using [`el.metadata.to`](http://el.metadata.to)`_dict()`. This includes several fields like filename, coordinates, category depth, and so on, provided by the unstructured-io library.

Finally, in addition to each element's information, the application also encapsulates other details, such as the filename, file extension, timestamp, and an UUID. These are all packaged into a JSON response and returned to the client.

By providing detailed metadata for each element in the JSON response, as well as overall information about the processed document, the application ensures comprehensive document analysis and enhances downstream tasks for users.

## API

Our Flask application exposes a single endpoint at the root ("/") that can process documents. It operates with the HTTP POST method, enabling clients to upload files for processing.

### Interacting with the Endpoint

To interact with this endpoint, send a POST request to the URL where the Flask application is hosted. The endpoint is expecting a file in the request body under the key "file."

Here's an example using `curl`:

```bash
curl -X POST -F 'file=@yourfile.docx' http://your-flask-app-url:5000/
```

POST Request Format and Payload The POST request should contain a file in the body under the key "file." The file can be of any type supported by the application. The file is received and saved locally in the server, then processed.

Responses and Their Structure The server will respond with a JSON object. The response includes file information, a timestamp, UUID, the process status, and output processed data.

The output contains an array of elements processed from the document. Each element, depending on its type, will have its text, type, and associated metadata.

If an error occurs during processing, the response will include an "error" field containing the error message.

Here's an example structure of a successful response:

```json
{
    "filename": "yourfile.docx",
    "file_extension": ".docx",
    "timestamp": "2021-12-05T20:04:36.295212",
    "uuid": "123e4567-e89b-12d3-a456-426614174000",
    "output": [
        {
            "text": "Title of the document",
            "type": "TitleElement",
            "metadata": {
                "font_size": 14,
                "font_color": "black",
                // Other possible metadata...
            }
        },
        // More elements ...
    ],
    "status": "ok"
}
```

The error response:

```json
{
    "status": "error",
    "errormsg": "No file selected for uploading",
    "trace": "Traceback (most recent call last): ..."
}
```

## Leveraging Unstructured Metadata in the JSON Response

In the provided example response, the Metadata from the Unstructured library is being included at two levels:

At the overall document level At the individual element level This involves extracting the metadata from the Element objects and adding it to the response. This is done within the loop that iterates over the elements extracted from the document.

Here's a snippet of how it's done in Python code:

```python
# Grabbing elements from the document

elements = partition_pdf(filepath)

output = []
for el in elements:
    ...
    output.append({
        ...
        'metadata': el.metadata.to_dict()  # The metadata for each individual element
    })
```

The metadata for each element is a comprehensive set of descriptive data, which includes the following:

* `file_directory` represents the directory in which the file was located.
    
* `filename` corresponds to the name of the original document from which the element is extracted.
    
* `filetype` provides the type of the original document, for example, "application/pdf".
    
* `last_modified` gives the latest timestamp that the original file was modified.
    
* `links` provides a list of links found within that specific element.
    
* `page_number` denotes the page number in the original document, where the element was found.
    
* `parent_id` presents a unique identifier for the parent element, which helps in establishing hierarchies.
    
* `coordinates` illustrates the positioning of the element in the document. It entails the bounding box coordinates (starting from the top left corner and proceeding counter-clockwise), layout dimensions, and the coordinate system (e.g., "PixelSpace").
    

This comprehensive metadata suite not only offers rich insights about the document and its elements but also enriches the final output, making it easy for downstream tasks to use it optimally. It highly aids a user to understand the context and nature of the extracted elements. For example, bounding box coordinates can be instrumental in understanding the positioning and layout of different elements in the document, providing a spatial perspective to the information. Similarly, information such as page numbers can be useful in context restoration during analysis tasks.

here the [`app.py`](http://app.py) code :

```python
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
```

You can find the source code here : [https://github.com/morandalex/scrape-pdf](https://github.com/morandalex/scrape-pdf)