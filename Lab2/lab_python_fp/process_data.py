import json
import sys
# ������� ������ ����������� �������

path = None

# ���������� � ���������� path ��������� ���� � �����, ������� ��� ������� ��� ������� ��������

with open(path) as f:
    data = json.load(f)

# ����� ���������� ����������� ��� ������� �� �������, ������� `raise NotImplemented`
# ��������������, ��� ������� f1, f2, f3 ����� ����������� � ���� ������
# � ���������� ������� f4 ����� ���� �� 3 �����

@print_result
def f1(arg):
    raise NotImplemented


@print_result
def f2(arg):
    raise NotImplemented


@print_result
def f3(arg):
    raise NotImplemented


@print_result
def f4(arg):
    raise NotImplemented


if __name__ == '__main__':
    with cm_timer_1():
        f4(f3(f2(f1(data))))