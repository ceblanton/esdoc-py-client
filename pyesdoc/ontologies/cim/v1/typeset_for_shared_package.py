# -*- coding: utf-8 -*-

"""
.. module:: cim.v1.typeset_for_shared_package.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: The set of types of the cim.v1.shared package.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using the esdoc-mp framework.

"""
import abc
import datetime
import uuid




class Calendar(object):
    """An abstract class within the cim v1 type system.

    Describes a method of calculating a span of dates.

    """
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        """Instance constructor.

        """
        super(Calendar, self).__init__()

        self.description = None                           # unicode (0.1)
        self.length = None                                # int (0.1)
        self.range = None                                 # shared.DateRange (0.1)


class Change(object):
    """A concrete class within the cim v1 type system.

    A description of [a set of] changes applied at a particular time, by a particular party, to a particular unit of metadata.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(Change, self).__init__()

        self.author = None                                # shared.ResponsibleParty (0.1)
        self.date = None                                  # datetime.datetime (0.1)
        self.description = None                           # unicode (0.1)
        self.details = []                                 # shared.ChangeProperty (1.N)
        self.name = None                                  # unicode (0.1)
        self.type = None                                  # shared.ChangePropertyType (0.1)


class Citation(object):
    """A concrete class within the cim v1 type system.

    An academic reference to published work.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(Citation, self).__init__()

        self.alternative_title = None                     # unicode (0.1)
        self.collective_title = None                      # unicode (0.1)
        self.date = None                                  # datetime.datetime (0.1)
        self.date_type = None                             # unicode (0.1)
        self.location = None                              # unicode (0.1)
        self.organisation = None                          # unicode (0.1)
        self.role = None                                  # unicode (0.1)
        self.title = None                                 # unicode (0.1)
        self.type = None                                  # unicode (0.1)


class Compiler(object):
    """A concrete class within the cim v1 type system.

    A description of a compiler used on a particular platform.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(Compiler, self).__init__()

        self.environment_variables = None                 # unicode (0.1)
        self.language = None                              # unicode (0.1)
        self.name = None                                  # unicode (1.1)
        self.options = None                               # unicode (0.1)
        self.type = None                                  # shared.CompilerType (0.1)
        self.version = None                               # unicode (1.1)


class DataSource(object):
    """An abstract class within the cim v1 type system.

    A DataSource can be realised by either a DataObject (file), a DataContent (variable), a Component (model), or a ComponentProperty (variable); all of those can supply data.

    """
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        """Instance constructor.

        """
        super(DataSource, self).__init__()

        self.purpose = None                               # shared.DataPurpose (0.1)


class DateRange(object):
    """An abstract class within the cim v1 type system.

    Creates and returns instance of date_range class.

    """
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        """Instance constructor.

        """
        super(DateRange, self).__init__()

        self.duration = None                              # unicode (0.1)


class DocGenealogy(object):
    """A concrete class within the cim v1 type system.

    A record of a document's history. A genealogy element contains a textual description and a set of relationships. Each relationship has a type and a reference to some target. There are different relationships for different document types.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(DocGenealogy, self).__init__()

        self.relationships = []                           # shared.DocRelationship (0.N)


class DocMetaInfo(object):
    """A concrete class within the cim v1 type system.

    Encapsulates document meta information.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(DocMetaInfo, self).__init__()

        self.author = None                                # shared.ResponsibleParty (0.1)
        self.create_date = None                           # datetime.datetime (1.1)
        self.drs_keys = []                                # unicode (0.N)
        self.drs_path = None                              # unicode (0.1)
        self.external_ids = []                            # shared.StandardName (0.N)
        self.genealogy = None                             # shared.DocGenealogy (0.1)
        self.id = None                                    # uuid.UUID (1.1)
        self.institute = None                             # unicode (0.1)
        self.language = None                              # unicode (1.1)
        self.project = None                               # unicode (1.1)
        self.sort_key = None                              # unicode (0.1)
        self.source = None                                # unicode (1.1)
        self.source_key = None                            # unicode (0.1)
        self.status = None                                # shared.DocStatusType (0.1)
        self.sub_projects = []                            # unicode (0.N)
        self.type = None                                  # unicode (1.1)
        self.type_display_name = None                     # unicode (0.1)
        self.type_sort_key = None                         # unicode (0.1)
        self.update_date = None                           # datetime.datetime (1.1)
        self.version = None                               # int (1.1)
        self.source = unicode("scripts")


class DocReference(object):
    """A concrete class within the cim v1 type system.

    A reference to another cim entity.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(DocReference, self).__init__()

        self.changes = []                                 # shared.Change (0.N)
        self.description = None                           # unicode (0.1)
        self.external_id = None                           # unicode (0.1)
        self.id = None                                    # uuid.UUID (0.1)
        self.name = None                                  # unicode (0.1)
        self.type = None                                  # unicode (0.1)
        self.url = None                                   # unicode (0.1)
        self.version = None                               # int (0.1)


