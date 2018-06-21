"""
Common utilities for Actuaries who want to use Python
"""

def format_perc(x, dec_places=1):
    """
    format_perc

    x: a number to format as a percentage
    dec_places: an integer for the number of digits past the decimal
    """
    format_str = '{{:,.{}f}}%'.format(dec_places)
    return format_str.format(float(100*x))