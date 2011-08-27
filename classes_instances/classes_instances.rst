クラスとインスタンス
--------------------

名前空間とは、Pythonオブジェクトへマッピングされた名前です。
スコープとは、検索可能な名前空間の範囲です。
名前空間を検索する順は、:

1. ローカル変数、関数定義の中
2. モジュール、グローバル変数
3. ビルトイン(built-ins)

名前空間の変更（代入、import、def、del）は、ローカルスコープでおこなわれます。
参照: http://docs.python.org/tutorial/classes.html#python-scopes-and-name-spaces

- クラス文は、新しい名前空間を作成し、名前の割り当てはクラスのオブジェクトへバインドされます
- インスタンスは、 `ClassName()` または `ClassName(parameters)` を呼び出すことによって作成されます

point1.py:

.. literalinclude:: scripts/point1.py

.. include:: classes_instances_a.code

演習:

Write a class Employee that tracks first name, last name, age, and manager.

Review: Classes

- Class creates a new namespace and a new class object, and wires them for inheritance.
- クラスオブジェクトを呼び出すと、インスタンスを生成します。
- If attribute lookup finds a method then a method object is returned. It handles sending self to the function.
- クラスは、単純なレコードとして使用することができます。
- モジュールおよび関数も、属性を持つことができます。
