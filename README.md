# YouTube Music Playlist Search Tool

A Python tool to search within your YouTube Music playlists using the unofficial ytmusicapi.

## Features

- 🔍 Search within specific playlists
- 🎵 Search across all your playlists at once
- 📋 List all your playlists
- 🔐 OAuth authentication for secure access
- 💡 Interactive command-line interface

## Setup

### 1. Set Up Virtual Environment

First, create and activate a virtual environment:

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Set Up Authentication

Run the setup script to authenticate with your YouTube Music account:

```bash
python setup_auth.py
```

This will:
- Open a browser window for Google OAuth authentication
- Save your credentials to `oauth.json`
- Allow the tool to access your YouTube Music library

**⚠️ SECURITY WARNING:** Keep the authentication files (`oauth.json`, `headers_auth.json`) secure and NEVER share them or commit them to version control. These files contain your personal authentication tokens.

## Usage

### Interactive Mode

Run the main script for an interactive experience:

```bash
# Make sure virtual environment is activated
source venv/bin/activate

# Run the search tool
python playlist_search.py
```

The interactive menu allows you to:
1. **List all playlists** - View all your playlists with their IDs
2. **Search within a specific playlist** - Search for songs in a particular playlist
3. **Search across all playlists** - Find songs across your entire library
4. **Exit** - Close the application

### Programmatic Usage

You can also use the `PlaylistSearcher` class in your own scripts:

```python
from playlist_search import PlaylistSearcher

# Initialize the searcher
searcher = PlaylistSearcher()

# List all playlists
playlists = searcher.get_all_playlists()

# Search within a specific playlist
results = searcher.search_in_playlist('playlist_id_here', 'search_term')

# Search across all playlists
all_results = searcher.search_across_all_playlists('search_term')
```

## Search Capabilities

The tool searches for your term in:
- **Song titles**
- **Artist names**
- **Album names**

Search is case-insensitive and matches partial text.

## Example Searches

- `"love"` - Find all songs with "love" in the title, artist, or album
- `"Beatles"` - Find all Beatles songs across your playlists
- `"Christmas"` - Find holiday music in your collection

## Files

- `setup_auth.py` - Authentication setup script
- `playlist_search.py` - Main search tool
- `search_train.py` - Example search script
- `requirements.txt` - Python dependencies
- `.gitignore` - Protects sensitive files from being committed
- `headers_auth.json` - Your authentication credentials (created after setup, **NEVER commit this**)
- `oauth.json` - Alternative auth file (if using OAuth, **NEVER commit this**)

## 🔒 Security & Version Control

If you plan to use Git/GitHub:

1. The `.gitignore` file is already configured to protect your authentication files
2. **NEVER** commit `headers_auth.json` or `oauth.json` to version control
3. These files contain your personal YouTube Music access tokens
4. Anyone with these files could access your YouTube Music account

## Troubleshooting

### Authentication Issues

If you get authentication errors:
1. Delete the `oauth.json` file
2. Run `python setup_auth.py` again
3. Make sure you're using a Google account that has YouTube Music access

### Rate Limiting

The YouTube Music API has rate limits. If you get rate limit errors:
- Wait a few minutes before trying again
- Avoid making too many rapid requests

### Empty Results

If your library appears empty:
- Make sure you're authenticated with the correct Google account
- Verify that your account has YouTube Music content
- Check that your playlists aren't private/restricted

## Requirements

- Python 3.10 or higher
- Internet connection for API access
- Google account with YouTube Music access

## Note

This tool uses the unofficial ytmusicapi and is not affiliated with or endorsed by Google or YouTube Music. 