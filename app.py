from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from langchain.agents import create_openai_tools_agent, AgentExecutor
from langchain import hub
from langchain_groq import ChatGroq
from composio_langchain import ComposioToolSet
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

# Initialize your tools
composio_toolset = ComposioToolSet()
create_event_tool = composio_toolset.get_tools(actions=['GOOGLECALENDAR_CREATE_EVENT'])[0]
find_event_tool = composio_toolset.get_tools(actions=['GOOGLECALENDAR_FIND_EVENT'])[0]
update_event_tool = composio_toolset.get_tools(actions=['GOOGLECALENDAR_UPDATE_EVENT'])[0]
delete_event_tool = composio_toolset.get_tools(actions=['GOOGLECALENDAR_DELETE_EVENT'])[0]
free_slots_tool = composio_toolset.get_tools(actions=['GOOGLECALENDAR_FIND_FREE_SLOTS'])[0]

tools = [create_event_tool, find_event_tool, update_event_tool, delete_event_tool, free_slots_tool]

# Initialize the language model
llm = ChatGroq(model='llama-3.3-70b-versatile')
current_date = datetime.now().strftime("%Y-%m-%d")
# Create the agent
prompt = hub.pull("hwchase17/openai-tools-agent")
agent = create_openai_tools_agent(llm, tools, prompt)

# Create the agent executor
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        user_message = data.get('message', '')
        user_message = f"{user_message} The current date is {current_date}"

        if not user_message:
            return jsonify({'error': 'No message provided'}), 400
            
        # Execute the task
        result = agent_executor.invoke({"input": user_message})
        
        return jsonify({
            'response': result.get('output', 'I apologize, but I couldn\'t process your request.'),
            'status': 'success'
        })
        
    except Exception as e:
        return jsonify({
            'error': str(e),
            'status': 'error'
        }), 500

if __name__ == '__main__':
    app.run(debug=True) 