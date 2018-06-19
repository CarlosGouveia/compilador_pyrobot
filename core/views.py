import re
import ply.lex as lex
from django.shortcuts import render, redirect
from .forms import cpf_form, expressao_form, compilador_form
from django.contrib import messages

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

    context            = {}
    lista              = []
    listaErro          = []
    listaErroSintatico = []
    listaSintaxe       = []

    if request.method == 'POST':
        codigo = request.POST.get('codigo')


        #############################################################################################################
        ############################################# ANÁLISE LÉXICA ################################################
        #############################################################################################################

        reserved = {
            'begin': 'INI_CODE',
            'end': 'FIM_CODE',
            'start': 'LIGA_ROBO',
            'off': 'DESLIGA_ROBO',
            'stop': 'PARAR',
            'if': 'IF',
            'else': 'ELSE',
            'loop': 'WHILE',
            'break': 'BREAK',
            'print': 'EXIBA',
        }

        tokens = [
             'COMENTARIO',
             'OP_RELACIONAL', 'OP_ARITMETICO',
             'A_PARENTE', 'F_PARENTE',
             'A_CHAVES', 'F_CHAVES',
             'QUEBRA_LINHA',
             'TIPO_BOOL',
             'TIPO_VAR',
             'NUM_FLOAT',
             'STRING',
             'NUMERO',
             'ATRIBUIR',
             'VARIAVEL',
             'DIR_ROBO',
             'MOVE_ROBO',
        ] + list(reserved.values())

        t_STRING = r'\["[^\"\]]*"\]'
        t_COMENTARIO = r"[\/\*][^\\]+[\\]"
        t_A_PARENTE = r"\("
        t_F_PARENTE = r"\)"
        t_OP_RELACIONAL = r"((<=){1})|((>=){1})|((==){1})|((!=){1})|((<){1})|((>){1})"
        t_OP_ARITMETICO = r"[\+|\-|\/|\*]"
        t_ATRIBUIR = r"="
        t_A_CHAVES = r"[\{]"
        t_F_CHAVES = r"[\}]"
        t_QUEBRA_LINHA = r";+"
        t_TIPO_BOOL = r"(false)|(true)"
        t_TIPO_VAR = r"(int)|(float)|(bool)|(str)"
        t_NUMERO = r"[\d]+"
        t_NUM_FLOAT = r"[\d]+\.[\d]{0,5}"
        t_VARIAVEL = r"(var_)[\d]+"
        t_DIR_ROBO = r"(right)|(left)"
        t_MOVE_ROBO = r"(forward)|(backward)"

        def t_RESERVED(t):
            r"(begin)|(end)|(start)|(off)|(stop)|(if)|(else)|(loop)|(break)|(print)"
            t.type = reserved.get(t.value, 'RESERVED')
            return t

        # Regra para quebra de linhas(rastrear)
        def t_newline(t):
            r'\n+'
            t.lexer.lineno += len(t.value)

        # Uma string contendo caracteres ignorados (espaços e tabulações)
        t_ignore = ' \t\r'

        # Erro ao manipular regra
        def t_error(t):
            erro = ''
            erro = "Illegal character '{0}' na linha {1} coluna {2}".format(t.value[0], t.lineno, find_column(code, t))

            lista.append(erro)
            listaErro.append(erro)
            t.lexer.skip(1)

        def find_column(input,tok):
            inicio = input.rfind('\n', 0, tok.lexpos) + 1
            coluna = (tok.lexpos - inicio) + 1
            return coluna

        # Constrói o lexer
        lexer = lex.lex()

        code = codigo

        lexer.input(code)

        # Tokenize
        while True:

            tok = lexer.token()
            token = ''
            if tok:
                toke = ""
                toke = 'LexToken(' + str(tok.type) + ',' + str(tok.value) + ',' + str(tok.lineno) + ',' + str(find_column(code, tok)) + ')'
                lista.append(toke)
            else:
                break

        if len(listaErro) == 0:
            tmp = ' Compilacao terminada sem erro lexico!'
            tmp2 ='---------------------------------------------------'
            lista.reverse()
            lista.append(tmp2)
            lista.append(tmp)
            lista.reverse()

            #############################################################################################################
            ############################################# ANÁLISE SINTÁTICA #############################################
            #############################################################################################################

            # precedence = (
            # 	('left', 'begin'),
            # 	('right', 'end')
            # )

            names = {}

            # NOVA GRAMATICA

            def p_programa(t):
                '''programa : INI_CODE A_CHAVES listacorpo F_CHAVES FIM_CODE
            				| INI_CODE A_CHAVES empty F_CHAVES FIM_CODE
            				| comentario
            	'''

            def p_corpo(t):
                '''corpo : declaracao
                        | atribuicao
                        | loop
                        | direcao
                        | movimenta
                        | iniciarobo
                        | break
                        | condicional
                        | parar
            			| mostrar
            			| comentario
                '''

            def p_corpo_robo_on(t):
                '''corpo_robo_on : declaracao
                        | atribuicao
                        | loop_robo_on
                        | direcao
                        | movimenta
                        | break
                        | condicional_robo_on
                        | parar
            			| mostrar
            			| comentario
                '''

            def p_empty(t):
                'empty : '
                pass

            def p_listacorpo(t):
                '''listacorpo : corpo
                            | corpo listacorpo
                '''

            def p_listacorpo_robo_on(t):
                '''listacorpo_robo_on : corpo_robo_on
                            | corpo_robo_on listacorpo_robo_on
                '''

            def p_declaracao(t):
                'declaracao : TIPO_VAR VARIAVEL QUEBRA_LINHA'

            def p_atribuicao(t):
                '''atribuicao : VARIAVEL ATRIBUIR operacao QUEBRA_LINHA
            				| VARIAVEL ATRIBUIR expressao_str QUEBRA_LINHA
            				| VARIAVEL ATRIBUIR expressao QUEBRA_LINHA
            				| VARIAVEL ATRIBUIR booleano QUEBRA_LINHA
            	'''

            def p_operacao(t):
                '''operacao : expressao OP_ARITMETICO expressao
            				| expressao OP_ARITMETICO operacao
            	'''

            def p_expressao_num(t):
                '''expressao : NUMERO
            				| NUM_FLOAT
            	'''

            def p_expressao_var(t):
                'expressao : VARIAVEL'

            def p_expressao_string(t):
                'expressao_str : STRING'

            def p_expressao_boolean(t):
                'booleano : TIPO_BOOL'

            def p_loop(t):
                '''loop : WHILE A_PARENTE comparacao F_PARENTE A_CHAVES listacorpo F_CHAVES
                        | WHILE A_PARENTE TIPO_BOOL F_PARENTE A_CHAVES listacorpo F_CHAVES
            			| WHILE A_PARENTE comparacao F_PARENTE A_CHAVES empty F_CHAVES
                        | WHILE A_PARENTE TIPO_BOOL F_PARENTE A_CHAVES empty F_CHAVES
                '''

            def p_loop_robo_on(t):
                '''loop_robo_on : WHILE A_PARENTE comparacao F_PARENTE A_CHAVES listacorpo_robo_on F_CHAVES
                        		| WHILE A_PARENTE TIPO_BOOL F_PARENTE A_CHAVES listacorpo_robo_on F_CHAVES
            					| WHILE A_PARENTE comparacao F_PARENTE A_CHAVES empty F_CHAVES
                        		| WHILE A_PARENTE TIPO_BOOL F_PARENTE A_CHAVES empty F_CHAVES
                '''

            def p_comparacao(t):
                '''comparacao : VARIAVEL OP_RELACIONAL NUMERO
                            | VARIAVEL OP_RELACIONAL VARIAVEL
            				| VARIAVEL OP_RELACIONAL NUM_FLOAT
            				| VARIAVEL OP_RELACIONAL TIPO_BOOL
                '''

            def p_condicional(t):
                '''condicional : IF A_PARENTE comparacao F_PARENTE A_CHAVES listacorpo F_CHAVES
                            | IF A_PARENTE comparacao F_PARENTE A_CHAVES listacorpo F_CHAVES ELSE A_CHAVES listacorpo F_CHAVES
            				| IF A_PARENTE comparacao F_PARENTE A_CHAVES empty F_CHAVES
                            | IF A_PARENTE comparacao F_PARENTE A_CHAVES empty F_CHAVES ELSE A_CHAVES empty F_CHAVES
            	'''

            def p_condicional_robo_on(t):
                '''condicional_robo_on : IF A_PARENTE comparacao F_PARENTE A_CHAVES listacorpo_robo_on F_CHAVES
                            		| IF A_PARENTE comparacao F_PARENTE A_CHAVES listacorpo_robo_on F_CHAVES ELSE A_CHAVES listacorpo_robo_on F_CHAVES
            						| IF A_PARENTE comparacao F_PARENTE A_CHAVES empty F_CHAVES
                            		| IF A_PARENTE comparacao F_PARENTE A_CHAVES empty F_CHAVES ELSE A_CHAVES empty F_CHAVES
            	'''

            def p_iniciarobo(t):
                '''iniciarobo : LIGA_ROBO QUEBRA_LINHA listacorpo_robo_on DESLIGA_ROBO QUEBRA_LINHA
            				| LIGA_ROBO QUEBRA_LINHA empty DESLIGA_ROBO QUEBRA_LINHA
            	'''

            def p_break(t):
                'break : BREAK QUEBRA_LINHA'

            def p_direcao(t):
                'direcao : DIR_ROBO QUEBRA_LINHA'

            def p_parar(t):
                'parar : PARAR QUEBRA_LINHA'

            def p_movimenta(t):
                'movimenta : MOVE_ROBO QUEBRA_LINHA'

            def p_mostrar(t):
                '''mostrar : EXIBA STRING QUEBRA_LINHA
                            | EXIBA VARIAVEL QUEBRA_LINHA
                            | EXIBA NUMERO QUEBRA_LINHA
                '''

            def p_comentario(t):
                'comentario : COMENTARIO'

            def p_error(t):
                # erro = ""
                erro = 'LexToken(' + str(t.type) + ',' + str(t.value) + ',' + str(t.lexer.lineno - num_linha()) + ')'
                listaSintaxe.append(erro)
                listaErroSintatico.append(str(t))

            def num_linha():
                cont = 0
                for i in code:
                    if i == '\n':
                        cont += 1
                return cont

            import ply.yacc as yacc
            parser = yacc.yacc()

            if not code:
                print("Erro ao receber dados")
            else:
                parser.parse(code)

            if len(listaErroSintatico) == 0:
                tmp = 'Compilacao terminada sem erro sintatico!'
                tmp2 = '-----------------------------------------------------'
                listaSintaxe.reverse()
                listaSintaxe.append(tmp2)
                listaSintaxe.append(tmp)
                listaSintaxe.reverse()
            else:

                tmp = '!Compilacao terminada com erro sintatico'
                tmp2 = '-----------------------------------------------------'
                listaSintaxe.reverse()
                listaSintaxe.append(tmp2)
                listaSintaxe.append(tmp)
                listaSintaxe.reverse()

        else:
            tmp = '!Compilacao terminada com erro lexico'
            tmp2 = '------------------------------------------------------'
            lista.reverse()
            lista.append(tmp2)
            lista.append(tmp)
            lista.reverse()

            listaSintaxe.append(tmp2)


    context['resposta'] = "\\n".join(lista)
    context['sintaxe']  = "\\n".join(listaSintaxe)
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