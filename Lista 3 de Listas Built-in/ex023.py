"""23) A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de espaço em disco no seu servidor de
arquivos. Para tentar resolver este problema, o Administrador de Rede precisa saber qual o espaço ocupado pelos
usuários, e identificar os usuários com maior espaço ocupado."""


def converte_MB(bytes):
    return bytes / (1024.00 * 1024.00)


def porcentagem(parte, total):
    return (100 * parte) / total


with open('usuarios.txt', 'r') as arquivo:
    dados_usuarios = [linha.strip().split() for linha in arquivo]


tamanho_total_em_bytes = sum(int(dados[1]) for dados in dados_usuarios)

# Cria o cabeçalho do relatório
cabecalho = f"ACME Inc.{'':26}Uso do espaço em disco pelos usuários\n"
cabecalho += "-" * 70 + "\n"
cabecalho += f"{'Nr.':<6}{'Usuário':<16}{'Espaço utilizado':>20}{'% do uso':>13}\n"

# Cria o corpo do relatório
corpo = ''
for i, dados in enumerate(dados_usuarios):
    nome, tamanho_em_bytes = dados
    tamanho_em_MB = converte_MB(int(tamanho_em_bytes))
    percentual_do_uso = porcentagem(int(tamanho_em_bytes), tamanho_total_em_bytes)
    corpo += f'{i+1:<6}{nome:<16}{tamanho_em_MB:>19.2f} MB{percentual_do_uso:>13.2f}%\n'

# Cria o rodapé do relatório
rodape = '-' * 70 + '\n'
rodape += f'{"Espaço total ocupado:":<37}{converte_MB(tamanho_total_em_bytes):>22.2f} MB\n'
rodape += f'{"Espaço médio ocupado:":<37}{converte_MB(tamanho_total_em_bytes / len(dados_usuarios)):>22.2f} MB\n'

with open('relatorio.txt', 'w') as arquivo:
    arquivo.write(cabecalho + corpo + rodape)