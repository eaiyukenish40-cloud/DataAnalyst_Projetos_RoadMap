-- Qual cliente fez mais transacoes em 2024
-- Tabela transacoes: IdTransacao	IdCliente	DtCriacao	QtdePontos	DescSistemaOrigem
SELECT
idCliente,
COUNT(IdTransacao)
FROM transacoes
WHERE DtCriacao >= '2024-01-01' AND DtCriacao < '2025-01-01'
GROUP BY idCliente
ORDER BY COUNT(IdTransacao) DESC
LIMIT 1