from supervisor import supervisor_review

response = input("Agent Response:\n")

final = supervisor_review(response)

print("\nFinal Response:\n")
print(final)