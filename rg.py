#RG: 
rg_1 = int(input("Digite os dois primeiros números do seu RG: "))
rg_2 = int(input("Digite os três segundos números do seu RG: "))
rg_3 = int(input("Digite os três terceiros números do seu RG: "))
rg_4 = int(input("Digite o(s) último(s) um/dois número(s) do seu RG: "))
dia_emissao = int(input("Digite o dia da emissão do seu RG: "))
mes_emissao = int(input("Digite o mês da emissão do seu RG: "))
ano_emissao = int(input("Digite o ano da emissão do seu RG: "))
nome = str(input("Qual é o seu nome?: "))
pai = str(input("Qual é o nome do seu pai?: "))
mae = str(input("Qual é o nome da sua mãe?: "))
nat = str(input("Em qual cidade você nasceu?: "))
dia_nasc = int(input("Em qual dia você nasceu?: "))
mes_nasc = int(input("Em qual mês você nasceu?: "))
ano_nasc = int(input("Em qual ano você nasceu?: "))
orgao_emissor = str(input("Qual é a sigla do órgão emissor do seu RG?: "))
cpf_1 = int(input("Digite os três primeiros números do seu CPF: "))
cpf_2 = int(input("Digite os três segundos números do seu CPF: "))
cpf_3 = int(input("Digite os três terceiros números do seu CPF: "))
cpf_4 = int(input("Digite o(s) último(s) um/dois número(s) do seu CPF:"))
rg = (f"{rg_1}.{rg_2}.{rg_3}-{rg_4}")
data_emissao = (f"{dia_emissao}/{mes_emissao}/{ano_emissao}")
data_nasc = (f"{dia_nasc}/{mes_nasc}/{ano_nasc}")
cpf = (f"{cpf_1}{cpf_2}{cpf_3}{cpf_4}")

print(f"Número do RG: {rg}     Data de emissão: {data_emissao}")
print(f"Nome: {nome}")
print("Filiação:")
print(f"Nome da mãe:  {mae}    Órgão emissor: {orgao_emissor}")
print(f"Nome do pai: {pai}")
print(f"Naturalidade: {nat}    Data de nascimento: {data_nasc}")
print(f"Número do CPF: {cpf}")