class IPAddress:
    def __init__(self, ipaddress):
        self.ipaddress = ipaddress

    def __str__(self):
        if isinstance(self.ipaddress, (list, tuple)):
            return '.'.join(map(str, self.ipaddress))
        return '.'.join(map(str, self.ipaddress.split('.')))

    def __repr__(self):
        if isinstance(self.ipaddress, (list, tuple)):
            return f"{self.__class__.__name__}('{'.'.join(map(str, self.ipaddress))}')"
        return f"{self.__class__.__name__}('{'.'.join(map(str, self.ipaddress.split('.')))}')"


ip = IPAddress([1, 1, 10, 10])

print(str(ip))
print(repr(ip))

ip = IPAddress('8.8.1.1')

print(str(ip))
print(repr(ip))