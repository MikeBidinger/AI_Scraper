import streamlit as st
from scrape import scrape_website, extract_html_body, clean_html_body, split_html_text
from parse import ollama_parse

st.title("AI Scraper")

col1, col2 = st.columns([0.74, 0.16], vertical_alignment="bottom")
with col1:
    url = st.text_input("Enter a Website URL: ")
with col2:
    st.link_button("Visit Website", url)

if st.button("Scrape Website"):
    # Insert a single-element container
    placeholder = st.empty()
    # Replace the single-element container
    placeholder.write("Scraping the website...")
    # Get the HTML of the website
    html = scrape_website(url)
    html_body = extract_html_body(html)
    html_clean = clean_html_body(html_body)
    # Store the HTML in the session
    st.session_state.html_content = html_clean
    # Clear the single-element container
    placeholder.empty()

if "html_content" in st.session_state:
    # Display the HTML
    with st.expander("View/Hide HTML content"):
        st.text_area("HTML content:", st.session_state.html_content, height=300)
    # User input
    parse_desc = st.text_area("What do you want to parse?")
    # Parse the HTML content
    if st.button("Parse Content"):
        if parse_desc:
            placeholder = st.empty()
            placeholder.write("Parsing the content...")
            html_batches = split_html_text(st.session_state.html_content)
            result = ollama_parse(html_batches, parse_desc)
            st.write(result)
            placeholder.empty()
