# -*- coding: utf-8 -*-

"""
.. module:: archive/manager.py
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Manages access to the document archive.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import os

from pyesdoc.archive import config
from pyesdoc.archive import constants
from pyesdoc.archive.file_info import ArchiveFileInfo
from pyesdoc.archive.folder_info import ArchiveFolderInfo


# Set of managed folders.
_FOLDERS = set()


def _create_folder(project, source):
    """Creates & returns a wrapped archive folder.

    """
    path = os.path.join(config.get_directory(), project)
    path = os.path.join(path, source)
    if not os.path.exists(path):
        os.makedirs(path)

    return ArchiveFolderInfo(project, source, path)


def init():
    """Initializes archive manager.

    """
    if not _FOLDERS:
        for project, source in config.get_project_sources():
            _FOLDERS.add(_create_folder(project, source))


def delete_error_files(project=None, source=None):
    """Deletes error files from archive.

    :param str project: Name of a supported project (e.g. cmip6).
    :param str source: Name of a document source (e.g. esdoc-q).

    """
    delete_files(project, source, constants.FILE_FILTER_ERROR)


def delete_ingested_files(project=None, source=None):
    """Deletes ingested files from archive.

    :param str project: Name of a supported project (e.g. cmip6).
    :param str source: Name of a document source (e.g. esdoc-q).

    """
    delete_files(project, source, constants.FILE_FILTER_INGESTED)


def delete_files(project=None, source=None, file_filter=None):
    """Deletes files from archive.

    :param str project: Name of a supported project (e.g. cmip6).
    :param str source: Name of a document source (e.g. esdoc-q).
    :param str file_filter: A file filter to apply.

    """
    for file_ in yield_files(project, source, file_filter):
        file_.delete()


def delete_folders(project=None, source=None):
    """Deletes folders from archive.

    :param str project: Name of a supported project (e.g. cmip6).
    :param str source: Name of a document source (e.g. esdoc-q).

    """
    delete_files(project, source)
    for folder in yield_folders(project, source):
        folder.delete()


def get_count(project=None, source=None, file_filter=None):
    """Returns archived document count.

    :param str project: Name of a supported project (e.g. cmip6).
    :param str source: Name of a document source (e.g. esdoc-q).
    :param str file_filter: A file filter to apply when deriving the count.

    :rtype: int

    """
    count = 0
    for folder in yield_folders(project, source):
        count += folder.get_count(file_filter)

    return count


def get_error_count(project=None, source=None):
    """Returns archived document error count.

    :param str project: Name of a supported project (e.g. cmip6).
    :param str source: Name of a document source (e.g. esdoc-q).

    :rtype: int

    """
    return get_count(project, source, constants.FILE_FILTER_ERROR)


def get_accepted_count(project=None, source=None):
    """Returns accepted archived document error count.

    :param str project: Name of a supported project (e.g. cmip6).
    :param str source: Name of a document source (e.g. esdoc-q).

    :rtype: int

    """
    return get_count(project, source, constants.FILE_FILTER_ACCEPTED)


def get_file(project, source, name, encoding):
    """Returns an archive file wrapper.

    :param str project: Name of a supported project (e.g. cmip6).
    :param str source: Name of a document source (e.g. esdoc-q).
    :param str name: File name.
    :param str encoding: File encoding.

    :returns: A file wrapper for processing.
    :rtype: pyesdoc.archive.ArchiveFileInfo

    """
    folder = get_folder(project, source)
    if not folder:
        raise ValueError("Archive folder could not be found.")
    path = os.path.join(folder.path, name)
    path = "{0}.{1}".format(path, encoding)

    return ArchiveFileInfo(folder, path)


def get_folder(project, source, create=False):
    """Returns an archive folder wrapper.

    :param str project: Name of a supported project (e.g. cmip6).
    :param str source: Name of a document source (e.g. esdoc-q).
    :param bool create: Flag indicating whether the folder should be created or not.

    :returns: A folder wrapper for processing.
    :rtype: pyesdoc.archive.ArchiveFolderInfo

    """
    for folder in _FOLDERS:
        if folder.project == project and folder.source == source:
            return folder

    if create:
        folder = _create_folder(project, source)
        _FOLDERS.add(folder)
        return folder


def yield_files(project=None, source=None, file_filter=None):
    """Yields files for processing.

    :param str project: Name of a supported project (e.g. cmip6).
    :param str source: Name of a document source (e.g. esdoc-q).
    :param str file_filter: A file filter to be applied.

    :returns: Set of files for processing.
    :rtype: generator

    """
    for folder in yield_folders(project, source):
        for file_ in folder.yield_files(file_filter):
            yield file_


def yield_folders(project=None, source=None):
    """Yields set of folders for processing.

    :param str project: Name of a supported project (e.g. cmip6).
    :param str source: Name of a document source (e.g. esdoc-q).

    :returns: Set of folders for processing.
    :rtype: generator

    """
    if project == "*":
        project = None
    if source == "*":
        source = None
    for folder in sorted(_FOLDERS, key=lambda f: f.path):
        if project and folder.project != project:
            continue
        if source and folder.source != source:
            continue
        yield folder


def find_file(uid, version):
    """Finds an archive file wrapper for processing.

    :param str uid: Document unique identifier.
    :param str version: Document version.

    :returns: A file wrapper to be processed.
    :rtype: pyesdoc.archive.ArchiveFileInfo

    """
    for folder in yield_folders():
        file_ = folder.find_file(uid, version)
        if file_:
            return file_


def file_exists(uid, version):
    """Returns flag indicating whether a matching archive file exists.

    :param str uid: Document unique identifier.
    :param str version: Document version.

    :returns: A flag indicating whether a matching archive file exists.
    :rtype: boolean

    """
    return find_file(uid, version) is not None


def delete_file(uid, version):
    """Deletes an archive file.

    :param str uid: Document unique identifier.
    :param str version: Document version.

    """
    file_ = find_file(uid, version)
    if file_:
        file_.delete()


def get_file_content(uid, version, encoding, must_exist=False):
    """Returns content of an archived file in the desired encoding.

    :param str uid: Document unique identifier.
    :param str version: Document version.

    :returns: The contents of an archived file in the desired encoding.
    :rtype: unicode

    """
    file_ = find_file(uid, version)
    if not file_ and must_exist:
        raise IOError("Document not found: {0}-{1}.".format(uid, version))
    if file_:
        return file_.get_content(encoding)


def get_file_document(uid, version, extend=True):
    """Returns document of an archived file.

    :param str uid: Document unique identifier.
    :param str version: Document version.
    :param bool extend: Flag instructing whether to extend document.

    :returns: A document loaded from an archived file.
    :rtype: object | null

    """
    file_ = find_file(uid, version)
    if file_:
        return file_.get_document(extend)


def delete(uid, version):
    """Deletes a document from archive.

    :param str uid: Document unique identifier.
    :param str version: Document version.

    """
    delete_file(uid, version)


def exists(uid, version):
    """Returns flag indicating whether a document is already archived.

    :param str uid: Document unique identifier.
    :param str version: Document version.

    :returns: Flag indicating whether a document is already archived.
    :rtype: boolean

    """
    return file_exists(uid, version)


def load(uid, version, encoding='json', must_exist=False):
    """Loads document content from archive.

    :param str uid: Document unique identifier.
    :param str version: Document version.
    :param bool must_exist: Flag indicating whether the document is expected to exist within the archive.

    :returns: Document content loaded from archive.
    :rtype: unicode | None

    """
    return get_file_content(uid, version, encoding, must_exist)


def load_reference(reference):
    """Loads a referenced document.

    """
    return load_references(reference)


def load_references(references):
    """Loads referenced documents.

    """
    def _load(ref):
        """Inner function to load document from archive.

        """
        try:
            ref.meta
        except AttributeError:
            return read(ref.id, ref.version)
        else:
            return ref

    try:
        iter(references)
    except TypeError:
        return _load(references)
    else:
        return [_load(i) for i in references]


def read(uid, version, extend=True):
    """Reads a document from archive.

    :param str uid: Document unique identifier.
    :param str version: Document version.
    :param bool extend: Flag instructing whether to extend document.

    :returns: A document.
    :rtype: object

    """
    return get_file_document(uid, version, extend)



def write(doc):
    """Writes a document to the archive.

    :param object doc: Document to be written.

    :returns: Pointer to archive file.
    :rtype: pyesdoc.archive.FileInfo

    """
    # Get associated archive folder.
    folder = get_folder(doc.meta.project, doc.meta.source, True)

    # Write document.
    return folder.write(doc)
