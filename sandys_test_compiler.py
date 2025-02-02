from ast import *
from compiler import *
from utils import repr_Module
import type_check_Pif
import type_check_Pwhile
import type_check_Cwhile

import type_check_Ltup
import type_check_Ctup
import interp_Ltup
import interp_Ctup

import type_check_Lfun
import type_check_Cfun
import interp_Lfun
import interp_Cfun

import interp_Pwhile
import interp_Pif
import interp_Cif
import interp_Pvar
from interp_x86 import eval_x86

# test program here
# prog = """
# a = 20 + - 30
# b = input_int() + 10 + 20
# print(a + b + 60)
# """

# prog = """
# v = 1
# w = 42
# x = v + 7
# y = x
# z = x + w
# print(z + -y )
# """

# prog = """
# a = 5
# b = 30
# c = a
# b = 10
# c = c + b
# """

# prog = """
# x1 = input_int()
# x2 = input_int()
# x3 = input_int()
# x4 = input_int()
# x5 = input_int()
# x6 = input_int()
# x7 = input_int()
# x8 = input_int()
# x9 = input_int()
# x10 = input_int()
# x11 = input_int()
# x12 = input_int()
# x13 = input_int()
# x14 = input_int()
# x15 = input_int()
# x16 = input_int()
# print(x1 + - x2 + x3 + - x4 + x5 + - x6 + x7 + - x8 + x9 + - x10 + x11 + - x12 + x13 + - x14 + x15 + - x16 + 42)
# """
# prog =  """
# x = input_int()
# y = input_int()
# if Constant(False) Or() Compare(Name('x'), [<ast.NotEq object at 0x7fe82dc85ea0>], [Name('y')]) And() Compare(Name('x'), [Eq()], [Name('y')]) Or() Constant(True):
#     u = x < y
#     v = x <ast.LtE object at 0x7fe82dc85f60> y
#     w = x > y
#     z = x <ast.GtE object at 0x7fe82dc86020> y
# else:
#     u = True
#     v = True
#     w = True
#     z = True

# print((x - y if not Name('u') And() Name('v') else 0))
# """

# prog = """
# x1 = 1
# x2 = 2
# x3 = 3
# x4 = 4
# x5 = 5
# x6 = 6
# x7 = 7
# x8 = 8
# x9 = 9
# x10 = 10
# x11 = 11
# x12 = 12
# x13 = 13
# x14 = 14
# x15 = 15
# x16 = 16
# print(x1 + - x2 + x3 + - x4 + x5 + - x6 + x7 + - x8 + x9 + - x10 + x11 + - x12 + x13 + - x14 + x15 + - x16 + 42)
# """


# prog = """
# pyc_temp_var_0 = input_int()
# pyc_temp_var_3 = 42 if (input_int() == 0 if pyc_temp_var_0 == 1 else input_int() == 2) else 777
# print(pyc_temp_var_3)
# """

# pyc_temp_var_0 = input_int()
# pyc_temp_var_3 = (10 + 32 if (let Name('pyc_temp_var_1') = Call(Name('input_int'), []) in Compare(Name('pyc_temp_var_1'), [Eq()], [Constant(0)]) if pyc_temp_var_0 == 1 else let Name('pyc_temp_var_2') = Call(Name('input_int'), []) in Compare(Name('pyc_temp_var_2'), [Eq()], [Constant(2)])) else 700 + 77)
# print(pyc_temp_var_3)

# prog = """
# pyc_temp_var_0 = (42 if 2 > 1 else 0)
# print(pyc_temp_var_0)
# """

# prog = """
# x = 1
# y = 1
# if False or x!= y and x == y or True:
#   u = x < y
#   v = x <= y
#   w = x > y
#   z = x >= y
# else:
#   u = True
#   v = True
#   w = True
#   z = True

# print((x +- y if not u and v else 0))
# """

# test program here
# prog = """
# a = 20 + - 30
# b = input_int() + 10 + 20
# print(a + b + 60)
# """

# prog = """
# v = 1
# w = 42
# x = v + 7
# y = x
# z = x + w
# print(z + -y )
# """

# prog = """
# x = input_int()
# y = input_int()
# print(x + -y)
# """

