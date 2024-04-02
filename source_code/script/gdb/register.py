import yaml

TEST_ARCH=[
    {'name': 'eax', 'width': 32}, 
    {'name': 'ecx', 'width': 32},
    {'name': 'edx', 'width': 32}, 
    {'name': 'ebx', 'width': 32}, 
    {'name': 'esp', 'width': 32}, 
    {'name': 'ebp', 'width': 32}, 
    {'name': 'esi', 'width': 32}, 
    {'name': 'edi', 'width': 32}, 
    {'name': 'eip', 'width': 32}, 
    {'name': 'eflags', 'width': 32}, 
    {'name': 'cs', 'width': 32}, 
    {'name': 'ss', 'width': 32}, 
    {'name': 'ds', 'width': 32}, 
    {'name': 'es', 'width': 32}, 
    {'name': 'fs', 'width': 32}, 
    {'name': 'gs', 'width': 32}    
]

REG_MAP={
    'TEST_ARCH':TEST_ARCH
}

def get_resgiter_info(**args):
    arch=args['arch']
    register_info=REG_MAP['TEST_ARCH']
    return register_info

if __name__=='__main__':
    print(get_resgiter_info(arch='TEST_ARCH'))