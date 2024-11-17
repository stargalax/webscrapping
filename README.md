# Flask Image Scraper

A simple Flask application that scrapes images from a specified URL, allows users to ignore certain images based on predefined keywords, and provides the option to download the images in a zip file.

## Features
 - Scrapes all images from a given webpage.
 - Allows users to specify additional keywords to ignore.
 - Provides a downloadable zip file containing the scraped images.
 - Option to create a separate zip file for ignored images.

## Requirements
 - Python 3.x
 - Flask
 - Requests
 - BeautifulSoup4

## Installation

1. Clone the repository:
   ```bash
    git clone https://github.com/yourusername/flask-image-scraper.git
    cd flask-image-scraper
    ```

 2. Install the required libraries:
    ```bash
    pip install Flask requests beautifulsoup4
    ```

## Folder Structure

flask-image-scraper/    (folder)
1. app.py - Main Flask application
2. templates/ - Folder for HTML templates

 - index.html - Homepage template

 - results.html - Results page template


 - download.html - Download page template


3. zips/ - Folder where zip files will be saved (generated automatically)

## Running the Application
 1. Run the application:
    ```bash
    python app.py
    ```

 2. Open your web browser and go to the local server address (typically `http://127.0.0.1:5000`).

 or click the link in the desc, it will take you to the website! ^_^
## Usage

 1. Enter the URL of the webpage you want to scrape in the input field.
 2. Optionally, enter keywords (one per line) for images you want to ignore during scraping.
 3. Click the "Scrape" button. The application will:
    - Display the images that were ignored.
    - Provide a link to download a zip file containing the valid images.
    - Allow you to select ignored images and create a zip file for them.

## Error Handling
 - If no images are found on the specified URL, the application will notify the user.
 - If the URL is invalid or an error occurs during scraping, an error message will be displayed.

## Note
 The website still needs a lot of work to be done! Just wanted to add this to track my progress! (┬┬﹏┬┬)
