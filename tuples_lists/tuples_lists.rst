タプル、リスト
--------------

.. include:: tuples_lists_a.code

演習:

.. include:: tuples_lists_b.code

reverse と sort メソッドは、リストオブジェクトを操作し返り値を返しません。
逆に、reversed と sorted 関数は、与えられたリストオブジェクトはそのままにし、新しいシーケンス（実際にはジェネレータ）を返り値として返します。

.. include:: tuples_lists_c.code

シーケンスのインデキシングとスライシング
----------------------------------------

.. include:: tuples_lists_d.code

演習:

.. include:: tuples_lists_e.code

インデキシングとスライシング操作をする場合は、文字列とタプルは不変オブジェクトであることに気をつけましょう。

リスト内包表記
--------------

.. include:: tuples_lists_f.code

演習:

.. include:: tuples_lists_g.code

加工して、並べ替えて、元に戻す
------------------------------

Decorate, Sort, Undecorate (DSU) Idiom

.. include:: tuples_lists_h.code

.. 演習:
..
..   Use the DSU idiom to sort months alphabetically.
..   Use operator.itemgetter and sort's key parameter to sort months by the number of days in the
..   month.
