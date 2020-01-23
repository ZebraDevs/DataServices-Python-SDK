"""
Information about a recalled medical device.
"""

class MetaResults:

    def __init__(self, deviceClass, deviceName, feiNumber, kNumber, 
    medicalSpecialtyDescription, registrationNumber, regulationNumber):
        self.deviceClass = deviceClass
        self.deviceName = deviceName
        self.feiNumber = feiNumber
        self.kNumber = kNumber
        self.medicalSpecialtyDescription = medicalSpecialtyDescription
        self.registrationNumber = registrationNumber
        self.regulationNumber = regulationNumber

    """
    A risk based classification system for all medical devices (Federal Food, Drug, and Cosmetic Act, section 513).
    """
    @property
    def deviceClass(self):
        return self.__deviceClass

    """
    This is the proprietary name, or trade name, of the cleared device.
    """
    @property
    def deviceName(self):
        return self.__deviceName

    """
    Facility identifier assigned to facility by the FDA Office of Regulatory Affairs.
    """
    @property
    def feiNumber(self):
        return self.__feiNumber

    """
    FDA-assigned premarket notification number, including leading letters. Leading letters "BK" indicates
    510(k) clearance, or Premarket Notification, cleared by Center for Biologics Evaluation and Research.
    Leading letters "DEN" indicates De Novo, or Evaluation of Automatic Class III Designation. Leading letter
    "K" indicates 510(k) clearance, or Premarket Notification. `Source`: 510(k)
    """
    @property
    def kNumber(self):
        return self.__kNumber

    """
    Regulation Medical Specialty is assigned based on the regulation (e.g. 21 CFR Part 888 is Orthopedic
    Devices) which is why Class 3 devices lack the "Regulation Medical Specialty" field.
    """
    @property
    def medicalSpecialtyDescription(self):
        return self.__medicalSpecialtyDescription

    """
    Facility identifier assigned to facility by the FDA Office of Regulatory Affairs.
    """
    @property
    def registrationNumber(self):
        return self.__registrationNumber

    """
    The classification regulation in the Code of Federal Regulations (CFR) under which the device is
    identified, described, and formally classified (Code of Federal regulations Title 21, 862.00 through
    892.00). The classification regulation covers various aspects of design, clinical evaluation,
    manufacturing, packaging, labeling, and postmarket surveillance of the specific medical device.
    """
    @property
    def regulationNumber(self):
        return self.__regulationNumber
