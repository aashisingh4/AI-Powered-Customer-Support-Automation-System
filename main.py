from graph import classify_intent, route_query

from agents import (
    sales_agent,
    technical_agent,
    billing_agent,
    account_agent
)

from supervisor import (
    requires_human_approval,
    human_approval,
    supervisor_review
)

from memory import save_conversation, get_last_issue


while True:

    query = input("\nCustomer Query (type 'exit' to quit): ")

    if query.lower() == "exit":
        print("Exiting...")
        break

    # Memory Recall
    if "previous support issue" in query.lower():

        print("\nMemory Recall")
        print("Your previous support issue was:")
        print(get_last_issue("David"))

        continue

    # Save current conversation
    save_conversation("David", query)

    state = {
        "query": query
    }

    state.update(classify_intent(state))

    print("\nIntent:", state["intent"])

    route = route_query(state)

    print("Route:", route)

    if route == "sales_agent":

        result = sales_agent(state)

    elif route == "technical_agent":

        result = technical_agent(state)

    elif route == "billing_agent":

        result = billing_agent(state)

    elif route == "account_agent":

        result = account_agent(state)

    else:

        result = {
            "agent_response": "Unknown request."
        }

    response = result["agent_response"]

    # Human Approval
    if requires_human_approval(query):

        print("\nHuman Approval Required")

        decision = human_approval()

        if decision.lower() != "approve":

            print("\nRequest rejected.")

            continue

    # Supervisor Review
    response = supervisor_review(response)

    print("\nFinal Response\n")

    print(response)