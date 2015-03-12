.. contents::

Introduction
============

`ploneintranet.core` provides shared functionality for the suite of ploneintranet packages.

It has two install profiles:

- `minimal` will install several browser views that are re-used in ploneintranet

- `default` extends `minimal` and additionally loads patternslib javascript and css bundles

If you want to use your own provided javascript and css, run only the `minimal` profile.
If you don't know what patternslib is, run the `default` profile.

Developer note
--------------

The stylesheets and javascripts in the `default` profile are copied over from `ploneintranet.theme_`.

To refresh those, run `make sync` and commit the changes.


Copyright (c) Plone Foundation
------------------------------

This package is Copyright (c) Plone Foundation.

Any contribution to this package implies consent and intent to irrevocably transfer all
copyrights on the code you contribute, to the `Plone Foundation`_,
under the condition that the code remains under a `OSI-approved license`_.

To contribute, you need to have signed a Plone Foundation `contributor agreement`_.
If you're `listed on Github`_ as a member of the Plone organization, you already signed.

.. _Plone Foundation: https://plone.org/foundation
.. _OSI-approved license: http://opensource.org/licenses
.. _contributor agreement: https://plone.org/foundation/contributors-agreement
.. _listed on Github: https://github.com/orgs/plone/people
