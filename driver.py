import sys
import os
import shutil
from pyke import knowledge_engine, krb_traceback

engine = knowledge_engine.engine(__file__)


# def bc_test():
#     engine.reset()

#     engine.activate('rules')

#     try:
#         with engine.prove_goal('rules.animal_class($class)') as gen:
#             for vars, plan in gen:
#                 print("O animal é: %s" % (vars['class']))

#     except Exception:

#         krb_traceback.print_exc()
#         sys.exit(1)

#     print("Programa Finalizado!")


def bc_test_question():
    engine.reset()

    engine.activate('more_rules')

    try:
        with engine.prove_goal('more_rules.animal_class($class)') as gen:
            for vars, plan in gen:
                print("O animal é um exemplo de %s!!" % (vars['class']))
                input("Press Enter to continue...")
                os.system('cls')
                bc_test_question()

    except:
        krb_traceback.print_exc()
        sys.exit(1)

    print("Programa Finalizado!")


# shutil.rmtree('./compiled_krb')
# driver.bc_test_question()