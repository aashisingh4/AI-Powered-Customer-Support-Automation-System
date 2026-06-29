from memory import save_conversation, get_last_issue

save_conversation(
    "David",
    "I have a billing issue"
)

previous_issue = get_last_issue("David")

print(previous_issue)