# AI Learning Journey

This repository documents my exploration and learning in Artificial Intelligence, focusing on practical implementations of modern AI techniques.

## Chapter 1: Retrieval-Augmented Generation (RAG) with LangChain, ChromaDB, and OpenAI GPT-3.5-turbo

### Overview

In this first chapter, I delved into building a Retrieval-Augmented Generation (RAG) system. The project demonstrates how to combine document retrieval with large language model capabilities to provide more accurate and contextually relevant responses.

### Key Concepts Explored

- **Document Loading and Processing**: Using LangChain's document loaders to handle PDF and Markdown files from a directory structure.
- **Text Chunking**: Implementing RecursiveCharacterTextSplitter to break down large documents into manageable chunks of 200 characters with 50-character overlap.
- **Embeddings Creation**: Utilizing SentenceTransformer's all-MiniLM-L6-v2 model to generate vector embeddings for each text chunk.
- **Vector Database Integration**: Setting up ChromaDB as the vector database to store and query document embeddings efficiently.
- **LLM Integration**: Connecting the system with OpenAI's GPT-5-mini model through LangChain, using structured prompts and output parsing.
- **Response Comparison**: Analyzing the difference between raw retrieval results and LLM-augmented responses to understand the value of RAG.

### Implementation Highlights

- Loaded documents from `github_data/my_articles/` (PDFs) and `github_data/markdown_files/` (Markdown).
- Created embeddings for semantic search capabilities.
- Built a ChromaDB collection to store vectorized content.
- Implemented a question-answering chain that retrieves relevant context and generates coherent responses.
- Demonstrated how RAG improves upon standalone LLM responses by providing domain-specific context.

### Files

- `1_chatgpt_langchain_chromadb_all_mini_l6_v2__llm_rag_integration/rag_llm_integration.ipynb`: Jupyter notebook containing the complete implementation.

---

## Chapter 2: Understanding How Embedding Models Work

### Overview

In this chapter, I explored the fundamental mechanics of how embedding models generate vector representations of text. This is a critical component in RAG systems and semantic search.

### Key Concepts Explored

- **Tokenization**: Understanding how sentences are split into tokens and converted to token IDs. Explored subword tokenization techniques like WordPiece and Byte Pair Encoding (BPE) used in models like BERT, where words like "unbelievable" are broken into subword units.
- **Token to Vector Conversion**: Learning how embedding matrices map token IDs to dense vector representations. Different models have varying embedding dimensions (e.g., BERT uses 768-dimensional embeddings).
- **Contextual Transformation**: Discovering how Transformer architectures use self-attention mechanisms to update token embeddings based on context, making embeddings context-aware rather than static.
- **Sentence Embedding Aggregation**: Understanding pooling strategies like mean pooling and max pooling that reduce individual token embeddings into a single sentence-level embedding vector.
- **Embedding Dimensionality**: Learning how embedding dimensions are model-specific and affect both computational efficiency and representation capability.

### Implementation Highlights

- Explored the step-by-step process from raw text to final embedding vectors.
- Analyzed the flow: Tokenization → Token Embedding → Contextual Transformation → Sentence Aggregation.
- Understood the role of embedding matrices as trainable parameters in models.
- Examined subword tokenization for handling complex words and out-of-vocabulary terms.

### Files

- `2_retrieval_augumented_generation/2_how_embedding_model_works.ipynb`: Jupyter notebook containing detailed explanation of embedding generation.

---

## Chapter 3: Implementing Similarity Search Techniques

### Overview

In this chapter, I delved into the practical implementation of similarity search methods used to find semantically relevant documents. These techniques are essential for the retrieval component in RAG systems.

### Key Concepts Explored

- **Cosine Similarity**: Measuring the angle between two embedding vectors. Focuses on direction rather than magnitude, making it ideal for high-dimensional sparse data. Implemented both using scikit-learn and manual implementation using dot product and vector magnitudes.
- **Euclidean Distance**: Calculating the straight-line distance between two vectors in embedding space. Suitable for measuring absolute distance and works well in lower-dimensional spaces. Implemented using both manual calculation and Python's `math.dist()` function.
- **Dot Product**: Direct multiplication of corresponding vector elements. Useful as a similarity metric, especially when vectors are normalized.
- **SentenceTransformer Integration**: Leveraging the all-MiniLM-L6-v2 model (384-dimensional embeddings) for practical similarity search implementations.
- **Query and Document Matching**: Implementing practical examples to find which documents are most relevant to a given query by comparing embedding vectors.

### Implementation Highlights

- Created embeddings for sample documents using SentenceTransformer.
- Implemented cosine similarity calculations both using scikit-learn and from scratch using NumPy.
- Calculated Euclidean distances to measure absolute separation between embeddings.
- Computed dot product similarity scores between query and document embeddings.
- Compared different similarity metrics to understand their use cases and output ranges.
- Demonstrated querying ("What is the capital of France?") against a document corpus.

### Files

- `2_retrieval_augumented_generation/3_how_similarity_search_works.ipynb`: Jupyter notebook containing practical implementations of different similarity search techniques.

---

## Future Chapters

[To be added as new explorations are completed]
