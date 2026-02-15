# 📝 Python Text Editor (Tkinter)

> **A lightweight, customizable desktop text editor built with Python and Tkinter. Designed for simplicity and cross-platform utility.**

This application provides a clean interface for handling `.txt` and `.html` files, offering a personalized writing experience through dynamic font and color customization.

---

## 📌 System Overview

The application is built on the **Model-View-Controller (MVC)** pattern logic within a single-threaded GUI loop:

```text
       [ User Interface (Tkinter) ]
                   |
        /----------+----------\
        |          |          |
 [ File I/O ]  [ Format ]  [ Events ]
     |             |          |
 (Open/Save)   (Fonts/Size) (Shortcuts)
     |             |          |
     \----------+----------/
                |
        [ OS File System ]
```

* **Frontend:** Tkinter standard GUI library.
* **Backend:** Python 3.x logic for file stream handling.
* **Configuration:** Dynamic system font retrieval and hex-color mapping.

---

## 🚀 Features

### 🛠 File Management
* **Broad Support:** Open and save both `.txt` and `.html` files.
* **Quick Clear:** Instant "Delete All" function via menu or shortcut.
* **Native Dialogs:** Uses standard OS file explorers for a familiar experience.

### 🎨 Customization (Format & Edit)
* **Typography:** Choose from a list of available system fonts.
* **Scaling:** Adjust font sizes ranging from **8** to **72** pt.
* **Themes:** Full customization of **Text Color** and **Background Color** via a color picker.

### ⌨️ Keyboard Shortcuts
| Shortcut | Action |
| :--- | :--- |
| `Ctrl + O` | Open an existing file |
| `Ctrl + S` | Save current work |
| `Ctrl + D` | Clear the entire editor |

---

## 🧰 Requirements

* **Python 3.x**
* **Tkinter:** Usually pre-installed with Python (if missing on Linux, install via `sudo apt-get install python3-tk`).

---

## 🛠 Installation & Usage

### 1️⃣ Download
Ensure you have Python installed, then clone or download the script:
```bash
git clone [https://github.com/AngelosFikias0/Python_Text_Editor.git](https://github.com/AngelosFikias0/Python_Text_Editor.git)
cd Python_Text_Editor
```

### 2️⃣ Run the Editor
```bash
python text_editor.py
```

### 3️⃣ Usage Tips
* Use the **File** menu to manage your documents.
* Access **Format** to change font family and size.
* Use the **Edit** menu to toggle colors for a "Dark Mode" or high-contrast experience.

---

## 📚 Technical Highlights

* **Event Binding:** Implemented `root.bind` to map physical keyboard keys to Python functions.
* **Resource Management:** Safe file stream handling using `askopenfilename` and `asksaveasfilename`.
* **System Integration:** Dynamically fetches `font.families()` to ensure compatibility across Windows, macOS, and Linux.

---

## 📄 License & About

* **License:** This project is open-source and free to use.
* **Author:** Created by **Angelos Fikias**.

---
*Developed as a practical study in Python GUI development and event-driven programming.*
