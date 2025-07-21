#!/usr/bin/env python3
"""
Quick setup guide for YouTube Music API authentication.
"""

def print_setup_instructions():
    print("=" * 60)
    print("🎵 YouTube Music Authentication Setup")
    print("=" * 60)
    print()
    print("To search your playlists, we need to get your browser headers.")
    print("Don't worry - this is safe and only gives us read access to your music.")
    print()
    print("📋 STEP-BY-STEP INSTRUCTIONS:")
    print()
    print("1. Open YouTube Music in your browser:")
    print("   https://music.youtube.com")
    print()
    print("2. Open Developer Tools:")
    print("   - Chrome/Edge: Press F12 or Ctrl+Shift+I")
    print("   - Firefox: Press F12 or Ctrl+Shift+I")
    print("   - Safari: Press Cmd+Option+I")
    print()
    print("3. Go to the 'Network' tab in Developer Tools")
    print()
    print("4. Refresh the YouTube Music page (Ctrl+R or Cmd+R)")
    print()
    print("5. In the Network tab, look for a request that starts with 'browse'")
    print("   (It might be called 'browse?alt=json' or similar)")
    print()
    print("6. Right-click on that request and select:")
    print("   - Chrome/Edge: 'Copy' → 'Copy request headers'")
    print("   - Firefox: 'Copy' → 'Copy Request Headers'")
    print("   - Safari: 'Copy' → 'Copy Request Headers'")
    print()
    print("7. Come back here and we'll set it up!")
    print()
    print("=" * 60)
    print()
    
    input("Press Enter when you have copied the headers...")
    
    print("\nNow let's set up the authentication:")
    print("When prompted, paste your headers and press Ctrl+D (or Cmd+D on Mac)")
    print()

if __name__ == "__main__":
    print_setup_instructions() 