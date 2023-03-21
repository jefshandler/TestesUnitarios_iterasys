# 1.4 - Modifique o teste positivo para que leia um arquivo CSV

import pytest
from util.ler_csv import ler_csv_file
from calculo_racao_p_m_g import cao_g


@pytest.mark.parametrize('peso_pet_g, peso_racao_g, resultado_esperado_g', ler_csv_file(r'..\vendors\csv\massa_pet_grande.csv'))
def test_cao_gedio(peso_pet_g, peso_racao_g, resultado_esperado_g):
    # 1 - Configura
    # n1 peso do pet
    # n2 gramas de ração
    # n1 = peso_pet
    # n2 = peso_racao?
    # resultado = n1*n2
    # 2 - Executa
    result_obitido = cao_g(int(peso_pet_g), int(peso_racao_g))
    # 3 - Valida
    assert int(resultado_esperado_g) == int(result_obitido)



