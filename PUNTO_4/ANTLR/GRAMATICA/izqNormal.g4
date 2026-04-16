grammar izqNormal;

programa: expresion EOF;

expresion
    : expresion SUM factor
    | expresion RES factor
    | factor
    ;

factor
    : factor MUL term
    | factor DIV term
    | term
    ;

term
    : NUM
    | RES NUM
    ;

SUM: '+';
RES: '-';
MUL: '*';
DIV: '/';

NUM: DECIMAL | ENTERO;
DECIMAL: DIGITO+ '.' DIGITO+; 
ENTERO: DIGITO+;

fragment DIGITO: [0-9];

WS: [ \t]+ -> skip;