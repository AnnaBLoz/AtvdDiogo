
def converter_massa_lunar(massa_kg):
    return massa_kg / 6


def converter_massa_marte(massa_kg):
    gravidade_terra = 9.81  # m/s²
    gravidade_marte = 3.71  # m/s²
    return (gravidade_marte / gravidade_terra) * massa_kg


def test_converter_massa_lunar():
    assert converter_massa_lunar(6) == 1, "Erro: 6 kg na Terra deveria ser 1 kg na Lua"
    assert converter_massa_lunar(12) == 2, "Erro: 12 kg na Terra deveria ser 2 kg na Lua"
    assert converter_massa_lunar(0) == 0, "Erro: 0 kg na Terra deveria ser 0 kg na Lua"


def test_converter_massa_marte():
    assert round(converter_massa_marte(9.81), 2) == 3.71, "Erro: 9.81 kg na Terra deveria ser 3.71 kg em Marte"
    assert round(converter_massa_marte(19.62), 2) == 7.42, "Erro: 19.62 kg na Terra deveria ser 7.42 kg em Marte"
    assert converter_massa_marte(0) == 0, "Erro: 0 kg na Terra deveria ser 0 kg em Marte"


if __name__ == "__main__":
    test_converter_massa_lunar()
    test_converter_massa_marte()
    print("Todos os testes foram concluídos com sucesso!")
