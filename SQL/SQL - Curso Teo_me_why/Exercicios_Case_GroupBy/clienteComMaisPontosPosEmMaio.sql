-- Tabela transacoes: IdTransacao	IdCliente	DtCriacao	QtdePontos	DescSistemaOrigem
-- Qual cliente juntou mais pontos positivo em maio de 2025
SELECT 
    IdCliente,
    SUM(QtdePontos) AS TotalPontos
FROM transacoes
WHERE QtdePontos > 0 AND DtCriacao >= '2025-05-01' AND DtCriacao <= 2025-05-31'
GROUP BY IdCliente
ORDER BY TotalPontos DESC
LIMIT 1