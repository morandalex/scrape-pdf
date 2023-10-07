FROM downloads.unstructured.io/unstructured-io/unstructured:latest

RUN pip install flask gunicorn

ENV PYTHONPATH /app:$PYTHONPATH
