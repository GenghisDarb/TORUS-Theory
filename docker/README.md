This directory contains Docker-related resources for the TORUS-Theory project.

This folder stores Dockerfiles that reproduce the TORUS analysis stack
(python 3.12, jupyterlab, black, papermill). Use:

docker build -t torus-dev -f docker/Dockerfile .
docker run -p 8888:8888 torus-dev

CI note: docker files are *not* built in GitHub Actions; keep them lightweight.
