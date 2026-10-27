from sympy import symbols, Symbol
from sympy.logic.boolalg import Implies, And, Or, Not
from sympy.logic.inference import satisfiable

is_ai_student_alice = Symbol('is_ai_student_alice')
takes_math_alice    = Symbol('takes_math_alice')
passes_exam_alice   = Symbol('passes_exam_alice')

is_ai_student_bob = Symbol('is_ai_student_bob')
takes_math_bob    = Symbol('takes_math_bob')
passes_exam_bob   = Symbol('passes_exam_bob')

rule1_alice = Implies(is_ai_student_alice, takes_math_alice)
rule2_alice = Implies(And(is_ai_student_alice, takes_math_alice), passes_exam_alice)

rule1_bob   = Implies(is_ai_student_bob, takes_math_bob)
rule2_bob   = Implies(And(is_ai_student_bob, takes_math_bob), passes_exam_bob)

fact_1 = is_ai_student_alice
fact_2 = Not(is_ai_student_bob)

knowledge_base = And(
    rule1_alice, rule2_alice,
    rule1_bob, rule2_bob,
    fact_1, fact_2
)

def prove_query(kb, query):
    test_formula = And(kb, Not(query))
    result = satisfiable(test_formula)

    if result is False:
        return "PROVEN TRUE (Unsatisfiable counter-example)"
    else:
        return f"CANNOT PROVE / FALSE (Satisfying Assignment found: {result})"

print("--- Automated Logic Inference ---")
print("Query 1: Does Alice pass the exam?")
print("Result:", prove_query(knowledge_base, passes_exam_alice))

print("\nQuery 2: Does Bob pass the exam?")
print("Result:", prove_query(knowledge_base, passes_exam_bob))
