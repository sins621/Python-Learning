from textual.app import App, ComposeResult
from textual.reactive import reactive
from textual.widgets import Button, Digits, TabbedContent, TabPane


class TimeDisplay(Digits):
    time = reactive(5)

    def on_mount(self, time):
        self.update_timer = self.set_interval(1, self.update_time, pause=True)
        self.update(f"{time}")

    def update_time(self):
        self.time -= 1

    def watch_time(self, time):
        minutes, seconds = divmod(time, 60)
        self.update(f"{minutes:02,.0f}:{seconds:02.0f}")
        print(time)
        print(self.time)

    def start(self):
        self.update_timer.resume()

    def stop(self):
        self.update_timer.pause()
        self.time = 40


class Stopwatch(TabPane):
    def __init__(self, title, id):
        super().__init__(title=title)
        self.id = id
        self.time = reactive(self.query_one(TimeDisplay).time)

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

    def action_show_tab(self, tab: str) -> None:
        """Switch to a new tab."""
        self.get_child_by_type(TabbedContent).active = tab


class Pomodoro(App):
    CSS_PATH = "stopwatch03.tcss"

    def __init__(self):
        self.time = reactive(self.query_one(Stopwatch).time)

    def on_mount(self) -> None:
        self.theme = "gruvbox"

    def compose(self) -> ComposeResult:
        with TabbedContent(initial="focus"):
            yield Stopwatch("Focus", id="focus")
            yield Stopwatch("Short Break", id="short_break")
            yield Stopwatch("Long Break", id="long_break")

    def watch_time(self, time):
        if time == 0:
            self.query_one(TabbedContent).active = "short_break"

    # Switch Tab Function Here:
        # if focus tab timer == 0:
            # self.query_one(TabbedContent).active = "short_break"

if __name__ == "__main__":
    app = Pomodoro()
    app.run()
