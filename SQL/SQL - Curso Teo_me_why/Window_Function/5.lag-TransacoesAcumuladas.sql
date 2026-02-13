-- Tabela transacao_produto: idTransacaoProduto	IdTransacao	IdProduto	QtdeProduto	vlProduto

-- Tabela transacoes: IdTransacao	IdCliente	DtCriacao	QtdePontos	DescSistemaOrigem

-- Tabela clientes: idCliente	flEmail	flTwitch	flYouTube	flBlueSky	flInstagram	qtdePontos	DtCriacao	DtAtualizacao

-- Tabela produtos: IdProduto	DescNomeProduto	DescDescricaoProduto	DescCategoriaProduto

-- Quantidade de transações Acumuladas ao longo do tempo?

WITH soma_transacoes_tempo AS (
    SELECT
        substr(DtCriacao,1,10) AS DtDia,
        COUNT(DISTINCT IdTransacao) AS QtdeTransacoes
    FROM transacoes
    GROUP BY DtDia 
),
acumulada AS (
    SELECT
        DtDia,
        QtdeTransacoes,
        SUM(QtdeTransacoes) OVER(ORDER BY DtDia) AS QtdeTransacoesAcumuladas
    FROM soma_transacoes_tempo
)
-- Caso deseja encontrar o valor base de algo (quando houve 100000 transacoes).
SELECT * 
FROM acumulada


    