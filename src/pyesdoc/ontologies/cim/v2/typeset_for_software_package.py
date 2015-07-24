# -*- coding: utf-8 -*-

"""
.. module:: cim.v2.typeset_for_software_package.py

   :copyright: @2015 Earth System Documentation (http://es-doc.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: The set of types of the cim.v2.software package.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using esdoc_mp.

"""
import abc
import datetime
import uuid

import typeset_for_science_package as science
import typeset_for_shared_package as shared



class ComponentBase(object):
    """An abstract class within the cim v2 type system.

    Base class for software component properties, whether a top level model,
    or a specific piece of code known as a component. In software terms, a
    component is a discrete set of code that takes input data and generates output data.
    Components may or may not have scientific descriptions.

    """
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        """Constructor.

        """
        super(ComponentBase, self).__init__()

        self.tuning_applied = None                        # science.Tuning
        self.name = None                                  # str
        self.description = None                           # shared.Cimtext
        self.long_name = None                             # str
        self.documentation = []                           # shared.Citation
        self.version = None                               # str
        self.development_history = None                   # software.DevelopmentPath
        self.release_date = None                          # datetime.datetime


class EntryPoint(object):
    """A concrete class within the cim v2 type system.

    Describes a function or subroutine of a SoftwareComponent.
    BFG will use these EntryPoints to define a schedule of subroutine calls for a coupled model.
    Currently, a very basic schedule can be approximated by using the "proceeds" and "follows" attributes,
    however a more complete system is required for full BFG compatibility.
    Every EntryPoint can have a set of arguments associated with it.
    These reference (previously defined) variables

    """
    def __init__(self):
        """Constructor.

        """
        super(EntryPoint, self).__init__()

        self.name = None                                  # str


class DevelopmentPath(object):
    """A concrete class within the cim v2 type system.

    Describes the software development path for this model/component.

    """
    def __init__(self):
        """Constructor.

        """
        super(DevelopmentPath, self).__init__()

        self.previous_version = None                      # str
        self.developed_in_house = None                    # bool
        self.funding_sources = []                         # shared.Responsibility
        self.consortium_name = None                       # str
        self.creators = []                                # shared.Responsibility


class Gridspec(object):
    """A concrete class within the cim v2 type system.

    Fully defines the computational grid used.

    """
    def __init__(self):
        """Constructor.

        """
        super(Gridspec, self).__init__()

        self.description = None                           # str


class Variable(object):
    """A concrete class within the cim v2 type system.

    An instance of a model software variable which may be prognostic or diagnostic, and which is
    available as a connection to other software components. Note that these variables may only exist
    within the software workflow as interim quantities or coupling endpoints. Input and output
    variables will be a subset of these software variables.

    """
    def __init__(self):
        """Constructor.

        """
        super(Variable, self).__init__()

        self.name = None                                  # str
        self.description = None                           # str
        self.prognostic = None                            # bool


class Composition(object):
    """A concrete class within the cim v2 type system.

    Describes how component variables are coupled together either to/from other
    SoftwareComponents or external data files. The variables specified by a component's
    composition must be owned by that component, or a  child of that component;
    child components cannot couple together parent variables.

    """
    def __init__(self):
        """Constructor.

        """
        super(Composition, self).__init__()

        self.couplings = []                               # str
        self.description = None                           # str


class SoftwareComponent(ComponentBase):
    """A concrete class within the cim v2 type system.

    An embedded piece of software that does not normally function as a standalone model (although
    it may be used standalone in a test harness).

    """
    def __init__(self):
        """Constructor.

        """
        super(SoftwareComponent, self).__init__()

        self.coupling_framework = None                    # software.CouplingFramework
        self.sub_components = []                          # software.SoftwareComponent
        self.language = None                              # software.ProgrammingLanguage
        self.license = None                               # str
        self.dependencies = []                            # software.EntryPoint
        self.grid = None                                  # software.Gridspec
        self.connection_points = []                       # software.Variable
        self.composition = None                           # software.Composition


class Model(ComponentBase):
    """A concrete class within the cim v2 type system.

    A model component: can be executed standalone, and has as scientific
    description available via a link to a science.domain document. (A configured model can
     be understood in terms of a simulation, a model, and a configuration.)

    """
    def __init__(self):
        """Constructor.

        """
        super(Model, self).__init__()

        self.extra_conservation_properties = None         # science.ConservationProperties
        self.scientific_domain = []                       # science.ScientificDomain
        self.coupled_software_components = []             # software.Model
        self.meta = shared.Meta()                         # shared.Meta
        self.internal_software_components = []            # software.SoftwareComponent
        self.coupler = None                               # software.CouplingFramework
        self.category = None                              # science.ModelTypes


class CouplingFramework(object):
    """An enumeration within the cim v2 type system.

    The set of terms which define known coupling frameworks
    """

    pass


class ProgrammingLanguage(object):
    """An enumeration within the cim v2 type system.

    The set of terms which define programming languages used for earth
    system simulation.
    """

    pass

