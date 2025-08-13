FROM python:latest


# set working directory
WORKDIR /home

# install java
RUN apt update && \
    apt install -y openjdk-17-jdk && \
    apt clean && \
    rm -rf /var/lib/apt/lists/*

# Set JAVA_HOME dynamically based on architecture
RUN JAVA_HOME=$(readlink -f /usr/bin/java | sed "s:/bin/java::") && \
    echo "JAVA_HOME=${JAVA_HOME}" >> /etc/environment && \
    echo "PATH=${JAVA_HOME}/bin:${PATH}" >> /etc/environment

# Source the environment file to set JAVA_HOME for subsequent RUN commands
ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk
RUN ln -sf $(readlink -f /usr/bin/java | sed "s:/bin/java::") /usr/lib/jvm/java-17-openjdk

# install python dependencies
COPY pyproject.toml .
COPY .python-version .
RUN pip install --upgrade pip && \
    pip install uv && \
    uv sync