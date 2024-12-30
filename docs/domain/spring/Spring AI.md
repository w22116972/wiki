# Spring AI

## Concepts

AI modes are algorithms designed to process and generate information.
- Input -> Gen AI Model -> Output

Prompts serve as input to guide the AI model to generate specific output.
- template `Tell me {prompt1} about {prompt2}`

Embeddings are numerical vector representations of relationships between inputs
- Input -> Embedding Model -> Vector/Embeddings -> Vectors Store
- Calculating the numerical distance between the vector representations of two inputs can determine the similarity between the objects used to generate the embedding vectors.

Tokens are building blocks of how an AI model works
- Input -> Tokenizer -> Tokens -> Embedding Model -> Embeddings
- Tokens are related to costs
- Models will limit the number of tokens they can process at once (aka context window)

RAG
![](./assets/images/30939100228371.png)
