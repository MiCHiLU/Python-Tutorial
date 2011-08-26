タプル、リスト
--------------

.. include:: tuples_lists_a.code

演習:

.. include:: tuples_lists_b.code

The reverse and sort methods mutate a list and return None.
The reversed and sorted functions don't mutate a sequence, and they return a new sequence (actually an iterator).

.. include:: tuples_lists_c.code

シーケンスのインデックスとスライス
----------------------------------

.. include:: tuples_lists_d.code

演習:

.. include:: tuples_lists_e.code

Note that indexing and slicing work on strings and tuples, too, but remember they are immutable.

リスト内包表記
--------------

.. include:: tuples_lists_f.code

演習:

.. include:: tuples_lists_g.code

加工して、並べ替えて、元に戻す
------------------------------

Decorate, Sort, Undecorate (DSU) Idiom

.. include:: tuples_lists_h.code

演習:

Use the DSU idiom to sort months alphabetically.
Use operator.itemgetter and sort's key parameter to sort months by the number of days in the
month.
