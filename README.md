<a name="readme-top"></a>

# Space Telegram

<details>
<summary><h2>Table of Contents</h2></summary>

  - [Overview](#overview)
  - [Features](#features)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Project objectives](#project-objectives)
  - [License](#license)
</details>

## Overview

**Space Telegram** is a sophisticated bot designed for space enthusiasts and Telegram users. This utility facilitates the automated retrieval and sharing of awe-inspiring space images directly in a Telegram channel. Users can fetch images from NASA's Astronomy Picture of the Day (APOD), Earth Polychromatic Imaging Camera (EPIC), and SpaceX launches, offering a wide range of cosmic visuals. Space Telegram stands out for its ability to create a seamless bridge between the wonders of space and the convenience of Telegram communication.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Features

- **Automated NASA Image Fetching:** automatically downloads images from NASA's APOD and EPIC databases, bringing celestial wonders directly to your Telegram channel.
- **SpaceX Launch Images:** fetches and shares images from specific SpaceX launches, offering a window into modern space exploration.
- **Customizable Photo Publishing:** provides options to publish either specific or random photos from the image directory to your Telegram channel, with the ability to set a specific frequency or establish a continuous loop.
- **Easy Configuration:** utilizes environment variables like `NASA_API_KEY`, `TG_BOT_TOKEN`, `TG_CHANNEL_ID` for secure and personalized bot setup.
- **User-Friendly Interface:** designed for accessibility, ensuring ease of use for all users, regardless of their technical background.
- **Integration with Telegram API:** employs the Python Telegram Bot library for stable and efficient communication with the Telegram API.
- **Support for Various Image Counts and Formats:** allows users to specify the number of images to be downloaded and manages their display and sharing in the Telegram channel.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Installation

To install Space Telegram, follow these steps:

### 1. 🐍 Environment setup

First of all, make sure you have Python 3 installed, version `3.8.0` or higher. If not, visit the [official Python website](https://www.python.org/) and download the latest version.

The command to check your Python version should show a version no lower than `3.5.0`. You might need to use aliases such as `python`, `py`, `python3.8`, or onwards up to `python3.12` instead of `python3`.

```
$ python --version
Python 3.8.10
```

### 2. 📥 Repository cloning

Clone the repository using the command below:

```
git clone https://github.com/WarLikeLaux/space-telegram
```

Then, navigate to the project folder:

```
cd space-telegram
```

### 3. 🧩 Dependencies installation

Use pip (or pip3, if there's a conflict with Python2) to install the dependencies:

```
pip install -r requirements.txt
```

### 4. 🗝️ Environment variables setup

To set up your environment variables, you'll need to create a `.env` file in the root directory of the project. If you already have a `.env.example` file, you can simply copy with rename it to `.env` using the command `cp .env.example .env`. Once you've done this, add or/and fill the following lines by values in your `.env` file:

- `NASA_API_KEY`: this is your personal API key from NASA. You can obtain it from the [official NASA website](https://api.nasa.gov/). This key is necessary for accessing NASA's API and downloading images.
- `TG_BOT_TOKEN`: your Telegram bot token. If you're unsure about how to obtain it, consider reading the article ["How to Get Your Telegram Bot Token"](https://helpdesk.bitrix24.com/open/17622486/). This token is essential for controlling your Telegram bot and publishing photos in your channel.
- `TG_CHANNEL_ID`: the nickname or ID of your Telegram channel. This is required so that your bot knows where to send the images.
- `IMAGES_DIRECTORY`: the path to the directory where images are stored. Specify the location on your computer or server where the downloaded photos will be saved.
- `PUBLISH_FREQUENCY_IN_MINUTES`: the frequency, in minutes, at which photos are published to your Telegram channel. This parameter determines how often your bot will send photos to the channel.

Please ensure that each environment variable is assigned the correct value.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Usage

To operate Space Telegram, follow these steps:

**1. Downloading NASA APOD Images:**
```
python fetch_nasa_apod_images.py [count]
```

**2. Downloading NASA EPIC Images:**
```
python fetch_nasa_epic_images.py [count]
```

**3. Downloading SpaceX Images from a Specific Launch or the Latest:**
```
python fetch_spacex_images.py [launch_id]
```

**4. Publishing a Specific or Random Photo from the Images Directory to a Telegram Channel:**
```
python publish_photo_to_tg.py [photo_path]
```

**5. Continuously Publishing All Photos from the Images Directory to a Telegram Channel at a Specific Frequency:**
```
python publish_photo_in_loop_to_tg.py
```

Replace `[count]` with the number of images you want to download (default is set to 5), and `[launch_id]` with the ID of the launch to download images from (default is set to the latest launch). Also, in `[photo_path]` specify a photo path to publish or leave empty to publish a random photo.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Project objectives

This code was written for educational purposes as part of an online course for web developers at [dvmn.org](https://dvmn.org/).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## License

This code is open-source and free for any modifications, distributions, and uses. Feel free to utilize it in any manner you see fit.

<p align="right">(<a href="#readme-top">back to top</a>)</p>