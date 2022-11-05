from applicaton.salary import calc_salary
from applicaton.db.people import  get_employess
from datetime import datetime
import heroes


if __name__ == '__main__':
    calc_salary()
    get_employess()
    print(datetime.today())
    print(heroes.genarr(9))


