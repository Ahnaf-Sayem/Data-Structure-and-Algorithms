class Solution:
    def __init__(self):
        # Generates all 256 characters matching values 0 through 255
        self.ascii_char = [chr(i) for i in range(256)]
        self.dict_encoding = {}
        self.dict_decoding = {}
        self.i = 0
        for element in self.ascii_char:
            self.dict_encoding[element] = self.i
            self.dict_decoding[self.i] = element
            self.i += 1


    def encode(self, strs: List[str]) -> str:
        parts = []
        for element in strs:
          for letter in element:
            conv_to_int =str(self.dict_encoding[letter])
            parts.append(conv_to_int)
        encoded_string = '_'.join(parts)
        return encoded_string


    def decode(self, s: str) -> List[str]:
        self.first_num = ''
        self.second_num = ''
        self.third_num = ''
        self.tracker = 0
        self.temp_str = f'{self.first_num}{self.second_num}{self.third_num}'
        parts = []
        for number in s:
            if number != '_':
              if self.tracker == 0:
                  self.first_num = number
              elif self.tracker == 1:
                  self.second_num = number
              elif self.tracker == 2:
                  self.third_num = number
              self.tracker += 1
            if number == '_' or number == s[-1]:
                self.temp_str = f'{self.first_num}{self.second_num}{self.third_num}'
                self.temp_str = int(self.temp_str)
                parts.append(self.dict_decoding[self.temp_str])
                self.tracker = 0
                self.first_num = ''
                self.second_num = ''
                self.third_num = ''
                self.temp_str = f'{self.first_num}{self.second_num}{self.third_num}'
        return ''.join(parts)

instance = Solution()
encoded = instance.encode(['hazel'])
decoded = instance.decode(encoded)
print(decoded)
