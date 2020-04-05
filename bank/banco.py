from datetime import date

class Conta(object):
    def __init__(self,nome, cpf, saldo):        
        self.agencia = '0001'
        self.conta = str(random.randint(10000, 99999)) 
        self.digitoConta = str(random.randint(0, 9))
        self.nome = nome
        self.cpf = cpf
        self.saldo = float(saldo)

import os
import random
import platform
import re

conta = None
extrato = []

def limpar_tela():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def boas_vindas_banco():
    print('$-----------------------$')
    print('BEM VINDO AO BANK OF MEG')
    print('$-----------------------$\n')

def exibir_menu():
    print('-------------------------')
    print('SELECIONE UMA DAS OPÇÕES')
    print('-------------------------')
    print('1 - ABRIR CONTA')
    print('2 - VISUALIZAR MEUS DADOS')
    print('3 - TRANSFERÊNCIA')
    print('4 - PAGAMENTO')
    print('5 - VISUALIZAR EXTRATO')
    print('0 - SAIR')
    print('-------------------------')

def selecionar_item():
    print('OPÇÃO: ')
    opcaoSelecionada = int(input())   
    print('OPÇÃO SELECIONADA: %s'%(opcaoSelecionada))
    print('-------------------------')
    return opcaoSelecionada

def inserir_item_extrato(tipoOperacao, valor, descricao):
    global extrato
    
    if tipoOperacao == 'C':
        valorTransacao = '+' + str(valor)
    else:
        valorTransacao = '-' + str(valor)

    transacao = str(date.today().strftime("%d/%m/%Y")) + ' | ' + valorTransacao + ' | ' + descricao
    extrato.append(transacao)

def exibir_extrato():
    global extrato
    global conta
    
    limpar_tela()
    if conta == None:          
        print('CONTA AINDA NÃO FOI ABERTA') 
    else:
        if len(extrato) > 0:
            print(*extrato, sep = "\n")
        else:
            print('NENHUM ITEM PARA SER EXIBIDO')  
           
    print('\nPRESSIONE ENTER PARA CONTINUAR...')
    input()
    limpar_tela()

def validar_cpf(cpf):    
    if not isinstance(cpf,str):
        return False
   
    cpf = re.sub("[^0-9]",'',cpf)
   
    if len(cpf) != 11:
        return False

    sum = 0
    weight = 10
   
    for n in range(9):
        sum = sum + int(cpf[n]) * weight
        
        weight = weight - 1

    verifyingDigit = 11 -  sum % 11

    if verifyingDigit > 9 :
        firstVerifyingDigit = 0
    else:
        firstVerifyingDigit = verifyingDigit
    
    sum = 0
    weight = 11
    for n in range(10):
        sum = sum + int(cpf[n]) * weight        
        weight = weight - 1

    verifyingDigit = 11 -  sum % 11

    if verifyingDigit > 9 :
        secondVerifyingDigit = 0
    else:
        secondVerifyingDigit = verifyingDigit

    if cpf[-2:] == "%s%s" % (firstVerifyingDigit,secondVerifyingDigit):
        return True
    return False

def abrir_conta():
    global conta

    if conta == None: 
        print('\nNOME:')  
        nome = input()
        while nome.replace(' ', '').isalpha() == False:
            print('\nATENÇÃO!! É PERMITIDO APENAS LETRAS NO NOME, DIGITE NOVAMENTE') 
            print('\nNOME:')  
            nome = input()

        print('\nCPF:')  
        cpf = input()        
        while validar_cpf(cpf) == False:
            print('\nATENÇÃO!! CPF INVÁLIDO, DIGITE NOVAMENTE') 
            print('\nCPF:')  
            cpf = input()

        print('\nSALDO:')  
        saldo = input().replace(',', '.')        
        conta = Conta(nome, cpf, saldo)
    else:
        limpar_tela() 
        print('CONTA JÁ CRIADA')          
        print('PRESSIONE ENTER PARA CONTINUAR...')
        input()
        limpar_tela() 

def visualizar_meus_dados():
    global conta
    
    limpar_tela() 
    if conta == None:          
        print('CONTA AINDA NÃO FOI ABERTA') 
    else:
        print('AGENCIA: ' + conta.agencia) 
        print('CONTA: ' + conta.conta + '-' + conta.digitoConta) 
        print('NOME: ' + conta.nome)  
        print('CPF: ' + conta.cpf)  
        print('SALDO: ' + str(conta.saldo)) 
           
    print('\nPRESSIONE ENTER PARA CONTINUAR...')
    input()
    limpar_tela()

def transferir_valor():
    global conta

    limpar_tela() 
    if conta == None:          
        print('CONTA AINDA NÃO FOI ABERTA') 
    else:
        print('ENTRE COM AS INFORMACOES DA CONTA DESTINO')
        print('\nAGENCIA:')  
        agenciaDestino = input()
        print('CONTA:')  
        contaDestino = input()
        print('DIGITO CONTA:')  
        digitoContaDestino = input()
        print('VALOR:')  
        valorTransferencia = float(input())

        if valorTransferencia > conta.saldo:
            print('SALDO INSUFICIENTE')
        else:            
            conta.saldo = conta.saldo - valorTransferencia
            inserir_item_extrato('D', valorTransferencia, 'TRANSFERENCIA PARA AGENCIA: ' + agenciaDestino + ', CONTA: ' + contaDestino + '-' + digitoContaDestino)
            print('\nTRANSFERÊNCIA REALIZADA COM SUCESSO')
            print('SALDO ATUAL: ' + str(conta.saldo))  

    print('\nPRESSIONE ENTER PARA CONTINUAR...')
    input()
    limpar_tela()  

def realizar_pagamento():
    global conta

    limpar_tela()
    if conta == None:          
        print('CONTA AINDA NÃO FOI ABERTA') 
    else:
        print('ENTRE COM AS INFORMACOES DO PAGAMENTO')
        print('\nNUMERO BOLETO:')  
        numeroBoleto = input()     
        print('\nCEDENTE:')  
        cedente = input()     
        print('\nVALOR:')  
        valorBoleto = float(input())

        if valorBoleto > conta.saldo:
            print('SALDO INSUFICIENTE')
        else:            
            conta.saldo = conta.saldo - valorBoleto
            inserir_item_extrato('D', valorBoleto, 'PAGAMENTO DE BOLETO, CEDENTE: ' + cedente)
            print('\nPAGAMENTO REALIZADO COM SUCESSO')
            print('SALDO ATUAL: ' + str(conta.saldo))  

    print('\nPRESSIONE ENTER PARA CONTINUAR...')
    input()
    limpar_tela()  

def executar_item(opcaoSelecionada):
    if opcaoSelecionada == 1:
        abrir_conta()
        limpar_tela()
    elif opcaoSelecionada == 2:
        visualizar_meus_dados()   
    elif opcaoSelecionada == 3:
        transferir_valor()
    elif opcaoSelecionada == 4:
        realizar_pagamento()
    elif opcaoSelecionada == 5:
        exibir_extrato()
    else:
        os.system('cls')  
        print('OPÇÃO INVÁLIDA')          
        print('PRESSIONE ENTER PARA CONTINUAR...')
        input()
        limpar_tela() 

def main():    
    boas_vindas_banco() 
    exibir_menu()
    opcao = selecionar_item()    

    while(opcao != 0):        
        executar_item(opcao)        
        exibir_menu()
        opcao = selecionar_item()        
    else:
        print("SAINDO...")        

if __name__ == '__main__':
    main()