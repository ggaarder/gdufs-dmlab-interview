from hashlib import md5


def get_md5(s1):
    if isinstance(s1, str):
        s1 = s1.encode("utf-8")
    elif isinstance(s1, bytes):
        s1 = s1
    else:
        raise TypeError("关键词类型错误！请检查类型！")
    m = md5()
    m.update(s1)
    return m.hexdigest()[8:-8]


def evaluate(user_file, answer_file):
    # 读取用户输出
    user_data = []
    with open(user_file, "r", encoding="utf-8") as f:
        for line in f:
            us = set([get_md5(w) for w in line.strip().split("\t")])
            user_data.append(us)

    # 读取答案
    answer_data = []
    with open(answer_file, "r", encoding="utf-8") as f:
        for line in f:
            answer_data.append(set(line.strip().split("\t")))

    assert len(user_data) == len(answer_data), "输出答案的行数有误！请检查！"
    jaccards = []
    for su, sa in zip(user_data, answer_data):
        jac = len(su & sa) / len(su | sa)
        jaccards.append(jac)
    return sum(jaccards) / len(jaccards)


if __name__ == '__main__':
    # 用户输出
    user_output_file = "./outputs.txt"
    # 答案文件
    answer_file = "./answer_enc.txt"

    score = evaluate(user_output_file, answer_file)
    print("你的成绩是：%.4f" % score)