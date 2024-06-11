from transformers import AutoTokenizer, AutoModelForCausalLM
import chromadb
from langchain_community.document_loaders import CSVLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
import re
from IPython.display import display, Markdown
import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, RegexpTokenizer,sent_tokenize
import nltk
import re

nltk.download('stopwords')
french_stopwords = set(stopwords.words('french'))

# ## AI Agent class :

# In[3]:

def preprocessing(text):
    # Convert to string and lowercase
    text = str(text).lower()
    
    # Remove URLs
    # text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    
    # Remove mentions
    text = re.sub(r'@\w+', ' ', text)

    text = re.sub(r'\xa0', ' ', text)
    
    # Remove \n
    text = re.sub(r'\n', ' ', text)
    
    # Remove specific unwanted characters
    text = re.sub(r'«|»|“|”|’|‘', ' ', text)
    
        
    # Remove punctuation
    # text = text.translate(str.maketrans("", "", string.punctuation))
    pattern = r"[dnl]['´`]|\w+|\$[\d\.]+|\S+"
    tokenizer = RegexpTokenizer(pattern)
    token_words = tokenizer.tokenize(text)
    
    # tokens = word_tokenize(text, language="french")
    token_words = [word for word in token_words if word not in french_stopwords]
    
    
    # Stemming
    # stemmer =nltk.stem.snowball.FrenchStemmer()
    # tokens_stemmed = [stemmer.stem(word) for word in tokens]
    
    # Join tokens back into a single string
    return ' '.join(token_words)

import os
def extract_answer_from_text(text):
    answer_match = re.search(r'Answer:\s*(.*)', text, re.DOTALL)
    answer = answer_match.group(1).strip() if answer_match else ""

    return answer
# Set your Hugging Face API token
HUGGINGFACE_HUB_TOKEN = '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'
os.environ['HUGGINGFACE_HUB_TOKEN'] = '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'


# In[13]:


# model_name="google/gemma-2b-it"
# model_name="aymanboufarhi/gemma-fstt"

class AIAgent:
    
    def __init__(self, model_name="aymanboufarhi/gemma2B-chat-bot-fstt", max_length=1000):
        self.max_length = max_length
        try:
            self.tokenizer = AutoTokenizer.from_pretrained(model_name, token=HUGGINGFACE_HUB_TOKEN)
            self.gemma_llm = AutoModelForCausalLM.from_pretrained(model_name, token=HUGGINGFACE_HUB_TOKEN)
        except Exception as e:
            raise ValueError(f"Error loading model: {e}")

    def create_prompt(self, query, context):
        # Prompt template
        prompt = f"""<|system|>
        You are an AI Agent specialized to answer questions about FSTT (faculty of science and technology in Tanger). 
        Vous allez repondre a des question sur les programmes , les profs , les formation dans la faculté
        Explain the concept or answer the question about FSTT.
        In order to create the answer,use the information from the context if it seems to be relevant to the question provided (Context). 
        and the context will be as a list, so you should use just the most relevent informations from the list.
        Answer with simple words.
        If needed, include also explanations.
        it's important to answer with french languge.
        return only the answer
        Context: {context}
        Question:<|user|> {query}
        <|assistant|>Answer:
        """
        return prompt
    
    def generate(self, query, retrieved_info="la fstt est la faculte de science et technique de tanger"):
        query = preprocessing(query) 
        prompt = self.create_prompt(query, retrieved_info)
        input_ids = self.tokenizer(prompt, return_tensors="pt").input_ids
        
        # Answer generation
        answer_ids = self.gemma_llm.generate(input_ids, max_new_tokens=self.max_length)
        
        # Decode and return the answer
        answer = self.tokenizer.decode(answer_ids[0], skip_special_tokens=True)
        
        return answer

# ### Test the AIAgent :

# In[14]:






# In[30]:
def connect():
    # Configure the ChromaDB client with persistence
    import chromadb.utils.embedding_functions as embedding_functions
    huggingface_ef = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="sentence-transformers/multi-qa-mpnet-base-dot-v1")
    client = chromadb.HttpClient(host='localhost', port=8000)
    collection = client.get_collection(name="text_embeddings",embedding_function=huggingface_ef)
    return collection

class RAGSystem:
    """Sentence embedding based Retrieval Based Augmented generation.
       Given a ChromaDB collection, retriever finds num_retrieved_docs relevant documents."""
    
    def __init__(self, ai_agent, collection=connect(), num_retrieved_docs=4):
        self.num_docs = num_retrieved_docs
        self.collection = collection
        self.ai_agent = ai_agent
    
    def retrieve(self, query):
        # Retrieve top k similar documents to query
        results = self.collection.query(query_texts=[query], n_results=self.num_docs)
        docs = [result for result in results['documents']]
        return docs
    
    def query(self, query):
        # Generate the answer
        context_docs = self.retrieve(query)
        context_docs = context_docs[0]
        print(context_docs)
        
        answer = self.ai_agent.generate(query, context_docs)

        
        return answer

# In[8]:


def colorize_text(text):
    for word, color in zip(["Question", "Prompt", "Answer", "Context"], ["blue", "magenta", "red", "green"]):
        text = text.replace(f"\n\n{word}:", f"\n\n**<font color='{color}'>{word}:</font>**")
    return text


# In[31]:









# In[34]:


# query = '''<|system|>FSTT c'est la Faculté des Sciences et Techniques de Tanger 
# <|user|> Donne le nombre de départements avec les noms et informations de chaque departement
# <|assistant|>'''




