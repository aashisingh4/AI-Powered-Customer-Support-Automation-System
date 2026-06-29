# AI-Powered Customer Support Automation System using LangGraph

## Project Overview

This project implements an AI-Powered Customer Support Automation System using LangGraph. The system automates customer support by classifying customer queries, routing them to specialized support agents, maintaining customer conversation history using SQLite, supporting human approval for critical requests, and generating professional responses through a supervisor agent.

The project is developed as part of the LangGraph Customer Support Automation assignment.

---

## Features

- Intent Classification
- Conditional Agent Routing
- Sales Support Agent
- Technical Support Agent
- Billing Support Agent
- Account Support Agent
- SQLite Conversation Memory
- Human-in-the-Loop Approval
- Supervisor Response Improvement
- Interactive Customer Query Processing

---

## Project Structure

```
customer_support_langgraph/
│
├── main.py
├── graph.py
├── state.py
├── agents.py
├── supervisor.py
├── memory.py
├── rag.py
├── memory.db
├── requirements.txt
├── README.md
├── Workflow.png
└── documents/
    ├── pricing.txt
    ├── faq.txt
    ├── policy.txt
    └── technical_manual.txt
```

---

## Technologies Used

- Python 3.9
- LangGraph
- LangChain
- SQLite
- OpenAI API
- VS Code

---

## Workflow

1. Customer enters a query.
2. Intent Classification identifies the query type.
3. Query is routed to the appropriate support agent.
4. Relevant response is generated.
5. Critical requests require human approval.
6. Supervisor reviews and improves the response.
7. Customer conversations are stored in SQLite memory.
8. Previous issues can be recalled from memory.

---

## Supported Departments

| Department | Purpose |
|------------|---------|
| Sales | Pricing, subscription plans, product information |
| Technical Support | Errors, crashes, installation, login issues |
| Billing | Payments, invoices, refunds |
| Account | Password reset, profile updates, account management |

---

## Human Approval Requests

The following requests require supervisor approval:

- Refund Requests
- Subscription Cancellation
- Account Closure
- Compensation Requests
- Escalation Requests

---

## Memory Implementation

SQLite is used to store customer conversations.

Example:

Customer:
```

My application crashes whenever I upload a file.

```

Later:

```

What was my previous support issue?

```

Output:

```

Memory Recall

Your previous support issue was:
My application crashes whenever I upload a file.

```

---

## Installation

### Clone the repository

```bash
git clone <repository-url>
```

### Navigate to the project

```bash
cd customer_support_langgraph
```

### Create virtual environment

```bash
python3 -m venv venv
```

### Activate virtual environment

macOS/Linux

```bash
source venv/bin/activate
```

Windows

```bash
venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Project

Run the application:

```bash
python main.py
```

The program accepts multiple customer queries until the user types:

```
exit
```

---

## Sample Queries

### Query 1

```
What are the pricing plans available for your software?
```

### Query 2

```
I forgot my account password.
```

### Query 3

```
My application crashes whenever I upload a file.
```

### Query 4

```
I need a refund for my annual subscription.
```

### Query 5

```
What was my previous support issue?
```

---

## Expected Output

- Intent Classification
- Agent Routing
- Specialized Agent Response
- Human Approval (for refund requests)
- Supervisor Improved Response
- SQLite Memory Recall

---

## Deliverables Included

- Source Code
- LangGraph Workflow
- SQLite Memory Database
- README.md
- Workflow Diagram
- Project Screenshots

---

## Author

**Name:** Aashi Singh

AI-Powered Customer Support Automation using LangGraph# AI-Powered-Customer-Support-Automation-System
