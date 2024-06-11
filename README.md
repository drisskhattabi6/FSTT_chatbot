# RAG-French-FSTT-chatbot

This README provides instructions on how to set up and run the Chroma Vector database using Docker, how to Create RAG System for **Gemma 2b LLM**, how to fine-turn Gemma 2b LLM and how to run the chatbot interface.

## Chroma Vector Database

### Prerequisites

- Docker must be installed on your system.
- Ensure you have internet access for downloading the necessary Docker image and model.

### Running the Chroma Vector Database

1. **Start the Docker container**

   Open your terminal and run the following command to start the Docker container for the Chroma Vector database:

   ```sh
   docker run -d --rm -v ./ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama
   ```
    In case of Having AMD GPU , run with the following command
    ```sh
    docker run -d --device /dev/kfd --device /dev/dri -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama:rocm
   ```
    This command will:
   - Run the container in detached mode (`-d`).
   - Remove the container when it exits (`--rm`).
   - Mount the `./ollama` directory to `/root/.ollama` inside the container.
   - Map port 11434 on your host to port 11434 on the container.
   - Name the container `ollama`.
   - Use the `ollama/ollama` Docker image.

2. **Download and run the model**

   Execute the following command to download and run the `nomic-embed-text` model inside the Docker container:

   ```sh
   docker exec -it ollama ollama run nomic-embed-text
   ```

   After the model downloads successfully, press `Ctrl+D` to exit the interactive terminal.

3. **Test the setup**

   You can test if the setup is working correctly by running the following `curl` command:

   ```sh
   curl http://localhost:11434/api/embeddings -d '{"model": "nomic-embed-text","prompt": "Here is an article about llamas..."}'
   ```

   This command sends a request to the embeddings API, using the `nomic-embed-text` model with a sample prompt.

### Saving Data to the Database

To save data to the Chroma Vector database, use the provided Jupyter Notebook.

1. Open the Jupyter Notebook located at `Data/save_to_chroma.ipynb`.

2. Follow the instructions within the notebook to save your data to the Chroma Vector database.

### Notes

- Ensure your Docker container is running before attempting to save data to the database.
- You can check the status of your Docker container by running:

  ```sh
  docker ps
  ```

- If you need to stop the Docker container, run:

  ```sh
  docker stop ollama
  ```

### Troubleshooting

- If you encounter any issues with the Docker container, check the logs using:

  ```sh
  docker logs ollama
  ```

- For any network-related issues, ensure that port 11434 is not being used by another application and that your firewall settings allow traffic on this port.

## RAG System :

- execute **'save_to_chroma'** notebook to create ChromaDB (Vector DataBase).
- execute **Docker compose app** notebook.

## Fine-Turn the LLM :

- 

---

This README file should help you get started with running and using the Chroma Vector database and chatbot app.
