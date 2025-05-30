SYSTEM_PROMPT_PREFIX = "[bright_black][[/][bold bright_magenta]system[/][bright_black]]:[/]\n"
HUMAN_PROMPT_PREFIX = "[bright_black][[/][bold bright_green]human[/][bright_black]]:[/]\n"
BOT_PROMPT_PREFIX = "[bright_black][[/][bold bright_blue]bot[/][bright_black]]:[/]\n"

from rich.console import Console

class Console(Console):

    def info(self, content: str):
        self.print(f"[bright_black]\[info]: {content}[/]")

    def error(self, content: str):
        self.print(f"[bright_red]\[error]: {content}[/]")

    def system_output(self, content: str):
        self.print(SYSTEM_PROMPT_PREFIX + content)

    def human_input(self) -> str:
        return self.input(HUMAN_PROMPT_PREFIX)

    def bot_output(self, content: str):
        self.print(BOT_PROMPT_PREFIX + content)

    def bot_start(self):
        self.print(BOT_PROMPT_PREFIX, end="")
    
    def bot_chunk(self, chunk: str):
        self.print(chunk, end="")

    def bot_end(self):
        self.print()