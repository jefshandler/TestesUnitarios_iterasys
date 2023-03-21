# 1.4 - Modifique o teste positivo para que leia um arquivo CSV

import pytest
from calculo_racao_p_m_g import cao_p
from util.ler_csv import ler_csv_file


@pytest.mark.parametrize('peso_pet_p, peso_racao_p, resultado_esperado_p', ler_csv_file(r'..\vendors\csv\massa_pet_pequeno.csv'))
def test_cao_pequeno(peso_pet_p, peso_racao_p, resultado_esperado_p):
    # 1 - Configura
    # n1 peso do pet
    # n2 gramas de ração
    # n1 = peso_pet
    # n2 = peso_racao
    # resultado = n1*n2
    # 2 - Executa
    result_obitido = cao_p(int(peso_pet_p), int(peso_racao_p))
    # 3 - Valida
    assert int(resultado_esperado_p) == int(result_obitido)
