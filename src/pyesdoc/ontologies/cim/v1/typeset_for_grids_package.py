"""
.. module:: cim.v1.typeset_for_grids_package.py

   :copyright: @2013 Earth System Documentation (http://esdocumentation.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: The set of types of the cim.v1.grids package.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@esdocumentation.org>
.. note:: Code generated using esdoc_mp @ 2013-08-30 17:49:36.050877.

"""
# Module imports.
import abc
import datetime
import uuid

import typeset_for_shared_package as shared




class CoordinateList(object):
    """A concrete class within the cim v1 type system.

    The CoordList type may be used to specify a list of coordinates, typically for the purpose of defining coordinates along the X, Y or Z axes. The length of the coordinate list is given by the attribute of that name. This may be used by software to allocate memory in advance of storing the coordinate values. The hasConstantOffset attribute may be used to indicate that the coordinate list consists of values with constant offset (spacing). In this case only the first coordinate value and the offset (spacing) value need to be specified; however, the length attribute must still define the final as-built size of the coordinate list.
    """
    def __init__(self):
        """Constructor.

        """
        super(CoordinateList, self).__init__()

        self.has_constant_offset = bool()            # type = bool
        self.length = int()                          # type = int
        self.uom = str()                             # type = str


class GridExtent(object):
    """A concrete class within the cim v1 type system.

    DataType for recording the geographic extent of a gridMosaic or gridTile.
    """
    def __init__(self):
        """Constructor.

        """
        super(GridExtent, self).__init__()

        self.maximum_latitude = str()                # type = str
        self.maximum_longitude = str()               # type = str
        self.minimum_latitude = str()                # type = str
        self.minimum_longitude = str()               # type = str
        self.units = str()                           # type = str


class GridMosaic(object):
    """A concrete class within the cim v1 type system.

    The GridMosaic class is used to define the geometry properties of an earth system model grid or an exchange grid. Such a grid definition may then be referenced by any number of earth system models. A GridMosaic object consists either of 1 or more child GridMosaics, or one or more child GridTiles, but not both. In the latter case the isLeaf property should be set to true, indicating that the mosaic is a leaf mosaic.
    """
    def __init__(self):
        """Constructor.

        """
        super(GridMosaic, self).__init__()

        self.citations = []                          # type = shared.Citation
        self.description = str()                     # type = str
        self.extent = None                           # type = grids.GridExtent
        self.has_congruent_tiles = bool()            # type = bool
        self.id = str()                              # type = str
        self.is_leaf = bool()                        # type = bool
        self.long_name = str()                       # type = str
        self.mnemonic = str()                        # type = str
        self.mosaic_count = int()                    # type = int
        self.mosaics = []                            # type = grids.GridMosaic
        self.short_name = str()                      # type = str
        self.tile_count = int()                      # type = int
        self.tiles = []                              # type = grids.GridTile
        self.type = str()                            # type = str


class GridProperty(shared.Property):
    """A concrete class within the cim v1 type system.

    
    """
    def __init__(self):
        """Constructor.

        """
        super(GridProperty, self).__init__()



class GridSpec(object):
    """A concrete class within the cim v1 type system.

    This is a container class for GridSpec objects. A GridSpec object can contain one or more esmModelGrid objects, and one or more esmExchangeGrid objects. These objects may be serialised to one or possibly several files according to taste. Since GridSpec is sub-typed from GML's AbstractGeometryType it can, and should, be identified using a gml:id attribute.
    """
    def __init__(self):
        """Constructor.

        """
        super(GridSpec, self).__init__()

        self.cim_info = None                         # type = shared.CimInfo
        self.esm_exchange_grids = []                 # type = grids.GridMosaic
        self.esm_model_grids = []                    # type = grids.GridMosaic


class GridTile(object):
    """A concrete class within the cim v1 type system.

    The GridTile class is used to model an individual grid tile contained within a grid mosaic. A GridTile consists of an array of grid cells which may be defined in one of four ways: 1) for simple grids, by use of the SimpleGridGeometry data type; 2) by defining an array of GridCell objects; 3) by specifying an array of references to externally defined GridCell objects; or 4) by specifying a URI to a remote data file containing the grid cell definitions.  For all but the simplest grid tiles, it is envisaged that method 4 above will be the most frequently used option. However, it should be remembered that the CIM is primarily concerned with encoding climate model metadata. Specifying the coordinates of individual grid tiles and cells will most likely not be required as part of such metadata descriptions.  A GridTile object is associated with a geodetic or projected CRS via the horizontalCRS property, and with a vertical CRS via the verticalCRS property.
    """
    def __init__(self):
        """Constructor.

        """
        super(GridTile, self).__init__()

        self.area = str()                            # type = str
        self.cell_array = str()                      # type = str
        self.cell_ref_array = str()                  # type = str
        self.coord_file = str()                      # type = str
        self.coordinate_pole = str()                 # type = str
        self.description = str()                     # type = str
        self.discretization_type = ''                # type = grids.DiscretizationEnum
        self.extent = None                           # type = grids.GridExtent
        self.geometry_type = ''                      # type = grids.GeometryTypeEnum
        self.grid_north_pole = str()                 # type = str
        self.horizontal_crs = str()                  # type = str
        self.horizontal_resolution = None            # type = grids.GridTileResolutionType
        self.id = str()                              # type = str
        self.is_conformal = bool()                   # type = bool
        self.is_regular = bool()                     # type = bool
        self.is_terrain_following = bool()           # type = bool
        self.is_uniform = bool()                     # type = bool
        self.long_name = str()                       # type = str
        self.mnemonic = str()                        # type = str
        self.nx = int()                              # type = int
        self.ny = int()                              # type = int
        self.nz = int()                              # type = int
        self.refinement_scheme = ''                  # type = grids.RefinementTypeEnum
        self.short_name = str()                      # type = str
        self.simple_grid_geom = str()                # type = str
        self.vertical_crs = str()                    # type = str
        self.vertical_resolution = None              # type = grids.GridTileResolutionType
        self.zcoords = None                          # type = grids.VerticalCoordinateList


class GridTileResolutionType(object):
    """A concrete class within the cim v1 type system.

    Provides a description and set of named properties for the horizontal or vertical resolution.
    """
    def __init__(self):
        """Constructor.

        """
        super(GridTileResolutionType, self).__init__()

        self.description = str()                     # type = str
        self.properties = []                         # type = grids.GridProperty


class VerticalCoordinateList(CoordinateList):
    """A concrete class within the cim v1 type system.

    There are some specific attributes that are associated with vertical coordinates.
    """
    def __init__(self):
        """Constructor.

        """
        super(VerticalCoordinateList, self).__init__()

        self.form = str()                            # type = str
        self.properties = []                         # type = grids.GridProperty
        self.type = str()                            # type = str


class DiscretizationEnum(object):
    """An enumeration within the cim v1 type system.

    
    """

    pass


class FeatureTypeEnum(object):
    """An enumeration within the cim v1 type system.

    
    """

    pass


class GeometryTypeEnum(object):
    """An enumeration within the cim v1 type system.

    
    """

    pass


class GridTypeEnum(object):
    """An enumeration within the cim v1 type system.

    
    """

    pass


class HorizontalCsEnum(object):
    """An enumeration within the cim v1 type system.

    
    """

    pass


class RefinementTypeEnum(object):
    """An enumeration within the cim v1 type system.

    
    """

    pass


class VerticalCsEnum(object):
    """An enumeration within the cim v1 type system.

    
    """

    pass


