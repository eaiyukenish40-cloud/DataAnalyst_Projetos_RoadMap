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
)
SELECT
    *,
    SUM(qtdeTransacoes) OVER(PARTITION BY IdCliente ORDER BY dtDia) AS transacoesAcumuladaCliente
FROM sumarioDiaCliente