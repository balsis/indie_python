class TimeZone:
    def __init__(self, name, offset_hour, offset_minute):
        self.name = name
        self.offset_hours = offset_hour
        self.offset_minutes = offset_minute

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or value.strip() == "":
            raise ValueError(f'Timezone bad name - {value}')
        self._name = value.strip()

    @property
    def offset_hours(self):
        return self._offset_hours

    @offset_hours.setter
    def offset_hours(self, value):
        if not isinstance(value, int):
            raise ValueError("Hour offset must be an integer.")
        elif not (-12 <= value <= 14):
            raise ValueError('Offset must be between -12:00 and +14:00.')
        self._offset_hours = value

    @property
    def offset_minutes(self):
        return self._offset_minutes

    @offset_minutes.setter
    def offset_minutes(self, value):
        if not isinstance(value, int):
            raise ValueError('Minutes offset must be an integer.')
        elif not (-59 <= value <= 59):
            raise ValueError('Minutes offset must between -59 and 59.')
        self._offset_minutes = value


try:
    TimeZone(' Abc ', -20.5, 34)
except ValueError as e:
    print(e)

try:
    TimeZone(' Abc ', -15, 34)
except ValueError as e:
    print(e)

try:
    TimeZone(' Abc ', 15, 34)
except ValueError as e:
    print(e)

tz = TimeZone(' Abc ', 10, 34)
print(tz.name)
print(tz.offset_hours)
print(tz.offset_minutes)
