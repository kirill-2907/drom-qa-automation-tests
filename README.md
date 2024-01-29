# Auto tests
tests/test_filter.py

tests/test_favorites.py

1. Install pip: `sudo apt install python3-pip`
2. Run commands: `pip install --no-cache-dir --upgrade pip`, `pip install --no-cache-dir -r requirements.txt`

Or manually install:

3. Install the Pytest plugin: `pip install pytest-playwright`
4. Install the required browsers: `playwright install`
5. Install allure: `sudo pip install allure-pytest`

Run tests: `pytest -v -s --alluredir results`

# Script 
`scrypt_parser/scrypt.py`
1. Install BeautifulSoup4 `pip install BeautifulSoup4` 
2. Install parser library `pip install lxml`
