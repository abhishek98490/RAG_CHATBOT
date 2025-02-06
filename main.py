from src.logger.logging import logging
from src.exception.exception import customexception
from src.data_ingestion.document_loader import Document_Loader
from src.chunking.chunking import Chunking

def main(file_path):
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
        for chunk in chunks:
            print(len(chunk.split()))
            print(chunk, '\n---\n')
        logging.info("Chunked text recived")
    except Exception as e:
        raise customexception(e,sys)

    
if __name__=="__main__":
    main("D:\\0MLOps\\RAG_Chatbot\\RAG_CHATBOT\\data\\Understanding_Climate_Change.pdf")
    