# 1.4 - Modifique o teste positivo para que leia um arquivo CSV

import pytest
from calculo_racao_p_m_g import cao_m
from util.ler_csv import ler_csv_file


@pytest.mark.parametrize('peso_pet_m, peso_racao_m, resultado_esperado_m', ler_csv_file(r'..\vendors\csv\massa_pet_medio.csv'))
def test_cao_medio(peso_pet_m, peso_racao_m, resultado_esperado_m):
    # 1 - Configura
    # n1 peso do pet
    # n2 gramas de ração
    # n1 = peso_pet
    # n2 = peso_racao
    # resultado = n1*n2
    # 2 - Executa
    result_obitido = cao_m(int(peso_pet_m), int(peso_racao_m))
    # 3 - Valida
    assert int(resultado_esperado_m) == int(result_obitido)



