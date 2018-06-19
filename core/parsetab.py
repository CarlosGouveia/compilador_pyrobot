
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ATRIBUIR A_CHAVES A_PARENTE BREAK COMENTARIO DESLIGA_ROBO DIR_ROBO ELSE EXIBA FIM_CODE F_CHAVES F_PARENTE IF INI_CODE LIGA_ROBO MOVE_ROBO NUMERO NUM_FLOAT OP_ARITMETICO OP_RELACIONAL PARAR QUEBRA_LINHA STRING TIPO_BOOL TIPO_VAR VARIAVEL WHILEprograma : INI_CODE A_CHAVES listacorpo F_CHAVES FIM_CODE\n            \t\t\t\t| INI_CODE A_CHAVES empty F_CHAVES FIM_CODE\n            \t\t\t\t| comentario\n            \tcorpo : declaracao\n                        | atribuicao\n                        | loop\n                        | direcao\n                        | movimenta\n                        | iniciarobo\n                        | break\n                        | condicional\n                        | parar\n            \t\t\t| mostrar\n            \t\t\t| comentario\n                corpo_robo_on : declaracao\n                        | atribuicao\n                        | loop_robo_on\n                        | direcao\n                        | movimenta\n                        | break\n                        | condicional_robo_on\n                        | parar\n            \t\t\t| mostrar\n            \t\t\t| comentario\n                empty : listacorpo : corpo\n                            | corpo listacorpo\n                listacorpo_robo_on : corpo_robo_on\n                            | corpo_robo_on listacorpo_robo_on\n                declaracao : TIPO_VAR VARIAVEL QUEBRA_LINHAatribuicao : VARIAVEL ATRIBUIR operacao QUEBRA_LINHA\n            \t\t\t\t| VARIAVEL ATRIBUIR expressao_str QUEBRA_LINHA\n            \t\t\t\t| VARIAVEL ATRIBUIR expressao QUEBRA_LINHA\n            \t\t\t\t| VARIAVEL ATRIBUIR booleano QUEBRA_LINHA\n            \toperacao : expressao OP_ARITMETICO expressao\n            \t\t\t\t| expressao OP_ARITMETICO operacao\n            \texpressao : NUMERO\n            \t\t\t\t| NUM_FLOAT\n            \texpressao : VARIAVELexpressao_str : STRINGbooleano : TIPO_BOOLloop : WHILE A_PARENTE comparacao F_PARENTE A_CHAVES listacorpo F_CHAVES\n                        | WHILE A_PARENTE TIPO_BOOL F_PARENTE A_CHAVES listacorpo F_CHAVES\n            \t\t\t| WHILE A_PARENTE comparacao F_PARENTE A_CHAVES empty F_CHAVES\n                        | WHILE A_PARENTE TIPO_BOOL F_PARENTE A_CHAVES empty F_CHAVES\n                loop_robo_on : WHILE A_PARENTE comparacao F_PARENTE A_CHAVES listacorpo_robo_on F_CHAVES\n                        \t\t| WHILE A_PARENTE TIPO_BOOL F_PARENTE A_CHAVES listacorpo_robo_on F_CHAVES\n            \t\t\t\t\t| WHILE A_PARENTE comparacao F_PARENTE A_CHAVES empty F_CHAVES\n                        \t\t| WHILE A_PARENTE TIPO_BOOL F_PARENTE A_CHAVES empty F_CHAVES\n                comparacao : VARIAVEL OP_RELACIONAL NUMERO\n                            | VARIAVEL OP_RELACIONAL VARIAVEL\n            \t\t\t\t| VARIAVEL OP_RELACIONAL NUM_FLOAT\n            \t\t\t\t| VARIAVEL OP_RELACIONAL TIPO_BOOL\n                condicional : IF A_PARENTE comparacao F_PARENTE A_CHAVES listacorpo F_CHAVES\n                            | IF A_PARENTE comparacao F_PARENTE A_CHAVES listacorpo F_CHAVES ELSE A_CHAVES listacorpo F_CHAVES\n            \t\t\t\t| IF A_PARENTE comparacao F_PARENTE A_CHAVES empty F_CHAVES\n                            | IF A_PARENTE comparacao F_PARENTE A_CHAVES empty F_CHAVES ELSE A_CHAVES empty F_CHAVES\n            \tcondicional_robo_on : IF A_PARENTE comparacao F_PARENTE A_CHAVES listacorpo_robo_on F_CHAVES\n                            \t\t| IF A_PARENTE comparacao F_PARENTE A_CHAVES listacorpo_robo_on F_CHAVES ELSE A_CHAVES listacorpo_robo_on F_CHAVES\n            \t\t\t\t\t\t| IF A_PARENTE comparacao F_PARENTE A_CHAVES empty F_CHAVES\n                            \t\t| IF A_PARENTE comparacao F_PARENTE A_CHAVES empty F_CHAVES ELSE A_CHAVES empty F_CHAVES\n            \tiniciarobo : LIGA_ROBO QUEBRA_LINHA listacorpo_robo_on DESLIGA_ROBO QUEBRA_LINHA\n            \t\t\t\t| LIGA_ROBO QUEBRA_LINHA empty DESLIGA_ROBO QUEBRA_LINHA\n            \tbreak : BREAK QUEBRA_LINHAdirecao : DIR_ROBO QUEBRA_LINHAparar : PARAR QUEBRA_LINHAmovimenta : MOVE_ROBO QUEBRA_LINHAmostrar : EXIBA STRING QUEBRA_LINHA\n                            | EXIBA VARIAVEL QUEBRA_LINHA\n                            | EXIBA NUMERO QUEBRA_LINHA\n                comentario : COMENTARIO'
    
