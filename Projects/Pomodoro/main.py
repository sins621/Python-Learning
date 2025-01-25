from time import monotonic

from textual.app import App, ComposeResult
from textual.containers import Container
from textual.reactive import reactive
from textual.widgets import Button, Digits


class TimeDisplay(Digits):
    """A Widget to display elapsed time."""

    start_time = reactive(monotonic)
    time = reactive(0.0)
    total = reactive(0.0)

    def on_mount(self) -> None:
        """Event handler called when widget is added to the app."""
        self.update_timer = self.set_interval(1 / 60, self.update_time, pause=True)

    def update_time(self) -> None:
        """Method to update the time to the current time."""
        self.time = self.total + (monotonic() - self.start_time)

    def watch_time(self, time: float) -> None:
        """Called when the time attribute changes."""
        minutes, seconds = divmod(time, 60)
        self.update(f"{minutes:02.0f}:{seconds:02.0f}")

    def start(self) -> None:
        """Method to start (or resume) time updating."""
        self.start_time = monotonic()
        self.update_timer.resume()

    def stop(self) -> None:
        """Method to stop the time display updating."""
        self.update_timer.pause()
        self.total += monotonic() - self.start_time
        self.time = self.total

    # def reset(self) -> None:
    #     """Method to reset the time display to zero."""
    #     self.total = 0
    #     self.time = 0


class Stopwatch(Container):
    """A stopwatch widget."""

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Event hander called when a button is pressed."""
        button_id = event.button.id
        time_display = self.query_one(TimeDisplay)
        if button_id == "start":
            time_display.start()
            self.add_class("started")
        elif button_id == "stop":
            time_display.stop()
            self.remove_class("started")
        # elif button_id == "reset":
        #     time_display.reset()

    def compose(self) -> ComposeResult:
        """Create child widgets of a stopwatch."""
        # yield Button("Reset", id="reset")
        yield TimeDisplay()
        yield Button("Start", id="start", variant="success")
        yield Button("Stop", id="stop", variant="error")


class Pomodoro(App):
    """A Textual app to manage stopwatches."""

    CSS_PATH = "stopwatch03.tcss"
    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]

    def on_mount(self) -> None:
        self.theme = "gruvbox"

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Stopwatch()

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.theme = (
            "textual-dark" if self.theme == "textual-light" else "textual-light"
        )


if __name__ == "__main__":
    app = Pomodoro()
    app.run()
