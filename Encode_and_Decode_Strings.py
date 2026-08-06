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
        self.parts = []
        self.actual = []
        for element in strs:
          for letter in element:
            conv_to_int = str(self.dict_encoding[letter])
            self.parts.append(conv_to_int)
          encoded_string = '_'.join(self.parts)
          self.parts.clear()
          self.actual.append(encoded_string)

        return '@'.join(self.actual)


    def decode(self, s: str) -> List[str]:
        self.first_num = ''
        self.second_num = ''
        self.third_num = ''
        self.tracker = 0
        self.temp_str = f'{self.first_num}{self.second_num}{self.third_num}'
        self.parts = []
        self.actual =[]
        self.i = 0
        for number in s:
            if number != '_' and number !='@':
              if self.tracker == 0:
                  self.first_num = number
              elif self.tracker == 1:
                  self.second_num = number
              elif self.tracker == 2:
                  self.third_num = number
              self.tracker += 1
            if number == '_' :
                self.temp_str = f'{self.first_num}{self.second_num}{self.third_num}'
                self.temp_str = int(self.temp_str)
                self.parts.append(self.dict_decoding[self.temp_str])
                self.tracker = 0
                self.first_num = ''
                self.second_num = ''
                self.third_num = ''
                self.temp_str = f'{self.first_num}{self.second_num}{self.third_num}'
            if number == '@':
                self.temp_str = f'{self.first_num}{self.second_num}{self.third_num}'
                self.temp_str = int(self.temp_str)
                self.parts.append(self.dict_decoding[self.temp_str])
                self.tracker = 0
                self.first_num = ''
                self.second_num = ''
                self.third_num = ''
                self.temp_str = f'{self.first_num}{self.second_num}{self.third_num}'
                self.actual.append(''.join(self.parts))
                self.parts.clear()
            if self.i == len(s) - 1:
                self.temp_str = f'{self.first_num}{self.second_num}{self.third_num}'
                self.temp_str = int(self.temp_str)
                self.parts.append(self.dict_decoding[self.temp_str])
                self.actual.append(''.join(self.parts))

            self.i += 1
        return self.actual
instance = Solution()
print(instance.decode("104_97_122_101_108@97_104_110_97_102"))