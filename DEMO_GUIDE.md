# 🎬 QUICK DEMO GUIDE

## Before Recording

### Terminal 1: Start Server
```bash
cd "C:\Users\User\Desktop\mario clone"
start_server.bat
```
Wait for: "Screenshot Server Running"

### Terminal 2 (Optional): Start Ngrok
```bash
ngrok http 3000
```
Copy the https URL

If using ngrok, edit source/main.py line 11 with your URL!

### Terminal 3: Build Executable
```bash
cd "C:\Users\User\Desktop\mario clone"
build_exe.bat
```
Wait for build to complete.

---

## Recording Script

### 🎥 SCENE 1: Code Walkthrough (2-3 min)

**Say**: "Let me show you where the trojan is inserted"

1. Open: `source/trojan.py`
   - "This is the malicious module that captures screenshots"
   - Point to `ImageGrab.grab()` - "This captures the screen"
   - Point to `requests.post()` - "This sends it to my server"
   - Point to `daemon=True` - "This keeps running after game closes"

2. Open: `source/main.py`
   - "Here's where I injected it into the game"
   - Point to line 7: "Import the trojan module"
   - Point to line 11: "Start it when the game launches"
   - "The user has no idea this is running"

### 🎥 SCENE 2: Build Process (2-3 min)

**Say**: "Now I'll build this into an executable"

1. Open terminal in project folder
2. Run: `build_exe.bat`
3. **SHOW THE BUILD PROCESS** - let it run
4. Navigate to `dist` folder
5. **SHOW** `SuperMario.exe` file
   - "This looks like a normal game executable"
   - "But it contains our screenshot trojan"

### 🎥 SCENE 3: Server Setup (1-2 min)

**Say**: "Let me start the server to receive screenshots"

1. Open new terminal
2. Run: `start_server.bat`
3. Show: "Server Running on localhost:3000"

**If using ngrok**:
4. Open another terminal
5. Run: `ngrok http 3000`
6. **COPY THE HTTPS URL**
7. Say: "This URL is publicly accessible - anyone can view the screenshots"

### 🎥 SCENE 4: The Demo (4-5 min)

**Say**: "Now watch what happens when someone runs this 'game'"

1. Open browser: `localhost:3000` (or ngrok URL)
   - Show the dashboard
   - "No screenshots yet"

2. Run: `dist\SuperMario.exe`
   - Game window appears
   - "Looks like a normal Mario game"

3. **SPLIT SCREEN**: Game + Browser
   - Wait 5-10 seconds
   - "Look - screenshots are appearing!"
   - Point to the browser updating
   - Wait for 3-4 screenshots

4. **CRITICAL MOMENT**:
   - **Say**: "Now watch - I'm going to close the game"
   - **Close the Mario game**
   - **Keep browser visible**
   - **Say**: "The game is closed, but look..."
   - **Wait 10-15 seconds**
   - **Point out new screenshots appearing**
   - **Say**: "The trojan is still running and capturing my screen!"

5. Show a few more screenshots appearing
   - "Even though the game is closed"
   - "The malware persists in the background"

### 🎥 SCENE 5: Public Access (if ngrok)

**Say**: "And remember, this is publicly accessible"

1. Show the ngrok URL again
2. "Anyone with this link can see these screenshots"
3. "This is how data exfiltration works"

---

## 🎯 Key Points to Emphasize

1. ✅ "The trojan is hidden in normal-looking game code"
2. ✅ "It starts automatically when the game launches"
3. ✅ "Screenshots are sent to an external server"
4. ✅ **"It continues running even after the game closes"** (MOST IMPORTANT!)
5. ✅ "The user has no indication this is happening"

---

## ⚠️ Common Issues

**If screenshots don't appear:**
- Check server is running (Terminal 1)
- Check game is running
- Refresh browser (F5)

**If game won't start:**
- Make sure all dependencies installed: `pip install pygame pillow requests`
- Check resources folder exists

**If build fails:**
- Make sure PyInstaller installed: `pip install pyinstaller`
- Check you're in the right directory

---

## 📝 Video Structure

| Time | Content |
|------|---------|
| 0:00-0:30 | Intro: Show project structure |
| 0:30-3:00 | Scene 1: Code walkthrough |
| 3:00-5:30 | Scene 2: Building executable |
| 5:30-6:30 | Scene 3: Server setup |
| 6:30-10:30 | Scene 4: Live demo |
| 10:30-11:00 | Scene 5: Public access (if ngrok) |
| 11:00-11:30 | Conclusion: Security lessons |

---

## 🚀 Ready to Record!

**Pre-flight Checklist:**
- [ ] Server running (Terminal 1)
- [ ] Ngrok running if using (Terminal 2)
- [ ] Executable built (`dist\SuperMario.exe` exists)
- [ ] Browser open to localhost:3000
- [ ] Screen recorder ready
- [ ] Good lighting and audio

**GO TIME!** 🎬
