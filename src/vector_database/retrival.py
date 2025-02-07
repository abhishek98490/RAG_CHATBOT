import os
import chromadb
from chromadb.utils import embedding_functions
from src.logger.logging import logging
from src.exception.exception import customexception

class Chroma_database():
    
    def __init__(self):
        logging.info(f"Initialising chromadb")
        self.client = chromadb.PersistentClient(path="D:\\0MLOps\\RAG_Chatbot\\RAG_CHATBOT\\chroma_db")
        self.sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(
            model_name="all-MiniLM-L6-v2"
        )

        self.collection = self.client.get_or_create_collection(
            name="collectiontesting",
            embedding_function=self.sentence_transformer_ef
        )
    
    def data_pre_processing(self,chunks,filename):
        try:
            logging.info(f"Processing the data")
            metadatas = [{"source": filename, "chunk": i} for i in range(len(chunks))]
            ids = [f"{filename}_chunk_{i}" for i in range(len(chunks))]

            return ids, chunks, metadatas
        except Exception as e:
            logging.info(f"Error processing {filename}: {str(e)}")
            raise customexception(e,sys)
    
    def add_to_collection(self,ids, texts, metadatas):
        if not texts:
            return
        batch_size = 200
        logging.info(f"adding data to the chromadb collection")
        try :
            for i in range(0, len(texts), batch_size):
                end_idx = min(i + batch_size, len(texts))
                self.collection.add(
                    documents=texts[i:end_idx],
                    metadatas=metadatas[i:end_idx],
                    ids=ids[i:end_idx]
                )
            logging.info(f"data added without any errors")
        except Exception as e:
            logging.info(f"Error adding {filename}: {str(e)}")
            raise customexception(e,sys)
    
    def process_and_add_documents(self,chunks, filename: str):
        ids, texts, metadatas = self.data_pre_processing(chunks,filename)
        self.add_to_collection(ids, texts, metadatas)
        
        print(f"Added {len(texts)} chunks to collection")
    
    def formated_context_with_sources(self,results):
        try:
            context = results[0]['documents']
            for i in range(1,len(results)):
                context += "\n\n"+ results[i]["documents"]
            sources = [f"{i['metadatas']['source']}(chunk {i['metadatas']['chunk']})" 
                    for i in results]

            return context, sources
        except Exception as e:
            logging.info(f"Error Formating {filename}: {str(e)}")
            raise customexception(e,sys)
    
    def retrive_text(self, query: str, filename:str, n_results: int = 2):
        try:
            results = self.collection.query(
                query_texts=[query],
                n_results=n_results
            )
            logging.info(f"data retrived from chromadb")
            if file_name:
                filtered_text = []
                for i in range(n_results):
                    if results['metadatas'][0][i]["source"] == filename:
                        filtered_text.append({"ids": results['ids'][0][i],
                                                "documents": results["documents"][0][i],
                                                "metadatas": results['metadatas'][0][i],
                                                "distances": results['distances'][0][i]
                                                })
            context, sources = formated_context_with_sources(filtered_text)
            logging.info(f"data formated")
            return context, sources
        except Exception as e:
            logging.info(f"Error retriving {filename}: {str(e)}")
            raise customexception(e,sys)
        
