# Web Crawler API

This project is a web crawler API that allows users to crawl a website up to a specified depth and returns the crawled links in a JSON format. The API is built using Flask and BeautifulSoup.

## Prerequisites

* Python 3.8+
* Docker (optional, for containerized deployment)

## Installation

### Clone the Repository

bashCopy

```bash
git clone https://github.com/codeBunny2022/web_crawler.git
cd web_crawler
```

### Install Dependencies

bashCopy

```javascript
pip install -r requirements.txt
```

## Running the Application

### Locally



1. Navigate to the project directory:

   bashCopy

   ```javascript
   cd web_crawler
   
   ```
2. Run the Flask app:

   bashCopy

   ```javascript
   python run.py
   
   ```
3. The server will start on `http://localhost:5000`.

### With Docker



1. Build the Docker image:

   bashCopy

   ```javascript
   docker build -t web_crawler .
   
   ```
2. Run the Docker container:

   bashCopy

   ```javascript
   docker run -d -p 5000:5000 web_crawler
   
   ```
3. The server will start on `http://localhost:5000`.

## API Usage

### Endpoint

`POST /crawl`

### Request Body

jsonCopy

```javascript
{
    "root_url": "https://abcdefg.com",
    "depth": 2
}
```

### Response

jsonCopy

```json
{
    "root_url": "https://qwerty.com",
    "depth": 2,
    "crawled_links": [
        "https://qwerty.com/page1",
        "https://qwerty.com/page2",
        ...
    ]
}
```

### Example Request

You can use tools like `curl` or Postman to make API requests.

**Using curl:**

bashCopy

```css
curl -X POST http://localhost:5000/crawl -H "Content-Type: application/json" -d '{"root_url": "https://qswdefr.com", "depth": 2}'
```

## Running Tests



1. Navigate to the project directory:

   bashCopy

   ```javascript
   cd web_crawler
   
   ```
2. Run the tests:

   bashCopy

   ```javascript
   python -m unittest discover tests
   
   ```

## Deployment

### Using GitHub Actions



1. Set up a GitHub repository and push your project files.
2. Create a `.github/workflows` directory in your repository.
3. Create a workflow file (e.g., `main.yml`) inside the `workflows` directory with the following content:

   yamlCopy

   ```bash
   name: Deploy Web Crawler
   
   on:
     push:
       branches:
         - main
   
   jobs:
     build:
       runs-on: ubuntu-latest
   
       steps:
         - name: Checkout code
           uses: actions/checkout@v2
   
         - name: Set up Python
           uses: actions/setup-python@v2
           with:
             python-version: '3.8'
   
         - name: Install dependencies
           run: |
             pip install -r requirements.txt
   
         - name: Run tests
           run: |
             python -m unittest discover tests
   
         - name: Deploy to server
           run: |
             scp -r ./* user@your-server.com:/path/to/your/project
             ssh user@your-server.com 'cd /path/to/your/project && python run.py'
   
   ```
4. Configure your server and ensure SSH access is set up.

## Contributing

Feel free to submit issues and pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License.

This README provides all the necessary information for deploying and running the web crawler API.