import os
import sys
from src.logger.logging import logging
from src.exception.exception import customexception
from src.data_ingestion.document_loader import Document_Loader
from src.chunking.chunking import Chunking
from src.vector_database.retrival import Chroma_database

db = Chroma_database()
def main(file_path,query):
    filename = os.path.basename(file_path)
    try:
        logging.info("Initialising RAG CHAT BOT")
        doc = Document_Loader()
        text = doc.document_loader(file_path)
        logging.info("Text extracted from the document")
    except Exception as e:
        raise customexception(e,sys)

    try:
        chunking = Chunking(200,30)
        chunks = chunking.sliding_window_chunking(text)
        logging.info("Chunked text recived")
    except Exception as e:
        raise customexception(e,sys)

    try:
        db.process_and_add_documents(chunks,filename)
        context, sources = db.retrive_text(query, filename,n_results=2)
        print(context)
        logging.info("Text extracted from the document")
    except Exception as e:
        raise customexception(e,sys)
    
if __name__=="__main__":
    query = "How much degree celsius does global temprature has risen?"
    main("D:\\0MLOps\\RAG_Chatbot\\RAG_CHATBOT\\data\\Understanding_Climate_Change.pdf",query)
    