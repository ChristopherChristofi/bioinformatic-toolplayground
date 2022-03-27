import pytest
from string_manipulations.complement_strand import run

@pytest.mark.parametrize(
    ('read_strand', 'complement', 'errexpected'),
    (
        pytest.param('AATGCAA', 'TTGCATT\n', '', id="adenine_to_thymine"),
        pytest.param('TTAGCTT', 'AAGCTAA\n', '', id="thymine_to_adenine"),
        pytest.param('GGATCGG', 'CCGATCC\n', '', id="guanine_to_cytosine"),
        pytest.param('CCATGCC', 'GGCATGG\n', '', id="cytosine_to_guanine"),
        pytest.param('TGCAACGT', 'ACGTTGCA\n', '', id="generate_complement"),
    ),
)
def test_complement_string(capsys, read_strand, complement, errexpected):
    run(read_strand)
    out, err = capsys.readouterr()
    assert out == complement
    assert err == errexpected

def test_complement_nonbase(capsys):
    run('ATGCB')
    out, err = capsys.readouterr()
    assert out == ''
    assert err == 'Error. Incorrect base: B\n'
