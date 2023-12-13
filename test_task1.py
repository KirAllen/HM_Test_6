import pytest

from homework.task001.task_1 import NumsLists


@pytest.fixture
def list1():
    """
    ��������, ������������ ������ �� ���������� [1, 2, 3, 4, 5].
    """
    return [1, 2, 3, 4, 5]


@pytest.fixture
def list2():
    """����������."""
    return [2, 3, 4, 5, 6]


def test_init(list1, list2):
    """�������� ���������� ������������� ������."""
    nums_list = NumsLists(list1, list2)
    assert nums_list.lst1 == list1
    assert nums_list.lst2 == list2


def test_get_lists_averages(list1, list2):
    """�������� ������� �������� ������� �������� ������ 1."""
    nums_list = NumsLists(list1, list2)
    assert nums_list.get_lists_averages() == (3, 4)


@pytest.mark.parametrize('lst1, lst2, result', [([1, 2, 3], [], (2, 0)),
                                                ([], [1, 2, 3], (0, 2)), ([], [], (0, 0))])
def test_get_empty_lists_averages(lst1, lst2, result):
    """�������� ������� ��������, ���� ���� ��� ��� ������ ������."""
    nums_list = NumsLists(lst1, lst2)
    assert nums_list.get_lists_averages() == result


@pytest.mark.parametrize('lst1, lst2, result', [([1, 2, 3], [5], (2, 5)),
                                                ([5], [1, 2, 3], (5, 2)), ([5], [5], (5, 5))])
def test_get_one_elemented_lists_averages(lst1, lst2, result):
    """�������� ������� ��������, ���� ���� ��� ��� ������ ����� ������ ���� �������."""
    nums_list = NumsLists(lst1, lst2)
    assert nums_list.get_lists_averages() == result


def test_first_average_more(list1, list2, capfd):
    """�������� ��������� ����� ������� �������� ������� ������ ������ �������."""
    nums_list = NumsLists(list2, list1)
    nums_list.compare_averages()
    captured = capfd.readouterr()
    assert captured.out.strip() == '������ ������ ����� ������� ������� ��������.'


def test_second_average_more(list1, list2, capfd):
    """�������� ��������� ����� ������� �������� ������� ������ ������ �������."""
    nums_list = NumsLists(list1, list2)
    nums_list.compare_averages()
    captured = capfd.readouterr()
    assert captured.out.strip() == '������ ������ ����� ������� ������� ��������.'


def test_equal_averages(list1, capfd):
    """�������� ��������� ����� ������� �������� ������� �����."""
    nums_list = NumsLists(list1, list1)
    nums_list.compare_averages()
    captured = capfd.readouterr()
    assert captured.out.strip() == '������� �������� �����.'