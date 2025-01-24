from textual.app import App, ComposeResult, RenderResult
from textual.binding import Binding
from textual.containers import Container
from textual.widget import Widget


class Hello(Widget):
    """Display a greeting."""

    def render(self) -> RenderResult:
        return "Hello, [b]World[/b]!"


class PomodoroApp(App):
    CSS_PATH = "styles.tcss"
    BINDINGS = [Binding("ctrl+c", "quit", "Quit", show=False, priority=True)]

    def on_mount(self) -> None:
        self.theme = "gruvbox"

    def compose(self) -> ComposeResult:
        timer = Container(Hello())
        timer.border_title = "Timer"
        yield timer

        tasks = Container(Hello())
        tasks.border_title = "Timer"
        yield tasks


if __name__ == "__main__":
    app = PomodoroApp()
    app.run()
