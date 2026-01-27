-- Tabela transacao_produto: idTransacaoProduto	IdTransacao	IdProduto	QtdeProduto	vlProduto

-- Tabela transacoes: IdTransacao	IdCliente	DtCriacao	QtdePontos	DescSistemaOrigem

-- Tabela clientes: idCliente	flEmail	flTwitch	flYouTube	flBlueSky	flInstagram	qtdePontos	DtCriacao	DtAtualizacao

-- Tabela produtos: IdProduto	DescNomeProduto	DescDescricaoProduto	DescCategoriaProduto

-- Categoria produtos mais vendidos
SELECT 
p.DescCategoriaProduto,
COUNT(tp.idTransacaoProduto) AS QtdeVendida
FROM transacao_produto tp
LEFT JOIN produtos p ON tp.IdProduto = p.IdProduto
GROUP BY p.DescCategoriaProduto
ORDER BY QtdeVendida DESC;