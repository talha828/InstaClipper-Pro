
![CheatBoard (1)](https://github.com/talha828/InstaClipper-Pro/assets/61588132/8b73dff1-69ed-4d4c-ae70-bd9a6c658497)

# Python Script for Batch Video Processing and Instagram Uploads

This repository contains two Python scripts that automate video processing and uploading to Instagram:

## Description

* **`video_processor.py`:** Converts videos in the `video` folder into Instagram-friendly short clips (58 seconds each) with the following enhancements:
    - Resizes videos to a portrait aspect ratio (1080x1920) suitable for Instagram Reels.
    - Adds a title overlay at the top of each clip for easy identification.
    - Saves processed clips in the `output` folder.

* **`instagram_uploader.py`:** Uploads the processed video clips from the `output` folder to your Instagram account using Selenium automation. This script requires you to provide your Instagram credentials.

## Features

* **Effortless Batch Processing:** Process and prepare multiple videos for Instagram at once, saving you time and effort.
* **Customizable Settings:** Adjust clip duration, target dimensions, and captions to match your specific preferences.
* **Automatic Uploads (Optional):** Schedule automated uploads of the processed videos to your Instagram account using the `instagram_uploader.py` script. (**Note:** Due to Instagram's automation restrictions, consider using this script with caution and at your own risk.)




## Benefits

* **Streamlined Workflow:** Simplifies the process of creating and sharing engaging video content on Instagram.
* **Consistent Formatting:** Ensures a uniform presentation for all your Instagram Reels.
* **Increased Efficiency:** Saves you valuable time by automating repetitive tasks.



## Installation

1. **Clone the repository:**

   ```bash
   git clone [https://github.com/your-username/python-video-processing-instagram-uploader.git](https://github.com/your-username/python-video-processing-instagram-uploader.git)
   ```
## Install dependencies:

  ```bash
    pip install moviepy webdriver-manager pynput selenium
  ```

## Usage

**Place your videos:** Copy your video files into the `video` folder.

**Customize (optional):** Modify the following variables in `video_processor.py` to suit your needs:

* `clip_duration`: Adjust the length of each short clip (in seconds).
* `target_width`: Set the desired width for the resized videos.
* `target_height`: Set the desired height for the resized videos.
* `start_part`: Choose a starting number for the clip titles.

 ![CheatBoard (2)](https://github.com/talha828/InstaClipper-Pro/assets/61588132/50d01519-9b5c-437a-8821-6eaf4f9e23aa) 

**Run video processing:** Execute `python video_processor.py` in your terminal.

**Instagram upload (optional):**

* Update `username` and `password` in `instagram_uploader.py` with your Instagram credentials.
* Ensure you have a Chrome browser installed.
* Run `python instagram_uploader.py` in your terminal. (**Disclaimer:** Use this script responsibly, as unauthorized automation may violate Instagram's terms of service.)

![CheatBoard (3)](https://github.com/talha828/InstaClipper-Pro/assets/61588132/cfdfbb58-bfe5-4629-918d-63c40171e419)

## Note

These scripts are provided as-is and may require adjustments to work flawlessly in your environment. Feel free to modify them according to your specific requirements.
