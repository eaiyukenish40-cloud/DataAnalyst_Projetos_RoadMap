-- Tabela transacoes: IdTransacao	IdCliente	DtCriacao	QtdePontos	DescSistemaOrigem
--Qual dia da semana teve mais pedidos em 2025?
SELECT
    STRFTIME('%w', substr(DtCriacao, 1, 10)) AS DiaSemana,
    COUNT(DISTINCT IdTransacao) AS QtdPedidos
FROM transacoes
WHERE substr(DtCriacao,1,4) = '2025'
GROUP BY DiaSemana