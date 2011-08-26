スクリプト、モジュールを書く
----------------------------

- Start with #!/usr/bin/env python
- Suffix .py (also .pyw on Windows)
- Python creates .pyc
- Use lowercase and valid python identifiers

play1.py:

.. literalinclude:: scripts_modules/play1.py
.. include:: scripts_modules_a.code

play2.py:

.. literalinclude:: scripts_modules/play2.py
.. include:: scripts_modules_b.code

play3.py:

.. literalinclude:: scripts_modules/play3.py
.. include:: scripts_modules_c.code

演習:

Edit your own play.py and load it.


関数の定義と呼び出し
--------------------

.. include:: scripts_modules_d.code

演習:

Define a function triple(n) in a module triple.py such that triple.triple(3) returns 9. Import triple and try it out.
Extend the plural function above to handle proper nouns (that start with a caiptal letter) that end in 'y', for example the correct plural of “Harry” is “Harrys”.
