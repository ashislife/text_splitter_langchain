from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader



loader=PyPDFLoader('Unit.pdf')



docs=loader.load()

splitter=CharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=0,
    separator=''

)


result=splitter.split_documents(docs)
print(result[0]) # print First chunk 

print(result[0].page_content) # print page content of first chunk  