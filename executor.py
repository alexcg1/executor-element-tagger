from jina import Executor, DocumentArray, requests, Document
import numpy as np
from typing import Any, Dict


class ElementTypeTagger(Executor):
    def __init__(self, key_name="element_type", traversal_paths: str = "@r", *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.key_name = key_name
        self.traversal_paths = traversal_paths

    @requests
    def tag_doc(self, docs: DocumentArray, parameters: Dict[str, Any], **kwargs):
        traversal_paths = parameters.get("traversal_paths", self.traversal_paths)

        for doc in docs[traversal_paths]:
            if self.key_name in doc.tags.keys():
                pass
            elif doc.tensor is not None:
                doc.tags[self.key_name] = "image"
            elif doc.text:
                doc.tags[self.key_name] = "text"
            else:
                doc.tags[self.key_name] = "unknown"


