from flask import Flask, request, render_template, send_from_directory, abort
import requests
from bs4 import BeautifulSoup
import zipfile
import os
from urllib.parse import urljoin

app = Flask(__name__)

# Directory where the zip files will be saved
ZIP_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'zips')
if not os.path.exists(ZIP_DIR):
    os.makedirs(ZIP_DIR)

# Predefined keywords to ignore
PREDEFINED_IGNORED_WORDS = ['logo', 'menu', 'bns', 'dns', 'arrow', 'sns', 
                            'instagram', 'insta', 'facebook', 'youtube', 
                            'fans', 'twitter', 'bg', 'btn', 'prev', 'next']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scrape', methods=['POST'])
def scrape():
    url = request.form['url']
    ignored_images = []
    valid_images = []

    user_keywords = request.form.get('keywords', '')
    user_ignored_words = [word.strip() for word in user_keywords.splitlines() if word.strip()]
    all_ignored_words = PREDEFINED_IGNORED_WORDS + user_ignored_words

    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        images = soup.find_all('img')

        for img in images:
            src = img.get('src')
            img_url = urljoin(url, src)

            if any(word in img_url for word in all_ignored_words):
                ignored_images.append(img_url)
            else:
                valid_images.append(img_url)

        zip_filename = os.path.join(ZIP_DIR, 'scraped_images.zip')
        with zipfile.ZipFile(zip_filename, 'w') as zipf:
            for img_url in valid_images:
                img_data = requests.get(img_url).content
                img_name = os.path.basename(img_url)
                zipf.writestr(img_name, img_data)

        # Check if there are no valid images
        if not valid_images:
            os.remove(zip_filename)  # Remove the empty zip file
            return "No images were scraped from the website."

        return render_template('results.html', ignored_images=ignored_images, zip_filename='scraped_images.zip')

    except Exception as e:
        return f"Oops! Something went wrong: {str(e)}"

@app.route('/create_ignored_zip', methods=['POST'])
def create_ignored_zip():
    selected_images = request.form.getlist('selected_images')
    zip_filename_ignored = os.path.join(ZIP_DIR, 'ignored_images.zip')
    
    if not selected_images:
        return "No images selected for zipping."

    with zipfile.ZipFile(zip_filename_ignored, 'w') as zipf:
        for img_url in selected_images:
            img_data = requests.get(img_url).content
            img_name = os.path.basename(img_url)
            zipf.writestr(img_name, img_data)

    return render_template('download.html', zip_filename_ignored='ignored_images.zip')

@app.route('/download/<filename>')
def download(filename):
    try:
        return send_from_directory(directory=ZIP_DIR, path=filename, as_attachment=True)
    except FileNotFoundError:
        abort(404, description="Resource not found")

if __name__ == '__main__':
    app.run(debug=True)
