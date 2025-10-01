#!/usr/bin/env python3
"""
Astro AI - Demo Application
A simple Python-based chat interface for testing the rebranded Astro AI.
"""

import os
import sys
import tkinter as tk
from tkinter import scrolledtext, messagebox
import threading
import time

class AstroAIDemo:
    def __init__(self, root):
        self.root = root
        self.root.title("Astro AI - Demo Chat Interface")
        self.root.geometry("900x700")
        self.root.configure(bg='#1a1a1a')
        
        # Create main container
        self.create_widgets()
        
        # Add welcome message
        self.add_message("Astro AI", "🚀 Welcome to Astro AI! This is a demo interface showcasing the rebranded application.\n\nIn the full version, you would be able to:\n• Chat with local LLM models\n• Use LocalDocs for document retrieval\n• Run completely offline and private\n• Access advanced AI features\n\nType a message to see how the interface works!")
        
        # Focus on input
        self.message_entry.focus()
    
    def create_widgets(self):
        """Create and layout all widgets"""
        # Title frame
        title_frame = tk.Frame(self.root, bg='#1a1a1a')
        title_frame.pack(fill=tk.X, padx=20, pady=(20, 10))
        
        # Title
        title_label = tk.Label(
            title_frame, 
            text="🚀 Astro AI", 
            font=('Arial', 28, 'bold'), 
            bg='#1a1a1a', 
            fg='#00BFA5'
        )
        title_label.pack()
        
        # Subtitle
        subtitle_label = tk.Label(
            title_frame, 
            text="Private AI Chat - Powered by Local Models", 
            font=('Arial', 14), 
            bg='#1a1a1a', 
            fg='#ffffff'
        )
        subtitle_label.pack(pady=(5, 0))
        
        # Chat frame
        chat_frame = tk.Frame(self.root, bg='#1a1a1a')
        chat_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        # Chat display area
        self.chat_display = scrolledtext.ScrolledText(
            chat_frame, 
            wrap=tk.WORD, 
            state=tk.DISABLED,
            bg='#2d2d2d',
            fg='white',
            font=('Arial', 12),
            height=25,
            selectbackground='#6A1B9A',
            selectforeground='white'
        )
        self.chat_display.pack(fill=tk.BOTH, expand=True)
        
        # Input frame
        input_frame = tk.Frame(self.root, bg='#1a1a1a')
        input_frame.pack(fill=tk.X, padx=20, pady=(0, 10))
        
        # Message input
        self.message_entry = tk.Entry(
            input_frame, 
            font=('Arial', 14),
            bg='#404040',
            fg='white',
            insertbackground='white',
            relief=tk.FLAT,
            bd=5
        )
        self.message_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10), ipady=8)
        self.message_entry.bind('<Return>', self.send_message)
        
        # Send button
        self.send_button = tk.Button(
            input_frame, 
            text="Send", 
            command=self.send_message,
            bg='#6A1B9A',
            fg='white',
            font=('Arial', 12, 'bold'),
            relief=tk.FLAT,
            padx=20,
            pady=8,
            cursor='hand2'
        )
        self.send_button.pack(side=tk.RIGHT)
        
        # Status frame
        status_frame = tk.Frame(self.root, bg='#1a1a1a')
        status_frame.pack(fill=tk.X, padx=20, pady=(0, 20))
        
        self.status_label = tk.Label(
            status_frame, 
            text="Status: Ready | Note: This is a demo interface. Full Astro AI requires model installation.",
            bg='#1a1a1a',
            fg='#00BFA5',
            font=('Arial', 10)
        )
        self.status_label.pack(side=tk.LEFT)
    
    def add_message(self, sender, message):
        """Add a message to the chat display"""
        self.chat_display.config(state=tk.NORMAL)
        
        # Add timestamp
        timestamp = time.strftime("%H:%M:%S")
        
        # Add sender and message with proper formatting
        if sender == "You":
            self.chat_display.insert(tk.END, f"[{timestamp}] You: ", "user")
            self.chat_display.insert(tk.END, f"{message}\n\n", "user_msg")
        else:
            self.chat_display.insert(tk.END, f"[{timestamp}] {sender}: ", "ai")
            self.chat_display.insert(tk.END, f"{message}\n\n", "ai_msg")
        
        # Configure text tags for styling
        self.chat_display.tag_config("user", foreground="#00BFA5", font=('Arial', 12, 'bold'))
        self.chat_display.tag_config("user_msg", foreground="#e0e0e0", font=('Arial', 12))
        self.chat_display.tag_config("ai", foreground="#6A1B9A", font=('Arial', 12, 'bold'))
        self.chat_display.tag_config("ai_msg", foreground="#ffffff", font=('Arial', 12))
        
        self.chat_display.config(state=tk.DISABLED)
        self.chat_display.see(tk.END)
    
    def send_message(self, event=None):
        """Handle sending a message"""
        message = self.message_entry.get().strip()
        if not message:
            return
        
        # Add user message
        self.add_message("You", message)
        self.message_entry.delete(0, tk.END)
        
        # Update status
        self.status_label.config(text="Status: Processing... (Demo Mode)")
        
        # Simulate AI response in a separate thread
        threading.Thread(target=self.simulate_ai_response, args=(message,), daemon=True).start()
    
    def simulate_ai_response(self, user_message):
        """Simulate an AI response"""
        # Simulate processing time
        time.sleep(2)
        
        # Generate demo response based on user input
        responses = {
            "hello": "Hello! I'm Astro AI, your private AI assistant. How can I help you today?",
            "hi": "Hi there! Welcome to Astro AI. I'm here to demonstrate the rebranded interface.",
            "how are you": "I'm doing great! I'm a demonstration of the Astro AI interface. In the full version, I'd be powered by local LLM models.",
            "what can you do": "In the full Astro AI application, I can:\n• Answer questions using local AI models\n• Help with writing and analysis\n• Search through your documents with LocalDocs\n• Provide coding assistance\n• All while keeping your data completely private!",
            "astro": "Astro AI is designed to provide powerful AI capabilities while maintaining your privacy. Everything runs locally on your device!",
            "demo": "This is indeed a demo! The full Astro AI application would require installing Qt and compiling the C++ backend for optimal performance.",
            "help": "I can help demonstrate the Astro AI interface! Try asking me about:\n• What Astro AI can do\n• How it maintains privacy\n• Features of the full application\n• Or just have a conversation!"
        }
        
        # Find appropriate response
        response = None
        for key, value in responses.items():
            if key in user_message.lower():
                response = value
                break
        
        if not response:
            response = f"I understand you said: '{user_message}'\n\nThis is a demo interface showing the Astro AI branding and design. In the full application, I would process your message using local LLM models and provide intelligent responses while keeping everything private on your device.\n\nTry asking me about Astro AI features or just say 'hello'!"
        
        # Update UI in main thread
        self.root.after(0, lambda: self.add_ai_response(response))
    
    def add_ai_response(self, response):
        """Add AI response and update status"""
        self.add_message("Astro AI", response)
        self.status_label.config(text="Status: Ready | Demo Mode Active")

def main():
    """Main entry point"""
    print("🚀 Starting Astro AI Demo...")
    print("This is a demonstration of the rebranded Astro AI interface.")
    print("The full application requires Qt compilation for complete functionality.\n")
    
    # Create the main window
    root = tk.Tk()
    
    # Make sure the window appears on top
    root.lift()
    root.attributes('-topmost', True)
    root.after_idle(root.attributes, '-topmost', False)
    
    # Create the app
    app = AstroAIDemo(root)
    
    print("GUI window should now be visible!")
    print("If you don't see the window, check your dock or try Alt+Tab")
    
    try:
        root.mainloop()
    except KeyboardInterrupt:
        print("\nShutting down Astro AI Demo...")
    
    print("Astro AI Demo closed successfully!")

if __name__ == "__main__":
    main()
