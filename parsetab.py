
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ALTER AND AS ASC ASTERISCO BIGINT BOOLEAN BY CADENADOBLE CADENASIMPLE CHAR CHARACTER COMA COMENTARIOMULTI COMENTARIONORMAL CONSTRAINT CREATE CURRENT_USER DATABASE DATABASES DECIMAL DECIMAL DEFAULT DELETE DESC DIFERENTE DISTINCT DOUBLE DROP ENTERO EXISTS FECHA FIRST FROM FULL GROUP HAVING ID IF IGUAL INNER INSERT INTEGER INTO JOIN LAST LEFT LIKE MAYOR MAYORIGUAL MENOR MENORIGUAL MODE MONEY NEGACION NOT NULL NULLS ON OR OUTER OWNER PARDER PARIZQ PRECISION PUNTO PUNTOCOMA REAL RENAME REPLACE RIGHT SELECT SESSION_USER SET SHOW SMALLINT TABLE TEXT TO TYPE UPDATE USING VALUES VARCHAR VARYING WHEREINICIO          : INSTRUCCIONESINSTRUCCIONES     : INSTRUCCIONES INSTRUCCIONINSTRUCCIONES    : INSTRUCCIONINSTRUCCION  : DQL_COMANDOS\n                    | DDL_COMANDOSDQL_COMANDOS       : SELECT LISTA_CAMPOS FROM NOMBRES_TABLAS CUERPO PUNTOCOMADQL_COMANDOS       : SELECT LISTA_CAMPOS FROM NOMBRES_TABLAS  PUNTOCOMADQL_COMANDOS       : SELECT  DISTINCTNT  LISTA_CAMPOS FROM NOMBRES_TABLAS CUERPO PUNTOCOMADQL_COMANDOS       : SELECT DISTINCTNT LISTA_CAMPOS FROM NOMBRES_TABLAS  PUNTOCOMALISTA_CAMPOS       : LISTA_CAMPOS LISTALISTA_CAMPOS    : LISTALISTA          : NOMBRE_T PUNTO CAMPOS SLISTA          : NOMBRE_T PUNTO CAMPOSLISTA          : CAMPOS SLISTA          : CAMPOSCAMPOS          : IDCAMPOS          : ASTERISCONOMBRE_T        : IDALIAS          : IDS          : COMA LISTAS          : AS ALIASDISTINCTNT          : DISTINCTNOMBRES_TABLAS       : NOMBRES_TABLAS TABLANOMBRES_TABLAS    : TABLATABLA   : NOMBRE_TTABLA   : NOMBRE_T S1S1          : COMA TABLAS1          : AS ALIASCUERPO   : WHERE CONDICIONESCUERPO   : MORESMORES       : MORES MOREEMORES    : MOREEMOREE   : INNERSMOREE   : GROUPSCONDICIONES : CONDICIONES CONDICIONCONDICIONES : CONDICIONCONDICION : CONDICION_REL SIMBOLO_LOGICO  CONDICION_REL  OTRO_LOGICOCONDICION : CONDICION_REL SIMBOLO_LOGICO CONDICION_RELCONDICION : CONDICION_RELCONDICION_REL : EXPRESIONNE OPERADOR EXPRESIONNECONDICION_REL : SIMBOLO_NEG  EXPRESIONNECONDICION_REL : EXPRESIONNEOTRO_LOGICO : SIMBOLO_LOGICO CONDICIONESEXPRESIONNE : NOMBRE_C PUNTO CAMPOSCEXPRESIONNE : CAMPOSC SIMBOLO_LOGICO : AND\n                      | OR SIMBOLO_NEG  :  NEGACIONNOMBRE_C : IDCAMPOSC     :  ID\n                    | ENTERO\n                    | DECIMAL\n                    | CADENASIMPLE\n                    | CADENADOBLE OPERADOR     : IGUAL\n                    | DIFERENTE\n                    | MAYOR\n                    | MENOR\n                    | MENORIGUAL\n                    | MAYORIGUAL INNERS : INNERS INNERRINNERS : INNERRINNERR : TIPOS_INNER JOIN TABLA_REF ON CONDICIONESINNERR :  JOIN TABLA_REF ON CONDICIONESINNERR : TIPOS_INNER JOIN TABLA_REF USING PARIZQ SUB_COLUMN PARDERINNERR :  JOIN TABLA_REF USING PARIZQ SUB_COLUMN PARDER INNERR   : WHERE CONDICIONESSUB_COLUMN  :  JOIN EXPRESIONNESUB_COLUMN  :  EXPRESIONNE TIPOS_INNER :  INNER OUTER TIPOS_INNER :  INNER TIPOS_INNER :  LEFT OUTER TIPOS_INNER :  LEFT TIPOS_INNER :  RIGHT OUTER TIPOS_INNER :  RIGHT TIPOS_INNER :  FULL OUTER TIPOS_INNER :  FULLTABLA_REF : IDTABLA_REF : ID AS IDGROUPS    : GROUPPGROUPP    : GROUP BY EXPRE_LIST MORE_ORDERGROUPP    : GROUP BY EXPRE_LISTEXPRE_LIST : EXPRE_LIST  EXPRESEXPRE_LIST    : EXPRESEXPRES    :  NOMBRE_T PUNTO CAMPOS S2EXPRES    :  NOMBRE_T PUNTO CAMPOS EXPRES    :  CAMPOS S2 EXPRES    :  CAMPOS EXPRES    :  NOMBRE_T PUNTO CAMPOS S2 STATE EXPRES    :  NOMBRE_T PUNTO CAMPOS STATEEXPRES    :  CAMPOS S2 STATEEXPRES    :  CAMPOS STATE S2 : AS ALIASMORE_ORDER  :  HAVING CONDICIONESSTATE : ASCSTATE : ASC NULLS FIRSTSTATE : ASC NULLS LASTSTATE : DESC STATE : DESC NULLS FIRSTSTATE : DESC NULLS LASTDQL_COMANDOS       : CREATE TABLE NOMBRES_TABLAS PARIZQ  CUERPO_CREATE_TABLE PARDER PUNTOCOMACUERPO_CREATE_TABLE       : LISTA_DE_COLUMNASLISTA_DE_COLUMNAS       : LISTA_DE_COLUMNAS LISTA2LISTA_DE_COLUMNAS    : LISTA2LISTA2          : NOMBRE_T TIPO_CAMPO VALIDACIONES_CREATE_TABLE COMALISTA2          : NOMBRE_T TIPO_CAMPO VALIDACIONES_CREATE_TABLETIPO_CAMPO   : SMALLINT\n                    | INTEGER\n                    | BIGINT\n                    | DECIMAL\n                    | REAL\n                    | MONEY\n                    | DOUBLE PRECISION\n                    | CHARACTER VARYING PARIZQ ENTERO PARDER\n                    | VARCHAR PARIZQ ENTERO PARDER\n                    | CHARACTER PARIZQ ENTERO PARDER\n                    | CHAR PARIZQ ENTERO PARDER\n                    | TEXT\n                    | BOOLEANVALIDACIONES_CREATE_TABLE    : LISTA3LISTA3          :  VALIDACION_CAMPO_CREATE LISTA3          :  VALIDACION_CAMPO_CREATE_VACIO VALIDACION_CAMPO_CREATE  : NOT NULL\n                                | DEFAULT CADENASIMPLE\n                                | DEFAULT CADENADOBLE\n                                | DEFAULT DECIMAL\n                                | DEFAULT ENTERO VALIDACION_CAMPO_CREATE_VACIO  :  VALIDACION_CAMPO_CREATE  : NULL  DDL_COMANDOS : CREATE_DATABASE\n                    | SHOW_DATABASES\n                    | ALTER_DATABASE\n                    | DROP_DATABASECREATE_DATABASE : CREATE REPLACE_OP DATABASE IF_NOT_EXISTIS ID OWNER_DATABASE MODE_DATABASEREPLACE_OP : OR REPLACEREPLACE_OP : IF_NOT_EXISTIS : IF NOT EXISTSIF_NOT_EXISTIS : OWNER_DATABASE : OWNER IGUAL IDOWNER_DATABASE : MODE_DATABASE : MODE IGUAL ENTEROMODE_DATABASE : SHOW_DATABASES : SHOW DATABASES SHOW_DATABASES_LIKESHOW_DATABASES_LIKE : LIKE CADENADOBLESHOW_DATABASES_LIKE : ALTER_DATABASE : ALTER DATABASE ID ALTER_DATABASE_OPALTER_DATABASE_OP : RENAME TO ID\n                        |  OWNER TO ALTER_TABLE_OP_OWALTER_TABLE_OP_OW : ID\n                        |  CURRENT_USER\n                        |  SESSION_USERALTER_DATABASE_OP : DROP_DATABASE : DROP DATABASE IF_EXISTS_DATABASE IDIF_EXISTS_DATABASE : IF EXISTSIF_EXISTS_DATABASE : '
    
