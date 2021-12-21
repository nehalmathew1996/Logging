import logging

# Logging can be done to console , db or a file

# DEBUG(10) - 
# INFO(20) - Confirming everything is working as expected
# WARNING(30) - Software is working ok for now , But an indicates some error may occur in the future
# ERROR(40) - Some things could not be performed 
# CRITICAL(50) - A serious error, program maybe unable to continue running

formatter=logging.basicConfig(filename='test.log', level=logging.DEBUG,
    format='%(asctime)s : %(levelname)s : %(message)s : Hi')
    
    
    # %(levelname)s]: RBAC: V1: %(asctime)s:"
    #                           "%(module)s: %(funcName)s: %(message)s:", "%Y-%m-%d %H:%M:%S')


def add(x,y):
    return x+y

num1=10
num2=6

add_result=(add(num1,num2))
logging.debug('Add: {} + {} = {}'.format(num1,num2,add_result))


add_result=(add(num1,num2))

handler = logging.StreamHandler()
handler.setFormatter(formatter)
log = logging.getLogger(__name__)
log.addHandler(handler)
log.setLevel(logging.DEBUG)


