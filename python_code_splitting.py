from langchain.text_splitter import RecursiveCharacterTextSplitter,Language


text="""
score = 85

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")
"""

# initialize the splitter 
splitter=RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size=400,
    chunk_overlap=0,

)

# perform the split 
chunk=splitter.split_text(text)

print(len(chunk))
print(chunk)