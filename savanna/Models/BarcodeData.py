 """
    Response object for UPC lookup
 """
class BarcodeData:

    """ 
    Sets the status code returned by the API.
    """
    def setCode(self, code):
        self.code = code
    
    """
    Gets the status code returned by the API.
    """
    def getCode(self):
        return self.code

    """
    Sets the total number of records matching the search criteria.
    """
    def setTotal(self, total):
        self.total = total
    
    """
    Gets the total number of records matching the search criteria.
    """
    def getTotal(self):
        return self.total

    """
    Sets the Offset variable.
    """
    def setOffset(self, offset):
        self.offset = offset
    
    """
    Gets the Offset (page) of results.
    """
    def getOffset(self):
        return self.offset

    """
    Sets the collection of items matching the UPC lookup query.
    """
    def setItems(self, items):
        self.items = items
    
    """
    Gets the collection of items matching the UPC lookup query.
    """
    def getOffset(self):
        return self.items

   

    
