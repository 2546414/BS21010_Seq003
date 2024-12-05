# Import of library - Graphviz
from graphviz import Digraph   

dot = Digraph(comment='EEG Data Processing Flow')
dot.attr(rankdir='TB', size='8,8')

dot.node('A', 'Input EEG Data')
dot.node('B', 'Preprocessing')
dot.node('C', 'Filtering')
dot.node('D', 'Feature Extraction')
dot.node('E', 'Visualization')
dot.node('F', 'Output Results')

dot.edge('A', 'B')
dot.edge('B', 'C')
dot.edge('C', 'D')
dot.edge('D', 'E')
dot.edge('E', 'F')

dot.render('EEG_processing_flow',format='png', cleanup=True)
print("Flow diagram has been generated as 'EEG_processing_flow.png'")

from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

def create_table(title, items):
    table = Table(title=title, show_header=False, expand=True)
    table.add_column("Items", style="cyan")
    for item in items:
        table.add_row(item)
    return table

# Input needed from the user
input_table = create_table("Input needed from the user", [
    "1. Raw EEG data file",
    "2. Sampling rate",
    "3. Electrode locations",
    "4. Time window of interest",
    "5. Frequency bands of interest"
])

# Decisions to be made
decisions_table = create_table("Decisions to be made", [
    "1. Type of preprocessing (e.g. artifact removal, referencing)",
    "2. Filtering methods (e.g., bandpass, notch)",
    "3. Feature extraction techniques (e.g. power spectral density, coherence)",
    "4. Visualization type (e.g. topographic maps, time-frequency plots)"
])

# How the results will be presented
results_table = create_table("How the results will be presented", [
    "1. Interactive plots",
    "2. Statistical summaries",
    "3. Exportable figures and data"
])

# Create a panel for each section
input_panel = Panel(input_table, title="User Input", border_style="green")
decisions_panel = Panel(decisions_table, title="Program Decisions", border_style="yellow")
results_panel = Panel(results_table, title="Result Presentation", border_style="blue")

# Print the panels
console.print(input_panel)
console.print(decisions_panel)
console.print(results_panel)
