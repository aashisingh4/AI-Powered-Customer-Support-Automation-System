from memory import save_conversation, get_last_issue

save_conversation(
    "David",
    "I have a billing issue"
)

print(
    "Customer: What was my previous support issue?"
)

print(
    get_last_issue("David")
)