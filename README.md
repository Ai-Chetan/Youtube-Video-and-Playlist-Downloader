# 🎬 YouTube Video/Playlist Downloader (pytubefix)

A simple, user-friendly command-line tool to download individual YouTube videos or entire playlists in the highest available resolution using [`pytubefix`](https://github.com/pytube/pytube).

---

## 📦 Features

- ✅ Download single videos in highest resolution.
- ✅ Download entire playlists with organized folder structure.
- ✅ Progress feedback during download.
- ✅ Simple CLI interface.
- ✅ Cross-platform support.

---

## 🚀 Getting Started

Follow the steps below to clone, install, and run this project.

### 1. 📥 Clone the Repository

```bash
git clone https://github.com/Ai-Chetan/youtube-downloader.git
```

### 2. 🐍 Create a Virtual Environment (Optional but Recommended)
For Windows
```bash
python -m venv venv
venv\Scripts\activate
```

For macOS/Linux
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. 📦 Install Requirements

- Make sure you have [Python](https://www.python.org/downloads/) 3.7+ installed.
- Then run following command in the terminal
```bash
pip install -r requirements.txt
```

### 4. ▶️ How to Use

Run the script from the terminal:
```bash
python youtube-downloader.py
```
You'll be prompted to:

- Enter the YouTube video or playlist URL.
- Specify an output directory (or press Enter for current directory).
- The program will automatically detect whether it's a single video or a playlist and proceed accordingly.

### 5. 📁 Example Usage
```bash
Download a Single Video
🔗 Enter the YouTube video or playlist URL: https://www.youtube.com/watch?v=abcd1234
📂 Enter output directory (leave blank for current folder): 
```
```bash
Download a Playlist
🔗 Enter the YouTube video or playlist URL: https://www.youtube.com/playlist?list=PLxyz...
📂 Enter output directory (leave blank for current folder): 
```
### 👨‍💻 Author

Developed by [Chetan Chaudhari](https://github.com/Ai-Chetan).