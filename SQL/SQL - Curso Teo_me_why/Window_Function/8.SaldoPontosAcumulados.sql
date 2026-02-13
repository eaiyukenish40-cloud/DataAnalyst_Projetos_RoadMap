-- Tabela transacao_produto: idTransacaoProduto	IdTransacao	IdProduto	QtdeProduto	vlProduto

-- Tabela transacoes: IdTransacao	IdCliente	DtCriacao	QtdePontos	DescSistemaOrigem

-- Tabela clientes: idCliente	flEmail	flTwitch	flYouTube	flBlueSky	flInstagram	qtdePontos	DtCriacao	DtAtualizacao

-- Tabela produtos: IdProduto	DescNomeProduto	DescDescricaoProduto	DescCategoriaProduto

-- Saldo de pontos acumulado de cada usuário

WITH pontos_acumulados AS (
    SELECT
        IdCliente,
        SUM(QtdePontos) totalPoints,
        substr(DtCriacao,1,10) AS DataTransacao
    FROM transacoes
    GROUP BY IdCliente, DataTransacao
)
SELECT *,
    SUM(totalPoints) OVER (PARTITION BY IdCliente ORDER BY DataTransacao) AS SaldoPontosAcumulados
FROM pontos_acumulados