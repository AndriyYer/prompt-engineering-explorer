import os
import json
import time
from datetime import datetime
from pathlib import Path
from typing import Dict, List
import typer
from openai import OpenAI, RateLimitError, APIError
from rich.console import Console
from rich.table import Table
from dotenv import load_dotenv

# Initialize Rich console for better output formatting
console = Console()
app = typer.Typer()

# Load environment variables
load_dotenv()

class PromptTester:
    def __init__(self, use_mock=False):
        self.use_mock = use_mock
        if not use_mock:
            self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.results_dir = Path("results/comparison_logs")
        self.results_dir.mkdir(parents=True, exist_ok=True)
        
    def load_prompts(self, technique: str) -> Dict:
        """Load prompt examples for the specified technique."""
        file_path = Path(f"src/examples/{technique}_prompts.json")
        if not file_path.exists():
            return {"default": "Summarize the main themes of Romeo and Juliet."}
        
        with open(file_path, "r") as f:
            return json.load(f)

    def mock_response(self, prompt: str) -> str:
        """Generate a mock response for testing without API calls."""
        return f"Mock response for prompt: {prompt[:50]}..."

    def test_prompt(self, prompt: str, max_retries=3, delay=2) -> str:
        """Test a single prompt with GPT-3.5 with retry logic."""
        if self.use_mock:
            return self.mock_response(prompt)

        for attempt in range(max_retries):
            try:
                response = self.client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": prompt}],
                    max_tokens=1000
                )
                return response.choices[0].message.content
            except RateLimitError as e:
                if attempt == max_retries - 1:
                    console.print(f"[red]Rate limit exceeded after {max_retries} attempts.[/red]")
                    return ""
                console.print(f"[yellow]Rate limit hit, waiting {delay} seconds...[/yellow]")
                time.sleep(delay)
                delay *= 2  # Exponential backoff
            except APIError as e:
                console.print(f"[red]API Error: {e}[/red]")
                return ""
            except Exception as e:
                console.print(f"[red]Error testing prompt: {e}[/red]")
                return ""

    def log_results(self, technique: str, results: List[Dict]):
        """Log test results to a file."""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        log_file = self.results_dir / f"{technique}_{timestamp}.json"
        
        with open(log_file, "w") as f:
            json.dump(results, f, indent=2)

    def display_results(self, results: List[Dict]):
        """Display results in a formatted table."""
        table = Table(title="Prompt Testing Results")
        table.add_column("Prompt Type", style="cyan")
        table.add_column("Prompt", style="green")
        table.add_column("Response Length", style="magenta")
        
        for result in results:
            table.add_row(
                result["type"],
                result["prompt"][:50] + "...",
                str(len(result["response"]))
            )
        
        console.print(table)

@app.command()
def test_prompts(
    technique: str = typer.Option(
        "basic",
        help="Prompting technique to test (basic, chain-of-thought, few-shot, role)",
    ),
    mock: bool = typer.Option(
        False,
        help="Use mock responses instead of real API calls"
    )
):
    """Test different prompting techniques and compare results."""
    tester = PromptTester(use_mock=mock)
    prompts = tester.load_prompts(technique)
    results = []

    with console.status("[bold green]Testing prompts..."):
        for prompt_type, prompt in prompts.items():
            response = tester.test_prompt(prompt)
            results.append({
                "type": prompt_type,
                "prompt": prompt,
                "response": response,
                "timestamp": datetime.now().isoformat()
            })

    tester.log_results(technique, results)
    tester.display_results(results)
    
    console.print("\n[bold green]Results have been logged to the results directory.[/bold green]")

if __name__ == "__main__":
    app()