encoded = """
   !!junk-77!! | [3::DW::ok] | [xx::DRSC::bad] |
   [1::NFFU::ok] | ##nothing## | [5::TQI_QNGWFWD::ok] |
   [2::OG::ok] | [4::XLI::ok] | [7::WT7::bad] |
   [6::GZ_7_VS::ok] | [99::IGNORE_ME::bad] | %%noise%%
"""
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

blocks = encoded.split('|')

nums = []
words = []

for block in blocks:
    block = block.strip()
    if block.startswith('[') and block.endswith(']'):
        inner = block[1:len(block) - 1]
        fields = inner.split('::')
        number = fields[0]
        text = fields[1]
        status = fields[2]

        if status == 'ok' and number.isdigit():
            valid_text = True
            for ch in text:
                if not (ch.isalpha() or ch == '_'):
                    valid_text = False
            if valid_text:
                num = int(number)

                decoded = ''
                for char in text:
                    if char == '_':
                        decoded = decoded + '_'
                    else:
                        idx = alphabet.find(char)
                        new_idx = idx - num
                        if new_idx < 0:      
                            new_idx = new_idx + 26
                        decoded = decoded + alphabet[new_idx]

                nums.append(num)
                words.append(decoded)

i = 0
while i < len(nums):
    smallest_pos = i
    j = i + 1
    while j < len(nums):
        if nums[j] < nums[smallest_pos]:
            smallest_pos = j
        j = j + 1
    temp_num = nums[i]
    nums[i] = nums[smallest_pos]
    nums[smallest_pos] = temp_num
    temp_word = words[i]
    words[i] = words[smallest_pos]
    words[smallest_pos] = temp_word
    i = i + 1

result = ''
for w in words:
    result = result + w
print(result)