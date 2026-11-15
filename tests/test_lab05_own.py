import pytest

from normalize import cpm, proportions
from sequence_utils import (
    clean_sequence,
    find_motif,
    gc_content,
    is_valid_dna,
    reverse_complement,
)


def test_proportions_input_unchanged_and_zero_total():
    raw = [50, 30, 20]
    result = proportions(raw)
    assert raw == [50, 30, 20]
    assert result is not raw
    assert result == pytest.approx([0.5, 0.3, 0.2])

    with pytest.raises(ValueError):
        proportions([0, 0, 0])
    with pytest.raises(ValueError):
        proportions([])


def test_cpm_explicit_library_size_and_errors():
    raw = [10, 20]
    assert cpm(raw, library_size=100) == pytest.approx([100_000.0, 200_000.0])
    assert raw == [10, 20]

    with pytest.raises(ValueError):
        cpm([10, 20], library_size=0)
    with pytest.raises(ValueError):
        cpm([10, 20], library_size=-5)


def test_is_valid_dna_allow_n_and_invalid_errors():
    assert clean_sequence(" atg\tcgt\r\n12 ") == "ATGCGT"
    assert is_valid_dna("ATGCN", allow_n=False) is False
    assert is_valid_dna("ATGCN", allow_n=True) is True

    with pytest.raises(ValueError):
        gc_content("ATGCN")
    with pytest.raises(ValueError):
        reverse_complement("ATGCN")


def test_find_motif_boundaries_and_empty_motif():
    assert find_motif("atgcgt", "CGT") == [3]
    assert find_motif("ATGC", "ATGCGT") == []

    with pytest.raises(ValueError):
        find_motif("ATGC", "")