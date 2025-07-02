FROM mcr.microsoft.com/devcontainers/python:3.11

RUN apt-get update && \
    apt-get install -y --no-install-recommends build-essential graphviz texlive-full && \
    pip install --no-cache-dir pandas numpy scipy matplotlib jupyterlab typer[all] papermill

# Clean up
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

EXPOSE 8888
