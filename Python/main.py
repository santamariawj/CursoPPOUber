from car import Car
from account import Account
from uberPool import UberPool
from uberX import UberX
from uberVan import UberVan
from uberBlack import UberBlack

if __name__ == "__main__":
    print("Hola mundo");
    car = Car("AMS234", Account("Andres Herrera","NPI1234"));
    print(vars(car));
    print(vars(car.driver));

    car2 = Car("QWY654", Account("Manuel Carmona", "NPI5678"))
    print(vars(car2));
    print(vars(car2.driver));

    uberX = UberX("YTG78I", Account("Melende Melona", "NPI90765"), "Chevrolet", "Onix");
    print(vars(uberX));
    print(vars(uberX.driver));
