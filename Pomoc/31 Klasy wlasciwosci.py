class kontoBankowe:
    __stan = 0

    @property     # Działa jako zmienna tylko do odczytu (właściwość) a nie funkcja bez ()
    def stan_konta(self):
        return  self.__stan

    @stan_konta.getter    # getter służy do pobierania danych
    def stan_konta(self):  # ważniejsza od property
        return 'stan konta: ' + str(self.__stan) + 'zł'

    @stan_konta.setter   #setter pozwala modyfikować daną (wartość)
    def stan_konta(self, wartosc):
        self.__stan += wartosc

konto = kontoBankowe()
print(konto.stan_konta)

konto.stan_konta = 50
print(konto.stan_konta)
konto.stan_konta = 100
print((konto.stan_konta))
konto.stan_konta = -150
print(konto.stan_konta)