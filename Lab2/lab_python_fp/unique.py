# �������� ��� �������� ����������
class Unique(object):
    def __init__(self, items = False, **kwargs):
        # ����� ����������� �����������
        self.ignore_case = items
        self.dict = kwargs

    def __next__(self):
        # ����� ����������� __next__    
        pass

    def __iter__(self):
        return self
    
def main():
    data = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
    print(Unique(data))
    print(Unique(data, ignore_case=True))

if __name__ == "__main__":
    main()