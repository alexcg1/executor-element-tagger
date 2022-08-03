from jina import DocumentArray, Document
from executor import ElementTypeTagger
import numpy as np

docs = DocumentArray(
    [
        Document(tags={"element_type": "foo"}),
        Document(text="J.R.R. Tolkien turns to p.3 on www.google.com"),
        Document(tensor=np.zeros([3, 3])),
        Document(blob="foo"),
    ]
)

ex = ElementTypeTagger(parameters={})
ex.tag_doc(docs, parameters={})

for doc in docs:
    print(doc.tags)