if __name__=="__main__":
    chunks = ["Greeting everyone. Today, I am here to deliver a speech on APJ Abdul Kalam. Dr APJ Abdul Kalam’s full name was Avul Pakir Zainuldeben Abdul Kalam, very few people know him by his full name as he was mostly addressed as ‘Missile Man of India’ and ‘People’s President’. He was born into a very poor family in Rameswaram on October 15, 1931. Since childhood, he enjoyed flying, and was equally curious to know how birds fly in the air? He was very intelligent and enjoyed reading, but his family did not have sufficient income for his school fees, so to support his education, he would wake up early in the morning and ride a bicycle 3 kilometres from home to collect newspapers and sell them. He was admitted to St. Joseph's College, Tiruchirapalli, and later he went on to complete a degree in physics in 1954 and then studied at the Madras Institute of Technology and graduated in aeronautical engineering in 1955. Since his childhood, Dr Abdul Alam wanted to be a pilot but couldn’t make his dream come true. He learned from his mistakes and accomplished numerous achievements in his life. After completing his degree, Abdul Kalam entered the",
                "be a pilot but couldn’t make his dream come true. He learned from his mistakes and accomplished numerous achievements in his life. After completing his degree, Abdul Kalam entered the Defense Department of India. He has been one of the key figures in building the nuclear capabilities of India. APJ Abdul Kalam was appointed to the Indian Ministry of Defense as a Technical Advisor in 1992, after which he served with DRDO and ISRO, the country's largest organization. Considered a national hero for successful nuclear tests in 1998, a second successful nuclear test was conducted in Pokhran the same year under his supervision, after which India was included in the list of nuclear-powered nations. Abdul Kalam has been active in all space programs and development programs in India as a scientist. For developing India's Agni missile, Kalam was called 'Missile Man.'Abdul Kalam made a special technological and scientific contribution, for which, along with Bharat Ratna, India's highest honour, he was awarded the Padma Bhushan, Padam Vibhushan, etc. He was also awarded an honorary doctorate by more than 30 universities in the world for the same. In 2002, he was elected President of India and was the country's first scientist and",
                "awarded an honorary doctorate by more than 30 universities in the world for the same. In 2002, he was elected President of India and was the country's first scientist and non-political president. He visited many countries during his tenure as President and led India's youth through his lectures and encouraged them to move forward. ‘My vision for India’ was a Famous Speech of APJ Abdul Kalam delivered at IIT Hyderabad in 2011, and is to this day my favourite speech. His far-reaching thinking gave India's growth a fresh path and became the youth's inspiration. Dr Abdul Kalam died on July 27, 2015, from an apparent cardiac arrest while delivering a lecture at IIM Shillong at the age of 83. He spent his entire life in service and inspiration for the nation and the youth, and his death is also while addressing the youth. His death is a never-ending loss to the country. Short APJ Abdul Kalam Speech In English For Students Today, I am here to deliver a speech on Dr APJ Abdul Kalam. APJ Abdul Kalam was born to Jainulabdeen and Ashiamma on October 15, 1931. His father was a boat owner and his mother was a homemaker. His",
                "Dr APJ Abdul Kalam. APJ Abdul Kalam was born to Jainulabdeen and Ashiamma on October 15, 1931. His father was a boat owner and his mother was a homemaker. His family's economic situation was not strong, so at an early age, he began helping his family financially. He graduated in 1955 from the Madras Institute of Technology and graduated from St. Joseph's College, Tiruchirappalli, in Aerospace Engineering. He joined the Defense Research and Development Organization's (DRDO) Aeronautical Development Base as a Chief Scientist after his graduation. He won credit as Project Director-General for making India's first indigenous satellite (SLV III) rocket. It was his ultimate support that brought nuclear power to India. In July 1992, he was appointed Scientific Advisor to the Indian Ministry of Defence. As a national counsellor, he played a significant role in the world-famous nuclear tests at Pokhran II. In 1981, he was awarded the Padma Bhushan Award, in 1909 the Padma Vibhushan, and in 1997 the highest civilian award of India' Bharat Ratna 'for modernizing the defence technology of India and his outstanding contribution. From July 25, 2002 - July 25, 2007, he served as President of India, becoming famous among Indians and receiving a",
                "the defence technology of India and his outstanding contribution. From July 25, 2002 - July 25, 2007, he served as President of India, becoming famous among Indians and receiving a lot of attention from Indian youth. He became popular as the People's President. Kalam worked as a professor, chancellor, and assistant at many institutions after leaving office. He experienced serious cardiac arrest on the evening of July 27, 2015, and fell unconscious and died 2 hours later. In 1999, Kalam published his autobiography and a book called The Wings of Fire. He has written many other books that are useful to the people of every generation."]
    db = Chroma_database()
    db.process_and_add_documents(chunks,"text.txt")
    query = "When did Dr. APJ Abdul Kalam pass away, and how?"
    results = db.retrive_text(query, file_name="text.txt",n_results=2)
    results