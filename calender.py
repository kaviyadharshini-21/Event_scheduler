
from langchain.agents import create_openai_functions_agent, AgentExecutor
from langchain import hub
from composio_langchain import ComposioToolSet, Action, App
from langchain_groq import ChatGroq
import os
os.environ["COMPOSIO_API_KEY"]='iybjz4h5dawwgqx8u0aw'
os.environ["GROQ_API_KEY"]='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'
from langchain.agents import create_openai_tools_agent, AgentExecutor
from langchain import hub
from langchain_groq import ChatGroq
from composio_langchain import ComposioToolSet

# Initialize your tools
composio_toolset = ComposioToolSet()
create_event_tool = composio_toolset.get_tools(actions=['GOOGLECALENDAR_CREATE_EVENT'])[0]
find_event_tool = composio_toolset.get_tools(actions=['GOOGLECALENDAR_FIND_EVENT'])[0]
update_event_tool = composio_toolset.get_tools(actions=['GOOGLECALENDAR_UPDATE_EVENT'])[0]
quick_event_tool = composio_toolset.get_tools(actions=['GOOGLECALENDAR_QUICK_ADD'])[0]
get_calender_tool = composio_toolset.get_tools(actions=['GOOGLECALENDAR_GET_CALENDAR'])[0]
delete_event_tool = composio_toolset.get_tools(actions=['GOOGLECALENDAR_DELETE_EVENT'])[0]
free_slots_tool = composio_toolset.get_tools(actions=['GOOGLECALENDAR_FIND_FREE_SLOTS'])[0]
find_event_tool = composio_toolset.get_tools(actions=['GOOGLECALENDAR_FIND_EVENT'])[0]
tools = [create_event_tool, find_event_tool, update_event_tool]


prompt = hub.pull("hwchase17/openai-tools-agent")

# Initialize the language model
llm = ChatGroq(model='llama-3.3-70b-versatile')

# Create the agent
agent = create_openai_tools_agent(llm, tools, prompt)

# Create the agent executor
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# Define your task
task = "Create a 1 hour meeting event at 6.00PM AEST on 2025-02-28 regarding the agents project"

# Execute the task
result = agent_executor.invoke({"input": task})
print(result)
