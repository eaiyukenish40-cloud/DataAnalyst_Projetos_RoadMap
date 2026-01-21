-- Qual a quantidade de pontos positivos médio por dia?
-- Tabela transacoes: IdTransacao	IdCliente	DtCriacao	QtdePontos	DescSistemaOrigem

SELECT 
    COUNT(DISTINCT STRFTIME('%Y-%m-%d', DtCriacao)) AS DiasDistintos,
    SUM(QtdePontos) AS TotalPontos,
    SUM(QtdePontos)/COUNT(DISTINCT STRFTIME('%Y-%m-%d', DtCriacao)) AS MediaPontosDia
FROM transacoes
WHERE QtdePontos > 0

