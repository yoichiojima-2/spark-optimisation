FROM python:latest


# set working directory
WORKDIR /home

# install java
RUN apt update && \
    apt install -y openjdk-17-jdk && \
    apt clean && \
    rm -rf /var/lib/apt/lists/*

ENV JAVA_HOME=/usr/bin/java
ENV PATH="${JAVA_HOME}/bin:${PATH}"

# install python dependencies
COPY pyproject.toml .
COPY .python-version .
RUN pip install --upgrade pip && \
    pip install uv && \
    uv sync