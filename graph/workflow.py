# graph/workflow.py

from langgraph.graph import StateGraph, END
from graph.state import AgentState
from nodes import (
    input_handler,
    intent_detector,
    planner,
    executor,
    output_formatter
)

def should_ask_clarification(state: AgentState) -> str:
    """Check if we need to ask user for clarification"""
    if state["needs_clarification"] and not state.get("user_clarification"):
        return "clarify"
    return "plan"

def should_continue_execution(state: AgentState) -> str:
    """Check if there are more steps to execute"""
    if state["current_step"] < len(state["execution_plan"]):
        return "execute"
    return "format"

# Build graph
workflow = StateGraph(AgentState)

# Add nodes
workflow.add_node("input", input_handler.process)
workflow.add_node("intent", intent_detector.process)
workflow.add_node("plan", planner.process)
workflow.add_node("execute", executor.process)
workflow.add_node("format", output_formatter.process)

# Define flow
workflow.set_entry_point("input")
workflow.add_edge("input", "intent")

workflow.add_conditional_edges(
    "intent",
    should_ask_clarification,
    {
        "clarify": END,  # Stop and ask user
        "plan": "plan"   # Continue to planning
    }
)

workflow.add_edge("plan", "execute")

workflow.add_conditional_edges(
    "execute",
    should_continue_execution,
    {
        "execute": "execute",  # Loop for multi-step
        "format": "format"     # Done executing
    }
)

workflow.add_edge("format", END)

# Compile
app = workflow.compile()