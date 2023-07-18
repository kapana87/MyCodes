class Postman:
    def __init__(self):
        self.delivery_data = []

    def add_delivery(self, street, house, apartment):
        self.delivery_data.append((street, house, apartment))

    def get_houses_for_street(self, street):
        get_houses = [key for key, value in {address[1]: address[2] for address in self.delivery_data if street in address}.items()]
        return get_houses

    def get_flats_for_house(self, street, house):
        return [key for key, value in {address[2]: address[1] for address in self.delivery_data if street in address and house in address}.items()]


postman = Postman()

postman.add_delivery('Советская', 151, 74)
postman.add_delivery('Советская', 151, 75)
postman.add_delivery('Советская', 90, 2)
postman.add_delivery('Советская', 151, 74)

print(postman.get_houses_for_street('Советская'))
print(postman.get_flats_for_house('Советская', 151))