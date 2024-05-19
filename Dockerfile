#
FROM python:3.10

#
WORKDIR /code

#
COPY requirements.txt ./

#
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6 -y
RUN apt-get update -y && apt-get install -y libgl1-mesa-glx


#
COPY . .

#
CMD ["uvicorn", "main:app", "--host", "114.70.23.79", "--port", "8088"]
