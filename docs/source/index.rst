.. stdm2 documentation master file, created by
   sphinx-quickstart on Sat Apr 27 13:03:11 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to stdm2's documentation!
=================================

.. meta::
   :description lang=en: STDM User Manual and API Documentation.


`Read the Docs`_ simplifies software documentation
by automating building, versioning, and hosting of your docs for you.
Think of it as *Continuous Documentation*.

Never out of sync
    Whenever you push code to your favorite version control system,
    whether that is Git, Mercurial, Bazaar, or Subversion,
    Read the Docs will automatically build your docs
    so your code and documentation are always up-to-date.

Multiple versions
    Read the Docs can host and build multiple versions of your docs
    so having a 1.0 version of your docs and a 2.0 version
    of your docs is as easy as having a separate branch or tag in your version control system.

Free and open source
    Read the Docs is free and open source and hosts documentation
    for nearly 100,000 large and small open source projects
    in almost every human and computer language.

.. _Read the docs: http://readthedocs.org/


First steps
-----------

STDM 2.0 Documentation.

* **Getting started**:
  :doc:`User Manual` |
  :doc:`API Documentation`

* **Importing your existing documentation**:
  :doc:`Import guide`

.. toctree::
   :maxdepth: 2
   :hidden:
   :caption: First Steps

.. _user-docs:

.. toctree::
   :maxdepth: 2
   :caption: User Documentation
 

.. _api-docs:

.. toctree::
   :maxdepth: 2
   :caption: Contents:


TestAPI Plugin
=================================
.. automodule:: test_plugin
   :members:

TestAPI Primes
=================================
.. automodule:: test_primes
   :members:

.. autoclass:: PrimesTestCase
   :members: test_is_five_prime

Indices and tables
=================================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
