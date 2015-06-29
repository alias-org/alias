import alias as al

af = al.ArgumentationFramework()
af.add_argument('a')
af.add_argument('b')
af.add_argument('c')
print af.get_arguments()
af.add_attack('a', 'b')
af.add_attack('b', 'c')
print af.get_attacks()
allin = al.all_in(af)
al.preffered_labellings(af)