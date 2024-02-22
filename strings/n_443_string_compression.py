from utils.time_measurement import time_measurement


class StringCompression:
    @staticmethod
    @time_measurement
    def solution(chars: list[str]):
        if len(chars) == 1:
            return len(chars)

        read_pointer = 0
        write_pointer = 0

        # 1. Iterate through the char list
        while read_pointer < len(chars):
            # 2. Assign the current char
            current_char = chars[read_pointer]
            start = read_pointer
            # 3. Count the number of occurrences of the current char
            while read_pointer < len(chars) and current_char == chars[read_pointer]:
                read_pointer += 1
            # 4. Write the current char to the write_pointer position
            chars[write_pointer] = current_char
            write_pointer += 1

            # 5. If the number of occurrences is greater than 1, then write the number of occurrences
            if read_pointer - start > 1:
                for digit in str(read_pointer - start):
                    chars[write_pointer] = digit
                    write_pointer += 1

        return write_pointer