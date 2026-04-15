grammar NoSQL;

programa
    : sentencia+ EOF
    ;

sentencia
    : create_stmt
    | read_stmt
    | update_stmt
    | delete_stmt
    ;

create_stmt
    : CREATE IDENT campo_lista END
    ;

read_stmt
    : READ col_lista END
    ;

update_stmt
    : UPDATE IDENT campo_lista END
    ;

delete_stmt
    : DELETE col_lista END
    ;

col_lista
    : ALL
    | IDENT (',' IDENT)*
    ;

campo_lista
    : campo (';' campo)*
    ;

campo
    : IDENT ':' valor
    ;

valor
    : NUMBER
    | STRING
    | IDENT
    | lista_valor
    | doc_anidado
    ;

lista_valor
    : '[' valor (',' valor)* ']'
    | '[' ']'
    ;

doc_anidado
    : '{' campo_lista '}'
    ;

CREATE  : C R E A T E ;
READ    : R E A D ;
UPDATE  : U P D A T E ;
DELETE  : D E L E T E ;
END     : E N D ;
ALL     : A L L ;

NUMBER  : '-'? [0-9]+ ('.' [0-9]+)? ;

STRING
    : '"'  (~["\r\n])* '"'
    | '\'' (~['\r\n])* '\''
    ;

IDENT   : [a-zA-Z_][a-zA-Z0-9_]* ;

WS      : [ \t\r\n]+ -> skip ;

fragment A:[aA]; fragment B:[bB]; fragment C:[cC]; fragment D:[dD];
fragment E:[eE]; fragment F:[fF]; fragment G:[gG]; fragment H:[hH];
fragment I:[iI]; fragment J:[jJ]; fragment K:[kK]; fragment L:[lL];
fragment M:[mM]; fragment N:[nN]; fragment O:[oO]; fragment P:[pP];
fragment Q:[qQ]; fragment R:[rR]; fragment S:[sS]; fragment T:[tT];
fragment U:[uU]; fragment V:[vV]; fragment W:[wW]; fragment X:[xX];
fragment Y:[yY]; fragment Z:[zZ];