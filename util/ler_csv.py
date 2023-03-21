import csv


def ler_csv_file(arquivo_csv):
    dados_csv = []
    try:
        with open(arquivo_csv, newline='') as massa:
            campos = csv.reader(massa, delimiter=',')
            next(campos)
            for linha in campos:
                dados_csv.append(linha)
            return dados_csv
    except FileNotFoundError:
        print(f'Arquivo de massa de dados não encontrado para o teste: {arquivo_csv}')
    except Exception as fail:
        print(f'Falha arquivo não encontrado!: {fail}')