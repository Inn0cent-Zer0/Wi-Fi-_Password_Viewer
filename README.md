# 🔐 Wi-Fi Password Viewer – Windows Terminal Edition

A fast and handy Python tool to fetch **saved Wi-Fi profiles and passwords** from your Windows machine.  
No GUI. No fuss. Just raw SSIDs and their secrets, printed directly to your terminal.

✨ Written with deep curiosity, one suspicious hotel Wi-Fi, and two cups of rage-coffee by **Vaish** 💻⚡☕

---

## 📸 Terminal Preview

![image](https://github.com/user-attachments/assets/79ea866c-62ad-4f71-975b-851b40d0484b)

## 💡 Features

* 📡 Lists all saved Wi-Fi profiles (SSIDs)
* 🔓 Shows saved passwords (if available)
* 📟 Neatly aligned terminal output
* 🪄 No external libraries – just pure Python & Windows magic
* 🧼 Gracefully handles errors or missing passwords

---

## 🚀 Technologies Used

* 🐍 Python 3
* 🛠️ `subprocess` – to run Windows `netsh` commands
* 🧠 Basic string parsing and formatting
* 💻 Windows Command Line environment

---

## 🕹️ How to Use

> ⚠️ **Works only on Windows**
> 🛑 Run as **administrator** if some profiles return no password

1. Clone or download this repo
2. Open Command Prompt or Terminal
3. Run the script: python wifi_passwords.py


---

## 📂 Folder Structure

![image](https://github.com/user-attachments/assets/b37c6f6b-db08-4592-a51e-f8277b5183b1)

---

## 🧠 What I Learned

This fun little tool helped reinforce:

* Working with `subprocess` for CLI automation
* Parsing and structuring command-line output
* Formatting terminal tables for better readability
* Handling missing or inaccessible data
* Writing useful tools with less than 50 lines 💥

---

## 💬 Feedback & Contributions

Wanna make it cooler?

* Export to CSV?
* GUI using Tkinter?
* Detect connected network only?
* Update this code to be run on Mac OS

Let’s go. Fork ⭐ it, submit a pull request, or just vibe with it.
Let’s keep learning, breaking, and building together 🚀
