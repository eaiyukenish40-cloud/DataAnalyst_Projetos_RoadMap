-- Tabela transacao_produto: idTransacaoProduto	IdTransacao	IdProduto	QtdeProduto	vlProduto

-- Tabela transacoes: IdTransacao	IdCliente	DtCriacao	QtdePontos	DescSistemaOrigem

-- Tabela clientes: idCliente	flEmail	flTwitch	flYouTube	flBlueSky	flInstagram	qtdePontos	DtCriacao	DtAtualizacao

-- Tabela produtos: IdProduto	DescNomeProduto	DescDescricaoProduto	DescCategoriaProduto

SELECT
COUNT(DISTINCT t.IdTransacao) AS QtdeTransacao,
t.IdCliente,
c.DtCriacao
FROM transacoes t
LEFT JOIN clientes c ON c.IdCliente = t.IdCliente
GROUP BY t.IdCliente
ORDER BY QtdeTransacao DESC
LIMIT 10

