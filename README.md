# Fine-Turn and RAG French FSTT chatbot

This repository contains a chatbot application french language designed to assist students and visitors of the Faculty of Sciences and Techniques in Tanger (FSTT) website. The chatbot utilizes natural language processing (NLP) to understand user queries and provide relevant information about the university's programs, courses, and other academic-related topics.

The ChatBot is implemented with two approach: 
- Retrival-Augmented Generation (RAG).
- Fine-Tuning.

This README provides instructions on how to set up and run the Chroma Vector database using Docker, how to Create *RAG* System for **Gemma 2b LLM**, how to *Fine-Turn* Gemma 2b LLM and how to run the chatbot interface.

## Prerequisites :

- **Docker** and **Python** must be installed on your system.
- Ensure you have internet access for downloading the necessary Docker image and model.

## Repository Structure

```
|FSTT_chatbot/
|
├── ChatBot-FSTT-Front-End/
|      # This folder contains the Front-End App of the Chatbot.
├── Data/
│   ├── scraping data/   # contains the code source of scraping the data 
│   └── fstt-articles.csv
│   └── fstt-clubs-info.csv
│   └── fstt-departements-info.csv
│   └── fstt-formation-initial.csv
│   └── general_info.csv
│   └── save_to_chroma.ipynb   # save the data into the vector database (ChromaDB)
├── Fine-tuning/
│   ├── Fine-tuning the model and save the Adaptor on Hugging Face.ipynb
|         # the source code of Fine-tuning the model and save the Adaptor on Hugging Face.
├── RAG_Gemma/
│   ├── RAG Gemma.ipynb   # contains the code source of the RAG System for Gemma-2b-it LLM
├── api/
│   ├── api.py   # Flask API App for generating answers fron RAG and Fine-turned LLM.
│   └── RAG.py   # the RAG System for Gemma-2b-it LLM
├── README.md
├── docker-compose.yml   # A Docker Compose file to set up and manage multi-container Docker applications.
└── requirements.txt   # Lists the Python dependencies needed to run the project.
```

## Running the Project :

### Install the Project :

   ```sh
   git clone https://github.com/drisskhattabi6/FSTT_chatbot.git
   cd FSTT_chatbot
   ```

### Set up the requisites :

- install the requirements python libraries :

  ```sh
  pip install -r requirements.txt
  ```

- run cmd (need good Internet):
  
  ```sh
   docker compose up
   ```

### Create Chroma Vector Database :

To save data to the Chroma Vector database, use the provided Jupyter Notebook.

1. Open the Jupyter Notebook located at `Data/save_to_chroma.ipynb`.

2. Follow the instructions within the notebook to save your data to the Chroma Vector database.


---

## Contributors

- **[Khattabi Idriss](https://github.com/drisskhattabi6)**
- **[Chihab Edin](https://github.com/novoSoftEng/)**
- **[Boufarhi Ayman](https://github.com/aymanboufarhi)**

---

**Abdelmalek Essaadi University** - Faculty of Sciences and Techniques Tangier
   - Department : Computer Engineering
   - Master : AI & DS
   - Module : Natural Language Processing
   - Framed by : Pr. Lotfi ELAACHAK
