from app.graph import graph

config = {"configurable": {"thread_id": "1"}}
def stream_graph_updates(user_input: str):
    stream = graph.stream(
        {"messages": [{"role": "user", "content": user_input}]},
        config,
        stream_mode="values",
    )

    for event in stream:
        if "messages" in event:
            event["messages"][-1].pretty_print()

user_input = input("Who do you want to talk to, at what age? ")
while True:
    try:
        if user_input.lower() in ["quit", "exit", "q"]:
            print("Goodbye!")
            break
        stream_graph_updates(user_input)
        user_input = input("User: ")
    except Exception as e:
        print(e)
