import re
import random
import string

def extract_garbled_characters(text):
    pattern = re.compile(r'[^\u0000-\u007F]+')  # 匹配非ASCII字符的正则表达式
    garbled_chars = re.findall(pattern, text)  # 提取乱码字符
    garbled_chars = list(set(garbled_chars))  # 去除重复字符
    garbled_chars.sort()  # 按顺序排序
    return garbled_chars

file_path = r"D:\CTF_Study\Reverse\BUU\4.第四页\[watevrCTF 2019]Repyc\1.py"  # 替换为你的文本文件路径

with open(file_path, "r", encoding="utf-8") as file:
    text = file.read()

garbled_chars = extract_garbled_characters(text)
print(garbled_chars)

values = ['䯂', '䵦', '亀', '佤', '侰', '俴', '괠', '괡', '괢', '괣', '굴', '굸', '굿', '궓', '꼖', '꽲', '꽺', '꾮', '꿚', '냃', '뉃', '댒', '돯', '듃', '딓', '떇', '뗋', '똷', '뚫', '띇', '렀', '렳', '뢯', '륇', '맳', '뫇', '뫻', '묇', '묟', '뭗', '뭿', '뮓', '뮳', '믃']

def generate_random_word():
    word_length = random.randint(3, 8)  # 随机生成单词长度，范围为3到8个字符
    letters = string.ascii_lowercase  # 获取所有小写字母
    word = ''.join(random.choice(letters) for _ in range(word_length))  # 随机生成单词
    return word

def convert_to_word_dictionary(lst):
    word_dictionary = {}
    for value in lst:
        word = generate_random_word()
        word_dictionary[value] = word
    return word_dictionary

word_dictionary = convert_to_word_dictionary(values)
print(word_dictionary)

"""
{'䯂': 'nffxmwgd', '䵦': 'mdrf', '亀': 'dfimrjq', '佤': 'kjgejlu', '侰': 'cezkgdde', '俴': 'mxecda', '괠': 'sihbc', '괡': 'fgebsjs', '괢': 'hih', '괣': 'qchs', '굴': 'mnydght', '굸': 'ssnar', '굿': 'beljcrtv', '궓': 'lxclcz', '꼖': 'kqtwsq', '꽲': 'hbbjpshl', '꽺': 'sqw', '꾮': 'qqmvcjx', '꿚': 'kiaqkqjz', '냃': 'aex', '뉃': 'lljg', '댒': 'owynr', '돯': 'ziyqjrh', '듃': 'kmyer', '딓': 'dzxnvp', '떇': 'qremlemw', '뗋': 'knqtb', '똷': 'qfzhzwb', '뚫': 'xirfwa', '띇': 'fanc', '렀': 'qyhcpfc', '렳': 'duuuoz', '뢯': 'erd', '륇': 'btz', '맳': 'wboy', '뫇': 'nrveyvb', '뫻': 'pckjique', '묇': 'qiknk', ' 
묟': 'tzylj', '뭗': 'vhvt', '뭿': 'nkc', '뮓': 'mkmkdwn', '뮳': 'mdrag', '믃': 'nawcdz'}
"""
def replace_characters(text, replacement_dict):
    for char, replacement in replacement_dict.items():
        text = text.replace(char, replacement)
    return text

input_file_path = r"D:\CTF_Study\Reverse\BUU\4.第四页\[watevrCTF 2019]Repyc\1.py"  # 替换为你的文本文件路径
output_file_path = r"D:\CTF_Study\Reverse\BUU\4.第四页\[watevrCTF 2019]Repyc\output.py"

replacement_dict = {'䯂': 'nffxmwgd', '䵦': 'mdrf', '亀': 'dfimrjq', '佤': 'kjgejlu', '侰': 'cezkgdde', '俴': 'mxecda', '괠': 'sihbc', '괡': 'fgebsjs', '괢': 'hih', '괣': 'qchs', '굴': 'mnydght', '굸': 'ssnar', '굿': 'beljcrtv', '궓': 'lxclcz', '꼖': 'kqtwsq', '꽲': 'hbbjpshl', '꽺': 'sqw', '꾮': 'qqmvcjx', '꿚': 'kiaqkqjz', '냃': 'aex', '뉃': 'lljg', '댒': 'owynr', '돯': 'ziyqjrh', '듃': 'kmyer', '딓': 'dzxnvp', '떇': 'qremlemw', '뗋': 'knqtb', '똷': 'qfzhzwb', '뚫': 'xirfwa', '띇': 'fanc', '렀': 'qyhcpfc', '렳': 'duuuoz', '뢯': 'erd', '륇': 'btz', '맳': 'wboy', '뫇': 'nrveyvb', '뫻': 'pckjique', '묇': 'qiknk', '묟': 'tzylj', '뭗': 'vhvt', '뭿': 'nkc', '뮓': 'mkmkdwn', '뮳': 'mdrag', '믃': 'nawcdz'}

# 读取输入文件
with open(input_file_path, 'r', encoding='utf-8') as input_file:
    input_text = input_file.read()

# 替换文本
replaced_text = replace_characters(input_text, replacement_dict)

# 写入输出文件
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    output_file.write(replaced_text)

print("替换完成并已写入到输出文件中。")