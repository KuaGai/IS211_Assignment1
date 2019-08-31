#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This is part 2 of the Assignment 1

class Book(object):
    """A book class.
    Args:
        author (str): Name of author
        title (str): Name of book
    """
    author = ""
    title = ""

    def __init__(self, author, title):
        """Initiator function."""

        self.author = author
        self.title = title

    def display(self):
        """Displays information about book.
        Returns:
            output (str): Author, Book
        """

        message = "{}, written by {}."
        output = message.format(self.author, self.title)
        return output

BOOK1 = Book("Of Mice and Men", "John Steinbeck")
BOOK2 = Book("To Kill a Mockingbird", "Harper Lee")

print BOOK1.display()
print BOOK2.display()
