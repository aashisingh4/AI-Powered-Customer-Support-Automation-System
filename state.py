from typing import TypedDict, List

class SupportState(TypedDict):
    customer_id: str
    query: str

    intent: str

    retrieved_context: str

    requires_approval: bool
    approval_status: str

    memory_context: str

    agent_response: str
    final_response: str

    conversation_history: List[str]