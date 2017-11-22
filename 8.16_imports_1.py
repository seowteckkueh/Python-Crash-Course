import module_name
ben=module_name.user('ben','kueh',color='blue',size=8)
print(ben)

from module_name import user
ben=module_name.user('ben','kueh',color='blue',size=8)
print(ben)

from module_name import user as fn
ben=fn('ben','kueh',color='blue',size=8)
print(ben)

import module_name as mn
ben=mn.user('ben','kueh',color='blue',size=8)
print(ben)

from module_name import *
ben=user('ben','kueh',color='blue',size=8)
print(ben)


