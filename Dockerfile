FROM python:3.7-buster as neologd_builder

RUN apt update \
    && apt upgrade -y \
    && apt install -y mecab \
    libmecab-dev \
    && apt clean \
    && rm -rf /var/lib/apt/lists/*

RUN git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd.git /tmp/neologd \
    && cd /tmp/neologd \
    && yes yes | ./bin/install-mecab-ipadic-neologd -n -u

FROM python:3.7-buster
COPY --from=neologd_builder /usr/lib/x86_64-linux-gnu/mecab/dic/mecab-ipadic-neologd /usr/lib/x86_64-linux-gnu/mecab/dic/mecab-ipadic-neologd

WORKDIR /app

RUN apt update \
    && apt upgrade -y \
    && apt install -y --no-install-recommends gcc

COPY pyproject.toml poetry.lock ./
RUN pip --disable-pip-version-check --no-cache-dir install poetry==1.0.2 && \
    poetry config virtualenvs.create false && \
    poetry install --no-ansi

ENV PYTHONPATH=".:$PYTHONPATH"

COPY entrypoint.sh ./
COPY models ./models/
COPY wikeyword ./wikeyword/

CMD ["bash", "entrypoint.sh"]
