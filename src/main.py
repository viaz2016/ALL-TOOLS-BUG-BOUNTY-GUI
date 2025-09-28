import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
import threading
import requests
import time

class BugBountyApp:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("Bug Bounty Tools - viaz2016")
        self.root.geometry("800x600")
        
        ctk.set_appearance_mode("Dark")
        self.setup_ui()
    
    def setup_ui(self):
        # Title
        title = ctk.CTkLabel(self.root, text="🐛 ALL-TOOLS-BUG-BOUNTY-GUI", font=("Arial", 20, "bold"))
        title.pack(pady=20)
        
        # Target input
        self.url_entry = ctk.CTkEntry(self.root, placeholder_text="https://example.com", width=400, height=35)
        self.url_entry.pack(pady=10)
        
        # Buttons
        btn_frame = ctk.CTkFrame(self.root)
        btn_frame.pack(pady=10)
        
        scan_btn = ctk.CTkButton(btn_frame, text="🔍 Quick Scan", command=self.start_scan, width=120, height=35)
        scan_btn.pack(side="left", padx=5)
        
        recon_btn = ctk.CTkButton(btn_frame, text="🌐 Reconnaissance", command=self.start_recon, width=120, height=35)
        recon_btn.pack(side="left", padx=5)
        
        # Results area
        self.results_text = ctk.CTkTextbox(self.root, height=300, font=("Consolas", 12))
        self.results_text.pack(fill="both", expand=True, padx=20, pady=10)
    
    def log(self, message):
        self.results_text.insert("end", message + "\n")
        self.results_text.see("end")
    
    def start_scan(self):
        url = self.url_entry.get().strip()
        if not url:
            messagebox.showerror("Error", "Please enter a URL")
            return
        
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
            
        self.log(f"🚀 Starting scan: {url}")
        self.log("=" * 50)
        thread = threading.Thread(target=self.scan_website, args=(url,))
        thread.daemon = True
        thread.start()
    
    def scan_website(self, url):
        try:
            # Check if website is alive
            self.log("📡 Checking website availability...")
            response = requests.get(url, timeout=10, verify=False)
            self.log(f"✅ Status: {response.status_code}")
            
            # Check security headers
            self.log("\n🔒 Security Headers Check:")
            headers = response.headers
            security_headers = {
                'X-Frame-Options': 'Clickjacking protection',
                'X-Content-Type-Options': 'MIME sniffing protection', 
                'Strict-Transport-Security': 'HTTPS enforcement',
                'Content-Security-Policy': 'XSS protection',
                'X-XSS-Protection': 'Browser XSS protection'
            }
            
            for header, description in security_headers.items():
                if header in headers:
                    self.log(f"   ✅ {header}: {headers[header]}")
                else:
                    self.log(f"   ❌ {header}: Missing - {description}")
            
            self.log("\n🎉 Scan completed!")
            
        except Exception as e:
            self.log(f"💥 Error: {str(e)}")
    
    def start_recon(self):
        url = self.url_entry.get().strip()
        if not url:
            messagebox.showerror("Error", "Please enter a URL")
            return
            
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
            
        self.log(f"🌐 Starting reconnaissance: {url}")
        self.log("=" * 50)
        thread = threading.Thread(target=self.do_recon, args=(url,))
        thread.daemon = True
        thread.start()
    
    def do_recon(self, url):
        try:
            self.log("📁 Checking common files...")
            common_files = ['robots.txt', 'sitemap.xml', '.env', 'backup.zip', 'admin', 'wp-admin']
            
            for file in common_files:
                try:
                    test_url = f"{url.rstrip('/')}/{file}"
                    response = requests.get(test_url, timeout=5, verify=False)
                    if response.status_code == 200:
                        self.log(f"   📄 Found: {test_url}")
                    elif response.status_code == 403:
                        self.log(f"   🔒 Access denied: {test_url}")
                except:
                    pass
            
            self.log("\n🎉 Reconnaissance completed!")
            
        except Exception as e:
            self.log(f"💥 Error: {str(e)}")
    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = BugBountyApp()
    app.run()