class DocRelationshipTarget(object):
    """A concrete class within the cim v1 type system.

    Creates and returns instance of doc_relationship_target class.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(DocRelationshipTarget, self).__init__()

        self.reference = None                             # shared.DocReference (0.1)


class License(object):
    """A concrete class within the cim v1 type system.

    A description of a license restricting access to a unit of data or software.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(License, self).__init__()

        self.contact = None                               # unicode (0.1)
        self.description = None                           # unicode (0.1)
        self.is_unrestricted = None                       # bool (0.1)
        self.name = None                                  # unicode (0.1)


class Machine(object):
    """A concrete class within the cim v1 type system.

    A description of a machine used by a particular platform.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(Machine, self).__init__()

        self.cores_per_processor = None                   # int (0.1)
        self.description = None                           # unicode (0.1)
        self.interconnect = None                          # shared.InterconnectType (0.1)
        self.libraries = []                               # unicode (0.N)
        self.location = None                              # unicode (0.1)
        self.maximum_processors = None                    # int (0.1)
        self.name = None                                  # unicode (1.1)
        self.operating_system = None                      # shared.OperatingSystemType (0.1)
        self.processor_type = None                        # shared.ProcessorType (0.1)
        self.system = None                                # unicode (0.1)
        self.type = None                                  # shared.MachineType (0.1)
        self.vendor = None                                # shared.MachineVendorType (0.1)


class MachineCompilerUnit(object):
    """A concrete class within the cim v1 type system.

    Associates a machine with a [set of] compilers.  This is a separate class in case a platform needs to specify more than one machine/compiler pair.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(MachineCompilerUnit, self).__init__()

        self.compilers = []                               # shared.Compiler (0.N)
        self.machine = None                               # shared.Machine (1.1)


class Platform(object):
    """A concrete class within the cim v1 type system.

    A platform is a description of resources used to deploy a component/simulation.  A platform pairs a machine with a (set of) compilers.  There is also a point of contact for the platform.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(Platform, self).__init__()

        self.contacts = []                                # shared.ResponsibleParty (0.N)
        self.description = None                           # unicode (0.1)
        self.long_name = None                             # unicode (0.1)
        self.meta = DocMetaInfo()                         # shared.DocMetaInfo (1.1)
        self.short_name = None                            # unicode (1.1)
        self.units = []                                   # shared.MachineCompilerUnit (1.N)


class Property(object):
    """A concrete class within the cim v1 type system.

    A simple name/value pair representing a property of some entity or other.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(Property, self).__init__()

        self.name = None                                  # unicode (0.1)
        self.value = None                                 # unicode (0.1)


class Relationship(object):
    """An abstract class within the cim v1 type system.

    A record of a relationship between one document and another. This class is abstract; specific document types must specialise this class for their relationshipTypes to be included in a document's genealogy.

    """
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        """Instance constructor.

        """
        super(Relationship, self).__init__()

        self.description = None                           # unicode (0.1)
        self.direction = None                             # shared.DocRelationshipDirectionType (1.1)


class ResponsibleParty(object):
    """A concrete class within the cim v1 type system.

    A person/organsiation responsible for some aspect of a climate science artefact.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(ResponsibleParty, self).__init__()

        self.abbreviation = None                          # unicode (0.1)
        self.address = None                               # unicode (0.1)
        self.email = None                                 # unicode (0.1)
        self.individual_name = None                       # unicode (0.1)
        self.organisation_name = None                     # unicode (0.1)
        self.role = None                                  # unicode (0.1)
        self.url = None                                   # unicode (0.1)


class Standard(object):
    """A concrete class within the cim v1 type system.

    Describes a name given to an entity from a recognised standard.  The CIM records the standard and the name.  For example, the standard might be CF and the name might be atmospheric_pressure.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(Standard, self).__init__()

        self.description = None                           # unicode (0.1)
        self.name = None                                  # unicode (1.1)
        self.version = None                               # unicode (0.1)


class StandardName(object):
    """A concrete class within the cim v1 type system.

    Describes a name given to an entity from a recognised standard.  The CIM records the standard and the name.  For example, the standard might be CF and the name might be atmospheric_pressure.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(StandardName, self).__init__()

        self.is_open = None                               # bool (1.1)
        self.standards = []                               # shared.Standard (0.N)
        self.value = None                                 # unicode (1.1)


class ChangeProperty(Property):
    """A concrete class within the cim v1 type system.

    A description of a single change applied to a single target.  Every ChangeProperty has a description, and may also have a name from a controlled vocabulary and a value.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(ChangeProperty, self).__init__()

        self.description = None                           # unicode (0.1)
        self.id = None                                    # unicode (0.1)