_lr_action_items = {'SELECT':([0,2,3,4,5,8,9,10,11,15,27,43,45,62,63,66,69,92,96,122,138,141,142,143,144,145,168,169,182,214,232,],[6,6,-3,-4,-5,-130,-131,-132,-133,-2,-145,-143,-152,-144,-146,-153,-7,-140,-6,-9,-142,-147,-148,-149,-150,-151,-8,-101,-134,-139,-141,]),'CREATE':([0,2,3,4,5,8,9,10,11,15,27,43,45,62,63,66,69,92,96,122,138,141,142,143,144,145,168,169,182,214,232,],[7,7,-3,-4,-5,-130,-131,-132,-133,-2,-145,-143,-152,-144,-146,-153,-7,-140,-6,-9,-142,-147,-148,-149,-150,-151,-8,-101,-134,-139,-141,]),'SHOW':([0,2,3,4,5,8,9,10,11,15,27,43,45,62,63,66,69,92,96,122,138,141,142,143,144,145,168,169,182,214,232,],[12,12,-3,-4,-5,-130,-131,-132,-133,-2,-145,-143,-152,-144,-146,-153,-7,-140,-6,-9,-142,-147,-148,-149,-150,-151,-8,-101,-134,-139,-141,]),'ALTER':([0,2,3,4,5,8,9,10,11,15,27,43,45,62,63,66,69,92,96,122,138,141,142,143,144,145,168,169,182,214,232,],[13,13,-3,-4,-5,-130,-131,-132,-133,-2,-145,-143,-152,-144,-146,-153,-7,-140,-6,-9,-142,-147,-148,-149,-150,-151,-8,-101,-134,-139,-141,]),'DROP':([0,2,3,4,5,8,9,10,11,15,27,43,45,62,63,66,69,92,96,122,138,141,142,143,144,145,168,169,182,214,232,],[14,14,-3,-4,-5,-130,-131,-132,-133,-2,-145,-143,-152,-144,-146,-153,-7,-140,-6,-9,-142,-147,-148,-149,-150,-151,-8,-101,-134,-139,-141,]),'$end':([1,2,3,4,5,8,9,10,11,15,27,43,45,62,63,66,69,92,96,122,138,141,142,143,144,145,168,169,182,214,232,],[0,-1,-3,-4,-5,-130,-131,-132,-133,-2,-145,-143,-152,-144,-146,-153,-7,-140,-6,-9,-142,-147,-148,-149,-150,-151,-8,-101,-134,-139,-141,]),'DISTINCT':([6,],[19,]),'ID':([6,16,17,18,19,21,22,23,24,28,29,30,31,32,33,34,35,36,37,38,39,40,41,46,48,49,50,51,52,53,54,55,56,57,58,59,60,67,70,78,84,85,87,88,90,91,94,95,97,98,99,100,101,103,104,105,106,107,108,109,111,113,116,124,125,126,127,128,129,130,131,136,137,140,146,147,148,149,150,151,152,153,154,155,156,157,158,159,161,163,164,165,167,170,171,172,173,175,177,184,185,186,187,188,189,191,192,195,196,197,198,199,200,201,202,203,204,205,206,207,208,215,216,217,218,219,222,223,224,225,229,230,231,233,237,238,239,240,241,242,243,245,],[22,22,22,-11,-22,-15,-16,-17,40,45,-155,40,-10,22,51,-14,22,54,40,-24,-25,-18,-138,66,40,40,-13,-16,-20,-21,-19,40,-23,-26,40,54,92,-154,105,115,40,-12,40,-104,-27,-28,141,143,105,-36,-39,-42,105,-45,-48,-50,-51,-52,-53,-54,105,115,22,-103,-128,-107,-108,-109,-110,-111,-112,-118,-119,-137,-35,105,-46,-47,105,-55,-56,-57,-58,-59,-60,-41,188,105,105,193,22,-84,-88,-106,-120,-121,-122,-129,-113,214,-38,-40,-44,-50,105,105,105,-83,105,51,-87,-92,54,-95,-98,-105,-123,-124,-125,-126,-127,105,-37,105,105,105,105,-86,-91,-93,-116,-115,-117,105,-85,-90,-96,-97,-99,-100,-114,-89,]),'ASTERISCO':([6,16,17,18,19,21,22,23,31,32,33,34,35,50,51,52,53,54,85,116,164,165,167,195,197,198,199,201,202,223,224,225,237,238,239,240,241,242,245,],[23,23,23,-11,-22,-15,-16,-17,-10,23,23,-14,23,-13,-16,-20,-21,-19,-12,23,23,-84,-88,-83,23,-87,-92,-95,-98,-86,-91,-93,-85,-90,-96,-97,-99,-100,-89,]),'TABLE':([7,],[24,]),'OR':([7,99,100,103,105,106,107,108,109,157,185,186,187,188,],[26,149,-42,-45,-50,-51,-52,-53,-54,-41,149,-40,-44,-50,]),'DATABASE':([7,13,14,25,42,],[-136,28,29,41,-135,]),'DATABASES':([12,],[27,]),'FROM':([16,18,21,22,23,31,32,34,50,51,52,53,54,85,],[30,-11,-15,-16,-17,-10,49,-14,-13,-16,-20,-21,-19,-12,]),'PUNTO':([20,22,102,105,166,],[33,-18,158,-49,197,]),'COMA':([21,22,23,39,40,50,51,125,126,127,128,129,130,131,136,137,170,171,172,173,175,177,204,205,206,207,208,229,230,231,243,],[35,-16,-17,58,-18,35,-16,-128,-107,-108,-109,-110,-111,-112,-118,-119,203,-120,-121,-122,-129,-113,-123,-124,-125,-126,-127,-116,-115,-117,-114,]),'AS':([21,22,23,39,40,50,51,115,167,223,],[36,-16,-17,59,-18,36,-16,163,200,200,]),'ASC':([22,23,51,54,167,198,223,225,237,],[-16,-17,-16,-19,201,201,201,-93,201,]),'DESC':([22,23,51,54,167,198,223,225,237,],[-16,-17,-16,-19,202,202,202,-93,202,]),'HAVING':([22,23,51,54,164,165,167,195,198,199,201,202,223,224,225,237,238,239,240,241,242,245,],[-16,-17,-16,-19,196,-84,-88,-83,-87,-92,-95,-98,-86,-91,-93,-85,-90,-96,-97,-99,-100,-89,]),'JOIN':([22,23,38,39,40,48,51,54,56,57,71,72,73,74,75,76,77,80,81,82,83,84,90,91,97,98,99,100,103,105,106,107,108,109,110,112,117,118,119,120,146,157,159,164,165,167,185,186,187,188,191,192,194,195,198,199,201,202,216,217,218,222,223,224,225,233,236,237,238,239,240,241,242,244,245,],[-16,-17,-24,-25,-18,78,-16,-19,-23,-26,78,-32,78,-34,-62,-80,113,-71,-73,-75,-77,78,-27,-28,-67,-36,-39,-42,-45,-50,-51,-52,-53,-54,-31,-61,-70,-72,-74,-76,-35,-41,-67,-82,-84,-88,-38,-40,-44,-50,-64,219,-81,-83,-87,-92,-95,-98,-37,-63,219,-94,-86,-91,-93,-43,-66,-85,-90,-96,-97,-99,-100,-65,-89,]),'WHERE':([22,23,38,39,40,48,51,54,56,57,71,72,73,74,75,76,84,90,91,97,98,99,100,103,105,106,107,108,109,110,112,146,157,159,164,165,167,185,186,187,188,191,194,195,198,199,201,202,216,217,222,223,224,225,233,236,237,238,239,240,241,242,244,245,],[-16,-17,-24,-25,-18,70,-16,-19,-23,-26,111,-32,111,-34,-62,-80,70,-27,-28,-67,-36,-39,-42,-45,-50,-51,-52,-53,-54,-31,-61,-35,-41,-67,-82,-84,-88,-38,-40,-44,-50,-64,-81,-83,-87,-92,-95,-98,-37,-63,-94,-86,-91,-93,-43,-66,-85,-90,-96,-97,-99,-100,-65,-89,]),'GROUP':([22,23,38,39,40,48,51,54,56,57,71,72,73,74,75,76,84,90,91,97,98,99,100,103,105,106,107,108,109,110,112,146,157,159,164,165,167,185,186,187,188,191,194,195,198,199,201,202,216,217,222,223,224,225,233,236,237,238,239,240,241,242,244,245,],[-16,-17,-24,-25,-18,79,-16,-19,-23,-26,79,-32,-33,-34,-62,-80,79,-27,-28,-67,-36,-39,-42,-45,-50,-51,-52,-53,-54,-31,-61,-35,-41,-67,-82,-84,-88,-38,-40,-44,-50,-64,-81,-83,-87,-92,-95,-98,-37,-63,-94,-86,-91,-93,-43,-66,-85,-90,-96,-97,-99,-100,-65,-89,]),'INNER':([22,23,38,39,40,48,51,54,56,57,71,72,73,74,75,76,84,90,91,97,98,99,100,103,105,106,107,108,109,110,112,146,157,159,164,165,167,185,186,187,188,191,194,195,198,199,201,202,216,217,222,223,224,225,233,236,237,238,239,240,241,242,244,245,],[-16,-17,-24,-25,-18,80,-16,-19,-23,-26,80,-32,80,-34,-62,-80,80,-27,-28,-67,-36,-39,-42,-45,-50,-51,-52,-53,-54,-31,-61,-35,-41,-67,-82,-84,-88,-38,-40,-44,-50,-64,-81,-83,-87,-92,-95,-98,-37,-63,-94,-86,-91,-93,-43,-66,-85,-90,-96,-97,-99,-100,-65,-89,]),'LEFT':([22,23,38,39,40,48,51,54,56,57,71,72,73,74,75,76,84,90,91,97,98,99,100,103,105,106,107,108,109,110,112,146,157,159,164,165,167,185,186,187,188,191,194,195,198,199,201,202,216,217,222,223,224,225,233,236,237,238,239,240,241,242,244,245,],[-16,-17,-24,-25,-18,81,-16,-19,-23,-26,81,-32,81,-34,-62,-80,81,-27,-28,-67,-36,-39,-42,-45,-50,-51,-52,-53,-54,-31,-61,-35,-41,-67,-82,-84,-88,-38,-40,-44,-50,-64,-81,-83,-87,-92,-95,-98,-37,-63,-94,-86,-91,-93,-43,-66,-85,-90,-96,-97,-99,-100,-65,-89,]),'RIGHT':([22,23,38,39,40,48,51,54,56,57,71,72,73,74,75,76,84,90,91,97,98,99,100,103,105,106,107,108,109,110,112,146,157,159,164,165,167,185,186,187,188,191,194,195,198,199,201,202,216,217,222,223,224,225,233,236,237,238,239,240,241,242,244,245,],[-16,-17,-24,-25,-18,82,-16,-19,-23,-26,82,-32,82,-34,-62,-80,82,-27,-28,-67,-36,-39,-42,-45,-50,-51,-52,-53,-54,-31,-61,-35,-41,-67,-82,-84,-88,-38,-40,-44,-50,-64,-81,-83,-87,-92,-95,-98,-37,-63,-94,-86,-91,-93,-43,-66,-85,-90,-96,-97,-99,-100,-65,-89,]),'FULL':([22,23,38,39,40,48,51,54,56,57,71,72,73,74,75,76,84,90,91,97,98,99,100,103,105,106,107,108,109,110,112,146,157,159,164,165,167,185,186,187,188,191,194,195,198,199,201,202,216,217,222,223,224,225,233,236,237,238,239,240,241,242,244,245,],[-16,-17,-24,-25,-18,83,-16,-19,-23,-26,83,-32,83,-34,-62,-80,83,-27,-28,-67,-36,-39,-42,-45,-50,-51,-52,-53,-54,-31,-61,-35,-41,-67,-82,-84,-88,-38,-40,-44,-50,-64,-81,-83,-87,-92,-95,-98,-37,-63,-94,-86,-91,-93,-43,-66,-85,-90,-96,-97,-99,-100,-65,-89,]),'PUNTOCOMA':([22,23,38,39,40,48,51,54,56,57,68,71,72,73,74,75,76,84,90,91,97,98,99,100,103,105,106,107,108,109,110,112,121,123,146,157,159,164,165,167,185,186,187,188,191,194,195,198,199,201,202,216,217,222,223,224,225,233,236,237,238,239,240,241,242,244,245,],[-16,-17,-24,-25,-18,69,-16,-19,-23,-26,96,-30,-32,-33,-34,-62,-80,122,-27,-28,-29,-36,-39,-42,-45,-50,-51,-52,-53,-54,-31,-61,168,169,-35,-41,-67,-82,-84,-88,-38,-40,-44,-50,-64,-81,-83,-87,-92,-95,-98,-37,-63,-94,-86,-91,-93,-43,-66,-85,-90,-96,-97,-99,-100,-65,-89,]),'REPLACE':([26,],[42,]),'LIKE':([27,],[44,]),'IF':([29,41,],[47,61,]),'PARIZQ':([37,38,39,40,54,56,57,90,91,133,134,135,162,178,190,],[55,-24,-25,-18,-19,-23,-26,-27,-28,179,180,181,192,209,218,]),'SMALLINT':([40,89,],[-18,126,]),'INTEGER':([40,89,],[-18,127,]),'BIGINT':([40,89,],[-18,128,]),'DECIMAL':([40,70,89,97,98,99,100,101,103,104,105,106,107,108,109,111,146,147,148,149,150,151,152,153,154,155,156,157,158,159,161,176,185,186,187,188,189,191,192,196,215,216,217,218,219,222,233,],[-18,107,129,107,-36,-39,-42,107,-45,-48,-50,-51,-52,-53,-54,107,-35,107,-46,-47,107,-55,-56,-57,-58,-59,-60,-41,107,107,107,207,-38,-40,-44,-50,107,107,107,107,107,-37,107,107,107,107,107,]),'REAL':([40,89,],[-18,130,]),'MONEY':([40,89,],[-18,131,]),'DOUBLE':([40,89,],[-18,132,]),'CHARACTER':([40,89,],[-18,133,]),'VARCHAR':([40,89,],[-18,134,]),'CHAR':([40,89,],[-18,135,]),'TEXT':([40,89,],[-18,136,]),'BOOLEAN':([40,89,],[-18,137,]),'CADENADOBLE':([44,70,97,98,99,100,101,103,104,105,106,107,108,109,111,146,147,148,149,150,151,152,153,154,155,156,157,158,159,161,176,185,186,187,188,189,191,192,196,215,216,217,218,219,222,233,],[62,109,109,-36,-39,-42,109,-45,-48,-50,-51,-52,-53,-54,109,-35,109,-46,-47,109,-55,-56,-57,-58,-59,-60,-41,109,109,109,206,-38,-40,-44,-50,109,109,109,109,109,-37,109,109,109,109,109,]),'RENAME':([45,],[64,]),'OWNER':([45,92,],[65,139,]),'EXISTS':([47,93,],[67,140,]),'NOT':([61,125,126,127,128,129,130,131,136,137,177,229,230,231,243,],[93,174,-107,-108,-109,-110,-111,-112,-118,-119,-113,-116,-115,-117,-114,]),'TO':([64,65,],[94,95,]),'NEGACION':([70,97,98,99,100,103,105,106,107,108,109,111,146,147,148,149,157,159,161,185,186,187,188,189,191,196,215,216,217,222,233,],[104,104,-36,-39,-42,-45,-50,-51,-52,-53,-54,104,-35,104,-46,-47,-41,104,104,-38,-40,-44,-50,104,104,104,104,-37,104,104,104,]),'ENTERO':([70,97,98,99,100,101,103,104,105,106,107,108,109,111,146,147,148,149,150,151,152,153,154,155,156,157,158,159,161,176,179,180,181,185,186,187,188,189,191,192,196,209,213,215,216,217,218,219,222,233,],[106,106,-36,-39,-42,106,-45,-48,-50,-51,-52,-53,-54,106,-35,106,-46,-47,106,-55,-56,-57,-58,-59,-60,-41,106,106,106,208,210,211,212,-38,-40,-44,-50,106,106,106,106,228,232,106,-37,106,106,106,106,106,]),'CADENASIMPLE':([70,97,98,99,100,101,103,104,105,106,107,108,109,111,146,147,148,149,150,151,152,153,154,155,156,157,158,159,161,176,185,186,187,188,189,191,192,196,215,216,217,218,219,222,233,],[108,108,-36,-39,-42,108,-45,-48,-50,-51,-52,-53,-54,108,-35,108,-46,-47,108,-55,-56,-57,-58,-59,-60,-41,108,108,108,205,-38,-40,-44,-50,108,108,108,108,108,-37,108,108,108,108,108,]),'BY':([79,],[116,]),'OUTER':([80,81,82,83,],[117,118,119,120,]),'PARDER':([86,87,88,103,105,106,107,108,109,124,125,126,127,128,129,130,131,136,137,170,171,172,173,175,177,187,188,203,204,205,206,207,208,210,211,212,220,221,228,229,230,231,234,235,243,],[123,-102,-104,-45,-50,-51,-52,-53,-54,-103,-128,-107,-108,-109,-110,-111,-112,-118,-119,-106,-120,-121,-122,-129,-113,-44,-50,-105,-123,-124,-125,-126,-127,229,230,231,236,-69,243,-116,-115,-117,244,-68,-114,]),'MODE':([92,138,214,],[-140,183,-139,]),'CURRENT_USER':([95,],[144,]),'SESSION_USER':([95,],[145,]),'AND':([99,100,103,105,106,107,108,109,157,185,186,187,188,],[148,-42,-45,-50,-51,-52,-53,-54,-41,148,-40,-44,-50,]),'IGUAL':([100,103,105,106,107,108,109,139,183,187,188,],[151,-45,-50,-51,-52,-53,-54,184,213,-44,-50,]),'DIFERENTE':([100,103,105,106,107,108,109,187,188,],[152,-45,-50,-51,-52,-53,-54,-44,-50,]),'MAYOR':([100,103,105,106,107,108,109,187,188,],[153,-45,-50,-51,-52,-53,-54,-44,-50,]),'MENOR':([100,103,105,106,107,108,109,187,188,],[154,-45,-50,-51,-52,-53,-54,-44,-50,]),'MENORIGUAL':([100,103,105,106,107,108,109,187,188,],[155,-45,-50,-51,-52,-53,-54,-44,-50,]),'MAYORIGUAL':([100,103,105,106,107,108,109,187,188,],[156,-45,-50,-51,-52,-53,-54,-44,-50,]),'ON':([114,115,160,193,],[161,-78,189,-79,]),'USING':([114,115,160,193,],[162,-78,190,-79,]),'DEFAULT':([125,126,127,128,129,130,131,136,137,177,229,230,231,243,],[176,-107,-108,-109,-110,-111,-112,-118,-119,-113,-116,-115,-117,-114,]),'NULL':([125,126,127,128,129,130,131,136,137,174,177,229,230,231,243,],[175,-107,-108,-109,-110,-111,-112,-118,-119,204,-113,-116,-115,-117,-114,]),'PRECISION':([132,],[177,]),'VARYING':([133,],[178,]),'NULLS':([201,202,],[226,227,]),'FIRST':([226,227,],[239,241,]),'LAST':([226,227,],[240,242,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'INICIO':([0,],[1,]),'INSTRUCCIONES':([0,],[2,]),'INSTRUCCION':([0,2,],[3,15,]),'DQL_COMANDOS':([0,2,],[4,4,]),'DDL_COMANDOS':([0,2,],[5,5,]),'CREATE_DATABASE':([0,2,],[8,8,]),'SHOW_DATABASES':([0,2,],[9,9,]),'ALTER_DATABASE':([0,2,],[10,10,]),'DROP_DATABASE':([0,2,],[11,11,]),'LISTA_CAMPOS':([6,17,],[16,32,]),'DISTINCTNT':([6,],[17,]),'LISTA':([6,16,17,32,35,],[18,31,18,31,52,]),'NOMBRE_T':([6,16,17,24,30,32,35,37,48,49,55,58,84,87,116,164,],[20,20,20,39,39,20,20,39,39,39,89,39,39,89,166,166,]),'CAMPOS':([6,16,17,32,33,35,116,164,197,],[21,21,21,21,50,21,167,167,223,]),'REPLACE_OP':([7,],[25,]),'S':([21,50,],[34,85,]),'NOMBRES_TABLAS':([24,30,49,],[37,48,84,]),'TABLA':([24,30,37,48,49,58,84,],[38,38,56,56,38,90,56,]),'SHOW_DATABASES_LIKE':([27,],[43,]),'IF_EXISTS_DATABASE':([29,],[46,]),'ALIAS':([36,59,200,],[53,91,225,]),'S1':([39,],[57,]),'IF_NOT_EXISTIS':([41,],[60,]),'ALTER_DATABASE_OP':([45,],[63,]),'CUERPO':([48,84,],[68,121,]),'MORES':([48,84,],[71,71,]),'MOREE':([48,71,84,],[72,110,72,]),'INNERS':([48,71,84,],[73,73,73,]),'GROUPS':([48,71,84,],[74,74,74,]),'INNERR':([48,71,73,84,],[75,75,112,75,]),'GROUPP':([48,71,84,],[76,76,76,]),'TIPOS_INNER':([48,71,73,84,],[77,77,77,77,]),'CUERPO_CREATE_TABLE':([55,],[86,]),'LISTA_DE_COLUMNAS':([55,],[87,]),'LISTA2':([55,87,],[88,124,]),'CONDICIONES':([70,111,161,189,196,215,],[97,159,191,217,222,233,]),'CONDICION':([70,97,111,159,161,189,191,196,215,217,222,233,],[98,146,98,146,98,98,146,98,98,146,146,146,]),'CONDICION_REL':([70,97,111,147,159,161,189,191,196,215,217,222,233,],[99,99,99,185,99,99,99,99,99,99,99,99,99,]),'EXPRESIONNE':([70,97,101,111,147,150,159,161,189,191,192,196,215,217,218,219,222,233,],[100,100,157,100,100,186,100,100,100,100,221,100,100,100,221,235,100,100,]),'SIMBOLO_NEG':([70,97,111,147,159,161,189,191,196,215,217,222,233,],[101,101,101,101,101,101,101,101,101,101,101,101,101,]),'NOMBRE_C':([70,97,101,111,147,150,159,161,189,191,192,196,215,217,218,219,222,233,],[102,102,102,102,102,102,102,102,102,102,102,102,102,102,102,102,102,102,]),'CAMPOSC':([70,97,101,111,147,150,158,159,161,189,191,192,196,215,217,218,219,222,233,],[103,103,103,103,103,103,187,103,103,103,103,103,103,103,103,103,103,103,103,]),'TABLA_REF':([78,113,],[114,160,]),'TIPO_CAMPO':([89,],[125,]),'OWNER_DATABASE':([92,],[138,]),'ALTER_TABLE_OP_OW':([95,],[142,]),'SIMBOLO_LOGICO':([99,185,],[147,215,]),'OPERADOR':([100,],[150,]),'EXPRE_LIST':([116,],[164,]),'EXPRES':([116,164,],[165,195,]),'VALIDACIONES_CREATE_TABLE':([125,],[170,]),'LISTA3':([125,],[171,]),'VALIDACION_CAMPO_CREATE':([125,],[172,]),'VALIDACION_CAMPO_CREATE_VACIO':([125,],[173,]),'MODE_DATABASE':([138,],[182,]),'MORE_ORDER':([164,],[194,]),'S2':([167,223,],[198,237,]),'STATE':([167,198,223,237,],[199,224,238,245,]),'OTRO_LOGICO':([185,],[216,]),'SUB_COLUMN':([192,218,],[220,234,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> INICIO","S'",1,None,None,None),
  ('INICIO -> INSTRUCCIONES','INICIO',1,'p_init','Gramatica.py',239),
  ('INSTRUCCIONES -> INSTRUCCIONES INSTRUCCION','INSTRUCCIONES',2,'p_instrucciones_lista','Gramatica.py',247),
  ('INSTRUCCIONES -> INSTRUCCION','INSTRUCCIONES',1,'p_instrucciones_instruccion','Gramatica.py',253),
  ('INSTRUCCION -> DQL_COMANDOS','INSTRUCCION',1,'p_instruccion','Gramatica.py',262),
  ('INSTRUCCION -> DDL_COMANDOS','INSTRUCCION',1,'p_instruccion','Gramatica.py',263),
  ('DQL_COMANDOS -> SELECT LISTA_CAMPOS FROM NOMBRES_TABLAS CUERPO PUNTOCOMA','DQL_COMANDOS',6,'p_instruccion_dql_comandos','Gramatica.py',272),
  ('DQL_COMANDOS -> SELECT LISTA_CAMPOS FROM NOMBRES_TABLAS PUNTOCOMA','DQL_COMANDOS',5,'p_instruccion_dql_comandosS','Gramatica.py',280),
  ('DQL_COMANDOS -> SELECT DISTINCTNT LISTA_CAMPOS FROM NOMBRES_TABLAS CUERPO PUNTOCOMA','DQL_COMANDOS',7,'p_instruccion_dql_comandosS1','Gramatica.py',287),
  ('DQL_COMANDOS -> SELECT DISTINCTNT LISTA_CAMPOS FROM NOMBRES_TABLAS PUNTOCOMA','DQL_COMANDOS',6,'p_instruccion_dql_comandosS2','Gramatica.py',293),
  ('LISTA_CAMPOS -> LISTA_CAMPOS LISTA','LISTA_CAMPOS',2,'p_ListaCampos_ListaCampos','Gramatica.py',305),
  ('LISTA_CAMPOS -> LISTA','LISTA_CAMPOS',1,'p_ListaCampos_Lista','Gramatica.py',312),
  ('LISTA -> NOMBRE_T PUNTO CAMPOS S','LISTA',4,'p_Lista_NombreS','Gramatica.py',318),
  ('LISTA -> NOMBRE_T PUNTO CAMPOS','LISTA',3,'p_Lista_Nombre','Gramatica.py',326),
  ('LISTA -> CAMPOS S','LISTA',2,'p_Lista_CampoS','Gramatica.py',334),
  ('LISTA -> CAMPOS','LISTA',1,'p_Lista_Campo','Gramatica.py',343),
  ('CAMPOS -> ID','CAMPOS',1,'p_Campos_id','Gramatica.py',351),
  ('CAMPOS -> ASTERISCO','CAMPOS',1,'p_Campos_Asterisco','Gramatica.py',359),
  ('NOMBRE_T -> ID','NOMBRE_T',1,'p_NombreT_id','Gramatica.py',367),
  ('ALIAS -> ID','ALIAS',1,'p_Alias_id','Gramatica.py',375),
  ('S -> COMA LISTA','S',2,'p_S_ComaLista','Gramatica.py',384),
  ('S -> AS ALIAS','S',2,'p_S_AsAlias','Gramatica.py',393),
  ('DISTINCTNT -> DISTINCT','DISTINCTNT',1,'p_Disctint_Rw','Gramatica.py',406),
  ('NOMBRES_TABLAS -> NOMBRES_TABLAS TABLA','NOMBRES_TABLAS',2,'p_NombresTablas_NombresTablas','Gramatica.py',417),
  ('NOMBRES_TABLAS -> TABLA','NOMBRES_TABLAS',1,'p_NombresTablas_Tabla','Gramatica.py',423),
  ('TABLA -> NOMBRE_T','TABLA',1,'p_Tabla_NombreT','Gramatica.py',429),
  ('TABLA -> NOMBRE_T S1','TABLA',2,'p_Tabla_NombreTS','Gramatica.py',437),
  ('S1 -> COMA TABLA','S1',2,'p_Ss_ComaLista','Gramatica.py',448),
  ('S1 -> AS ALIAS','S1',2,'p_Ss_AsAlias','Gramatica.py',457),
  ('CUERPO -> WHERE CONDICIONES','CUERPO',2,'p_Cuerpo_Where','Gramatica.py',472),
  ('CUERPO -> MORES','CUERPO',1,'p_Cuerpo_Mores','Gramatica.py',480),
  ('MORES -> MORES MOREE','MORES',2,'p_MORES_ListaCampos','Gramatica.py',487),
  ('MORES -> MOREE','MORES',1,'p_MORES_Lista','Gramatica.py',495),
  ('MOREE -> INNERS','MOREE',1,'p_Mores_Inners','Gramatica.py',508),
  ('MOREE -> GROUPS','MOREE',1,'p_Mores_Groups','Gramatica.py',515),
  ('CONDICIONES -> CONDICIONES CONDICION','CONDICIONES',2,'p_Condiciones_Lista','Gramatica.py',530),
  ('CONDICIONES -> CONDICION','CONDICIONES',1,'p_Condiciones_Condicion','Gramatica.py',538),
  ('CONDICION -> CONDICION_REL SIMBOLO_LOGICO CONDICION_REL OTRO_LOGICO','CONDICION',4,'p_Condicion_CondicionRel','Gramatica.py',546),
  ('CONDICION -> CONDICION_REL SIMBOLO_LOGICO CONDICION_REL','CONDICION',3,'p_Condicion_CondicionRel_Sin','Gramatica.py',551),
  ('CONDICION -> CONDICION_REL','CONDICION',1,'p_Condicion_CondiRel','Gramatica.py',557),
  ('CONDICION_REL -> EXPRESIONNE OPERADOR EXPRESIONNE','CONDICION_REL',3,'p_CondicionRel_Expresionn','Gramatica.py',565),
  ('CONDICION_REL -> SIMBOLO_NEG EXPRESIONNE','CONDICION_REL',2,'p_CondicionRel_Negacion','Gramatica.py',572),
  ('CONDICION_REL -> EXPRESIONNE','CONDICION_REL',1,'p_CondicionRel_Expre','Gramatica.py',577),
  ('OTRO_LOGICO -> SIMBOLO_LOGICO CONDICIONES','OTRO_LOGICO',2,'p_OtroLogico_SimboloLogic','Gramatica.py',583),
  ('EXPRESIONNE -> NOMBRE_C PUNTO CAMPOSC','EXPRESIONNE',3,'p_Expresion_Nombre','Gramatica.py',595),
  ('EXPRESIONNE -> CAMPOSC','EXPRESIONNE',1,'p_Expresion_CampoC','Gramatica.py',600),
  ('SIMBOLO_LOGICO -> AND','SIMBOLO_LOGICO',1,'p_SimboloLogico_Logicos','Gramatica.py',607),
  ('SIMBOLO_LOGICO -> OR','SIMBOLO_LOGICO',1,'p_SimboloLogico_Logicos','Gramatica.py',608),
  ('SIMBOLO_NEG -> NEGACION','SIMBOLO_NEG',1,'p_SimboloNegacion_sim','Gramatica.py',618),
  ('NOMBRE_C -> ID','NOMBRE_C',1,'p_NombreC_id','Gramatica.py',628),
  ('CAMPOSC -> ID','CAMPOSC',1,'p_CamposC_id','Gramatica.py',636),
  ('CAMPOSC -> ENTERO','CAMPOSC',1,'p_CamposC_id','Gramatica.py',637),
  ('CAMPOSC -> DECIMAL','CAMPOSC',1,'p_CamposC_id','Gramatica.py',638),
  ('CAMPOSC -> CADENASIMPLE','CAMPOSC',1,'p_CamposC_id','Gramatica.py',639),
  ('CAMPOSC -> CADENADOBLE','CAMPOSC',1,'p_CamposC_id','Gramatica.py',640),
  ('OPERADOR -> IGUAL','OPERADOR',1,'p_SimboloRela_Simbolos','Gramatica.py',646),
  ('OPERADOR -> DIFERENTE','OPERADOR',1,'p_SimboloRela_Simbolos','Gramatica.py',647),
  ('OPERADOR -> MAYOR','OPERADOR',1,'p_SimboloRela_Simbolos','Gramatica.py',648),
  ('OPERADOR -> MENOR','OPERADOR',1,'p_SimboloRela_Simbolos','Gramatica.py',649),
  ('OPERADOR -> MENORIGUAL','OPERADOR',1,'p_SimboloRela_Simbolos','Gramatica.py',650),
  ('OPERADOR -> MAYORIGUAL','OPERADOR',1,'p_SimboloRela_Simbolos','Gramatica.py',651),
  ('INNERS -> INNERS INNERR','INNERS',2,'p_Inners_Lista','Gramatica.py',662),
  ('INNERS -> INNERR','INNERS',1,'p_Inners_Inner','Gramatica.py',670),
  ('INNERR -> TIPOS_INNER JOIN TABLA_REF ON CONDICIONES','INNERR',5,'p_Inner_InnerJoin','Gramatica.py',679),
  ('INNERR -> JOIN TABLA_REF ON CONDICIONES','INNERR',4,'p_Inner_Join','Gramatica.py',686),
  ('INNERR -> TIPOS_INNER JOIN TABLA_REF USING PARIZQ SUB_COLUMN PARDER','INNERR',7,'p_Inner_InnerJoinUsing','Gramatica.py',696),
  ('INNERR -> JOIN TABLA_REF USING PARIZQ SUB_COLUMN PARDER','INNERR',6,'p_Inner_JoinUsing','Gramatica.py',703),
  ('INNERR -> WHERE CONDICIONES','INNERR',2,'p_Inner_Where','Gramatica.py',709),
  ('SUB_COLUMN -> JOIN EXPRESIONNE','SUB_COLUMN',2,'p_SubColumn_join','Gramatica.py',716),
  ('SUB_COLUMN -> EXPRESIONNE','SUB_COLUMN',1,'p_SubColumn_Expresione','Gramatica.py',724),
  ('TIPOS_INNER -> INNER OUTER','TIPOS_INNER',2,'p_TiposInner_InnerOuter','Gramatica.py',731),
  ('TIPOS_INNER -> INNER','TIPOS_INNER',1,'p_TiposInner_Inner','Gramatica.py',735),
  ('TIPOS_INNER -> LEFT OUTER','TIPOS_INNER',2,'p_TiposInner_LefOuter','Gramatica.py',740),
  ('TIPOS_INNER -> LEFT','TIPOS_INNER',1,'p_TiposInner_Left','Gramatica.py',744),
  ('TIPOS_INNER -> RIGHT OUTER','TIPOS_INNER',2,'p_TiposInner_RightOuter','Gramatica.py',749),
  ('TIPOS_INNER -> RIGHT','TIPOS_INNER',1,'p_TiposInner_Right','Gramatica.py',753),
  ('TIPOS_INNER -> FULL OUTER','TIPOS_INNER',2,'p_TiposInner_FullOuter','Gramatica.py',758),
  ('TIPOS_INNER -> FULL','TIPOS_INNER',1,'p_TiposInner_Full','Gramatica.py',763),
  ('TABLA_REF -> ID','TABLA_REF',1,'p_TablaRef_Id','Gramatica.py',772),
  ('TABLA_REF -> ID AS ID','TABLA_REF',3,'p_TablaRef_IdAS','Gramatica.py',777),
  ('GROUPS -> GROUPP','GROUPS',1,'p_Groups_ListaG','Gramatica.py',796),
  ('GROUPP -> GROUP BY EXPRE_LIST MORE_ORDER','GROUPP',4,'p_Group_GroupBy','Gramatica.py',803),
  ('GROUPP -> GROUP BY EXPRE_LIST','GROUPP',3,'p_Group_GroupBySin','Gramatica.py',810),
  ('EXPRE_LIST -> EXPRE_LIST EXPRES','EXPRE_LIST',2,'p_ExpreList_Lista','Gramatica.py',818),
  ('EXPRE_LIST -> EXPRES','EXPRE_LIST',1,'p_ExpreList_Expresion','Gramatica.py',824),
  ('EXPRES -> NOMBRE_T PUNTO CAMPOS S2','EXPRES',4,'p_Expre_Campo1','Gramatica.py',831),
  ('EXPRES -> NOMBRE_T PUNTO CAMPOS','EXPRES',3,'p_Expre_Campo2','Gramatica.py',836),
  ('EXPRES -> CAMPOS S2','EXPRES',2,'p_Expre_Campo3','Gramatica.py',841),
  ('EXPRES -> CAMPOS','EXPRES',1,'p_Expre_Campo4','Gramatica.py',846),
  ('EXPRES -> NOMBRE_T PUNTO CAMPOS S2 STATE','EXPRES',5,'p_Expre_Campo5','Gramatica.py',852),
  ('EXPRES -> NOMBRE_T PUNTO CAMPOS STATE','EXPRES',4,'p_Expre_Campo6','Gramatica.py',859),
  ('EXPRES -> CAMPOS S2 STATE','EXPRES',3,'p_Expre_Campo7','Gramatica.py',865),
  ('EXPRES -> CAMPOS STATE','EXPRES',2,'p_Expre_Campo8','Gramatica.py',870),
  ('S2 -> AS ALIAS','S2',2,'p_S2','Gramatica.py',881),
  ('MORE_ORDER -> HAVING CONDICIONES','MORE_ORDER',2,'p_MoreOrder_Having','Gramatica.py',886),
  ('STATE -> ASC','STATE',1,'p_State_orden1','Gramatica.py',891),
  ('STATE -> ASC NULLS FIRST','STATE',3,'p_State_orden2','Gramatica.py',896),
  ('STATE -> ASC NULLS LAST','STATE',3,'p_State_orden3','Gramatica.py',900),
  ('STATE -> DESC','STATE',1,'p_State_orden4','Gramatica.py',905),
  ('STATE -> DESC NULLS FIRST','STATE',3,'p_State_orden5','Gramatica.py',911),
  ('STATE -> DESC NULLS LAST','STATE',3,'p_State_orden6','Gramatica.py',916),
  ('DQL_COMANDOS -> CREATE TABLE NOMBRES_TABLAS PARIZQ CUERPO_CREATE_TABLE PARDER PUNTOCOMA','DQL_COMANDOS',7,'p_instruccion_dml_comandos_CREATE_TABLE','Gramatica.py',945),
  ('CUERPO_CREATE_TABLE -> LISTA_DE_COLUMNAS','CUERPO_CREATE_TABLE',1,'p_instruccion_dml_comandos_CUERPO','Gramatica.py',950),
  ('LISTA_DE_COLUMNAS -> LISTA_DE_COLUMNAS LISTA2','LISTA_DE_COLUMNAS',2,'p_CREATE_TABLE_LISTA_CAMPOS','Gramatica.py',957),
  ('LISTA_DE_COLUMNAS -> LISTA2','LISTA_DE_COLUMNAS',1,'p_CREATE_TABLE_LISTA2_CAMPOS','Gramatica.py',963),
  ('LISTA2 -> NOMBRE_T TIPO_CAMPO VALIDACIONES_CREATE_TABLE COMA','LISTA2',4,'p_Create_TABLE_CAMPOS','Gramatica.py',969),
  ('LISTA2 -> NOMBRE_T TIPO_CAMPO VALIDACIONES_CREATE_TABLE','LISTA2',3,'p_Create_TABLE_CAMPOS2','Gramatica.py',974),
  ('TIPO_CAMPO -> SMALLINT','TIPO_CAMPO',1,'p_Create_TABLE_TIPO_CAMPO','Gramatica.py',978),
  ('TIPO_CAMPO -> INTEGER','TIPO_CAMPO',1,'p_Create_TABLE_TIPO_CAMPO','Gramatica.py',979),
  ('TIPO_CAMPO -> BIGINT','TIPO_CAMPO',1,'p_Create_TABLE_TIPO_CAMPO','Gramatica.py',980),
  ('TIPO_CAMPO -> DECIMAL','TIPO_CAMPO',1,'p_Create_TABLE_TIPO_CAMPO','Gramatica.py',981),
  ('TIPO_CAMPO -> REAL','TIPO_CAMPO',1,'p_Create_TABLE_TIPO_CAMPO','Gramatica.py',982),
  ('TIPO_CAMPO -> MONEY','TIPO_CAMPO',1,'p_Create_TABLE_TIPO_CAMPO','Gramatica.py',983),
  ('TIPO_CAMPO -> DOUBLE PRECISION','TIPO_CAMPO',2,'p_Create_TABLE_TIPO_CAMPO','Gramatica.py',984),
  ('TIPO_CAMPO -> CHARACTER VARYING PARIZQ ENTERO PARDER','TIPO_CAMPO',5,'p_Create_TABLE_TIPO_CAMPO','Gramatica.py',985),
  ('TIPO_CAMPO -> VARCHAR PARIZQ ENTERO PARDER','TIPO_CAMPO',4,'p_Create_TABLE_TIPO_CAMPO','Gramatica.py',986),
  ('TIPO_CAMPO -> CHARACTER PARIZQ ENTERO PARDER','TIPO_CAMPO',4,'p_Create_TABLE_TIPO_CAMPO','Gramatica.py',987),
  ('TIPO_CAMPO -> CHAR PARIZQ ENTERO PARDER','TIPO_CAMPO',4,'p_Create_TABLE_TIPO_CAMPO','Gramatica.py',988),
  ('TIPO_CAMPO -> TEXT','TIPO_CAMPO',1,'p_Create_TABLE_TIPO_CAMPO','Gramatica.py',989),
  ('TIPO_CAMPO -> BOOLEAN','TIPO_CAMPO',1,'p_Create_TABLE_TIPO_CAMPO','Gramatica.py',990),
  ('VALIDACIONES_CREATE_TABLE -> LISTA3','VALIDACIONES_CREATE_TABLE',1,'p_CREATE_TABLE_LISTA3_CAMPOS','Gramatica.py',994),
  ('LISTA3 -> VALIDACION_CAMPO_CREATE','LISTA3',1,'p_Create_TABLE_CAMPOS3','Gramatica.py',999),
  ('LISTA3 -> VALIDACION_CAMPO_CREATE_VACIO','LISTA3',1,'p_Create_TABLE_CAMPOS4','Gramatica.py',1003),
  ('VALIDACION_CAMPO_CREATE -> NOT NULL','VALIDACION_CAMPO_CREATE',2,'p_Create_TABLE_TIPO_CAMPO2','Gramatica.py',1008),
  ('VALIDACION_CAMPO_CREATE -> DEFAULT CADENASIMPLE','VALIDACION_CAMPO_CREATE',2,'p_Create_TABLE_TIPO_CAMPO2','Gramatica.py',1009),
  ('VALIDACION_CAMPO_CREATE -> DEFAULT CADENADOBLE','VALIDACION_CAMPO_CREATE',2,'p_Create_TABLE_TIPO_CAMPO2','Gramatica.py',1010),
  ('VALIDACION_CAMPO_CREATE -> DEFAULT DECIMAL','VALIDACION_CAMPO_CREATE',2,'p_Create_TABLE_TIPO_CAMPO2','Gramatica.py',1011),
  ('VALIDACION_CAMPO_CREATE -> DEFAULT ENTERO','VALIDACION_CAMPO_CREATE',2,'p_Create_TABLE_TIPO_CAMPO2','Gramatica.py',1012),
  ('VALIDACION_CAMPO_CREATE_VACIO -> <empty>','VALIDACION_CAMPO_CREATE_VACIO',0,'p_Create_TABLE_TIPO_CAMPO3','Gramatica.py',1016),
  ('VALIDACION_CAMPO_CREATE -> NULL','VALIDACION_CAMPO_CREATE',1,'p_Create_TABLE_TIPO_CAMPO4','Gramatica.py',1020),
  ('DDL_COMANDOS -> CREATE_DATABASE','DDL_COMANDOS',1,'p_comando_ddl','Gramatica.py',1027),
  ('DDL_COMANDOS -> SHOW_DATABASES','DDL_COMANDOS',1,'p_comando_ddl','Gramatica.py',1028),
  ('DDL_COMANDOS -> ALTER_DATABASE','DDL_COMANDOS',1,'p_comando_ddl','Gramatica.py',1029),
  ('DDL_COMANDOS -> DROP_DATABASE','DDL_COMANDOS',1,'p_comando_ddl','Gramatica.py',1030),
  ('CREATE_DATABASE -> CREATE REPLACE_OP DATABASE IF_NOT_EXISTIS ID OWNER_DATABASE MODE_DATABASE','CREATE_DATABASE',7,'p_create_database','Gramatica.py',1035),
  ('REPLACE_OP -> OR REPLACE','REPLACE_OP',2,'p_replace_op','Gramatica.py',1039),
  ('REPLACE_OP -> <empty>','REPLACE_OP',0,'p_replace_op_e','Gramatica.py',1043),
  ('IF_NOT_EXISTIS -> IF NOT EXISTS','IF_NOT_EXISTIS',3,'p_if_not_exists','Gramatica.py',1047),
  ('IF_NOT_EXISTIS -> <empty>','IF_NOT_EXISTIS',0,'p_if_not_exists_e','Gramatica.py',1051),
  ('OWNER_DATABASE -> OWNER IGUAL ID','OWNER_DATABASE',3,'p_owner_database','Gramatica.py',1055),
  ('OWNER_DATABASE -> <empty>','OWNER_DATABASE',0,'p_owner_database_e','Gramatica.py',1059),
  ('MODE_DATABASE -> MODE IGUAL ENTERO','MODE_DATABASE',3,'p_mode_database','Gramatica.py',1063),
  ('MODE_DATABASE -> <empty>','MODE_DATABASE',0,'p_mode_database_e','Gramatica.py',1067),
  ('SHOW_DATABASES -> SHOW DATABASES SHOW_DATABASES_LIKE','SHOW_DATABASES',3,'p_show_databases','Gramatica.py',1071),
  ('SHOW_DATABASES_LIKE -> LIKE CADENADOBLE','SHOW_DATABASES_LIKE',2,'p_show_databases_like','Gramatica.py',1075),
  ('SHOW_DATABASES_LIKE -> <empty>','SHOW_DATABASES_LIKE',0,'p_show_databases_like_e','Gramatica.py',1079),
  ('ALTER_DATABASE -> ALTER DATABASE ID ALTER_DATABASE_OP','ALTER_DATABASE',4,'p_alter_database','Gramatica.py',1083),
  ('ALTER_DATABASE_OP -> RENAME TO ID','ALTER_DATABASE_OP',3,'p_alter_database_op','Gramatica.py',1087),
  ('ALTER_DATABASE_OP -> OWNER TO ALTER_TABLE_OP_OW','ALTER_DATABASE_OP',3,'p_alter_database_op','Gramatica.py',1088),
  ('ALTER_TABLE_OP_OW -> ID','ALTER_TABLE_OP_OW',1,'p_alter_database_op_ow','Gramatica.py',1092),
  ('ALTER_TABLE_OP_OW -> CURRENT_USER','ALTER_TABLE_OP_OW',1,'p_alter_database_op_ow','Gramatica.py',1093),
  ('ALTER_TABLE_OP_OW -> SESSION_USER','ALTER_TABLE_OP_OW',1,'p_alter_database_op_ow','Gramatica.py',1094),
  ('ALTER_DATABASE_OP -> <empty>','ALTER_DATABASE_OP',0,'p_alter_database_op_e','Gramatica.py',1098),
  ('DROP_DATABASE -> DROP DATABASE IF_EXISTS_DATABASE ID','DROP_DATABASE',4,'p_drop_database','Gramatica.py',1102),
  ('IF_EXISTS_DATABASE -> IF EXISTS','IF_EXISTS_DATABASE',2,'p_if_exists_database','Gramatica.py',1106),
  ('IF_EXISTS_DATABASE -> <empty>','IF_EXISTS_DATABASE',0,'p_if_exists_database_e','Gramatica.py',1110),
]
