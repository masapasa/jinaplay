from docarray import DocumentArray, Document
index_file_paths = ['index1.txt', 'index2.txt', 'index3.txt']  # path to all of your indices
da = DocumentArray()
for path in index_file_paths:  # accumulate all your indices into one DocumentArray
    d = Document(uri=path).load_uri_to_text()
    da_path = DocumentArray(Document(text=s.strip()) for s in d.text.split('\n') if s.strip())
    da.extend(da_path)

da.apply(lambda d: d.embed_feature_hashing())

q = (
    Document(text='....................')
    .embed_feature_hashing()
    .match(da, limit=5, exclude_self=True, metric='jaccard', use_scipy=True)
)

print(q.matches[:, ('text', 'scores__jaccard')])