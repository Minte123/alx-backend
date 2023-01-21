#!/usr/bin/env python3
""" Simple helper function """


def index_range(page: int, page_size: int) -> tuple:
    """ calculates the start and end index
    Parameters
    ----------
    page : int
        page number
    page_size : int
        page content size

    Returns
    -------
    tuple
        tuple of size two containing a start index
        and an end index corresponding
        to the range of indexes to return in a list for those
        particular pagination parameters
    """
    return ((page - 1) * page_size, page * page_size)
