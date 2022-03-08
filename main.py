from utils import hangul_util


def main():
    code_point = hangul_util.unicode_block_start
    char_count = 0
    for first_sound in hangul_util.first_sounds:
        for middle_sound in hangul_util.middle_sounds:
            # 双音节
            print(f'U+{code_point:04X} {chr(code_point)} = {first_sound} {middle_sound}')
            code_point += 1
            char_count += 1
            for last_sound in hangul_util.last_sounds:
                # 三音节
                print(f'U+{code_point:04X} {chr(code_point)} = {first_sound} {middle_sound} {last_sound}')
                code_point += 1
                char_count += 1
    assert char_count == hangul_util.unicode_char_count


if __name__ == '__main__':
    main()
