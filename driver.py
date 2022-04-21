import sys
import os
from pyke import knowledge_engine, krb_traceback

engine = knowledge_engine.engine(__file__)

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

    for x in range (0,1):
        print("Animal nao encontrado")

# driver.bc_test_question()