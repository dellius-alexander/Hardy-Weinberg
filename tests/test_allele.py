from hardyweinbergcalculator.genetics import Allele


def test_allele():
    a = Allele(["A", "a", "B", "b", "C", "c"])
    print(a.to_json())
    assert a.symbols == ["A", "a", "B", "b", "C", "c"]
