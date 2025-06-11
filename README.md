# 🔐 SecureKey Logger — Advanced Keylogger with GUI + Auto Emailing 💻✉️

Welcome to **SecureKey Logger**, a powerful keylogging tool built as part of my internship at **Pinnacle Labs**.  
This project demonstrates advanced GUI integration, keystroke logging, and secure email delivery using **Mailtrap.io** for demo/testing purposes.

> ⚠️ **For ethical & educational use only. Do not use this tool on anyone's system without consent.**

---

## 📦 Features

- ✅ Logs all keystrokes silently in the background.
- ✅ Beautiful GUI with start/stop logging options.
- ✅ Auto-emails keystroke logs every 60 seconds.
- ✅ Logs are sent securely using SMTP (Mailtrap.io).
- ✅ Built with ❤️ using Python, Tkinter, and `pynput`.

---

## 🛠️ Technologies Used

- Python 🐍
- Tkinter (for GUI)
- `pynput` (for keystroke monitoring)
- `smtplib` & `email.mime` (for sending emails)
- Mailtrap SMTP (for secure demo delivery)

---

## 🚀 How to Run This Project

1. Clone the repository:

```bash
git clone https://github.com/yourusername/securekey-logger.git
cd securekey-logger

2. Install dependencies:
  pip install pynput

3. Add your Mailtrap credentials in the code:
      smtp_user = "your_mailtrap_username"
      smtp_pass = "your_mailtrap_password"

4. Run the logger:
      python keylogger_gui.py



## 📸 Screenshots

![GUI](https://raw.githubusercontent.com/sandesh362/Pinnacle-labs---Cybersecurity--Intern/main/assets/Screenshot%202025-06-11%20113912.png)

![Logs](https://raw.githubusercontent.com/sandesh362/Pinnacle-labs---Cybersecurity--Intern/main/assets/Screenshot%202025-06-11%20113926.png)





**## 📧 Email Automation**
This project uses a background thread that auto-sends logs every 60 seconds using smtplib. You can change the time interval in the auto_email_sender() function.

**👨‍💻 Internship Contribution**
This project was developed as part of my internship at Pinnacle Labs, focusing on real-world cybersecurity concepts.

⭐ Feel free to star this repository if you found it useful!

**📜 License**
MIT License — use responsibly!







    
