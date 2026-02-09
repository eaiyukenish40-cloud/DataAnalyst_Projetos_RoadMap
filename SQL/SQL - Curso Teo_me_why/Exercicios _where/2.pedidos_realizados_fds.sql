
-- Para Encontrar os pedidos realizados no final de semana (sábado e domingo), é necessário obter somente a informação de data e posteriormente aplicar a função STRFTIME onde será possível identificar o dia da semana correspondente a cada data. Neste caso 0 representa domingo e 6 representa sábado, criando a coluna TipoDia, classificando FDS ou Semana. O filtro é feito por meio do WHERE
SELECT
CASE WHEN STRFTIME('%w', DATE(DtCriacao)) IN ('0','6') THEN 'FDS' ELSE 'Semana' END AS TipoDia
FROM transacoes
WHERE TipoDia = 'FDS';


-- Solução simplificada:
SELECT
DtCriacao
FROM transacoes
WHERE STRFTIME('%w', DATE(DtCriacao)) IN ('0','6');