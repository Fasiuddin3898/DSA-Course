# LangGraph
LangGraph is a framework for building stateful, contolled LLM workflows and agentic applications using graph-based execution. It represents an application as nodes and edges, where nodes perform operations and edges determine how execution moves between them. It is especially useful for multi-step agents, loops, conditional workflows, human-in-the-loop systems, and multi-agent architectures.

LangChain = components
LangGraph = workflow orchestration

# Why LangGraph
Imagine this workflow: User -> Planner -> Research -> Analysis -> Validation -> Final Answer
But Sometimes:  Validation -> FAILED -> Research again
That's a loop
Normal Chain: A->B->C->D
LangGraph:
       ┌──────────────┐
       ↓              │
A → B → C → D         │
       │              │
       └──── failure ──┘
This is where graphs are powerful

# LangGraph core components
1. State: Stores information shared across the workflow
   class state(TypeDict):
         question: str
         context: list
         answer: str
    Think: state = shared memory of the workflow

2. Nodes: A node performs an operation
   Example: retrieve(), generate(), validate(), search()
   Conceptiually:
   def retrieve(state):
        ...
        return {"context": documemnts}
3. Edges: Edges determine where execution goes next
   retrieve -> generate
4. Conditional Edges: This is extremely important
   Example:
   Generate
   ↓
    Validate
    ↓
    ┌──────────────┐
    │              │
    Valid         Invalid
    │              │
    ↓              ↓
    END          Retrieve Again
