-- Tabela transacao_produto: idTransacaoProduto	IdTransacao	IdProduto	QtdeProduto	vlProduto

-- Tabela transacoes: IdTransacao	IdCliente	DtCriacao	QtdePontos	DescSistemaOrigem

-- Tabela clientes: idCliente	flEmail	flTwitch	flYouTube	flBlueSky	flInstagram	qtdePontos	DtCriacao	DtAtualizacao

-- Tabela produtos: IdProduto	DescNomeProduto	DescDescricaoProduto	DescCategoriaProduto

-- Curva de churn no curso de SQL (período do curso 2025-08-25 a 2025-08-29)


-- identificar os clientes do primeiro dia (data de fixação para cálculo de churn)
WITH ChurnClientes AS(
    SELECT
        DISTINCT IdCliente
        
    FROM transacoes
    WHERE DtCriacao >= '2025-08-25' AND DtCriacao < '2025-08-26' -- primeiro dia
    ORDER BY DtCriacao
)
SELECT
    substr(t.DtCriacao,1,10) AS DataDia,
    COUNT(DISTINCT cc.IdCliente) AS clientesInicio,
    1.* COUNT(DISTINCT cc.IdCliente)/(select count(*) from ChurnClientes) AS percentualRetencao -- obter o percentual de retencao através da subquerie contando a quantidade de clientes no inicio
    
FROM ChurnClientes cc
LEFT JOIN transacoes t ON t.IdCliente = cc.IdCliente -- filtra apenas os Id's de quem participou do primeiro dia para poder encontrar o churn

WHERE t.DtCriacao >= '2025-08-25' AND t.DtCriacao < '2025-08-30' -- período do curso
GROUP BY DataDia
ORDER BY DataDia

--p.DescNomeProduto = 'Lista de presença'


-- Cenário simples e direito,  porém errado. Estes dados não traduzem o churn real, mas sim a participação diárias dos clientes nos dias da live. Não selecionando a participação de um mesmo cliente em todos os dias.
--WITH participacoes AS(
--    SELECT 
--        COUNT(DISTINCT IdCliente) AS participacao,
--        substr(DtCriacao,1,10) AS DataDia
--    FROM transacoes 

--    WHERE DataDia >= '2025-08-25' AND DataDia < '2025-08-30'
--    GROUP BY DataDia
--    ORDER BY DataDia
--)