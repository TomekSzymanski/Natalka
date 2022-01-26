yearly_salary = 100000

FIRST_RANGE_END = 85528
FIRST_TAX_RATE = 17
SECOND_TAX_RATE = 32
if (yearly_salary <= FIRST_RANGE_END):
    print(yearly_salary * FIRST_TAX_RATE / 100)
if (yearly_salary > FIRST_RANGE_END):
    do_pierwszego_progu = FIRST_RANGE_END * FIRST_TAX_RATE / 100
    nadwyzka = yearly_salary - FIRST_RANGE_END
    print(do_pierwszego_progu + nadwyzka * SECOND_TAX_RATE / 100)