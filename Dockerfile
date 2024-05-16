#
FROM python:3.10

#
WORKDIR /code

#
COPY requirements.txt ./

#
<<<<<<< HEAD
=======
RUN pip install --upgrade pip
>>>>>>> 392bb16 (배포)
RUN pip install -r requirements.txt

#
COPY . .

#
CMD ["uvicorn", "main:app", "--host", "114.70.23.79", "--port", "5432"]