import code
import doctest
import sys

file_list = """\
numbers/numbers_a.code
strings/strings_a.code
strings/strings_c.code
strings/strings_unicode.code
strings/strings_e.code
strings/strings_g.code
tuples_lists/tuples_lists_a.code
tuples_lists/tuples_lists_d.code
tuples_lists/tuples_lists_f.code
tuples_lists/tuples_lists_h.code
objects_variables/objects_variables_a.code
objects_variables/objects_variables_b.code
objects_variables/objects_variables_d.code
objects_variables/objects_variables_i.code
scripts_modules/scripts_modules_a.code
scripts_modules/scripts_modules_b.code
scripts_modules/scripts_modules_c.code
scripts_modules/scripts_modules_d.code
generators/generators_a.code
generators/generators_c.code
generators/generators_d.code
"""
#objects_variables/objects_variables_f.code
#generators/generators_b.code
#generators/generators_e.code
#classes_instances/classes_instances_a.code
#exceptions/exceptions_a.code

sys.path.append("scripts")

lines_all = []
for file_name in file_list.splitlines():
    lines = "".join(open(file_name).readlines())
    lines_all.extend(doctest.script_from_examples(lines).splitlines())
ones_set = []
one = []
for line in lines_all:
    if line.strip().startswith("#"): continue
    if not line.startswith(" ") and one:
        ones_set.append(one)
        one = []
    one.append(line)
else:
    ones_set.append(one)

console = code.InteractiveConsole()
for one in ones_set:
    for line in one:
        if line.startswith(" "):
            print "...",
        else:
            print ">>>",
        console.raw_input(line)
    for line in one:
        console.push(line)
    else:
        console.push("")

if __name__ == "__main__":
    pass
