import time


class Timer:
    def __init__(self):
        self.start_time = None
        self.elapsed = None

    def start(self):
        self.start_time = time.perf_counter()
        return self

    def stop(self):
        if self.start_time is None:
            raise RuntimeError("Timer was not started")
        self.elapsed = time.perf_counter() - self.start_time
        return self.elapsed

    def elapsed_formatted(self):
        if self.elapsed is None:
            raise RuntimeError("Timer was not stopped")
        minutes = int(self.elapsed // 60)
        seconds = int(self.elapsed % 60)
        return f"{minutes}m {seconds}s"

    def print_elapsed(self, label: str = "Generated in"):
        print(f"{label} {self.elapsed_formatted()}")
