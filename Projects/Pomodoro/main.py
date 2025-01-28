from textual.app import App, ComposeResult
from textual.reactive import reactive
from textual.widgets import Button, Digits, TabbedContent, TabPane


class TimeDisplay(Digits):
    time = reactive(40 * 60)

    def on_mount(self, time):
        self.update_timer = self.set_interval(1, self.update_time, pause=True)
        self.update(f"{time}")

    def update_time(self):
        self.time -= 1

    def watch_time(self, time):
        minutes, seconds = divmod(time, 60)
        self.update(f"{minutes:02,.0f}:{seconds:02.0f}")

    def start(self):
        self.update_timer.resume()
        # update

    def stop(self):
        self.update_timer.pause()
        self.time = 40


class Stopwatch(TabPane):
    def __init__(self, title):
        super().__init__(title=title)

    def on_button_pressed(self, event: Button.Pressed) -> None:
        button_id = event.button.id
        time_display = self.query_one(TimeDisplay)
        if button_id == "start":
            time_display.start()
            self.add_class("started")
        elif button_id == "stop":
            time_display.stop()
            self.remove_class("started")

    def compose(self) -> ComposeResult:
        yield TimeDisplay()
        yield Button("Start", id="start", variant="success")
        yield Button("Stop", id="stop", variant="error")


class Pomodoro(App):
    CSS_PATH = "stopwatch03.tcss"
    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]

    def on_mount(self) -> None:
        self.theme = "gruvbox"

    def compose(self) -> ComposeResult:
        with TabbedContent():
            yield Stopwatch("Pane1")
            yield Stopwatch("Pane2")
            yield Stopwatch("Pane3")

    def action_toggle_dark(self) -> None:
        self.theme = (
            "textual-dark" if self.theme == "textual-light" else "textual-light"
        )


if __name__ == "__main__":
    app = Pomodoro()
    app.run()
