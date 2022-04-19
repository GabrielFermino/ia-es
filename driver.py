from pickle import TRUE
import sys
import os
import shutil
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

    print("Animal nao encontrado") #printa a mesma quantidade de vezes que o sistema executa de forma certa

# shutil.rmtree('./compiled_krb')
# driver.bc_test_question()