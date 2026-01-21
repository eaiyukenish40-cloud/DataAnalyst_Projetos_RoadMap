-- Tabela transacoes: IdTransacao	IdCliente	DtCriacao	QtdePontos	DescSistemaOrigem
--listar todas as transacoes adicionando uma coluna nova sinalizando: alto,medio e baixo para o valor dos pontos [<10;<500;>=500]

SELECT 
    IdTransacao,
    CASE
        WHEN QtdePontos < 10 THEN 'baixo'
        WHEN QtdePontos < 500 THEN 'medio'
        ELSE 'alto'
    END AS NivelPontos
FROM transacoes