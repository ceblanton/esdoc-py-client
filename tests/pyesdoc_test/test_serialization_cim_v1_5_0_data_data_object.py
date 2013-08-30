"""
.. module:: test_decoding_cim_v1_5_0_data_data_object.py
   :copyright: Copyright "Aug 7, 2013", Earth System Documentation
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Tests a cim v1.5.0 data data object document.

.. moduleauthor:: Mark Conway-Greenslade (formerly Morgan) <momipsl@ipsl.jussieu.fr>


"""
# Module imports.
import nose
import uuid

from dateutil import parser as dateutil_parser

import pyesdoc.ontologies.cim as cim
import pyesdoc_test.test_utils as tu



# Test type.
_TEST_TYPE = cim.v1.DataObject

# Test representation file.
_TEST_FILE = 'cim/v1_5_0/data.data_object.xml'


def test_open_test_file():
    assert tu.get_test_file(_TEST_FILE) is not None


def test_decode_from_xml_metafor_cim_v1():
    obj = tu.decode_from_xml_metafor_cim_v1(_TEST_FILE, _TEST_TYPE)

    tu.assert_pyesdoc_obj(obj, '834151a4-978d-4627-954e-285916bb907a', '1', '2011-09-28T16:08:41')

    assert obj.acronym == 'HADGEM2_20C3M_1_D0_hus700'
    assert obj.child_object == []
    for i in range(1):
        c = obj.citations[i]
        assert c is not None
        assert isinstance(c, cim.v1.Citation)
        assert c.title.startswith(str(i + 1) + ' - ')
        assert c.date == dateutil_parser.parse('2009-02-11')
    assert len(obj.content) == 1
    assert obj.content[0].aggregation == 'sum'
    assert obj.content[0].frequency == 'Other'
    assert obj.content[0].topic.name == 'specific_humidity'
    assert obj.content[0].topic.description.find('specific" means per unit mass') >= 0
    assert obj.content[0].topic.unit == 'm s-1'
    for i in range(1):
        dp = obj.data_property[i]
        assert isinstance(dp, cim.v1.DataProperty)
        assert dp.name == 'TestProperty' + str(i + 1)
        assert dp.value == str(i + 1)
    assert obj.data_status == 'complete'
    assert obj.description.startswith('This dataset represents daily output: instantaneous daily')
    assert obj.distribution.access == 'OnlineFileHTTP'
    assert obj.distribution.format == 'NetCDF'
    assert obj.distribution.responsible_party.individual_name == 'Met Office (HC)'
    assert obj.distribution.responsible_party.organisation_name == 'Hadley Centre'
    assert obj.distribution.responsible_party.role == 'distributor'
    assert obj.extent.geographical.east == float(360)
    assert obj.extent.geographical.south == float(-90)
    assert obj.extent.geographical.west == float(0)
    assert obj.extent.geographical.north == float(90)
    assert obj.extent.temporal.begin == dateutil_parser.parse('1859-12-1')
    assert obj.extent.temporal.end == dateutil_parser.parse('1999-12-30')
    assert obj.extent.temporal.time_interval.factor == int(-1)
    assert obj.extent.temporal.time_interval.radix == int(50430)
    assert obj.extent.temporal.time_interval.unit == 'day'
    # TODO set type correctly
    # assert obj.geometry_model is None
    assert obj.hierarchy_level.name == 'experiment'
    assert obj.hierarchy_level.value == 'HADGEM2_20C3M_1_D0_hus700'
    assert obj.hierarchy_level.is_open == True
    assert obj.keyword == 'Test keyword'
    assert obj.parent_object is None
    assert obj.parent_object_reference is None
    assert obj.purpose == 'test'
    assert len(obj.restriction) == 0
    # TODO set type correctly
    # assert obj.source_simulation is None
    assert len(obj.storage) == 0


@nose.tools.raises(NotImplementedError)
def test_encode_xml_metafor_cim_v1():
    doc = tu.decode_from_xml_metafor_cim_v1(_TEST_FILE, _TEST_TYPE)

    tu.encode_to_xml_metafor_cim_v1(doc)


def test_decode_dict():
    doc1 = tu.decode_from_xml_metafor_cim_v1(_TEST_FILE, _TEST_TYPE)

    as_dict = tu.encode_to_dict(doc1)

    doc = tu.decode_from_dict(as_dict)


def test_encode_dict():
    doc = tu.decode_from_xml_metafor_cim_v1(_TEST_FILE, _TEST_TYPE)

    d = tu.encode_to_dict(doc)
    assert d['cim_info']['id'] == uuid.UUID('834151a4-978d-4627-954e-285916bb907a')

    assert d['acronym'] == 'HADGEM2_20C3M_1_D0_hus700'
    assert len(d['content']) == 1
    assert d['extent']['temporal']['begin'] == dateutil_parser.parse('1859-12-1')


def test_decode_json():
    doc1 = tu.decode_from_xml_metafor_cim_v1(_TEST_FILE, _TEST_TYPE)

    as_json = tu.encode_to_json(doc1)

    doc = tu.decode_from_json(as_json)


def test_encode_json():
    doc = tu.decode_from_xml_metafor_cim_v1(_TEST_FILE, _TEST_TYPE)

    tu.encode_to_json(doc)


@nose.tools.raises(NotImplementedError)
def test_decode_xml():
    doc1 = tu.decode_from_xml_metafor_cim_v1(_TEST_FILE, _TEST_TYPE)

    as_xml = tu.encode_to_xml(doc1)

    doc = tu.decode_from_xml(as_xml)


def test_encode_xml():
    doc = tu.decode_from_xml_metafor_cim_v1(_TEST_FILE, _TEST_TYPE)

    tu.encode_to_xml(doc)

