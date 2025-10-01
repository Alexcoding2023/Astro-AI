#!/usr/bin/env python3
"""
Astro AI - Fixed Demo Application
A simplified demo that should work reliably on all systems.
"""

import tkinter as tk
from tkinter import scrolledtext
import threading
import time

class AstroAIDemo:
    def __init__(self, root):
        self.root = root
        self.root.title("Astro AI - Demo Chat Interface")
        self.root.geometry("1000x800")
        self.root.configure(bg='#1a1a1a')
        
        # Force window to front
        self.root.lift()
        self.root.attributes('-topmost', True)
        self.root.after(100, lambda: self.root.attributes('-topmost', False))
        
        self.create_simple_interface()
        self.show_welcome_message()
        
    def create_simple_interface(self):
        """Create a simple, reliable interface"""
        
        # Header
        header_frame = tk.Frame(self.root, bg='#1a1a1a', height=100)
        header_frame.pack(fill=tk.X, padx=20, pady=20)
        header_frame.pack_propagate(False)
        
        # Title with larger font
        title = tk.Label(
            header_frame,
            text="🚀 ASTRO AI",
            font=('Helvetica', 32, 'bold'),
            bg='#1a1a1a',
            fg='#00BFA5'
        )
        title.pack(pady=(10, 5))
        
        # Subtitle
        subtitle = tk.Label(
            header_frame,
            text="Private AI Chat - Local Models Demo",
            font=('Helvetica', 16),
            bg='#1a1a1a',
            fg='#ffffff'
        )
        subtitle.pack()
        
        # Chat area with explicit sizing
        chat_frame = tk.Frame(self.root, bg='#1a1a1a')
        chat_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=(0, 20))
        
        # Text area with scrollbar
        self.chat_text = scrolledtext.ScrolledText(
            chat_frame,
            wrap=tk.WORD,
            width=80,
            height=25,
            bg='#2d2d2d',
            fg='#ffffff',
            font=('Courier', 13),
            insertbackground='white',
            selectbackground='#6A1B9A'
        )
        self.chat_text.pack(fill=tk.BOTH, expand=True, pady=(0, 20))
        
        # Input area
        input_frame = tk.Frame(self.root, bg='#1a1a1a', height=80)
        input_frame.pack(fill=tk.X, padx=20, pady=(0, 20))
        input_frame.pack_propagate(False)
        
        # Entry with larger font
        self.entry = tk.Entry(
            input_frame,
            font=('Helvetica', 16),
            bg='#404040',
            fg='white',
            insertbackground='white',
            relief=tk.FLAT,
            bd=10
        )
        self.entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 20), pady=20)
        self.entry.bind('<Return>', self.send_message)
        
        # Send button
        self.send_btn = tk.Button(
            input_frame,
            text="SEND",
            font=('Helvetica', 14, 'bold'),
            bg='#6A1B9A',
            fg='white',
            relief=tk.FLAT,
            padx=30,
            pady=15,
            command=self.send_message,
            cursor='hand2'
        )
        self.send_btn.pack(side=tk.RIGHT, pady=20)
        
        # Status bar
        status_frame = tk.Frame(self.root, bg='#1a1a1a', height=40)
        status_frame.pack(fill=tk.X, padx=20, pady=(0, 10))
        status_frame.pack_propagate(False)
        
        self.status = tk.Label(
            status_frame,
            text="STATUS: Ready to chat | DEMO MODE ACTIVE",
            font=('Helvetica', 12),
            bg='#1a1a1a',
            fg='#00BFA5'
        )
        self.status.pack(pady=10)
        
        # Focus on entry
        self.entry.focus_set()
    
    def show_welcome_message(self):
        """Show initial welcome message"""
        welcome_text = """
════════════════════════════════════════════════════════════════
                        🚀 WELCOME TO ASTRO AI 🚀
════════════════════════════════════════════════════════════════

This is a DEMO of your rebranded Astro AI application!

✨ WHAT ASTRO AI OFFERS:
• Private AI conversations with local models
• Document search with LocalDocs (RAG)
• Complete offline operation
• No data sent to external servers
• OpenAI-compatible API server mode

🎯 DEMO FEATURES:
• Interactive chat interface
• Astro AI branding and design
• Simulated AI responses
• Modern dark theme with your brand colors

💬 TRY THESE COMMANDS:
• Say "hello" or "hi"
• Ask "what can you do?"
• Type "help" for more options
• Ask about "privacy" or "features"

Type a message below and press ENTER to start chatting!
════════════════════════════════════════════════════════════════
        """
        
        self.chat_text.insert(tk.END, welcome_text)
        self.chat_text.see(tk.END)
    
    def add_message(self, sender, message, color):
        """Add a message to the chat"""
        timestamp = time.strftime("%H:%M:%S")
        
        # Format message
        formatted_msg = f"\n[{timestamp}] {sender}:\n{message}\n"
        formatted_msg += "─" * 60 + "\n"
        
        # Insert with color (simplified for reliability)
        self.chat_text.insert(tk.END, formatted_msg)
        self.chat_text.see(tk.END)
    
    def send_message(self, event=None):
        """Handle user message"""
        message = self.entry.get().strip()
        if not message:
            return
        
        # Show user message
        self.add_message("YOU", message, "#00BFA5")
        self.entry.delete(0, tk.END)
        
        # Update status
        self.status.config(text="STATUS: Processing your message...")
        
        # Start AI response in thread
        threading.Thread(target=self.generate_response, args=(message,), daemon=True).start()
    
    def generate_response(self, user_message):
        """Generate AI response"""
        # Simulate thinking time
        time.sleep(1.5)
        
        # Response logic
        msg_lower = user_message.lower()
        
        if any(word in msg_lower for word in ['hello', 'hi', 'hey']):
            response = "Hello! I'm Astro AI, your private AI assistant. I'm excited to show you what I can do in this demo interface!"
            
        elif any(word in msg_lower for word in ['help', 'commands']):
            response = """Here are some things you can try:
            
🔹 Ask me about Astro AI features
🔹 Inquire about privacy and security
🔹 Ask "what can you do?"
🔹 Try "tell me about LocalDocs"
🔹 Ask about the full application
🔹 Just have a normal conversation!"""
            
        elif 'what can you do' in msg_lower or 'features' in msg_lower:
            response = """Astro AI offers powerful features:
            
🤖 LOCAL AI MODELS: Run LLMs completely offline
📚 LOCALDOCS: Search your documents with AI
🔒 PRIVACY FIRST: No data leaves your device
⚡ FAST RESPONSES: Optimized for your hardware
🔧 API SERVER: OpenAI-compatible endpoints
🎨 MODERN UI: Beautiful, user-friendly interface
🌍 CROSS-PLATFORM: Windows, Mac, Linux support"""
            
        elif any(word in msg_lower for word in ['privacy', 'private', 'security']):
            response = """Privacy is Astro AI's core strength:
            
🔐 100% LOCAL: Everything runs on your device
🚫 NO CLOUD: No data sent to external servers
🔒 YOUR DATA: Documents stay on your computer
🛡️ SECURE: No account required, no tracking
⚡ OFFLINE: Works without internet connection
            
Your conversations and documents never leave your machine!"""
            
        elif any(word in msg_lower for word in ['localdocs', 'documents', 'rag']):
            response = """LocalDocs is Astro AI's document intelligence feature:
            
📁 SMART SEARCH: Find relevant info in your files
🧠 AI UNDERSTANDING: Semantic search, not just keywords
📋 MULTIPLE FORMATS: PDF, TXT, MD, DOC files supported
⚡ REAL-TIME: Index updates as you add files
🎯 CONTEXTUAL: AI uses your docs to answer questions
🔒 PRIVATE: All processing happens locally
            
It's like having a personal research assistant!"""
            
        elif 'demo' in msg_lower or 'full' in msg_lower:
            response = """This is a demo of the Astro AI interface!
            
🎨 SHOWS: Rebranded UI, colors, and design
⚡ SIMULATES: How conversations would work
🔧 MISSING: Actual AI models (requires compilation)
📦 FULL VERSION: Needs Qt + C++ backend build
            
The real Astro AI would have actual LLMs running locally with all the features I mentioned!"""
            
        else:
            response = f"""I heard you say: "{user_message}"
            
In the full Astro AI application, I would:
• Process your message with a local LLM
• Provide intelligent, contextual responses
• Search your documents if relevant
• Maintain conversation history
• All while keeping everything private!
            
This demo shows the interface design for your rebranded Astro AI. Try asking about features or saying 'help'!"""
        
        # Update UI in main thread
        self.root.after(0, lambda: self.show_ai_response(response))
    
    def show_ai_response(self, response):
        """Show AI response"""
        self.add_message("ASTRO AI", response, "#6A1B9A")
        self.status.config(text="STATUS: Ready to chat | DEMO MODE ACTIVE")

def main():
    print("🚀 Starting Astro AI Demo Interface...")
    print("Creating window...")
    
    root = tk.Tk()
    app = AstroAIDemo(root)
    
    print("✅ Astro AI Demo is now running!")
    print("📱 Look for the window titled 'Astro AI - Demo Chat Interface'")
    print("💬 Try typing 'hello' to start a conversation")
    
    try:
        root.mainloop()
    except Exception as e:
        print(f"Error: {e}")
    
    print("👋 Astro AI Demo closed")

if __name__ == "__main__":
    main()
