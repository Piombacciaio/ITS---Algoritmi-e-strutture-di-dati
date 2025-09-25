import Lezione2.Modules.for_module as for_loop
import Lezione2.Modules.while_module as while_loop
import Lezione2.Modules.ifelse as if_else
import Lezione2.Modules.pass_module as pass_module
import Lezione2.Modules.stringhe as stringhe

lista_opzioni = [
    "Scegli un opzione:\n"
    "1. For\n",
    "2. While\n",
    "3. If-Else\n",
    "4. Pass\n",
    "5. Stringhe\n",
    "99. Exit\n"
]

lista_funz = {
    1: for_loop.main,
    2: while_loop.main,
    3: if_else.main,
    4: pass_module.main,
    5: stringhe.main
}