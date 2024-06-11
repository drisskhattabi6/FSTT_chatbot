FROM chromadb/chroma
USER root
WORKDIR /
COPY save_to_chroma.py save_to_chroma.py
COPY . .
# Install Python if needed
RUN apt-get update && apt-get install -y python3 python3-pip
RUN apt-get update \
	&& apt-get install -y build-essential \
	&& apt-get install -y wget \
	&& apt-get clean \ 
	&& rm -rf /var/lib/apt/lists/*
ENV CONDA_DIR /opt/conda
RUN ["/bin/bash", "-c", "chmod -R a+rw /opt/"]
RUN wget --quiet https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh && \
    /bin/bash ~/miniconda.sh -b -p /opt/conda
COPY environment_droplet.yml .
# Put conda in path so we can use conda activate
ENV PATH=$CONDA_DIR/bin:$PATH
# Put conda in path so we can use conda activate
RUN conda env create -f environment_droplet.yml  
# create conda environment
RUN conda init bash \
    && . ~/.bashrc && conda activate nlp && conda install -n nlp nltk && pip install langdetect
SHELL ["conda", "run", "-n", "nlp", "/bin/bash", "-c"] 
# Ensure the script is executable
RUN chmod +x /save_to_chroma.py
# Run the script to populate the database
RUN conda run --no-capture-output -n nlp python save_to_chroma.py 
