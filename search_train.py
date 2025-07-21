#!/usr/bin/env python3
"""
Quick search for "train" in Favorites playlist
"""

from playlist_search import PlaylistSearcher

def find_and_search_favorites():
    """Find the Favorites playlist and search for 'train'"""
    
    print("🔍 Searching for 'train' in your Favorites playlist...")
    print("-" * 60)
    
    # Initialize searcher
    searcher = PlaylistSearcher()
    
    # Get all playlists
    print("📋 Finding your Favorites playlist...")
    playlists = searcher.get_all_playlists()
    
    favorites_playlist = None
    for playlist in playlists:
        title = playlist.get('title', '').lower()
        if 'favorites' in title or 'favourite' in title:
            favorites_playlist = playlist
            break
    
    if not favorites_playlist:
        print("❌ Could not find a playlist named 'Favorites'")
        print("\n📋 Available playlists:")
        for i, playlist in enumerate(playlists[:10], 1):  # Show first 10
            title = playlist.get('title', 'Unknown Playlist')
            track_count = playlist.get('count', 'Unknown')
            print(f"{i:2d}. {title} ({track_count} songs)")
        
        if len(playlists) > 10:
            print(f"    ... and {len(playlists) - 10} more playlists")
        
        return
    
    # Found favorites playlist
    playlist_title = favorites_playlist.get('title', 'Favorites')
    playlist_id = favorites_playlist.get('playlistId')
    track_count = favorites_playlist.get('count', 'Unknown')
    
    print(f"✅ Found playlist: '{playlist_title}' ({track_count} songs)")
    print(f"   Playlist ID: {playlist_id}")
    print()
    
    # Search for "train"
    print("🔍 Searching for 'train'...")
    results = searcher.search_in_playlist(playlist_id, 'train')
    
    # Display results
    searcher.display_search_results(results, playlist_title)
    
    if results:
        print(f"\n🎵 Found {len(results)} song(s) with 'train' in your {playlist_title} playlist!")
    
if __name__ == "__main__":
    find_and_search_favorites() 