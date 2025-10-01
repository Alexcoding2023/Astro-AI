#!/usr/bin/env python3
"""
🚀 Astro AI - Launch Application
A desktop AI chat application powered by your rebranded technology
"""

import tkinter as tk
from tkinter import messagebox
import subprocess
import sys
import os

def main():
    """Launch Astro AI with a professional splash screen"""
    
    # Create splash window
    splash = tk.Tk()
    splash.title("Astro AI")
    splash.geometry("600x400")
    splash.configure(bg='#1a1a1a')
    splash.resizable(False, False)
    
    # Center the window
    splash.eval('tk::PlaceWindow . center')
    
    # Create content
    title_frame = tk.Frame(splash, bg='#1a1a1a')
    title_frame.pack(expand=True, fill=tk.BOTH)
    
    # Logo/Title
    title_label = tk.Label(
        title_frame,
        text="🚀",
        font=('Arial', 72),
        bg='#1a1a1a',
        fg='#00BFA5'
    )
    title_label.pack(pady=(50, 10))
    
    company_label = tk.Label(
        title_frame,
        text="Astro AI",
        font=('Arial', 36, 'bold'),
        bg='#1a1a1a',
        fg='#00BFA5'
    )
    company_label.pack(pady=(0, 10))
    
    subtitle_label = tk.Label(
        title_frame,
        text="Private AI Chat Application",
        font=('Arial', 16),
        bg='#1a1a1a',
        fg='#ffffff'
    )
    subtitle_label.pack(pady=(0, 30))
    
    # Status
    status_label = tk.Label(
        title_frame,
        text="Initializing...",
        font=('Arial', 12),
        bg='#1a1a1a',
        fg='#6A1B9A'
    )
    status_label.pack(pady=(0, 20))
    
    # Buttons frame
    button_frame = tk.Frame(title_frame, bg='#1a1a1a')
    button_frame.pack(pady=20)
    
    def launch_demo():
        """Launch the main demo application"""
        splash.destroy()
        try:
            # Get the directory of this script
            script_dir = os.path.dirname(os.path.abspath(__file__))
            demo_path = os.path.join(script_dir, 'astro_ai_demo.py')
            
            if os.path.exists(demo_path):
                subprocess.run([sys.executable, demo_path])
            else:
                messagebox.showerror("Error", "Demo application not found!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to launch demo: {str(e)}")
    
    def show_info():
        """Show information about Astro AI"""
        info_text = """Astro AI - Private AI Chat Application

This is a rebranded version of the GPT4All application, 
customized for your company.

Features:
• Private, local AI conversations
• No data sent to external servers
• Support for multiple LLM models
• Document search with LocalDocs
• OpenAI-compatible API server
• Cross-platform desktop application

Note: This demo showcases the rebranded interface.
The full application requires model downloads and 
additional setup for complete functionality.

Your company: Astro AI
Technology: Based on GPT4All open-source project"""
        
        messagebox.showinfo("About Astro AI", info_text)
    
    # Launch button
    launch_btn = tk.Button(
        button_frame,
        text="Launch Astro AI Demo",
        command=launch_demo,
        bg='#6A1B9A',
        fg='white',
        font=('Arial', 14, 'bold'),
        padx=30,
        pady=10,
        relief=tk.FLAT,
        cursor='hand2'
    )
    launch_btn.pack(side=tk.LEFT, padx=10)
    
    # Info button
    info_btn = tk.Button(
        button_frame,
        text="About",
        command=show_info,
        bg='#00BFA5',
        fg='white',
        font=('Arial', 14, 'bold'),
        padx=30,
        pady=10,
        relief=tk.FLAT,
        cursor='hand2'
    )
    info_btn.pack(side=tk.LEFT, padx=10)
    
    # Exit button
    exit_btn = tk.Button(
        button_frame,
        text="Exit",
        command=splash.destroy,
        bg='#404040',
        fg='white',
        font=('Arial', 14, 'bold'),
        padx=30,
        pady=10,
        relief=tk.FLAT,
        cursor='hand2'
    )
    exit_btn.pack(side=tk.LEFT, padx=10)
    
    # Update status
    status_label.config(text="Ready to launch")
    
    # Run the splash screen
    splash.mainloop()

if __name__ == "__main__":
    main()
