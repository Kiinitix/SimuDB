FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PATH="/root/.cargo/bin:$PATH"
ENV PYTHONPATH=/app

RUN apt-get update && apt-get install -y \
    python3-pip \
    build-essential \
    cmake \
    curl \
    libssl-dev \
    pkg-config \
    git \
    && rm -rf /var/lib/apt/lists/*

RUN curl https://sh.rustup.rs -sSf | bash -s -- -y

WORKDIR /app
COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

WORKDIR /app/core_rust
RUN pip install .

WORKDIR /app
ENTRYPOINT ["python3", "cli/main.py"]


# docker build -t simudb .
# docker run --rm simudb --ops 20 --fail_rate 0.1