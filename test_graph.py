from workflows.support_graph import (
    support_graph
)

result = support_graph.invoke(

    {
        "transcript":
        "I have a question about your services."
    }

)

print(result)

