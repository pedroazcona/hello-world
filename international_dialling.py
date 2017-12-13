class CallToSelfError(Exception):
    def __init__(self, line):
        super()
        self.line = line

class MissingDataError(Exception):
    def __init__(self, line):
        super()
        self.line = line

class Country(object):
    def __init__(self, name, intl_call_prefix, country_call_code):
        self.name = name
        self.intl_call_prefix = intl_call_prefix
        self.country_call_code = country_call_code
        
    def validate(self):
        if not (self.name and self.intl_call_prefix and self.country_call_code):
            raise MissingDataError(self)
        
class Line(object):
    def __init__(self, country, national_number):
        self.country = country
        self.national_number = national_number
        
    def validate(self):
        if not (self.country and self.national_number):
            raise MissingDataError(self)
        self.country.validate()
        
    def call_to(self, other_line):
        self.validate()
        other_line.validate()
        if other_line is self:
            raise CallToSelfError(self)
        elif self.country is other_line.country:
            return other_line.national_number
        else:
            return self.country.intl_call_prefix + \
                other_line.country.country_call_code + \
                other_line.national_number

def self_test():
    c0 = Country('United States', '011', '1')
    c1 = Country('United Kingdom', '00', '44')
    c2 = Country('Spain', '00', '34')
    cx = Country('Italy', None, '34')
    c0n0 = Line(c0, '1231231234')
    c0n1 = Line(c0, '2342342345')
    c1n0 = Line(c1, '3453453456')
    c1n1 = Line(c1, '4564564567')
    c2n0 = Line(c2, '567567567')
    c2n1 = Line(c2, '678678678')
    cxn0 = Line(cx, '789789789')  # Country missing data
    c0nx = Line(c0, None)  # Line missing data
    assert c0n0.call_to(c0n1) == '2342342345'
    assert c0n0.call_to(c1n1) == '011444564564567'
    assert c0n0.call_to(c2n1) == '01134678678678'
    assert c1n0.call_to(c0n1) == '0012342342345'
    assert c1n0.call_to(c1n1) == '4564564567'
    assert c1n0.call_to(c2n1) == '0034678678678'
    assert c2n0.call_to(c0n1) == '0012342342345'
    assert c2n0.call_to(c1n1) == '00444564564567'
    assert c2n0.call_to(c2n1) == '678678678'
    try:
        c0n0.call_to(c0n0)
        assert False, "Expected exception not raised: CallToSelfError"
    except Exception as e:
        assert type(e) == CallToSelfError
    try:
        c0n0.call_to(cxn0)
        assert False, "Expected exception not raised: MissingDataError"
    except Exception as e:
        assert type(e) == MissingDataError
    try:
        c0nx.call_to(c0n0)
        assert False, "Expected exception not raised: MissingDataError"
    except Exception as e:
        assert type(e) == MissingDataError
    print('All tests completed successfully.')

if __name__ == '__main__':
    self_test()