_lr_action_items = {'A_PARENTE':([9,22,47,53,],[31,41,80,83,]),'STRING':([24,40,],[43,65,]),'OP_RELACIONAL':([60,],[84,]),'BREAK':([3,5,7,8,11,15,16,18,23,25,26,27,28,29,30,34,35,38,39,45,48,50,51,52,54,55,56,57,58,59,64,76,77,78,87,88,89,90,93,95,102,105,106,116,117,118,119,120,121,122,123,124,133,134,135,136,137,138,140,145,147,148,151,152,],[-71,12,-9,-14,12,-4,-10,-11,-7,-12,-8,-13,-6,-5,12,-64,-65,-66,-67,-21,-16,12,-24,-18,-15,-22,-19,-23,-17,-20,-30,-69,-68,-70,-33,-31,-32,-34,-62,-63,12,12,12,12,12,12,-56,-54,-45,-43,-44,-42,-58,-60,-47,-49,-46,-48,12,12,-57,-55,-59,-61,]),'TIPO_VAR':([3,5,7,8,11,15,16,18,23,25,26,27,28,29,30,34,35,38,39,45,48,50,51,52,54,55,56,57,58,59,64,76,77,78,87,88,89,90,93,95,102,105,106,116,117,118,119,120,121,122,123,124,133,134,135,136,137,138,140,145,147,148,151,152,],[-71,17,-9,-14,17,-4,-10,-11,-7,-12,-8,-13,-6,-5,17,-64,-65,-66,-67,-21,-16,17,-24,-18,-15,-22,-19,-23,-17,-20,-30,-69,-68,-70,-33,-31,-32,-34,-62,-63,17,17,17,17,17,17,-56,-54,-45,-43,-44,-42,-58,-60,-47,-49,-46,-48,17,17,-57,-55,-59,-61,]),'F_CHAVES':([3,5,7,8,10,11,14,15,16,18,23,25,26,27,28,29,33,34,35,38,39,45,48,50,51,52,54,55,56,57,58,59,64,76,77,78,82,87,88,89,90,93,95,102,105,106,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,133,134,135,136,137,138,139,143,144,146,147,148,149,150,151,152,],[-71,-25,-9,-14,32,-26,36,-4,-10,-11,-7,-12,-8,-13,-6,-5,-27,-64,-65,-66,-67,-21,-16,-28,-24,-18,-15,-22,-19,-23,-17,-20,-30,-69,-68,-70,-29,-33,-31,-32,-34,-62,-63,-25,-25,-25,119,120,121,122,123,124,-25,-25,-25,-56,-54,-45,-43,-44,-42,133,134,135,136,137,138,-58,-60,-47,-49,-46,-48,-25,147,148,-25,-57,-55,151,152,-59,-61,]),'NUM_FLOAT':([40,84,86,],[70,99,70,]),'LIGA_ROBO':([3,5,7,8,11,15,16,18,23,25,26,27,28,29,34,35,38,39,64,76,77,78,87,88,89,90,93,95,102,105,106,119,120,121,122,123,124,140,147,148,],[-71,6,-9,-14,6,-4,-10,-11,-7,-12,-8,-13,-6,-5,-64,-65,-66,-67,-30,-69,-68,-70,-33,-31,-32,-34,-62,-63,6,6,6,-56,-54,-45,-43,-44,-42,6,-57,-55,]),'QUEBRA_LINHA':([6,12,13,19,20,37,42,43,44,65,66,67,68,69,70,71,72,73,79,81,103,104,],[30,34,35,38,39,64,76,77,78,-40,87,-39,-37,-41,-38,88,89,90,93,95,-35,-36,]),'IF':([3,5,7,8,11,15,16,18,23,25,26,27,28,29,30,34,35,38,39,45,48,50,51,52,54,55,56,57,58,59,64,76,77,78,87,88,89,90,93,95,102,105,106,116,117,118,119,120,121,122,123,124,133,134,135,136,137,138,140,145,147,148,151,152,],[-71,9,-9,-14,9,-4,-10,-11,-7,-12,-8,-13,-6,-5,47,-64,-65,-66,-67,-21,-16,47,-24,-18,-15,-22,-19,-23,-17,-20,-30,-69,-68,-70,-33,-31,-32,-34,-62,-63,9,9,9,47,47,47,-56,-54,-45,-43,-44,-42,-58,-60,-47,-49,-46,-48,9,47,-57,-55,-59,-61,]),'ATRIBUIR':([21,],[40,]),'COMENTARIO':([0,3,5,7,8,11,15,16,18,23,25,26,27,28,29,30,34,35,38,39,45,48,50,51,52,54,55,56,57,58,59,64,76,77,78,87,88,89,90,93,95,102,105,106,116,117,118,119,120,121,122,123,124,133,134,135,136,137,138,140,145,147,148,151,152,],[3,-71,3,-9,-14,3,-4,-10,-11,-7,-12,-8,-13,-6,-5,3,-64,-65,-66,-67,-21,-16,3,-24,-18,-15,-22,-19,-23,-17,-20,-30,-69,-68,-70,-33,-31,-32,-34,-62,-63,3,3,3,3,3,3,-56,-54,-45,-43,-44,-42,-58,-60,-47,-49,-46,-48,3,3,-57,-55,-59,-61,]),'PARAR':([3,5,7,8,11,15,16,18,23,25,26,27,28,29,30,34,35,38,39,45,48,50,51,52,54,55,56,57,58,59,64,76,77,78,87,88,89,90,93,95,102,105,106,116,117,118,119,120,121,122,123,124,133,134,135,136,137,138,140,145,147,148,151,152,],[-71,19,-9,-14,19,-4,-10,-11,-7,-12,-8,-13,-6,-5,19,-64,-65,-66,-67,-21,-16,19,-24,-18,-15,-22,-19,-23,-17,-20,-30,-69,-68,-70,-33,-31,-32,-34,-62,-63,19,19,19,19,19,19,-56,-54,-45,-43,-44,-42,-58,-60,-47,-49,-46,-48,19,19,-57,-55,-59,-61,]),'FIM_CODE':([32,36,],[62,63,]),'MOVE_ROBO':([3,5,7,8,11,15,16,18,23,25,26,27,28,29,30,34,35,38,39,45,48,50,51,52,54,55,56,57,58,59,64,76,77,78,87,88,89,90,93,95,102,105,106,116,117,118,119,120,121,122,123,124,133,134,135,136,137,138,140,145,147,148,151,152,],[-71,20,-9,-14,20,-4,-10,-11,-7,-12,-8,-13,-6,-5,20,-64,-65,-66,-67,-21,-16,20,-24,-18,-15,-22,-19,-23,-17,-20,-30,-69,-68,-70,-33,-31,-32,-34,-62,-63,20,20,20,20,20,20,-56,-54,-45,-43,-44,-42,-58,-60,-47,-49,-46,-48,20,20,-57,-55,-59,-61,]),'INI_CODE':([0,],[2,]),'DIR_ROBO':([3,5,7,8,11,15,16,18,23,25,26,27,28,29,30,34,35,38,39,45,48,50,51,52,54,55,56,57,58,59,64,76,77,78,87,88,89,90,93,95,102,105,106,116,117,118,119,120,121,122,123,124,133,134,135,136,137,138,140,145,147,148,151,152,],[-71,13,-9,-14,13,-4,-10,-11,-7,-12,-8,-13,-6,-5,13,-64,-65,-66,-67,-21,-16,13,-24,-18,-15,-22,-19,-23,-17,-20,-30,-69,-68,-70,-33,-31,-32,-34,-62,-63,13,13,13,13,13,13,-56,-54,-45,-43,-44,-42,-58,-60,-47,-49,-46,-48,13,13,-57,-55,-59,-61,]),'VARIAVEL':([3,5,7,8,11,15,16,17,18,23,24,25,26,27,28,29,30,31,34,35,38,39,40,41,45,48,50,51,52,54,55,56,57,58,59,64,76,77,78,80,83,84,86,87,88,89,90,93,95,102,105,106,116,117,118,119,120,121,122,123,124,133,134,135,136,137,138,140,145,147,148,151,152,],[-71,21,-9,-14,21,-4,-10,37,-11,-7,42,-12,-8,-13,-6,-5,21,60,-64,-65,-66,-67,67,60,-21,-16,21,-24,-18,-15,-22,-19,-23,-17,-20,-30,-69,-68,-70,60,60,101,67,-33,-31,-32,-34,-62,-63,21,21,21,21,21,21,-56,-54,-45,-43,-44,-42,-58,-60,-47,-49,-46,-48,21,21,-57,-55,-59,-61,]),'NUMERO':([24,40,84,86,],[44,68,100,68,]),'WHILE':([3,5,7,8,11,15,16,18,23,25,26,27,28,29,30,34,35,38,39,45,48,50,51,52,54,55,56,57,58,59,64,76,77,78,87,88,89,90,93,95,102,105,106,116,117,118,119,120,121,122,123,124,133,134,135,136,137,138,140,145,147,148,151,152,],[-71,22,-9,-14,22,-4,-10,-11,-7,-12,-8,-13,-6,-5,53,-64,-65,-66,-67,-21,-16,53,-24,-18,-15,-22,-19,-23,-17,-20,-30,-69,-68,-70,-33,-31,-32,-34,-62,-63,22,22,22,53,53,53,-56,-54,-45,-43,-44,-42,-58,-60,-47,-49,-46,-48,22,53,-57,-55,-59,-61,]),'OP_ARITMETICO':([66,67,68,70,103,],[86,-39,-37,-38,86,]),'A_CHAVES':([2,85,91,92,107,108,109,131,132,141,142,],[5,102,105,106,116,117,118,139,140,145,146,]),'EXIBA':([3,5,7,8,11,15,16,18,23,25,26,27,28,29,30,34,35,38,39,45,48,50,51,52,54,55,56,57,58,59,64,76,77,78,87,88,89,90,93,95,102,105,106,116,117,118,119,120,121,122,123,124,133,134,135,136,137,138,140,145,147,148,151,152,],[-71,24,-9,-14,24,-4,-10,-11,-7,-12,-8,-13,-6,-5,24,-64,-65,-66,-67,-21,-16,24,-24,-18,-15,-22,-19,-23,-17,-20,-30,-69,-68,-70,-33,-31,-32,-34,-62,-63,24,24,24,24,24,24,-56,-54,-45,-43,-44,-42,-58,-60,-47,-49,-46,-48,24,24,-57,-55,-59,-61,]),'$end':([1,3,4,62,63,],[0,-71,-3,-2,-1,]),'TIPO_BOOL':([40,41,83,84,],[69,74,96,98,]),'ELSE':([119,120,133,134,],[131,132,141,142,]),'F_PARENTE':([61,74,75,94,96,97,98,99,100,101,],[85,91,92,107,108,109,-53,-52,-50,-51,]),'DESLIGA_ROBO':([3,30,34,35,38,39,45,46,48,49,50,51,52,54,55,56,57,58,59,64,76,77,78,82,87,88,89,90,133,134,135,136,137,138,151,152,],[-71,-25,-64,-65,-66,-67,-21,79,-16,81,-28,-24,-18,-15,-22,-19,-23,-17,-20,-30,-69,-68,-70,-29,-33,-31,-32,-34,-58,-60,-47,-49,-46,-48,-59,-61,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'condicional_robo_on':([30,50,116,117,118,145,],[45,45,45,45,45,45,]),'expressao':([40,86,],[66,103,]),'listacorpo_robo_on':([30,50,116,117,118,145,],[46,82,125,127,129,149,]),'condicional':([5,11,102,105,106,140,],[18,18,18,18,18,18,]),'programa':([0,],[1,]),'atribuicao':([5,11,30,50,102,105,106,116,117,118,140,145,],[29,29,48,48,29,29,29,48,48,48,29,48,]),'empty':([5,30,102,105,106,116,117,118,139,146,],[10,49,110,112,114,126,128,130,143,150,]),'corpo_robo_on':([30,50,116,117,118,145,],[50,50,50,50,50,50,]),'corpo':([5,11,102,105,106,140,],[11,11,11,11,11,11,]),'comentario':([0,5,11,30,50,102,105,106,116,117,118,140,145,],[4,8,8,51,51,8,8,8,51,51,51,8,51,]),'expressao_str':([40,],[72,]),'booleano':([40,],[73,]),'iniciarobo':([5,11,102,105,106,140,],[7,7,7,7,7,7,]),'direcao':([5,11,30,50,102,105,106,116,117,118,140,145,],[23,23,52,52,23,23,23,52,52,52,23,52,]),'listacorpo':([5,11,102,105,106,140,],[14,33,111,113,115,144,]),'declaracao':([5,11,30,50,102,105,106,116,117,118,140,145,],[15,15,54,54,15,15,15,54,54,54,15,54,]),'parar':([5,11,30,50,102,105,106,116,117,118,140,145,],[25,25,55,55,25,25,25,55,55,55,25,55,]),'movimenta':([5,11,30,50,102,105,106,116,117,118,140,145,],[26,26,56,56,26,26,26,56,56,56,26,56,]),'mostrar':([5,11,30,50,102,105,106,116,117,118,140,145,],[27,27,57,57,27,27,27,57,57,57,27,57,]),'loop_robo_on':([30,50,116,117,118,145,],[58,58,58,58,58,58,]),'loop':([5,11,102,105,106,140,],[28,28,28,28,28,28,]),'break':([5,11,30,50,102,105,106,116,117,118,140,145,],[16,16,59,59,16,16,16,59,59,59,16,59,]),'operacao':([40,86,],[71,104,]),'comparacao':([31,41,80,83,],[61,75,94,97,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programa","S'",1,None,None,None),
  ('programa -> INI_CODE A_CHAVES listacorpo F_CHAVES FIM_CODE','programa',5,'p_programa','views.py',335),
  ('programa -> INI_CODE A_CHAVES empty F_CHAVES FIM_CODE','programa',5,'p_programa','views.py',336),
  ('programa -> comentario','programa',1,'p_programa','views.py',337),
  ('corpo -> declaracao','corpo',1,'p_corpo','views.py',341),
  ('corpo -> atribuicao','corpo',1,'p_corpo','views.py',342),
  ('corpo -> loop','corpo',1,'p_corpo','views.py',343),
  ('corpo -> direcao','corpo',1,'p_corpo','views.py',344),
  ('corpo -> movimenta','corpo',1,'p_corpo','views.py',345),
  ('corpo -> iniciarobo','corpo',1,'p_corpo','views.py',346),
  ('corpo -> break','corpo',1,'p_corpo','views.py',347),
  ('corpo -> condicional','corpo',1,'p_corpo','views.py',348),
  ('corpo -> parar','corpo',1,'p_corpo','views.py',349),
  ('corpo -> mostrar','corpo',1,'p_corpo','views.py',350),
  ('corpo -> comentario','corpo',1,'p_corpo','views.py',351),
  ('corpo_robo_on -> declaracao','corpo_robo_on',1,'p_corpo_robo_on','views.py',355),
  ('corpo_robo_on -> atribuicao','corpo_robo_on',1,'p_corpo_robo_on','views.py',356),
  ('corpo_robo_on -> loop_robo_on','corpo_robo_on',1,'p_corpo_robo_on','views.py',357),
  ('corpo_robo_on -> direcao','corpo_robo_on',1,'p_corpo_robo_on','views.py',358),
  ('corpo_robo_on -> movimenta','corpo_robo_on',1,'p_corpo_robo_on','views.py',359),
  ('corpo_robo_on -> break','corpo_robo_on',1,'p_corpo_robo_on','views.py',360),
  ('corpo_robo_on -> condicional_robo_on','corpo_robo_on',1,'p_corpo_robo_on','views.py',361),
  ('corpo_robo_on -> parar','corpo_robo_on',1,'p_corpo_robo_on','views.py',362),
  ('corpo_robo_on -> mostrar','corpo_robo_on',1,'p_corpo_robo_on','views.py',363),
  ('corpo_robo_on -> comentario','corpo_robo_on',1,'p_corpo_robo_on','views.py',364),
  ('empty -> <empty>','empty',0,'p_empty','views.py',368),
  ('listacorpo -> corpo','listacorpo',1,'p_listacorpo','views.py',372),
  ('listacorpo -> corpo listacorpo','listacorpo',2,'p_listacorpo','views.py',373),
  ('listacorpo_robo_on -> corpo_robo_on','listacorpo_robo_on',1,'p_listacorpo_robo_on','views.py',377),
  ('listacorpo_robo_on -> corpo_robo_on listacorpo_robo_on','listacorpo_robo_on',2,'p_listacorpo_robo_on','views.py',378),
  ('declaracao -> TIPO_VAR VARIAVEL QUEBRA_LINHA','declaracao',3,'p_declaracao','views.py',382),
  ('atribuicao -> VARIAVEL ATRIBUIR operacao QUEBRA_LINHA','atribuicao',4,'p_atribuicao','views.py',385),
  ('atribuicao -> VARIAVEL ATRIBUIR expressao_str QUEBRA_LINHA','atribuicao',4,'p_atribuicao','views.py',386),
  ('atribuicao -> VARIAVEL ATRIBUIR expressao QUEBRA_LINHA','atribuicao',4,'p_atribuicao','views.py',387),
  ('atribuicao -> VARIAVEL ATRIBUIR booleano QUEBRA_LINHA','atribuicao',4,'p_atribuicao','views.py',388),
  ('operacao -> expressao OP_ARITMETICO expressao','operacao',3,'p_operacao','views.py',392),
  ('operacao -> expressao OP_ARITMETICO operacao','operacao',3,'p_operacao','views.py',393),
  ('expressao -> NUMERO','expressao',1,'p_expressao_num','views.py',397),
  ('expressao -> NUM_FLOAT','expressao',1,'p_expressao_num','views.py',398),
  ('expressao -> VARIAVEL','expressao',1,'p_expressao_var','views.py',402),
  ('expressao_str -> STRING','expressao_str',1,'p_expressao_string','views.py',405),
  ('booleano -> TIPO_BOOL','booleano',1,'p_expressao_boolean','views.py',408),
  ('loop -> WHILE A_PARENTE comparacao F_PARENTE A_CHAVES listacorpo F_CHAVES','loop',7,'p_loop','views.py',411),
  ('loop -> WHILE A_PARENTE TIPO_BOOL F_PARENTE A_CHAVES listacorpo F_CHAVES','loop',7,'p_loop','views.py',412),
  ('loop -> WHILE A_PARENTE comparacao F_PARENTE A_CHAVES empty F_CHAVES','loop',7,'p_loop','views.py',413),
  ('loop -> WHILE A_PARENTE TIPO_BOOL F_PARENTE A_CHAVES empty F_CHAVES','loop',7,'p_loop','views.py',414),
  ('loop_robo_on -> WHILE A_PARENTE comparacao F_PARENTE A_CHAVES listacorpo_robo_on F_CHAVES','loop_robo_on',7,'p_loop_robo_on','views.py',418),
  ('loop_robo_on -> WHILE A_PARENTE TIPO_BOOL F_PARENTE A_CHAVES listacorpo_robo_on F_CHAVES','loop_robo_on',7,'p_loop_robo_on','views.py',419),
  ('loop_robo_on -> WHILE A_PARENTE comparacao F_PARENTE A_CHAVES empty F_CHAVES','loop_robo_on',7,'p_loop_robo_on','views.py',420),
  ('loop_robo_on -> WHILE A_PARENTE TIPO_BOOL F_PARENTE A_CHAVES empty F_CHAVES','loop_robo_on',7,'p_loop_robo_on','views.py',421),
  ('comparacao -> VARIAVEL OP_RELACIONAL NUMERO','comparacao',3,'p_comparacao','views.py',425),
  ('comparacao -> VARIAVEL OP_RELACIONAL VARIAVEL','comparacao',3,'p_comparacao','views.py',426),
  ('comparacao -> VARIAVEL OP_RELACIONAL NUM_FLOAT','comparacao',3,'p_comparacao','views.py',427),
  ('comparacao -> VARIAVEL OP_RELACIONAL TIPO_BOOL','comparacao',3,'p_comparacao','views.py',428),
  ('condicional -> IF A_PARENTE comparacao F_PARENTE A_CHAVES listacorpo F_CHAVES','condicional',7,'p_condicional','views.py',432),
  ('condicional -> IF A_PARENTE comparacao F_PARENTE A_CHAVES listacorpo F_CHAVES ELSE A_CHAVES listacorpo F_CHAVES','condicional',11,'p_condicional','views.py',433),
  ('condicional -> IF A_PARENTE comparacao F_PARENTE A_CHAVES empty F_CHAVES','condicional',7,'p_condicional','views.py',434),
  ('condicional -> IF A_PARENTE comparacao F_PARENTE A_CHAVES empty F_CHAVES ELSE A_CHAVES empty F_CHAVES','condicional',11,'p_condicional','views.py',435),
  ('condicional_robo_on -> IF A_PARENTE comparacao F_PARENTE A_CHAVES listacorpo_robo_on F_CHAVES','condicional_robo_on',7,'p_condicional_robo_on','views.py',439),
  ('condicional_robo_on -> IF A_PARENTE comparacao F_PARENTE A_CHAVES listacorpo_robo_on F_CHAVES ELSE A_CHAVES listacorpo_robo_on F_CHAVES','condicional_robo_on',11,'p_condicional_robo_on','views.py',440),
  ('condicional_robo_on -> IF A_PARENTE comparacao F_PARENTE A_CHAVES empty F_CHAVES','condicional_robo_on',7,'p_condicional_robo_on','views.py',441),
  ('condicional_robo_on -> IF A_PARENTE comparacao F_PARENTE A_CHAVES empty F_CHAVES ELSE A_CHAVES empty F_CHAVES','condicional_robo_on',11,'p_condicional_robo_on','views.py',442),
  ('iniciarobo -> LIGA_ROBO QUEBRA_LINHA listacorpo_robo_on DESLIGA_ROBO QUEBRA_LINHA','iniciarobo',5,'p_iniciarobo','views.py',446),
  ('iniciarobo -> LIGA_ROBO QUEBRA_LINHA empty DESLIGA_ROBO QUEBRA_LINHA','iniciarobo',5,'p_iniciarobo','views.py',447),
  ('break -> BREAK QUEBRA_LINHA','break',2,'p_break','views.py',451),
  ('direcao -> DIR_ROBO QUEBRA_LINHA','direcao',2,'p_direcao','views.py',454),
  ('parar -> PARAR QUEBRA_LINHA','parar',2,'p_parar','views.py',457),
  ('movimenta -> MOVE_ROBO QUEBRA_LINHA','movimenta',2,'p_movimenta','views.py',460),
  ('mostrar -> EXIBA STRING QUEBRA_LINHA','mostrar',3,'p_mostrar','views.py',463),
  ('mostrar -> EXIBA VARIAVEL QUEBRA_LINHA','mostrar',3,'p_mostrar','views.py',464),
  ('mostrar -> EXIBA NUMERO QUEBRA_LINHA','mostrar',3,'p_mostrar','views.py',465),
  ('comentario -> COMENTARIO','comentario',1,'p_comentario','views.py',469),
]
