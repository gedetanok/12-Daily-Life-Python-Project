
import re
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter

# Define regex patterns for various filters
patterns = {
    'emails': r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',
    'mentions': r'@\w+',
    'hashtags': r'#\w+',
    'links': r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',
    'html_tags': r'<[^>]+>',
    'phone_numbers': r'\+?\d{1,3}[-.\s]?\(?\d{1,4}?\)?[-.\s]?\d{1,4}[-.\s]?\d{1,9}',
    'dates': r'\b\d{1,2}[/-]\d{1,2}[/-]\d{2,4}\b|\b\d{4}[/-]\d{1,2}[/-]\d{1,2}\b',
    'currency': r'\$\d+(?:\.\d{2})?|€\d+(?:\.\d{2})?|£\d+(?:\.\d{2})?|USD\s\d+(?:\.\d+)?',
    'emojis': r'[\U0001F600-\U0001F64F\U0001F300-\U0001F5FF\U0001F680-\U0001F6FF\U0001F700-\U0001F77F\U0001F900-\U0001F9FF]+',
}

def process_text(text, filters, mode):
    if mode == 'extract':
        return {filter_type: re.findall(patterns[filter_type], text) for filter_type in filters}
    elif mode == 'clean':
        cleaned_text = text
        for filter_type in filters:
            cleaned_text = re.sub(patterns[filter_type], '', cleaned_text)
        return {'cleaned_text': cleaned_text}

def plot_data(data, title):
    # Count occurrences of each item and get the top 15
    item_counts = Counter(data).most_common(15)
    items, counts = zip(*item_counts)
    # Create a bar plot
    plt.figure(figsize=(10, 5))
    sns.barplot(x=list(items), y=list(counts), palette='viridis')
    plt.title(title)
    plt.xlabel('Items')
    plt.ylabel('Counts')
    plt.xticks(rotation=45)
    st.pyplot(plt)

# Title of the app
st.title("Text Filter and Cleaner Web App")
# File upload for CSV
uploaded_file = st.file_uploader("Upload a CSV file", type='csv')
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("Data Preview:")
    st.dataframe(df)
    # Column selection dropdown
    selected_column = st.selectbox("Select a column to process:", df.columns.tolist())
    # Mode selection dropdown
    st.sidebar.header("Mode Selection")
    mode = st.sidebar.selectbox("Select mode:", ['extract', 'clean'])
    # Filter options
    st.sidebar.header("Filter Options")
    selected_filters = st.sidebar.multiselect("Select filters to apply:", list(patterns.keys()))
    # Button to apply filters or clean
    if st.button("Process Selected Column"):
        if selected_column and not df[selected_column].isnull().all():
            text_input = df[selected_column].astype(str).str.cat(sep=' ')
            processed_info = process_text(text_input, selected_filters, mode)
            # Display results
            if mode == 'extract':
                st.subheader("Extracted Information")
                # Plot for each extracted filter
                for filter_type in selected_filters:
                    data = processed_info.get(filter_type, [])
                    if data:
                        plot_data(data, f'Top 15 {filter_type.capitalize()} Used')
                st.dataframe(pd.DataFrame.from_dict(processed_info, orient='index').transpose())
            elif mode == 'clean':
                st.subheader("Cleaned Text")
                st.write(processed_info['cleaned_text'])
        else:
            st.error("Please select a valid column with data.")
else:
    # Input text area for manual entry if no file uploaded
    text_input = st.text_area("Enter text to filter or clean:", height=200)

    # Button to apply filters or clean for manual entry
    if st.button("Process Text"):
        if text_input:
            processed_info = process_text(text_input, selected_filters, mode)

            # Display the filtered or cleaned information
            st.subheader("Processed Information")
            if mode == 'extract':
                for filter_type in selected_filters:
                    data = processed_info.get(filter_type, [])
                    if data:
                        plot_data(data, f'Top 15 {filter_type.capitalize()} Used')
                st.dataframe(pd.DataFrame.from_dict(processed_info, orient='index').transpose())
            elif mode == 'clean':
                st.write(processed_info['cleaned_text'])
        else:
            st.error("Please enter text to process.")