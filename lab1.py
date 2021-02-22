class InvestmentCompany:
    data_source='PitchBook Company'

    def __init__(self, country="", employees=0, name="", address="", capital=0, investments=0,):
        self.country=country
        self.employees=employees
        self.name=name
        self.address=address
        self.capital=capital
        self.investments=investments

    def __del__(self):
        pass

    def __str__(self):
        return f"Country: {self.country}\n" \
               f"Employees: {self.employees}\n" \
               f"Name: {self.name}\n" \
               f"Address: {self.address}\n" \
               f"Capital: {self.capital}\n" \
               f"Investments: {self.investments}"



    @staticmethod
    def show_data_source():
        return InvestmentCompany.data_source

def main():
        company1 = InvestmentCompany("USA", 75, "Accel-KKR", " 2500 Sand Hill Road Suite 300. Menlo Park, California 94025", 10, 200)
        company2 = InvestmentCompany("USA", 180, "Berkshire Partners","200 Clarendon Street 35th Floor Boston, MA 02116 USA", 16, 100)
        company3 = InvestmentCompany("USA", 41, "Brentwood Associates","11150 Santa Monica Blvd.Suite 1200Los Angeles, CA 90025", 3, 50)

        print(company1, company2, company3)

if __name__ == "__main__":
        main()