# prog = """
# a = 5
# b = 30
# c = a
# b = 10
# c = c + b
# """

# prog = """
# x1 = input_int()
# x2 = input_int()
# x3 = input_int()
# x4 = input_int()
# x5 = input_int()
# x6 = input_int()
# x7 = input_int()
# x8 = input_int()
# x9 = input_int()
# x10 = input_int()
# x11 = input_int()
# x12 = input_int()
# x13 = input_int()
# x14 = input_int()
# x15 = input_int()
# x16 = input_int()
# print(x1 + - x2 + x3 + - x4 + x5 + - x6 + x7 + - x8 + x9 + - x10 + x11 + - x12 + x13 + - x14 + x15 + - x16 + 42)
# """



IfElseProg = """
x = 1
y = 1
if x == y:
    print (x + 5)
else:
    print (y + 7)
print(x + y)
"""

# nestedIfsProg = """
# x = 0
# if not x == 1:
#     if x == 0:
#       y = 42
#     else:
#         y = 777
# else:
#   y = 0

# print(y)
# """

nestedIfsProg2 = """
x = 1
y = 10
z = True and x == 1
print(y + 2 if (x == 0 if x < 1 else x == 2) else y + 10)
"""
# weirdCase = """
# x = 0
# y = 1 and 0
# if x == 1 == false:
#     print(666)
# else:
#     print(80085)
# """

whileCaseFromBook = """
sum = 0
i = 5
while i > 0:
    sum = sum + i
    i = i - 1
print(sum)
"""
while_while = """
sum = 0
m = 3
n = 4
i = 1
while i < m:
    j = 1
    while j < n:
        sum = sum + i + j
        j = j + 1
    i = i + 1

print(sum)
"""

while_if = """
x = 0
while (True if input_int() == 5 else False):
    x = x + 42

print(x)
"""

while_from_class = """
sum = 0
i = 5
while i > 0:
	sum = sum + i
	i = i - 1
print(sum)
"""

simple_tuple = """
print( ((42,),)[0][0] )
"""

simple_tuple2 = """
print(8)
t1 = (1,2,3)
print(7)
"""

just_zero = """
if True:
    0
else:
    print(7)
"""

complex_touple_from_p80_of_book = """
t1 = 3, 7
t2 = t1
t3 = 3, 7
print( 42 if (t1 is t2) and not (t1 is t3) else 0)
"""

simple_function = """

def sum(a:int,b:int,c:int,d:int,e:int,f:int,g:int,h:int)-> int :
    return a + b + c + d + e + f + g + h

print(sum(5, 5, 5, 5, 5, 5, 5, 7))

"""

collect_in_function = """
def g(x:int)-> int :
    v = (0,1,2,3,4,5,6,7,8,9,)
    if x == 0:
        return 0
    else:
        return g(x - v[1])
n = input_int()
w = (0,1,2,3,4,5,6,7,8,9,)
y = g(10)
print(y + w[0] + n)
"""

function_with_tuple = """
def id(x:int)-> int :
    return x
def f(n:int, clos:tuple[(Callable[([int],int,)],tuple[(int,)],)])-> int:
    if n == 1:
        return clos[0](clos[1][0])
    else:
        clos2 = (clos[0],clos[1],)
        return f(n + 1, clos2)
n = 4
print(f(0, (id,(n,),)))
"""

example_simple_function = """
def add(x:int,y:int)-> int :
	return x + y
print(add(40, 2))
"""

call_in_cond = """
def greaterThanThree(x: int) -> bool:
    if x > 3:
        return True
    else:
        return False

if greaterThanThree(7):
    print(666)
else:
    print(2)
"""

tail_if_fun = """
def sum(x:int,s:int)-> int :
    return (s if x == 0 else sum(x - 1, x + s))
n = 7
print(sum(n, 0) + 36)
"""

def sum(x:int,s:int)-> int :
    return (s if x == 0 else sum(x - 1, x + s))
n = 7
print(sum(n, 0) + 36)


progs = [IfElseProg, nestedIfsProg2, whileCaseFromBook, while_while, while_from_class, simple_tuple]

prog = tail_if_fun


############################################################################
# Run
############################################################################

