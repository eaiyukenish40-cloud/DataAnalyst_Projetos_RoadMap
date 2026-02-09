-- Tabela transacao_produto: idTransacaoProduto	IdTransacao	IdProduto	QtdeProduto	vlProduto

-- Tabela transacoes: IdTransacao	IdCliente	DtCriacao	QtdePontos	DescSistemaOrigem

-- Tabela clientes: idCliente	flEmail	flTwitch	flYouTube	flBlueSky	flInstagram	qtdePontos	DtCriacao	DtAtualizacao

-- Tabela produtos: IdProduto	DescNomeProduto	DescDescricaoProduto	DescCategoriaProduto

WITH dataDia AS(
    SELECT
        COUNT(DISTINCT IdTransacao) as qtdeTransacoes, 
        substr(DtCriacao,1,10) AS dataDia
    FROM transacoes
    GROUP BY dataDia
)
SELECT
    dataDia,
    SUM(qtdeTransacoes) OVER(ORDER BY dataDia ASC) as somaAcumuladaTransacoes
FROM dataDia
