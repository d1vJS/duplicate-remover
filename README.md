# 🧹 Duplicate Remover

A simple Tkinter-based desktop tool that removes duplicate lines from a selected `.txt` file and saves the cleaned result back to the same file.

## ✨ Features

- 🖱️ Easy file selection via a graphical dialog
- 🔁 Automatically detects and removes duplicate lines
- 💾 Saves the result directly back to the same file
- ⚡ No extra dependencies — uses only Python's standard library

## 🚀 Installation

Just need Python 3.x installed. No extra packages required — `tkinter` ships with most Python distributions.

```bash
git clone https://github.com/your-username/duplicate-remover.git
cd duplicate-remover
```

## ▶️ Usage

```bash
python remove_duplicates.py
```

Running the script opens a file selection dialog. Once you select a `.txt` file:

1. The file is read
2. Duplicate lines are removed
3. The cleaned content is saved back to the same file
4. A confirmation message is printed to the terminal

## ⚠️ Notes

- The script does **not preserve the original line order**, since it uses Python's `set()` (which is unordered).
- The operation **overwrites the original file** — it's recommended to back up your file before running it.
- Comparison is case-sensitive (`"Apple"` and `"apple"` are treated as different lines).

## 🛠️ Possible Improvements

- [ ] Preserve original line order
- [ ] Add automatic backup before overwriting
- [ ] Case-insensitive comparison option
- [ ] Support other file formats (.csv, .log, etc.)

## 📜 License

MIT License
