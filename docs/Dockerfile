FROM python:3.8

COPY ./ /docs/

WORKDIR /docs/
RUN ls

RUN pip install mkdocs
EXPOSE 8001

CMD ["mkdocs", "serve"]