class ClosedDateRange(DateRange):
    """A concrete class within the cim v1 type system.

    A date range with specified start and end points.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(ClosedDateRange, self).__init__()

        self.end = None                                   # datetime.datetime (0.1)
        self.start = None                                 # datetime.datetime (1.1)


class Daily360(Calendar):
    """A concrete class within the cim v1 type system.

    Creates and returns instance of daily_360 class.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(Daily360, self).__init__()



class DocRelationship(Relationship):
    """A concrete class within the cim v1 type system.

    Contains the set of relationships supported by a Document.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(DocRelationship, self).__init__()

        self.target = None                                # shared.DocRelationshipTarget (1.1)
        self.type = None                                  # shared.DocRelationshipType (1.1)


class OpenDateRange(DateRange):
    """A concrete class within the cim v1 type system.

    A date range without a specified start and/or end point.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(OpenDateRange, self).__init__()

        self.end = None                                   # datetime.datetime (0.1)
        self.start = None                                 # datetime.datetime (0.1)


class PerpetualPeriod(Calendar):
    """A concrete class within the cim v1 type system.

    Creates and returns instance of perpetual_period class.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(PerpetualPeriod, self).__init__()



class RealCalendar(Calendar):
    """A concrete class within the cim v1 type system.

    Creates and returns instance of real_calendar class.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(RealCalendar, self).__init__()



class ChangePropertyType(object):
    """An enumeration within the cim v1 type system.

    Creates and returns instance of change_property_type enum.
    """
    is_open = False
    members = [
        "AncillaryFile",
        "BoundaryCondition",
        "CodeChange",
        "Decrement",
        "Increment",
        "InitialCondition",
        "InputMod",
        "ModelMod",
        "ParameterChange",
        "Redistribution",
        "Replacement",
        "Unused"
        ]


class CompilerType(object):
    """An enumeration within the cim v1 type system.

    Creates and returns instance of compiler_type enum.
    """
    is_open = True
    members = []


class DataPurpose(object):
    """An enumeration within the cim v1 type system.

    Purpose of the data - i.e. ancillaryFile, boundaryCondition or initialCondition.
    """
    is_open = False
    members = [
        "ancillaryFile",
        "boundaryCondition",
        "initialCondition"
        ]


class DocRelationshipDirectionType(object):
    """An enumeration within the cim v1 type system.

    Creates and returns instance of relationship_direction_type enum.
    """
    is_open = False
    members = [
        "fromTarget",
        "toTarget"
        ]


class DocRelationshipType(object):
    """An enumeration within the cim v1 type system.

    Creates and returns instance of document_relationship_type enum.
    """
    is_open = False
    members = [
        "fixedVersionOf",
        "laterVersionOf",
        "other",
        "previousVersionOf",
        "similarTo"
        ]


class DocStatusType(object):
    """An enumeration within the cim v1 type system.

    Status of cim document.
    """
    is_open = False
    members = [
        "complete",
        "in-progress",
        "incomplete"
        ]


class DocType(object):
    """An enumeration within the cim v1 type system.

    Creates and returns instance of doc_type enum.
    """
    is_open = False
    members = [
        "assimilation",
        "cimQuality",
        "dataObject",
        "dataProcessing",
        "downscalingSimulation",
        "ensemble",
        "gridSpec",
        "modelComponent",
        "numericalExperiment",
        "platform",
        "processorComponent",
        "simulationComposite",
        "simulationRun",
        "statisticalModelComponent"
        ]


class InterconnectType(object):
    """An enumeration within the cim v1 type system.

    A list of connectors between machines.
    """
    is_open = True
    members = []


class MachineType(object):
    """An enumeration within the cim v1 type system.

    A list of known machines.
    """
    is_open = False
    members = [
        "Beowulf",
        "Parallel",
        "Vector"
        ]


class MachineVendorType(object):
    """An enumeration within the cim v1 type system.

    A list of organisations that create machines.
    """
    is_open = True
    members = []


class OperatingSystemType(object):
    """An enumeration within the cim v1 type system.

    A list of common operating systems.
    """
    is_open = True
    members = []


class ProcessorType(object):
    """An enumeration within the cim v1 type system.

    A list of known cpu's.
    """
    is_open = True
    members = []


class UnitType(object):
    """An enumeration within the cim v1 type system.

    A list of scientific units.
    """
    is_open = True
    members = []


