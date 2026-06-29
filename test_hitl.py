from supervisor import (
    requires_human_approval,
    human_approval
)

query = input("Customer Query: ")

if requires_human_approval(query):

    print(
        "\nHuman approval required."
    )

    decision = human_approval()

    print(
        "\nDecision:",
        decision
    )

else:

    print(
        "\nNo approval required."
    )