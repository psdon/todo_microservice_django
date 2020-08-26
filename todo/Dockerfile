# FROM revolutionsystems/python:3.6.3-wee-optimized-lto as python-base
FROM python:3.8
ENV PYTHONUNBUFFERED 1
# RUN apt-get update && apt-get install -y git build-essential
RUN pip install -U pip

COPY requirements /requirements

RUN pip install -r /requirements/local.txt
# RUN pip install -e git+https://gitlab+deploy-token-60342:Xs78xdAhrkn3pCucL2uP@gitlab.com/careerlyft-team/careerlyft-shared.git#egg=cv_utils

RUN mkdir /code
COPY . /code

# RUN find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf

EXPOSE 5000

WORKDIR /code
ENV DJANGO_SETTINGS_MODULE api.settings.production

CMD gunicorn -k uvicorn.workers.UvicornWorker -b 0.0.0.0:5000 run:app --access-logfile -