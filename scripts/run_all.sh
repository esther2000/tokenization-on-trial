#!/usr/bin/env bash

# python scrape_links.py  # uncomment this to scrape new links

# Get text from parallel links, save to files
python get_text.py

# Align sentences from parallel files, write to one file per language
python align.py

# Make train, dev and test splits
python split.py
