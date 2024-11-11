from langchain import hub
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_community.vectorstores import FAISS
from langchain_core.tools import create_retriever_tool
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_text_splitters import RecursiveCharacterTextSplitter


def create_tools():
    def search_tool():
        search = TavilySearchResults()
        return search

    def retriever_tool():
        loader = WebBaseLoader("https://docs.smith.langchain.com/overview")
        docs = loader.load()
        documents = RecursiveCharacterTextSplitter(
            chunk_size=1000, chunk_overlap=200
        ).split_documents(docs)
        vector = FAISS.from_documents(documents, OpenAIEmbeddings())
        retriever = vector.as_retriever()

        retriever_tool = create_retriever_tool(
            retriever,
            "langsmith_search",
            "Search for information about LangSmith. For any questions about LangSmith, you must use this tool!",
        )
        return retriever_tool

    return [search_tool(), retriever_tool()]



def create_agent():
    llm = ChatOpenAI(model="gpt-3.5-turbo-0125", temperature=0)
    prompt = hub.pull("hwchase17/openai-functions-agent")
    tools = create_tools()
    agent = create_tool_calling_agent(llm, tools, prompt)
    return agent, tools

def run():
    agent, tools = create_agent()
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

    inp = input("Ask me anything: ")
    while inp != 'Q':
        agent_executor.invoke({"input": inp})
        inp = input("Ask me anything: ")