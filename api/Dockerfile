# Use the official Python image as the base image
FROM python:3.11-slim
# Set the working directory
USER root
WORKDIR /app
RUN apt-get update \
	&& apt-get install -y build-essential \
	&& apt-get install -y wget \
	&& apt-get clean \ 
	&& rm -rf /var/lib/apt/lists/*
ENV CONDA_DIR /opt/conda
RUN ["/bin/bash", "-c", "chmod -R a+rw /opt/"]
RUN wget --quiet https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh && \
    /bin/bash miniconda.sh -b -p /opt/conda
COPY environment_droplet.yml .
# Put conda in path so we can use conda activate
ENV PATH=$CONDA_DIR/bin:$PATH
# Install the dependencies
RUN conda env create -f environment_droplet.yml 
SHELL ["conda", "run", "-n", "nlp", "/bin/bash", "-c"] 
# Copy the rest of the application
COPY . .

# Expose port 5000
EXPOSE 8500
ENTRYPOINT ["conda", "run", "--no-capture-output", "-n", "nlp", "python", "api.py"]

