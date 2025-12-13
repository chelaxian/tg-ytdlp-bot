#!/bin/bash

# Create TXT directory if it doesn't exist
mkdir -p TXT

# Download porn_domains.txt
echo "Enter URL from which to download 'porn_domains.txt':"
read -r URL_DOMAINS
curl -sL "$URL_DOMAINS" -o "TXT/porn_domains.txt"
echo "Downloaded porn_domains.txt to TXT/porn_domains.txt"

# Download porn_keywords.txt
echo "Enter URL from which to download 'porn_keywords.txt':"
read -r URL_KEYWORDS
curl -sL "$URL_KEYWORDS" -o "TXT/porn_keywords.txt"
echo "Downloaded porn_keywords.txt to TXT/porn_keywords.txt"

echo "Download completed!"
