FROM nginx/unit:1.9.0-python3.5
RUN apt update && apt -y install python3-pip && \
    rm -rf /var/lib/apt/lists/*

COPY config/requirements.txt /config/requirements.txt
RUN pip3 install -r /config/requirements.txt
