from langchain.text_splitter import RecursiveCharacterTextSplitter


text="""
My Name is Ashish
I am 35 year old

I live in Gurgoan
How are you 
"""

# initialize the splitter 
splitter=RecursiveCharacterTextSplitter(
    chunk_size=25,
    chunk_overlap=0,

)

# perform the split 
chunk=splitter.split_text(text)

print(len(chunk))
print(chunk)