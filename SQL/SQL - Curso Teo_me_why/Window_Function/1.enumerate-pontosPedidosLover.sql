-- Tabela transacao_produto: idTransacaoProduto	IdTransacao	IdProduto	QtdeProduto	vlProduto

-- Tabela transacoes: IdTransacao	IdCliente	DtCriacao	QtdePontos	DescSistemaOrigem

-- Tabela clientes: idCliente	flEmail	flTwitch	flYouTube	flBlueSky	flInstagram	qtdePontos	DtCriacao	DtAtualizacao

-- Tabela produtos: IdProduto	DescNomeProduto	DescDescricaoProduto	DescCategoriaProduto

WITH join_produtos AS(
SELECT
    t.IdCliente,
    p.DescCategoriaProduto,
    SUM(t.QtdePontos) as somaLovers
FROM transacoes t
LEFT JOIN transacao_produto tp ON tp.IdTransacao = t.IdTransacao
LEFT JOIN produtos p ON p.IdProduto = tp.IdProduto
WHERE p.DescCategoriaProduto = 'lovers'
GROUP BY t.IdCliente
)
SELECT*,
    ROW_NUMBER() OVER(ORDER BY somaLovers ASC) as rankPontosPedidosLovers
FROM join_produtos
