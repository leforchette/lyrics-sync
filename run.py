#!/usr/bin/env python3
"""
Command-line interface for lyrics-sync.

Usage:
    python run.py <audio_path> <lyrics_path> [--lang LANG]
    
Examples:
    python run.py song/ineverused.mp3 song/ineverused.txt --lang it-IT
    python run.py song/song.wav song/lyrics.txt --lang en-US
"""

import argparse
import sys
from lsync import LyricsSync


def main():
    parser = argparse.ArgumentParser(
        description="Synchronize lyrics with audio to produce time-aligned .lrc files"
    )
    parser.add_argument("audio_path", help="Path to the audio file (mp3, wav, etc.)")
    parser.add_argument("lyrics_path", help="Path to the lyrics text file")
    parser.add_argument(
        "--lang", 
        default="en-US",
        choices=["en-US", "en-US-base", "zh-CN", "it-IT"],
        help="Language code for the lyrics (default: en-US)"
    )
    parser.add_argument(
        "--blank-id",
        type=int,
        default=0,
        help="Blank token ID for CTC alignment (default: 0)"
    )
    
    args = parser.parse_args()
    
    print(f"Processing: {args.audio_path}")
    print(f"Lyrics: {args.lyrics_path}")
    print(f"Language: {args.lang}")
    print("-" * 50)
    
    try:
        lsync = LyricsSync(lang=args.lang, blank_id=args.blank_id)
        words, lrc = lsync.sync(args.audio_path, args.lyrics_path)
        print("\nSynchronized LRC output:")
        print("=" * 50)
        print(lrc)
        print("=" * 50)
        print("\nOutput saved to ./output/ directory")
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()

