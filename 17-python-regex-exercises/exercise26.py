# ========question========
# Exercise 26: Extract Date from URL
#
# Problem Statement: Write a Python program to extract the year, month, and day components from a URL string formatted as https://example.com/yyyy/mm/dd/article-slug.
#
# Purpose: This exercise practises using multiple capturing groups to pull structured data out of a predictably formatted string. Extracting date segments from URLs is a common task in web scraping, content management systems, and analytics pipelines where publication dates are embedded in permalink structures.
#
# Given Input: urls = ["https://example.com/2026/05/22/my-article", "https://news.site.org/2019/11/03/breaking-story", "https://blog.example.com/2023/07/30/summer-update"]
#
# Expected Output:
#
# URL: https://example.com/2026/05/22/my-article
#   Year: 2026 | Month: 05 | Day: 22
#
# URL: https://news.site.org/2019/11/03/breaking-story
#   Year: 2019 | Month: 11 | Day: 03
#
# URL: https://blog.example.com/2023/07/30/summer-update
#   Year: 2023 | Month: 07 | Day: 30
#
# Source: https://pynative.com/python-regex-exercises/


# ========hints========
# Separate parsing a date from formatting or doing arithmetic with it.


# Write your code below.

