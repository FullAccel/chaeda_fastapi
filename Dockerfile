#
FROM python:3.10

#
WORKDIR /code

#
COPY requirements.txt ./

#
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

#
COPY . .

#
CMD ["uvicorn", "main:app", "--host", "114.70.23.79", "--port", "8088"]