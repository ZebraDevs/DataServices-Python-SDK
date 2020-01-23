"""
Information about the results.
"""

class MetaResults:

    def __init__(self, skip, limit, total):
        self.skip = skip
        self.limit = limit
        self.total = total

    """
    Offset (page) of results, defined by the skip query parameter.
    """
    @property
    def skip(self):
        return self.__skip

    """
    Number of records returned, defined by the limit query parameter. If there is no limit parameter, the
    API returns one result.
    """
    @property
    def limit(self):
        return self.__limit

    """
    Total number of records matching the search criteria.
    """
    @property
    def total(self):
        return self.__total