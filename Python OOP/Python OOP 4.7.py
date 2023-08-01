def check_type(*arg_types):
    def decorator(func):
        def wrapped(self, other, *args, **kwargs):
            if isinstance(other, arg_types):
                return func(self, other, *args, **kwargs)
            return NotImplemented
        return wrapped
    return decorator


class PTime:
    pass


class Time(PTime):
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes
        self.normalize_time()

    def normalize_time(self):
        self.hours += self.minutes // 60
        self.minutes %= 60
        self.hours %= 24

    def __str__(self):
        return f"{self.hours:02d}:{self.minutes:02d}"

    @check_type(PTime)
    def __add__(self, other):
        total_hours = self.hours + other.hours
        total_minutes = self.minutes + other.minutes

        return Time(total_hours, total_minutes)

    @check_type(PTime)
    def __iadd__(self, other):
        self.hours += other.hours
        self.minutes += other.minutes
        self.normalize_time()

        return self


t = Time(22, 0)
t += Time(3, 0)
print(t)

print()

t1 = Time(15, 50)
t2 = Time(2, 20)
print(t1 + t2)

t1 += Time(2, 20)
print(t1)

print()

t = Time(13, 0)
print(t)
id1 = id(t)

t += Time(2, 30)
id2 = id(t)
print(t)
print(id1 == id2)