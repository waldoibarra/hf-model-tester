import time


class Timer:
    def __init__(self) -> None:
        self.start_time: float | None = None
        self.elapsed: float | None = None

    def start(self) -> "Timer":
        self.start_time = time.perf_counter()
        return self

    def stop(self) -> float:
        if self.start_time is None:
            raise RuntimeError("Timer was not started")
        self.elapsed = time.perf_counter() - self.start_time
        return self.elapsed

    def elapsed_formatted(self) -> str:
        if self.elapsed is None:
            raise RuntimeError("Timer was not stopped")
        minutes = int(self.elapsed // 60)
        seconds = int(self.elapsed % 60)
        return f"{minutes}m {seconds}s"

    def print_elapsed(self, label: str = "Generated in") -> None:
        print(f"{label} {self.elapsed_formatted()}")
