from crew import AITrendAnalysisCrew
import os

def main():
    # Create output directory if it doesn't exist
    os.makedirs('output', exist_ok=True)
    
    # Initialize the crew
    ai_analysis_crew = AITrendAnalysisCrew()
    
    try:
        # Get the crew instance and run it
        crew = ai_analysis_crew.run()
        result = crew.kickoff()
        
        print("\n🎉 Analysis Complete! 🎉")
        print("\nCheck the output/ai_analysis_report.md file for the detailed report.")
        
        print(f"API Key: {os.getenv('OPENAI_API_KEY')}")  # Just print the first few characters
        
        return result
        
    except Exception as e:
        print(f"❌ An error occurred: {str(e)}")
        raise

if __name__ == "__main__":
    main()
