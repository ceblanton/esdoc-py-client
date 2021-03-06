# -*- coding: utf-8 -*-

"""
.. module:: designing_numerical_experiment.py
   :platform: Unix, Windows
   :synopsis: Extends a cim.v1.designing.numerical_experiment document.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
from pyesdoc.constants import VIEWER_URL_BY_ID
from pyesdoc.ontologies import cim



def get_extenders():
    """Returns set of extension functions.

    """
    return (
        _set_viewer_urls,
        _set_summary_fields
        )


def _set_viewer_urls(ctx):
    """Sets related experiment viewer urls.

    """
    for i in ctx.doc.related_experiments + ctx.doc.related_mips:
        try:
            i.meta
        except AttributeError:
            i.viewer_url = VIEWER_URL_BY_ID.format(ctx.meta.project, i.id, i.version)
        else:
            i.viewer_url = VIEWER_URL_BY_ID.format(ctx.meta.project, i.meta.id, i.meta.version)


def _set_summary_fields(ctx):
    """Sets related experiment viewer urls.

    """
    ctx.ext.summary_fields += (
        ctx.doc.canonical_name,
        ctx.doc.name,
        ctx.doc.long_name
    )

