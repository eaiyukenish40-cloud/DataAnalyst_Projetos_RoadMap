-- Tabela transacao_produto: idTransacaoProduto	IdTransacao	IdProduto	QtdeProduto	vlProduto

-- Tabela transacoes: IdTransacao	IdCliente	DtCriacao	QtdePontos	DescSistemaOrigem

-- Tabela clientes: idCliente	flEmail	flTwitch	flYouTube	flBlueSky	flInstagram	qtdePontos	DtCriacao	DtAtualizacao

-- Tabela produtos: IdProduto	DescNomeProduto	DescDescricaoProduto	DescCategoriaProduto

SELECT

t.IdCliente,
t.IdTransacao,
tp.IdProduto,
p.DescNomeProduto,
p.DescCategoriaProduto,
sum(t.QtdePontos) AS totalPoints


FROM transacao_produto tp
LEFT JOIN transacoes t ON t.IdTransacao = tp.IdTransacao
LEFT JOIN produtos p ON p.IdProduto = tp.IdProduto

WHERE p.DescCategoriaProduto = 'lovers'
GROUP BY t.IdCliente
ORDER BY totalPoints ASC