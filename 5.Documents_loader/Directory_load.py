from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader

loader = DirectoryLoader(
    path=r"Documents_loader\Notes",
    glob="*.pdf",
    loader_cls=PyPDFLoader
)

#docs = loader.load()
#lazy loading of documents
docs = loader.lazy_load()

print(type(docs))
#print(f"Total documents loaded: {len(docs)}")
print(f"First Document content :\n {docs.__next__().page_content}")