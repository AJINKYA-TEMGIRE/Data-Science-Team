from agno.agent import Agent
from agno.models.groq import Groq
from agno.os import AgentOS
from agno.team import Team
from agno.db.sqlite import SqliteDb
from agno.tools.csv_toolkit import CsvTools
from agno.tools.file import FileTools
from agno.tools.pandas import PandasTools
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.python import PythonTools
from agno.tools.shell import ShellTools
from agno.tools.visualization import VisualizationTools
from dotenv import load_dotenv
from pathlib import Path


load_dotenv()

llm = Groq(id = "openai/gpt-oss-120b")

base_dir = Path(__file__).parent

data_path = Path(__file__).parent / "data" / "Pune_property_data.csv"

db = SqliteDb(db_file="memory.db",
              session_table="session_table")


data_loader_agent = Agent(
    id="data-loader-agent",
    name="Data Loader Agent",
    model=llm,
    role="Data loading and reading csv files",
    db=db,
    add_history_to_context=True,
    num_history_runs=3,
    instructions=[
        "You are an expert in loading csv files from the project folder.",
        "You have the capability to list csv files and read them when the user asks about data.",
        "Only use tools when the user asks about files, csv data, or data analysis.",
        "If the user asks general questions (like greetings or 'what can you do'), respond normally without using tools.",
        "Never call a tool with empty or null arguments.",
        "When reading CSV files, do not read more than 20–30 rows.",
        "Use the CSV tool for reading CSV files."
    ],
    tools=[CsvTools(csvs=[data_path] , row_limit = 30 , enable_query_csv_file = False)],
)

file_manager_agent = Agent(
    id="file-manager-agent",
    name="File Manager Agent",
    model=llm,
    role="Manages Filesystem",
    instructions=["You are an expert File Management Agent",
                  "Your task is to list down files when asked to do it",
                  "you can also read and write files",
                  "make sure to never read csv files, you can only list them"],
    tools=[FileTools(base_dir=base_dir)]
)

data_understanding_agent = Agent(
    id="data-understanding-agent",
    name="Data Understanding Agent",
    model=llm,
    role="Data understanding and Exploration assistant",
    db=db,
    add_history_to_context=True,
    num_history_runs=3,
    read_chat_history=True,
    instructions=["You are an expert in handling pandas operations on a df",
                  "you can create df and also perform operations on it",
                  "the operations you perform on a df are head(), tail(), info(), describe() for numerical columns and you can also calculate the value_counts() for categorical columns",
                  "make sure to list down the numerical and categorical columns in the df",
                  "you can also check the shape of the df using the .shape attribute",
                  "you also have access to tools which can search for data files"
                  ],
    tools=[PandasTools(), FileTools(base_dir=base_dir)],
)


if __name__ == "__main__":
    data_loader_agent.cli_app()