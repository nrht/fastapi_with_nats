FROM python:3


WORKDIR /usr/src

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
EXPOSE 8000

WORKDIR /usr/src/app
# CMD ["uvicorn", "main:app"]
# CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000", "--root-path", $ROOT_PATH]
CMD uvicorn main:app --reload --port 8000 --root-path $ROOT_PATH
# CMD ["bash", "-c", "uvicorn main:app --reload --host 0.0.0.0 --port 8000 --root-path $ROOT_PATH"]
#  "django-admin startproject $PROJECTNAME"
