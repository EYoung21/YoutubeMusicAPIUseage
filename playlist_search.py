#!/usr/bin/env python3
"""
YouTube Music Playlist Search Tool

This script allows you to search within your YouTube Music playlists.
"""

import json
import sys
from typing import List, Dict, Any, Optional
from ytmusicapi import YTMusic

class PlaylistSearcher:
    def __init__(self, auth_file: str = None):
        """Initialize the playlist searcher with authentication."""
        # Try different authentication files
        auth_files = []
        if auth_file:
            auth_files.append(auth_file)
        else:
            auth_files = ["oauth.json", "headers_auth.json"]
        
        authenticated = False
        for file in auth_files:
            try:
                self.yt = YTMusic(file)
                print(f"✅ Successfully authenticated with YouTube Music using {file}")
                authenticated = True
                break
            except FileNotFoundError:
                continue
            except Exception as e:
                print(f"❌ Authentication failed with {file}: {e}")
                continue
        
        if not authenticated:
            print("❌ No valid authentication found.")
            print("Please run 'python setup_auth.py' first to set up authentication.")
            sys.exit(1)
    
    def get_all_playlists(self) -> List[Dict[str, Any]]:
        """Get all user playlists."""
        try:
            playlists = self.yt.get_library_playlists(limit=None)
            return playlists
        except Exception as e:
            print(f"Error fetching playlists: {e}")
            return []
    
    def get_playlist_contents(self, playlist_id: str) -> List[Dict[str, Any]]:
        """Get all songs in a specific playlist."""
        try:
            playlist = self.yt.get_playlist(playlist_id, limit=None)
            return playlist.get('tracks', [])
        except Exception as e:
            print(f"Error fetching playlist contents: {e}")
            return []
    
    def search_in_playlist(self, playlist_id: str, search_term: str) -> List[Dict[str, Any]]:
        """Search for songs containing the search term within a specific playlist."""
        tracks = self.get_playlist_contents(playlist_id)
        results = []
        
        search_term_lower = search_term.lower()
        
        for track in tracks:
            if not track:  # Skip None tracks
                continue
                
            # Search in title
            title = track.get('title', '').lower()
            
            # Search in artists
            artists = []
            if track.get('artists'):
                artists = [artist.get('name', '').lower() for artist in track['artists']]
            artist_text = ' '.join(artists)
            
            # Search in album
            album = ''
            if track.get('album') and track['album'].get('name'):
                album = track['album']['name'].lower()
            
            # Check if search term is in any of these fields
            if (search_term_lower in title or 
                search_term_lower in artist_text or 
                search_term_lower in album):
                results.append(track)
        
        return results
    
    def search_across_all_playlists(self, search_term: str) -> Dict[str, List[Dict[str, Any]]]:
        """Search for songs across all user playlists."""
        playlists = self.get_all_playlists()
        all_results = {}
        
        for playlist in playlists:
            playlist_id = playlist.get('playlistId')
            playlist_title = playlist.get('title', 'Unknown Playlist')
            
            if playlist_id:
                results = self.search_in_playlist(playlist_id, search_term)
                if results:
                    all_results[playlist_title] = results
        
        return all_results
    
    def display_search_results(self, results: List[Dict[str, Any]], playlist_name: str = None):
        """Display search results in a readable format."""
        if not results:
            if playlist_name:
                print(f"No results found in playlist '{playlist_name}'")
            else:
                print("No results found")
            return
        
        if playlist_name:
            print(f"\n🎵 Results in playlist '{playlist_name}' ({len(results)} song(s)):")
        else:
            print(f"\n🎵 Search Results ({len(results)} song(s)):")
        
        print("-" * 80)
        
        for i, track in enumerate(results, 1):
            title = track.get('title', 'Unknown Title')
            
            # Get artist names
            artists = []
            if track.get('artists'):
                artists = [artist.get('name', '') for artist in track['artists']]
            artist_text = ', '.join(artists) if artists else 'Unknown Artist'
            
            # Get album name
            album = 'Unknown Album'
            if track.get('album') and track['album'].get('name'):
                album = track['album']['name']
            
            # Get duration
            duration = track.get('duration', 'Unknown Duration')
            
            print(f"{i:2d}. {title}")
            print(f"    Artist(s): {artist_text}")
            print(f"    Album: {album}")
            print(f"    Duration: {duration}")
            if track.get('videoId'):
                print(f"    Video ID: {track['videoId']}")
            print()
    
    def list_playlists(self):
        """List all user playlists."""
        playlists = self.get_all_playlists()
        
        if not playlists:
            print("No playlists found.")
            return
        
        print(f"\n📋 Your Playlists ({len(playlists)} total):")
        print("-" * 60)
        
        for i, playlist in enumerate(playlists, 1):
            title = playlist.get('title', 'Unknown Playlist')
            track_count = playlist.get('count', 'Unknown')
            playlist_id = playlist.get('playlistId', 'Unknown ID')
            
            print(f"{i:2d}. {title}")
            print(f"    Songs: {track_count}")
            print(f"    ID: {playlist_id}")
            print()

def main():
    """Main function for interactive playlist searching."""
    searcher = PlaylistSearcher()
    
    while True:
        print("\n" + "="*60)
        print("🎵 YouTube Music Playlist Search Tool")
        print("="*60)
        print("1. List all playlists")
        print("2. Search within a specific playlist")
        print("3. Search across all playlists")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == '1':
            searcher.list_playlists()
            
        elif choice == '2':
            playlist_id = input("\nEnter playlist ID: ").strip()
            search_term = input("Enter search term: ").strip()
            
            if playlist_id and search_term:
                print(f"\nSearching for '{search_term}' in playlist...")
                results = searcher.search_in_playlist(playlist_id, search_term)
                searcher.display_search_results(results)
            else:
                print("Please provide both playlist ID and search term.")
                
        elif choice == '3':
            search_term = input("\nEnter search term: ").strip()
            
            if search_term:
                print(f"\nSearching for '{search_term}' across all playlists...")
                all_results = searcher.search_across_all_playlists(search_term)
                
                if not all_results:
                    print("No results found in any playlist.")
                else:
                    for playlist_name, results in all_results.items():
                        searcher.display_search_results(results, playlist_name)
            else:
                print("Please provide a search term.")
                
        elif choice == '4':
            print("Goodbye! 👋")
            break
            
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main() 