#!/usr/bin/env python3
"""
Setup script for YouTube Music API OAuth authentication.
Run this script to authenticate with your YouTube Music account.
"""

from ytmusicapi import setup_oauth

def setup_authentication():
    """Set up OAuth authentication for YouTube Music API."""
    print("Setting up YouTube Music API authentication...")
    print("This will open a browser window for you to authenticate with Google.")
    print("Follow the instructions and authorize the application.")
    
    try:
        # Setup OAuth authentication with default credentials
        setup_oauth(filepath="oauth.json")
        print("\n✅ Authentication setup complete!")
        print("Your credentials have been saved to 'oauth.json'")
        print("You can now use the YouTube Music API with your account.")
        
    except Exception as e:
        print(f"❌ Error setting up authentication: {e}")
        print("\nLet's try the browser-based authentication method instead...")
        
        # Try browser authentication as fallback
        try:
            from ytmusicapi import setup
            setup(filepath="headers_auth.json")
            print("\n✅ Browser authentication setup complete!")
            print("Your credentials have been saved to 'headers_auth.json'")
            
        except Exception as e2:
            print(f"❌ Browser authentication also failed: {e2}")
            print("\nPlease follow manual setup instructions:")
            print("1. Go to https://music.youtube.com in your browser")
            print("2. Open Developer Tools (F12)")
            print("3. Go to Network tab")
            print("4. Refresh the page")
            print("5. Look for a request to 'browse' or similar")
            print("6. Copy the request headers")
            print("7. Create a headers_auth.json file with those headers")

if __name__ == "__main__":
    setup_authentication() 