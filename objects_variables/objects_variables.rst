オブジェクトと変数
------------------

Restart python to empty the local namespace.

.. include:: objects_variables_a.code

Everything in Python is an object and has:

- a single id,
- a single value,
- some number of attributes (part of its value),
- a single type,
- (zero or) one or more names (in one or more namespaces),
-  and usually (indirectly), one or more base classes.

.. include:: objects_variables_b.code

演習:

It is suggested you restart python to empty the local namespace.

.. include:: objects_variables_c.code

辞書オブジェクト
----------------

.. include:: objects_variables_d.code

演習:

.. include:: objects_variables_e.code

ブロック、forループ
-------------------

.. include:: objects_variables_f.code

演習:

.. include:: objects_variables_g.code

高度な演習:

.. include:: objects_variables_h.code

イテレータ式、ジェネレータ式
----------------------------

- In a for loop the expression is evaluated to get an iterable, and then iter() is called to produce an iterator.
- The iterator's next() method is called repeatedly until StopIteration is raised
- iter(foo)

    - If foo.__iter__() exists it is called.
    - Else if foo.__getitem__() exists, calls it starting at zero, handles IndexError by raising StopIteration.

- Note: iter(callable, sentinel) behaves differently.

.. include:: objects_variables_i.code

演習:

.. include:: objects_variables_j.code
