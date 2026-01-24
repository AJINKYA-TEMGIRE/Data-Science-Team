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

llm = Groq(id = "llama-3.1-8b-instant")

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

if __name__ == "__main__":
    data_loader_agent.cli_app()