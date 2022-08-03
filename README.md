# ElementTypeTagger

This Executor looks at the `tensor` and `text` attributes of a Document and assigns a tag accordingly. By default it stores the value (one of `text`, `image` or `uknown`) in `doc.tags["element_type]`. This can be modified with the `key_name` parameter.

It is intended to be used in a PDF search engine, where tables are extracted first and pre-tagged as `table`. This then allows filtering with (for example) [AnnLiteIndexer](https://hub.jina.ai/executor/7yypg8qk)
