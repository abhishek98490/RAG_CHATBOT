# RAG Chatbot Project 

This is a **Retrieval-Augmented Generation (RAG) Chatbot** project that enables users to interact with a Large Language Model (LLM) based on the contents of uploaded documents. The documents (in `.txt`, `.docx`, or `.pdf` formats) are processed to extract their text content, which is then used to answer user queries.

## Features

- **Document Upload & Processing**: Users can upload `.txt`, `.docx`, and `.pdf` files, which are then processed for text extraction.
- **Text Chunking with Sliding Window**: The extracted text is chunked using a sliding window technique, with overlapping tokens, making it easier to search and retrieve relevant information.
- **Semantic Search for Information Retrieval**: A semantic search method is used to retrieve contextually relevant text chunks based on user queries.
- **LLM Integration via SambaNova**: Users can interact with the Llama3.1 8B LLM via the [SambaNova AI Cloud API](https://cloud.sambanova.ai/apis), allowing for advanced querying and generation capabilities.
- **Logging and Error Handling**: The project includes robust logging and custom error handling for better debugging and traceability.

## Installation

1. **Clone the repository:**
    ```bash
    git clonehttps://github.com/abhishek98490/RAG_CHATBOT.git
    cd RAG_Chatbot
    ```

2. **Set up a virtual environment (optional but recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up your `.env` file for SambaNova API keys:**\
   You can find the API keys for SambaNova on their official website.\
   Once you have obtained the API keys, you can set up your `.env` file by adding the following lines:

   ```bash
    SAMBANOVA_API_KEY=YOUR_API_KEY
   ```
   Replace `YOUR_API_KEY` and `YOUR_API_SECRET` with the actual API keys provided by SambaNova.


## Project Structure

The project is organized as follows:

- `src/`: Contains all the core modules for the project.
    - `logger/`: Custom logging functionality for better traceability.
    - `exception/`: Custom exceptions for error handling.
    - `data_ingestion/`: Modules for document loading and text extraction.
    - `chunking/`: Responsible for breaking down documents into smaller chunks using a sliding window.
    - `vector_database/`: Handles database operations for storing and retrieving document chunks.
    - `LLM_gateway/`: Manages the communication with the SambaNova Large Language Model API.

## Workflow

1. **Document Loading & Text Extraction**:
    - When a document is uploaded, the content is loaded using the `Document_Loader` class. Supported formats include `.txt`, `.docx`, and `.pdf`.

2. **Chunking**:
    - The loaded text is processed into chunks using the **sliding window technique** with overlapping tokens. This method ensures that important context is retained across adjacent chunks, enabling better retrieval for queries.

3. **Storing in Vector Database**:
    - The chunked text is added to a vector database (`Chroma_database`), where each chunk is stored with metadata and an ID.

4. **Semantic Search for Information Retrieval**:
    - When a user submits a query, the system retrieves relevant chunks from the vector database based on the semantic meaning of the query using `retrive_text`. The results are ranked based on relevance.

5. **Interaction with LLM**:
    - The context retrieved from the database is sent to an LLM via the **SambaNova AI Cloud API** (`LLM_gateway`), which generates a response to the user’s query.

## Running the Chatbot

1. **Main Entry Point**:
    - The `main.py` file is the main entry point for running the RAG chatbot. It accepts two arguments: `file_path` (path to the document) and `query` (the question to ask).

2. **Run the chatbot**:
    - To run the chatbot with a document and a query, use the following command:
    ```bash
    python main.py "path/to/your/document.pdf" "Your query here"
    ```

    Example:
    ```bash
    python main.py "data/Understanding_Climate_Change.pdf" "How much degree Celsius has the global temperature risen?"
    ```

## Code Breakdown

- **`Document_Loader`**: Responsible for loading the document and extracting the text.
- **`Chunking`**: Handles the splitting of large documents into smaller chunks using the sliding window technique with overlapping tokens.
- **`Chroma_database`**: A vector database used for storing and retrieving document chunks.
- **`LLM_gateway`**: Sends the context to the SambaNova AI Cloud API and retrieves a response based on the query.

## Logging and Error Handling

- The project uses a custom logger to track the flow of execution and important events. It ensures that errors are logged for easier debugging.
- Custom exceptions are raised and handled to make the code more resilient and easier to maintain.


## Planned Features

- **Multi-file Upload**: Support for uploading multiple files at once.
- **Improved Query Handling**: Enhance the LLM’s ability to handle more complex queries.
- **Real-time Information Retrieval**: The chatbot will provide responses based on the extracted text from the documents (implemented in `main.py`).
- **User Interface**: A graphical user interface (GUI) for easier interaction with the chatbot. (yet to be developed).

## Future Improvements

- **User Interface**: A graphical user interface (GUI) for easier interaction with the chatbot.
- **Deployment**: Host the chatbot on a cloud platform (e.g., AWS, Azure) for public access.
- **Enhanced Chunking Algorithms**: Implement more sophisticated chunking methods for better context retrieval.
