# A user-friendly YouTube video downloader using pytubefix.
from pytubefix import YouTube, Playlist
from pytubefix.cli import on_progress
import os
import sys

def download_video(url, output_path=None):
    """Downloads a single YouTube video."""
    try:
        print("\n⏳ Fetching video information...")
        yt = YouTube(url, on_progress_callback=on_progress)
        
        print(f"\n🎬 Video Found: {yt.title}")
        
        # Select the highest resolution stream
        stream = yt.streams.get_highest_resolution()

        if not stream:
            print("\n❗ Error: Could not find a high-resolution stream.")
            return

        print(f"\n💾 Downloading '{yt.title}'...")
        stream.download(output_path=output_path)
        print(f"\n\n✅ Download of '{yt.title}' completed!\n")

    except Exception as e:
        print(f"\n❌ An error occurred: {e}")
        print("Please check the URL and your internet connection.")

def download_playlist(url, output_path=None):
    """Downloads all videos from a YouTube playlist."""
    try:
        print("\n⏳ Fetching playlist information...")
        p = Playlist(url)
        playlist_title = p.title

        print(f"\n🎶 Playlist Found: {playlist_title}")
        print(f"\nTotal videos to download: {len(p.video_urls)}")

        # Create a folder for the playlist
        if not output_path:
            # Sanitize the playlist title for use as a folder name
            valid_folder_name = "".join(c for c in playlist_title if c.isalnum() or c in " _-").rstrip()
            output_path = os.path.join(os.getcwd(), valid_folder_name)
            if not os.path.exists(output_path):
                os.makedirs(output_path)
                print(f"\n📁 Created directory for downloads: {output_path}")

        for i, video_url in enumerate(p.video_urls, 1):
            print(f"\n--- Downloading video {i}/{len(p.video_urls)} ---")
            download_video(video_url, output_path=output_path)

        print(f"\n✅ All videos in playlist '{playlist_title}' have been downloaded!\n")

    except Exception as e:
        print(f"\n❌ An error occurred: {e}")
        print("Please check the playlist URL and your internet connection.")

def main():
    """Main function to handle user interaction."""
    print("\n\n--------------------------------------------------")
    print("          YouTube Video/Playlist Downloader       ")
    print("--------------------------------------------------")
    
    url = input("\n🔗 Enter the YouTube video or playlist URL: ")
    
    # Simple check to see if it's a playlist
    is_playlist = "playlist?list=" in url or "/playlist?list=" in url
    
    output_path = input("\n📂 Enter output directory (leave blank for current folder): ")
    
    # Use current directory if path is empty
    if not output_path:
        output_path = os.getcwd()

    if is_playlist:
        download_playlist(url, output_path)
    else:
        download_video(url, output_path)

if __name__ == "__main__":
    main()