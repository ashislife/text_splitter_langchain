from langchain_experimental.text_splitter import SemanticChunker
from langchain_openai.embeddings import OpenAIEmbeddings

from dotenv import load_dotenv

load_dotenv()


text_splitter = SemanticChunker(
    OpenAIEmbeddings(),
    breakpoint_threshold_type="standard_deviation",
    breakpoint_threshold_amount=1
)

text="""
Artificial Intelligence (AI) is one of the most transformative technologies of the modern era. It enables computers to perform tasks that normally require human intelligence, such as understanding language, recognizing images, making decisions, and solving complex problems. AI is used in various industries, including healthcare, education, finance, agriculture, transportation, and entertainment.

Machine Learning is a branch of AI that allows systems to learn from data instead of being explicitly programmed. Algorithms analyze large datasets, identify patterns, and make predictions based on previous experiences. Deep Learning, a subset of Machine Learning, uses artificial neural networks with multiple layers to process information and achieve remarkable accuracy in tasks such as image classification and speech recognition.

Natural Language Processing (NLP) is another important field of AI. It focuses on enabling computers to understand, interpret, and generate human language. Applications of NLP include chatbots, language translation, sentiment analysis, document summarization, question-answering systems, and voice assistants.

"""
chunk=text_splitter.create_documents([text])

print(len(chunk))
print(chunk)