from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from alert_engine import process_log_line
import time

LOG_FILE = "../logs/auth.log"

class LogHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith("auth.log"):
            with open(LOG_FILE, 'r') as f:
                lines = f.readlines()
                if lines:
                    last_line = lines[-1]
                    process_log_line(last_line)

if __name__ == "__main__":
    path = "../logs"
    event_handler = LogHandler()
    observer = Observer()
    observer.schedule(event_handler, path=path, recursive=False)
    observer.start()
    print("[👁️] Watching logs in real-time...")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
