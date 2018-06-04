import re
import ply.lex as lex
from django.shortcuts import render, redirect
from .forms import cpf_form, expressao_form, compilador_form
from django.contrib import messages
from django.core.files.uploadedfile import UploadedFile

def home(request):
    return render(request, 'home.html')

def homecpf(request):
    return render(request, 'homecpf.html', {'cpf_form': cpf_form})

def homepos(request):
    return render(request, 'homepos.html', {'expressao_form': expressao_form})

def homecompilador(request):
    return render(request, 'homecompilador.html', {'compilador_form': compilador_form})

def validacpf(request):
    context = {}
    if request.method == 'POST':
        form = cpf_form(request.POST)
        messages.set_level(request, messages.INFO)
        if form.is_valid():
            texto = form.cleaned_data['cpf']
            context['is_valid'] = True
            form = cpf_form()

            cpf = re.compile(r'^[0-9]{3}\.[0-9]{3}\.[0-9]{3}\-[0-9]{2}$')
            r = re.search(cpf, texto)
            if r:
                dig1 = ((int(texto[0]) * 1) + (int(texto[1]) * 2) + (int(texto[2]) * 3) + (int(texto[4]) * 4) + (
                    int(texto[5]) * 5) + (int(texto[6]) * 6) + (int(texto[8]) * 7) + (int(texto[9]) * 8) + (
                            int(texto[10]) * 9)) % 11
                dig2 = ((int(texto[0]) * 9) + (int(texto[1]) * 8) + (int(texto[2]) * 7) + (int(texto[4]) * 6) + (
                    int(texto[5]) * 5) + (int(texto[6]) * 4) + (int(texto[8]) * 3) + (int(texto[9]) * 2) + (
                            int(texto[10]) * 1)) % 11

                if dig1 >= 10:
                    dig1 = 0
                if dig2 >= 10:
                    dig2 = 0

                if dig1 == int(texto[12]) and dig2 == int(texto[13]):
                    # self.mensagem["text"] = "CPF Valido"
                    estado = ["Rio Grande do Sul", "Distrito Federal, Goias Mato Grosso, Mato Grosso do Sul, Tocantins",
                              "Amazonas, Para, Roraima, Amapa, Acre, Rondonia", "Ceara, Maranhao, Piaui",
                              "Paraiba, Pernambuco, Alagoas, Rio Grande do Norte", "Bahia, Sergipe", "Minas Gerais",
                              "Rio de Janeiro, Espirito Santo", "Sao Paulo", "Parana, Santa Catarina"]

                    messages.success(request, texto + '   ...  CPF Válido')
                    messages.success(request, str(estado[int(texto[10])]))


                else:
                    messages.error(request, texto + '   ...  CPF inválido')
            else:
                messages.error(request, texto + '   ...  CPF inválido')

            return redirect('/cpf/#cpf')
    else:
        form = cpf_form()
    context['form'] = form
    template_name = 'homecpf.html'
    return redirect('/cpf/#cpf')
    # return render(request, template_name, context)

def gerarposfixa(request):
    class Stack:
        def __init__(self):
            self.items = []

        def push(self, item):
            self.items.append(item)

        def pop(self):
            return self.items.pop()

        def isEmpty(self):
            return (self.items == [])

        def len(self):
            return len(self.items)

    context = {}

    if request.method == 'POST':
        form = expressao_form(request.POST)
        if form.is_valid():
            texto = form.cleaned_data['expressao']
            context['is_valid'] = True
            form = expressao_form()

            flag, flag1, flag2 = 0, 0, 0
            padrao = re.compile(r'^[\d]{1}([\*\/\+\-]{1}[\d]{1})+$')
            x = re.compile(r'\(|\)')
            texto1 = x.split(texto)
            texto2 = "".join(texto1)
            resp = re.search(padrao, texto2)

            # validacao do tamanho
            if len(texto) > 2:
                for k in range(1, len(texto) - 1, 1):

                    if texto[k - 1] in "0123456789" and texto[k] == '(' and texto[k + 1] in "*/+-":
                        flag = 1
                        break
                    elif texto[k - 1] in "*/+-" and texto[k] == ')' and texto[k + 1] in "0123456789":
                        flag = 1
                        break
                    elif texto[k - 1] in "0123456789" and texto[k] in "()" and texto[k + 1] in "0123456789":
                        flag = 1
                        break
                    elif texto[k - 1] in "*/+-" and texto[k] in "()" and texto[k + 1] in "*/+-":
                        flag = 1
                        break
                    elif texto[k - 1] == '(' and texto[k] in "*/+-" and texto[k + 1] in "0123456789":
                        flag = 1
                        break
                    elif (texto[k - 1] == '(' and texto[k] == ')') or (texto[k] == '(' and texto[k + 1] == ')'):
                        flag = 1
                        break
                    # validacao dos parenteses
                    if flag == 0:
                        esquerda = 0
                        direita = 0
                        for i in range(len(texto)):
                            if texto[i] == '(':
                                esquerda += 1
                            elif texto[i] == ')':
                                direita += 1
                                if esquerda > 0:
                                    esquerda -= 1
                                    direita -= 1
                        if esquerda or direita:
                            flag = 1

                # validacao expressao pos-fixa
                if flag == 0 and resp:
                    pilha = Stack()
                    posfixo = ""

                    for i in texto:
                        if i == '(':
                            pilha.push(i)
                        elif i == ')':
                            while 1:
                                teste = pilha.pop()
                                if teste == '(':
                                    break
                                posfixo += teste
                        elif i.isdigit():
                            posfixo += i
                        else:
                            if pilha.isEmpty():
                                if i in "*/+-":
                                    pilha.push(i)
                            else:
                                teste = pilha.pop()
                                if teste == '(':
                                    pilha.push(teste)
                                    pilha.push(i)
                                else:

                                    if (teste in "*/") and (i in "+-"):
                                        posfixo += teste
                                        if flag1 == 1:
                                            teste = pilha.pop()
                                            if teste in "+-":
                                                posfixo += teste
                                                flag1 = 0
                                            else:
                                                pilha.push(teste)
                                        pilha.push(i)
                                    elif (teste in "*/") and (i in "*/"):
                                        posfixo += teste
                                        pilha.push(i)
                                    elif (teste in "+-/") and (i in "*/"):
                                        pilha.push(teste)
                                        pilha.push(i)
                                        flag1 = 1
                                    elif (teste in "+-") and (i in "+-"):
                                        posfixo += teste
                                        pilha.push(i)
                    if pilha.len() <= 2:
                        while not pilha.isEmpty():
                            teste = pilha.pop()
                            posfixo += teste
                        messages.success(request, posfixo)
                    else:
                        messages.error(request, 'Expressao incorreta!')
                else:
                    messages.error(request, 'Expressao incorreta!')
            else:
                messages.error(request, 'Expressao incorreta!')

            return redirect('/pos/#pos')
    else:
        form = expressao_form()
    context['form'] = form
    template_name = 'homepos.html'
    return redirect('/pos/#pos')

