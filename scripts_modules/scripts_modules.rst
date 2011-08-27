スクリプト、モジュールを書く
----------------------------

- `#!/usr/bin/env python` を1行目に書きます
- 拡張子は、 `.py`
- 高速に実行するため `.pyc` が生成されます

play1.py:

.. literalinclude:: scripts/play1.py
.. include:: scripts_modules_a.code

play2.py:

.. literalinclude:: scripts/play2.py
.. include:: scripts_modules_b.code

play3.py:

.. literalinclude:: scripts/play3.py
.. include:: scripts_modules_c.code

演習:

`play.py` を作成して、モジュールをロードし、実行してみましょう。

関数の定義と呼び出し
--------------------

.. include:: scripts_modules_d.code

演習:

Define a function triple(n) in a module triple.py such that triple.triple(3) returns 9. Import triple and try it out.
Extend the plural function above to handle proper nouns (that start with a caiptal letter) that end in 'y', for example the correct plural of “Harry” is “Harrys”.
