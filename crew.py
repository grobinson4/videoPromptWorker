from crewai import Agent, Crew, Process, Task
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize the LLM
llm = ChatOpenAI(
    model="gpt-4",
    temperature=0.7,
    api_key=os.getenv("OPENAI_API_KEY")
)

class AITrendAnalysisCrew:
    """Crew for analyzing and documenting latest AI developments"""

    def research_analyst(self) -> Agent:
        return Agent(
            role="Research Analyst",
            goal="Analyze latest developments in AI technology with focus on Grok-2 and similar models",
            backstory="""You are an expert AI research analyst with deep knowledge of 
            large language models and their technical capabilities. You specialize in 
            analyzing AI breakthroughs and their potential impact.""",
            verbose=True,
            allow_delegation=False,
            llm=llm
        )

    def technical_writer(self) -> Agent:
        return Agent(
            role="Technical Writer",
            goal="Create comprehensive technical documentation and analysis reports",
            backstory="""You are a skilled technical writer with expertise in AI and ML. 
            You excel at translating complex technical concepts into clear, 
            well-structured documentation.""",
            verbose=True,
            allow_delegation=False,
            llm=llm
        )

    def create_tasks(self):
        return [
            Task(
                description="""Analyze the latest developments in AI technology, focusing on:
                1. Recent breakthroughs in large language models
                2. Technical capabilities of Grok-2 compared to other models
                3. Potential applications and impact
                4. Key challenges and limitations
                
                Provide specific examples and technical details.""",
                agent=self.research_analyst(),
                expected_output="A detailed analysis of current AI developments with focus on Grok-2"
            ),
            Task(
                description="""Create a comprehensive technical report based on the analysis:
                1. Executive summary of key findings
                2. Detailed technical analysis
                3. Comparative analysis with other models
                4. Future implications and recommendations
                
                Format the report in clear sections with examples and technical details.""",
                agent=self.technical_writer(),
                expected_output="A well-structured technical report on AI developments",
                output_file='output/ai_analysis_report.md'
            )
        ]

    def run(self) -> Crew:
        """Creates and runs the AI Trend Analysis crew"""
        crew = Crew(
            agents=[self.research_analyst(), self.technical_writer()],
            tasks=self.create_tasks(),
            process=Process.sequential,
            verbose=True
        )
        return crew
