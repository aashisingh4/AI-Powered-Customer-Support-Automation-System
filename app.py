from graph import classify_intent, route_query
from agents import (
    sales_agent,
    technical_agent,
    billing_agent,
    account_agent
)

query = input("Enter query: ")

state = {
    "query": query
}

state.update(classify_intent(state))

print("Intent:", state["intent"])

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
    result = {"agent_response": "No agent found"}

print("\nResponse:")
print(result["agent_response"])