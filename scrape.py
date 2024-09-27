import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
from parse import ollama_parse


def scrape_website(url: str) -> str:
    print("Launching Chrome browser...")
    # Setup Chrome driver
    chrome_driver_path = "./chromedriver"
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")
    driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)
    # Open the website within the Chrome driver
    try:
        driver.get(url)
        print("Webpage loaded.")
        html = driver.page_source
        return html
    finally:
        driver.quit()


def extract_html_body(html: str) -> str:
    # Parse the html
    soup = BeautifulSoup(html, "html.parser")
    # Get the body of the html
    html_body = soup.body
    if html_body:
        return str(html_body)
    return ""


def clean_html_body(html_body: str) -> str:
    # Parse the html
    soup = BeautifulSoup(html_body, "html.parser")
    # Remove script and style tags and content
    for tag in soup(["script", "style"]):
        tag.extract()
    # Remove all double newlines that don't contain text ("\n\n")
    html_clean = soup.get_text(separator="\n")
    html_clean = "\n".join(
        line.strip() for line in html_clean.splitlines() if line.strip()
    )
    return html_clean


def split_html_text(html_text: str, max_len: int = 6000) -> str:
    # Split the html text into batches to limit the maximum amount of characters
    return [html_text[i : i + max_len] for i in range(0, len(html_text), max_len)]


def write_file(file_path: str, text: str) -> None:
    with open(file_path, "w") as f:
        f.write(text)


def read_file(file_path: str) -> str:
    with open(file_path, "r") as f:
        result = f.read()
    return result


if __name__ == "__main__":
    url = "https://techwithtim.net"
    html = scrape_website(url)
    write_file("content.html", html)

    # html = read_file("html.html")
    # html_body = extract_html_body(html)
    # html_clean = clean_html_body(html_body)
    # html_batches = split_html_text(html_clean)
    # parse_desc = input("Enter the prompt to parse: ")
    # result = ollama_parse(html_batches, parse_desc)
    # print(result)
