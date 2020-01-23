"""
Device recall report.
"""

class Device:

    def __init__(self, applicationNumber, brandName, genericName, isOriginalPackager, 
    manufacturerName, NUI, originalPackagerProductNDC, packageNDC,
    pharmClassCS, pharmClassEPC, pharmClassPE, pharm_class_moa, productNDC, productType,
    route, RxCUI, SPLId, SPLSetId, substanceName, UnII, upc):
        self.applicationNumber = applicationNumber
        self.brandName = brandName
        self.genericName = genericName
        self.isOriginalPackager = isOriginalPackager
        self.manufacturerName = manufacturerName
        self.NUI = NUI
        self.originalPackagerProductNDC = originalPackagerProductNDC
        self.packageNDC = packageNDC
        self.pharmClassCS = pharmClassCS
        self.pharmClassEPC = pharmClassEPC
        self.pharm_class_moa = pharm_class_moa
        self.productNDC = productNDC
        self.productType = productType
        self.route = route
        self.RxCUI = RxCUI
        self.SPLId = SPLId
        self.SPLSetId = SPLSetId
        self.substanceName = substanceName
        self.UnII = UnII
        self.upc = upc

    """
    This corresponds to the NDA, ANDA, or BLA number reported by the labeler for products which have the
    corresponding Marketing Category designated. If the designated Marketing Category is OTC Monograph Final or
    OTC Monograph Not Final, then the application number will be the CFR citation corresponding to the
    appropriate Monograph (e.g. "part 341"). For unapproved drugs, this field will be null.
    """
    @property
    def eventDateTerminated(self):
        return self.__applicationNumber

    """
    Brand or trade name of the drug product.
    """
    @property
    def brandName(self):
        return self.__brandName

    """
    Generic name(s) of the drug product.
    """
    @property
    def genericName(self):
        return self.__genericName

    """
    Whether or not the drug has been repackaged for distribution.
    """
    @property
    def isOriginalPackager(self):
        return self.__isOriginalPackager

    """
    Name of manufacturer or company that makes this drug product, corresponding to the labeler code segment of
    the NDC.
    """
    @property
    def manufacturerName(self):
        return self.__manufacturerName

    """
    Unique identifier applied to a drug concept within the National Drug File Reference Terminology (NDF-RT).
    https://www.nlm.nih.gov/research/umls/sourcereleasedocs/current/NDFRT/
    """
    @property
    def NUI(self):
        return self.__NUI

    """
    This NDC identifies the original packager.
    """
    @property
    def originalPackagerProductNDC(self):
        return self.__originalPackagerProductNDC

    """
    This number, known as the NDC, identifies the labeler, product, and trade package size. The first segment,
    the labeler code, is assigned by the FDA. A labeler is any firm that manufactures (including repackers or
    relabelers), or distributes (under its own name) the drug.
    """
    @property
    def packageNDC(self):
        return self.__packageNDC

    """
    Chemical structure classification of the drug product’s pharmacologic class. Takes the form of the
    classification, followed by `[Chemical/Ingredient]` (such as `Thiazides [Chemical/Ingredient]` or
    `Antibodies, Monoclonal [Chemical/Ingredient].
    """
    @property
    def pharmClassCS(self):
        return self.__pharmClassCS

    """
    Established pharmacologic class associated with an approved indication of an active moiety (generic drug)
    that the FDA has determined to be scientifically valid and clinically meaningful. Takes the form of the
    pharmacologic class, followed by `[EPC]` (such as `Thiazide Diuretic [EPC]` or `Tumor Necrosis Factor
    Blocker [EPC]`.
    """
    @property
    def pharmClassEPC(self):
        return self.__pharmClassEPC

    """
    Mechanism of action of the drug—molecular, subcellular, or cellular functional activity—of the drug’s
    established pharmacologic class. Takes the form of the mechanism of action, followed by `[MoA]` (such as
    `Calcium Channel Antagonists [MoA]` or `Tumor Necrosis Factor Receptor Blocking Activity [MoA]`.
    """
    @property
    def pharm_class_moa(self):
        return self.__pharm_class_moa

    """
    Mechanism of action of the drug—molecular, subcellular, or cellular functional activity—of the drug’s
    established pharmacologic class. Takes the form of the mechanism of action, followed by `[MoA]` (such as
    `Calcium Channel Antagonists [MoA]` or `Tumor Necrosis Factor Receptor Blocking Activity [MoA]`.
    """
    @property
    def productNDC(self):
        return self.__productNDC

    """
    Type of drug product.
    http://www.fda.gov/ForIndustry/DataStandards/StructuredProductLabeling/ucm162063.html
    """
    @property
    def productType(self):
        return self.__productType

    """
    The route of administation of the drug product.
    http://www.fda.gov/ForIndustry/DataStandards/StructuredProductLabeling/ucm162034.html
    """
    @property
    def route(self):
        return self.__route

    """
    The RxNorm Concept Unique Identifier. RxCUI is a unique number that describes a semantic concept about the
    drug product, including its ingredients, strength, and dose forms.
    https://www.nlm.nih.gov/research/umls/rxnorm/docs/2012/rxnorm_doco_full_2012-3.html
    """
    @property
    def RxCUI(self):
        return self.__RxCUI

    """
    Unique identifier for a particular version of a Structured Product Label for a product. Also referred to as
    the document ID.
    """
    @property
    def SPLId(self):
        return self.__SPLId

    """
    Unique identifier for the Structured Product Label for a product, which is stable across versions of the
    label. Also referred to as the set ID.
    """
    @property
    def SPLSetId(self):
        return self.__SPLSetId

    """
    The list of active ingredients of a drug product.
    """
    @property
    def substanceName(self):
        return self.__substanceName

    """
    Unique Ingredient Identifier, which is a non-proprietary, free, unique, unambiguous, non-semantic,
    alphanumeric identifier based on a substance’s molecular structure and/or descriptive information.
    http://fdasis.nlm.nih.gov/srs/srs.jsp
    """
    @property
    def UnII(self):
        return self.__UnII

    """
    Universal Product Code
    https://en.wikipedia.org/wiki/Universal_Product_Code
    """
    @property
    def upc(self):
        return self.__upc