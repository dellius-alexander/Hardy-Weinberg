from src import Allele, Gene


def test_gene():
    g: Gene = Gene(Allele(["A", "a"]), Allele(["B", "b"]))
    print(g.to_json())
    assert g.metadata['heterozygous'] == [
            [
                "A",
                "b"
            ],
            [
                "a",
                "B"
            ]
        ]
