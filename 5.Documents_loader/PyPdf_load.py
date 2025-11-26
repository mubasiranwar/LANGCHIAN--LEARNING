from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('Documents_loader\Andrew Ng Deep Learning Notes.pdf')

docs = loader.load()

print(type(docs))
print(f"Pages in pdf :{len(docs)}")
print(f"First Page content :\n {docs[0].page_content}")
print(docs[0].metadata)
print(f"2nd Page content :\n {docs[1].page_content}")
print(docs[1].metadata)