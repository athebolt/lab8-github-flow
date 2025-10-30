from adventure.utils import read_events_from_file
import random
from rich.console import Console

console = Console()

default_message = "You stand still, unsure what to do. The forest swallows you."

def step(choice: str, events):
    random_event = random.choice(events)

    if choice == "left":
        return left_path(random_event)
    elif choice == "right":
        return right_path(random_event)
    else:
        return "[dim]You stand still, unsure what to do. The forest[/] [bold red]swallows you[/][dim].[/]"

def left_path(event):
    return "[bold cyan]You walk[/] [bold green]left[/][bold cyan].[/] " + event

def right_path(event):
    return "[bold cyan]You walk[/] [bold yellow]right[/][bold cyan].[/] " + event

if __name__ == "__main__":
    events = read_events_from_file('events.txt')

    console.print("[dim]You wake up in a dark forest. You can go[/] [bold green]left[/] [dim]or[/] [bold yellow]right[/][dim].[/]")
    while True:
        choice = console.input("[bold white]Which direction do you choose?[/] [dim]([/][bold green]left[/][dim]/[/][bold yellow]right[/][dim]/[/][bold red]exit[/][dim]):[/] ")
        choice = choice.strip().lower()
        if choice == 'exit':
            console.print("[bold white]Goodbye.[/]")
            break
        
        console.print(step(choice, events))
