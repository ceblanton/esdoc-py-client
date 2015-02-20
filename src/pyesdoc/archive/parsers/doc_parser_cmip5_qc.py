# -*- coding: utf-8 -*-
"""
.. module:: handlers_dkrz_qc.py
   :copyright: @2013 Earth System Documentation (http://es-doc.org)
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Exposes DKRZ QC document processing handlers.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""



def get_parsers():
    """Returns set of document parsers."""
    return _set_institute


def _set_institute(doc):
    """Sets institute code."""
    # Escape if no external id has been defined.
    if len(doc.meta.external_ids) == 0:
        return

    # Derive DRS.
    drs = doc.meta.external_ids[0].value
    drs = drs.split('.')[2:]

    # Derive institute from DRS.
    if len(drs) > 0:
        doc.meta.institute = drs[0].upper()

