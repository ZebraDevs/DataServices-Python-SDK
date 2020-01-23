"""
Includes a disclaimer, a link to the openFDA data license, and information about the results.
"""

class Meta:

    def __init__(self, disclaimer, terms, license, lastUpdated, results):
        self.disclaimer = disclaimer
        self.terms = terms
        self.license = license
        self.lastUpdated = lastUpdated
        self.results = results

    """
    Important details notes about openFDA data and limitations of the dataset.
    """
    @property
    def disclaimer(self):
        return self.__disclaimer

    """
    Link to a web page with license terms that govern data within openFDA.
    """
    @property
    def terms(self):
        return self.__terms

    """
    Link to a web page with the license that governs data within openFDA.
    """
    @property
    def license(self):
        return self.__license

    """
    The last date when this openFDA endpoint was updated. Note that this does not correspond to the most recent
    record for the endpoint or dataset. Rather, it is the last time the openFDA API was itself updated.
    """
    @property
    def lastUpdated(self):
        return self.__lastUpdated

    """
    Information about the results.
    """
    @property
    def results(self):
        return self.__results

    


    
    