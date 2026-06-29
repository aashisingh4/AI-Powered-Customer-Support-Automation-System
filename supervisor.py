from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="llama3.2:3b",
    temperature=0
)


def requires_human_approval(query):

    query = query.lower()

    keywords = [
        "refund",
        "cancel subscription",
        "close account",
        "account closure",
        "compensation",
        "management"
    ]

    return any(word in query for word in keywords)


def human_approval():

    decision = input(
        "Supervisor Approval (approve/reject): "
    )

    return decision


def supervisor_review(response):

    prompt = f"""
You are a customer support supervisor.

Improve the following response.
Make it polite, professional and concise.

Response:
{response}
"""

    result = llm.invoke(prompt)

    return result.content