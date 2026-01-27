-- Tabela transacao_produto: idTransacaoProduto	IdTransacao	IdProduto	QtdeProduto	vlProduto

-- Tabela transacoes: IdTransacao	IdCliente	DtCriacao	QtdePontos	DescSistemaOrigem

-- Tabela clientes: idCliente	flEmail	flTwitch	flYouTube	flBlueSky	flInstagram	qtdePontos	DtCriacao	DtAtualizacao

-- Tabela produtos: IdProduto	DescNomeProduto	DescDescricaoProduto	DescCategoriaProduto

WITH sumarioDia AS (
    SELECT
        substr(dtCriacao,1,10) as dtDia,
        COUNT(DISTINCT IdTransacao) AS qtdeTransacoes

    FROM transacoes

    WHERE dtDia >= '2025-08-25' AND dtDia < '2025-08-30'
    GROUP BY dtDia
)

SELECT *,
    SUM(qtdeTransacoes) OVER (ORDER BY dtDia) AS soma_acumulada_dia
FROM sumarioDia