def compilar(request):

    context = {}
    lista = []

    # arquivo = UploadedFile(open('static/arquivo.txt', 'r'), 'arquivo.txt')
    # unica_linha = arquivo.read()
    # arquivo.close()

    # print(unica_linha)

    if request.method == 'POST':
        codigo = request.POST.get('codigo')

        # print(type(codigo))
        # print(codigo)

        reserved = {
            'begin': 'ini_code',
            'end': 'fim_code',
            'start': 'liga_robo',
            'off': 'desliga_robo',
            'stop': 'parar',
            'if': 'if',
            'else': 'else',
            'elif': 'elif',
            'loop': 'while',
            'break': 'break',
            'return': 'retorno',
            'print': 'exiba',
        }

        tokens = [
                     'comentario',
                     'op_relacional', 'op_aritmetico',
                     'a_parente', 'f_parente',
                     'a_chaves', 'f_chaves',
                     'a_colchetes', 'f_colchetes',
                     'quebra_linha',
                     'tip_bool',
                     'tipo_var',
                     'numero',
                     'string',
                     'atribuir',
                     'variavel',
                     'dir_robo',
                     'move_robo',
                     'RESERVED',
                 ] + list(reserved.values())

        t_comentario = r"[\/][\*]+[\w\W]+[\*]+[\/]"
        t_string = r"[\"]+[\w\W]+[\"]"
        t_a_parente = r"\("
        t_f_parente = r"\)"
        t_op_relacional = r"((<=){1})|((>=){1})|((==){1})|((!=){1})|((<){1})|((>){1})"
        t_op_aritmetico = r"[\+|\-|\/|\*]"
        t_atribuir = r"="
        t_a_chaves = r"[\{]"
        t_f_chaves = r"[\}]"
        t_a_colchetes = r"[\[]"
        t_f_colchetes = r"[\]]"
        t_quebra_linha = r";+"
        t_tip_bool = r"(false)|(true)"
        t_tipo_var = r"(int)|(float)|(bool)|(str)"
        t_numero = r"[\d]+"
        t_variavel = r"(var_)[\d]+"
        t_dir_robo = r"(right)|(left)"
        t_move_robo = r"(forward)|(backward)"

        def t_RESERVED(t):
            r"(begin)|(end)|(start)|(off)|(right)|(left)|(stop)|(if)|(else)|(elif)|(loop)|(break)|(return)|(print)"
            t.type = reserved.get(t.value, 'RESERVED')
            return t

        # Regra para quebra de linhas(rastrear)
        def t_newline(t):
            # t.lexer.lineno = 0
            r'\n+'
            t.lexer.lineno += len(t.value)

        # Uma string contendo caracteres ignorados (espaços e tabulações)
        t_ignore = ' \t\r'

        # Erro ao manipular regra
        def t_error(t):
            erro = ''
            erro = "Illegal character '{0}' na linha {1} coluna {2}".format(t.value[0], t.lineno, t.lexpos)
            lista.append(erro)
            t.lexer.skip(1)

        # Constrói o lexer
        lexer = lex.lex()

        code = codigo.split('\r')

        for i in range(len(code)):
            # print(code[i])
            lexer.input(code[i])

            # Tokenize
            while True:

                tok = lexer.token()
                # print(tok)
                token = ''
                if tok:
                    lista.append(str(tok))
                else:
                    break


    context['resposta'] = "\\n".join(lista)
    l = ""
    flag = 0
    for i in codigo:
        if (i == "\n" or i == "\r") and flag == 0:
            l += "\\r"
            flag = 1
        elif i != "\n":
            l += i
            flag = 0
    context['codigo'] = l
    template_name = 'homecompilador.html'
    return render(request, template_name, context)