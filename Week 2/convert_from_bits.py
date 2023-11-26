#Take input number of bits
str_bit = input("Please input number of bits ")
number_bits = int(str_bit)

#Convert
byte = 8
kilobyte = 1024 * byte
megabyte = 1024 * kilobyte

#Calculate
number_of_megabyte = number_bits // megabyte
number_of_bits_remain_megabyte = number_bits % megabyte

number_of_kilobyte = number_of_bits_remain_megabyte // kilobyte
number_of_bits_remain_kilobyte = number_of_bits_remain_megabyte % kilobyte

number_of_byte = number_of_bits_remain_kilobyte // byte
remain_bits = number_of_bits_remain_kilobyte % byte

#Result
# str_result = "The result is " + str(number_of_megabyte) + "MB " + str(number_of_kilobyte) + "KB " + str(number_of_byte) + "B " + str(remain_bits) + "b"
# print(str_result)




