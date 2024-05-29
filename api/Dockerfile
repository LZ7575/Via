FROM python:3.12
COPY ./requirements.txt /requirements.txt
COPY ./setup.py /setup.py
RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY ./src /src/
CMD ["uvicorn", "src.api:app", "--host", "0.0.0.0", "--port", "3000"]