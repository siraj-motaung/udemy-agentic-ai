import tiktoken

enc = tiktoken.encoding_for_model("gpt-4o")


text = "Hey There! My name is Siraj Motaung"

token = enc.encode(text)

print(token)
print(enc.decode(token))
