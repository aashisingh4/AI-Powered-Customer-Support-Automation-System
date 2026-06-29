def classify_intent(state):

    query = state["query"].lower()

    if "pricing" in query or "plan" in query:
        return {"intent": "sales"}

    elif "password" in query:
        return {"intent": "account"}

    elif "refund" in query:
        return {"intent": "billing"}

    elif "crash" in query:
        return {"intent": "technical"}

    elif "previous issue" in query:
        return {"intent": "memory"}

    return {"intent": "general"}


def route_query(state):

    intent = state["intent"]

    if intent == "sales":
        return "sales_agent"

    elif intent == "technical":
        return "technical_agent"

    elif intent == "billing":
        return "billing_agent"

    elif intent == "account":
        return "account_agent"

    elif intent == "memory":
        return "memory_manager"

    return "unknown"