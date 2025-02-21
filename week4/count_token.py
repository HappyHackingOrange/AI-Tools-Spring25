import tiktoken

enc = tiktoken.encoding_for_model('gpt-4o')
tokens = enc.encode('Say "Hello world" in Python')

print(tokens)
print([enc.decode_single_token_bytes(token) for token in tokens])