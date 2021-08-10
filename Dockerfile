FROM python:slim

RUN pip install -q --no-cache-dir pytest

WORKDIR /github/workspace

CMD pytest
