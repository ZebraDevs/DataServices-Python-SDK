"""
Offer for an item provided by a merchant.
"""

class MetaResults:

    def __init__(self, merchant, domain, title, currency, listPrice, 
    price, shipping, condition, availability, link, updatedTimestamp):
        self.merchant = merchant
        self.domain = domain
        self.title = title
        self.currency = currency
        self.listPrice = listPrice
        self.price = price
        self.shipping = shipping
        self.condition = condition
        self.availability = availability
        self.link = link
        self.updatedTimestamp = updatedTimestamp

    """
    Online store name.
    """
    @property
    def merchant(self):
        return self.__merchant

    """
    Online store domain.
    """
    @property
    def domain(self):
        return self.__domain

    """
    Item name marketed by the merchant.
    """
    @property
    def title(self):
        return self.__title

    """
    Currency of listPrice Can be "USD", "CAD", "EUR", "GBP", "SEK".
    Default "" means "USD".
    """
    @property
    def currency(self):
        return self.__currency

    """
    Original price from the store.
    """
    @property
    def listPrice(self):
        return self.__listPrice

    """
    Sale price.
    """
    @property
    def price(self):
        return self.__price

    """
    "Free Shipping" or other shipping information if not free.
    """
    @property
    def shipping(self):
        return self.__shipping

    """
    "New" or "Used"
    """
    @property
    def condition(self):
        return self.__condition

    """
    Default "" means available or "Out of Stock"
    """
    @property
    def availability(self):
        return self.__availability

    """
    Shop link of the item.
    """
    @property
    def link(self):
        return self.__link

    """
    Unix timestamp of when the offer was last updated.
    """
    @property
    def updatedTimestamp(self):
        return self.__updatedTimestamp