-- selecione a primeira transacao diária
WITH transacoes_ordenadas AS(
    SELECT 
        IdTransacao,
        IdCliente,
        DtCriacao,
        ROW_NUMBER() OVER (PARTITION BY substr(DtCriacao,1,10)  ORDER BY DtCriacao) AS RowNumber
    FROM transacoes
    ORDER BY DtCriacao
)
SELECT *
FROM transacoes_ordenadas
WHERE RowNumber = 1