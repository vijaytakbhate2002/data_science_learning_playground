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

## Chapter 2.1: Understanding How Embedding Models Work

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

## Chapter 2.2: Implementing Similarity Search Techniques

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

## Chapter 3.1: Understanding How Transformers Work - Self-Attention Mechanism

### Overview

In this chapter, I explored the core mechanism that powers modern transformers: **self-attention**. This mechanism is fundamental to understanding how transformer models like BERT, GPT, and others process sequential information and capture contextual relationships between tokens.

### Key Concepts Explored

- **Input Embeddings**: Understanding how tokens are converted to dense vector representations. The notebook demonstrates this with a simple example of "The cat sat" with 4-dimensional embeddings.
- **Query, Key, Value Projections**: Learning how input embeddings are transformed into three different representations:
  - **Query (Q)**: Represents the current token being processed and what it's "looking for"
  - **Key (K)**: Represents what each token "contains" or can offer
  - **Value (V)**: Contains the actual information to be aggregated based on attention weights
- **Attention Score Computation**: Computing raw attention scores using the dot product between Query and transposed Key matrices (Q · K^T). These scores indicate how much each token should "attend to" other tokens.
- **Scaling Mechanism**: Dividing attention scores by √(embedding_dimension) (variance stabilizer) to prevent gradient saturation in softmax, which is why it's called "Scaled Dot-Product Attention".
- **Probability Distribution**: Applying softmax to attention scores to convert them into normalized probability distributions, allowing the model to determine how much weight each position should have.
- **Weighted Value Aggregation**: Computing the final output by taking a weighted sum of value vectors using the attention probabilities. This produces context-aware embeddings for each token.
- **Contextual Understanding**: Understanding how attention scores reveal semantic relationships (e.g., diagonal values show self-attention, off-diagonal values show inter-token relationships).

### Implementation Highlights

- Implemented self-attention mechanism from scratch using NumPy, visualizing each step with heatmaps.
- Started with simple 4-dimensional embeddings for clarity and understanding.
- Computed Query, Key, and Value matrices through linear transformations with learnable weight matrices.
- Calculated raw attention scores and visualized their distribution before and after scaling.
- Applied softmax to obtain normalized attention probabilities.
- Demonstrated how attention weights influence final token representations by showing weighted value aggregation for each token.
- Showed practical insights: the diagonal of attention matrices reveals self-attention (each token attending to itself), and off-diagonal values show inter-token relationships (e.g., "cat" and "sat" showing ~25% attention to each other).

### Mathematical Formula

The complete self-attention formula is:

$$\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V$$

Where:

- Q, K, V are Query, Key, and Value matrices
- $d_k$ is the embedding dimension (used as the variance stabilizer)
- The scaling factor prevents attention scores from becoming too extreme

### Why This Matters

Self-attention is the foundational building block of transformer architectures. It enables:

- **Parallel Processing**: All tokens are processed simultaneously (unlike RNNs)
- **Long-Range Dependencies**: The mechanism can capture relationships between distant tokens
- **Interpretability**: Attention weights show which parts of the input the model focuses on
- **Context Awareness**: Each token's representation is updated based on its relationship with all other tokens

### Resources

- **Inspiration**: YouTube video by Andrej Karpathy explaining self-attention in transformers
  - Link: https://youtu.be/vkhPtpUiLd8?si=IDipB1yL8X2tcnPf

### Files

- `3_understanding_transformer_working/1_self_attention.ipynb`: Jupyter notebook containing step-by-step NumPy implementation of the self-attention mechanism with visualizations.

---

## Future Chapters

[To be added as new explorations are completed]
