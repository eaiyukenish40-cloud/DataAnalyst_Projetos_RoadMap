-- Tabela transacao_produto: idTransacaoProduto	IdTransacao	IdProduto	QtdeProduto	vlProduto

-- Tabela transacoes: IdTransacao	IdCliente	DtCriacao	QtdePontos	DescSistemaOrigem

-- Tabela clientes: idCliente	flEmail	flTwitch	flYouTube	flBlueSky	flInstagram	qtdePontos	DtCriacao	DtAtualizacao

-- Tabela produtos: IdProduto	DescNomeProduto	DescDescricaoProduto	DescCategoriaProduto

WITH sumarioDiaCliente AS (
    SELECT
        IdCliente,
        substr(dtCriacao,1,10) as dtDia,
        COUNT(DISTINCT IdTransacao) AS qtdeTransacoes

    FROM transacoes

    WHERE dtDia >= '2025-08-25' AND dtDia < '2025-08-30'
    GROUP BY IdCliente, dtDia
),
tabela_lag AS(
SELECT
    *,
    LAG(qtdeTransacoes) OVER(PARTITION BY IdCliente ORDER BY dtDia) AS lag 
FROM sumarioDiaCliente
)
SELECT
    *,
    1.0*qtdeTransacoes/lag AS tendenciaEngajamento
FROM tabela_lag
