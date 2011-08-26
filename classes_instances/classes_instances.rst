クラスとインスタンス
--------------------

A namespace is a mapping from names to objects.
A scope is a section of Python text where a namespace is directly accessible. The namespace search
order is:

1. locals, enclosing functions (or module if not in a function)
2. module, including global
3. built-ins

All namespaces changes (assignment, import, def, del) happen in the local scope.
See http://docs.python.org/tutorial/classes.html#python-scopes-and-name-spaces

- The class statement creates a new namespace and all its name assignments (e.g. function defi- nitions) are bound to the class object.
- Instances are created by "calling" the class as in ClassName() or ClassName(parameters)

point1.py:

.. literalinclude:: scripts/point1.py

.. include:: classes_instances_a.code

演習:

Write a class Employee that tracks first name, last name, age, and manager.

Review: Classes

- Class creates a new namespace and a new class object, and wires them for inheritance.
- Calling the class object creates an instance.
- If attribute lookup finds a method then a method object is returned. It handles sending self to the function.
- Classes can be used as simple records.
- Modules and functions can also have attributes.
