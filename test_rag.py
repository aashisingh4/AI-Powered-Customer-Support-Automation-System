from rag import retrieve_context

query = input("Enter query: ")

context = retrieve_context(query)

print("\nRetrieved Context:\n")
print(context)