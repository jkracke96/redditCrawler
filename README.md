# Selenium Reddit Crawler

This is a Python script that utilizes Selenium to crawl through the "hot" page of the r/wallstreetbets subreddit on Reddit. It takes screenshots of the posts and their corresponding comments.

## Prerequisites

- Python 3.x
- Selenium package (`pip install selenium`)
- Chrome WebDriver executable (compatible with your Chrome browser version)

## Getting Started

1. Clone this repository or download the script file.

2. Install the required dependencies by running the following command:

3. Download the appropriate Chrome WebDriver executable from the [official website](https://sites.google.com/a/chromium.org/chromedriver/downloads). Make sure to choose the version that matches your Chrome browser version.

4. Place the WebDriver executable in the same directory as the script.

5. Run the script using the following command:



## Features

- Accepts cookies on the Reddit website.
- Takes screenshots of the posts and their corresponding comments.
- Deletes existing screenshots before each run.
- Creates audio files from post/comment text
- Creates videos for each post from screenshots with respective audio

## Explanation

1. The script starts by importing the necessary modules and defining helper functions.

2. It then sets up the Chrome WebDriver options and initializes two WebDriver instances: one for capturing post screenshots (`driver`) and another for capturing comment screenshots (`comments_driver`).

3. Existing screenshots in the `screenshots/posts` and `screenshots/comments` directories are deleted before each run.

4. The `driver` instance navigates to the "hot" page of the r/wallstreetbets subreddit.

5. The script accepts cookies on the Reddit website to avoid any cookie consent banners.

6. The script iterates over the `<div>` elements on the page and identifies the ones with `data_testid="post-container"`.

7. For each post container element, a screenshot is taken and saved in the `screenshots/posts` directory. The script also retrieves the link to the comments section for that post.

8. The `go_to_comments` function is used to find the comments link within a post container element.

9. The script switches to the `comments_driver` instance and navigates to the comments link for each post. It then captures up to five comment screenshots per post and saves them in the `screenshots/comments/post_{counter}` directory.

10. After capturing the post and comment screenshots, the script switches back to the `driver` instance and continues the loop.

11. Once all the posts have been processed, the script finishes execution.

Please note that this script uses Selenium for web scraping, and it should be used responsibly and in accordance with Reddit's terms of service.
