"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start=100):
        self.start = start
        
    def __repr__(self):
        return f"<Serial Number Generator starting at {self.start}>"
    
    def generate(self):
        """Gets the next number of the series"""
        self.start = self.start + 1
        return self.start

    def reset(self):
        """Returns the start number to its original state"""
        self.start = 100
        return self.start