interp = interp_Lfun.InterpLfun()
# interp = interp_Ltup.InterpLtup()
# interp = interp_Pif.InterpPif()
# interp = interp_Pvar.InterpPvar()

def run1(prog):

    p = parse(prog)

    print("\n======= AST of the original program")
    print(p)

    type_check_Lfun.TypeCheckLfun().type_check(p)
    print("\n======= type check passes")

    # print("\n======= interpreting original program")
    # interp.interp(p)

    compiler = Compiler()

    print("\n======= shrinked program")
    p_shrinked = compiler.shrink(p)
    print(p_shrinked)
    print("\n======= interpreting shrinked program")
    interp.interp(p_shrinked)

    print("\n======= reveal functions")
    p_revealed = compiler.reveal_functions(p_shrinked)
    print(p_revealed)

    print("\n======= reveal functions AST")
    print(ast.dump(p_revealed))

    print("\n======= interpreting revealed functions program")
    interp.interp(p_revealed)

    print("\n======= limit functions")
    p_limited = compiler.limit_functions(p_revealed)
    print(p_limited)

    print("\n======= limit functions AST")
    print(ast.dump(p_limited))

    print("\n======= interpreting limit functions program")
    interp.interp(p_limited)
    type_check_Lfun.TypeCheckLfun().type_check(p_limited)

    print("\n======= doing RCO")
    p_rcoed = compiler.remove_complex_operands(p_limited)

    print("\n======= RCOed program AST")
    print(ast.dump(p_rcoed))

    print("\n======= printing RCOed program")
    print(p_rcoed)

    print("\n======= interpreting RCOed program")
    interp.interp(p_rcoed)


    print("\n======= explicate control")
    p_exped = compiler.explicate_control(p_rcoed)
    print("\n======= printing EXPed program")
    print(p_exped)

    print("\n======= type checking EXPed program")
    type_check_Cfun.TypeCheckCfun().type_check(p_exped)


    print("\n======= interpreting EXPed program")
    cif_interp = interp_Cfun.InterpCfun()
    cif_interp.interp(p_exped)

    print("\n======= selecting instructions")
    p_x64 = compiler.select_instructions(p_exped)
    print(p_x64)

    # print("\n======= evaluating x86 program")
    # eval_x86.interp_x86(p_x64)

    # print("\n======= uncovering live after sets")
    # las = compiler.uncover_live(p_x64)
    # for (label, block) in p_x64.body.items():
    #     print(label)
    #     for s in block:
    #         print(repr(s) + '\t' + str(las[s]))

    # print("\n======= building interference graph")
    # las_dict = compiler.uncover_live(p_x64)
    # rv = compiler.build_interference(las_dict)
    # print(compiler.int_graph.show())

    # print("\n======= building move graph")
    # rv = compiler.build_move_graph(p_x64.body)
    # print(compiler.move_graph.show())

    # print("\n======= graph coloring")
    # coloring = compiler.color_graph(compiler.int_graph)
    # print(coloring)

    print("\n======= assigning homes")
    p_x64_reg = compiler.assign_homes(p_x64)
    print(p_x64_reg)

    # print("\n======= evaluating x86 program")
    # eval_x86.interp_x86(p_x64_reg)

    print("\n======= patching instructions")
    p_x64_patched = compiler.patch_instructions(p_x64_reg)
    print(p_x64_patched)

    print("\n======= geenrating prelude and conclusion")
    p_x64_final = compiler.prelude_and_conclusion(p_x64_patched)
    print(p_x64_final)

def runAll():
    for prog in progs:
        print("\n############################ New Program ############################")
        print(prog)
        print("#####################################################################")

        run1(prog)

# def runPrelude():
#     p = parse(simple_tuple2)
#     compiler = Compiler()
# print('error in rco_exp, unsupported expression ' + repr(BoolOp(And(), [Name('u'), Name('v')])))
# print('error in rco_exp, unsupported expression ' + repr(Compare(Name('x'), [Name('z')], [Name('y')])))
# print('error in rco_exp, unsupported expression ' + repr(BoolOp(Name('And()'), [Name("Name('u')"), Name("Name('v')")])))

############################################################################
# Start
############################################################################

run1(prog)
# runAll()

