# Author: jcharrisjr
# Date: 2024-03-10
# License: MIT
# Exercise: PaginationHelper (https://www.codewars.com/kata/515bb423de843ea99400000a)
#
# This script provides a solution to the PaginationHelper exercise on Codewars.
# The PaginationHelper class is designed to assist with paginating large collections
# of items, offering methods to get page and item information efficiently.

class PaginationHelper:
    
    # The constructor takes in an array of items and an integer indicating
    # how many items fit within a single page
    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page
    
    # Display class info
    def display_info(self):
        print(f"Collection: {self.collection}")
        print(f"Items per page: {self.items_per_page}")
    
    # returns the number of items within the entire collection
    def item_count(self):
        
        return len(self.collection)
    
    # returns the number of pages
    def page_count(self):
        if len(self.collection) == 0:
            return 0
    
        # Calculate the number of pages and handle remainder
        pages, remainder = divmod(len(self.collection), self.items_per_page)
        if remainder != 0:
            pages += 1
        
        return pages

    
    # returns the number of items on the given page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self, page_index):
        if page_index < 0 or page_index >= self.page_count():
        # Return -1 if page_index is out of range
            return -1

        length = len(self.collection)
        pages, remainder = divmod(length, self.items_per_page)

        # Increment pages if there's a remainder
        if remainder != 0:
            pages += 1

        # Return the number of items on the given page
        if page_index == pages - 1:
            return remainder if remainder != 0 else self.items_per_page
        else:
            return self.items_per_page
    
    # determines what page an item at the given index is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self, item_index):
        if item_index < 0 or item_index >= len(self.collection):
        # Return -1 if item_index is out of range
            return -1

    # Calculate the page index
        return item_index // self.items_per_page
