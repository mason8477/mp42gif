# MP4toGIF Converter

A simple Python tool with a graphical interface to convert MP4 video files to GIF format using the MoviePy library.

## Features

- User-friendly graphical interface
- One-click conversion from MP4 to GIF
- Background processing that keeps the UI responsive
- Automatic output filename generation
- Simple status notifications

## Requirements

- Python 3.x
- tkinter (Python standard library)
- moviepy library

## Installation

1. Ensure Python 3.x is installed
2. Install the required package:
   ```
   pip install moviepy
   ```
3. Download the script

## Usage

1. Run the Python script:
   ```
   python mp4togif.py
   ```
2. Click the "Select MP4 and convert to GIF" button
3. Select the MP4 file you want to convert
4. Wait for the conversion to complete
5. A success message will display when finished, showing the path to the new GIF file

## Notes

- The output GIF is saved in the same location as the source MP4 file with the same name but .gif extension
- Converting large video files may take significant time and memory
- The application remains responsive during conversion as processing happens in a background thread
- No special settings for GIF quality or size are available in this simple version
- If you encounter memory issues, consider using external tools for very large files

## Known Limitations

- Converting long videos may result in large GIF files
- No progress bar is provided for the conversion process
- Default settings are used for the conversion
