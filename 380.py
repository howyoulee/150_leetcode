import random

class RandomizedSet(object):

    def __init__(self):
        self.num_list = []  # 存储元素
        self.num_dict = {}  # 哈希表，存储 val -> index

    def insert(self, val):
        if val in self.num_dict:
            return False  # 已经存在
        self.num_dict[val] = len(self.num_list)  # 记录索引
        self.num_list.append(val)
        return True

    def remove(self, val):
        if val not in self.num_dict:
            return False

        # 1. 获取 val 的索引
        idx = self.num_dict[val]

        # 2. 获取最后一个元素
        last_element = self.num_list[-1]

        # 3. 交换 val 和最后一个元素
        self.num_list[idx] = last_element
        self.num_dict[last_element] = idx  # 更新哈希表
        
        # 4. 删除最后一个元素
        self.num_list.pop()
        del self.num_dict[val]

        return True

    def getRandom(self):
        return random.choice(self.num_list)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()