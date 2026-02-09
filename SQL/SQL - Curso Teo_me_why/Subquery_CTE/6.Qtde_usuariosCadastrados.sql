-- Tabela transacao_produto: idTransacaoProduto	IdTransacao	IdProduto	QtdeProduto	vlProduto

-- Tabela transacoes: IdTransacao	IdCliente	DtCriacao	QtdePontos	DescSistemaOrigem

-- Tabela clientes: idCliente	flEmail	flTwitch	flYouTube	flBlueSky	flInstagram	qtdePontos	DtCriacao	DtAtualizacao

-- Tabela produtos: IdProduto	DescNomeProduto	DescDescricaoProduto	DescCategoriaProduto

--Qtde de usuários cadastrados (absoluto e acumulado) ao longo do tempo

WITH clientesDia AS(
    SELECT 
        COUNT(DISTINCT idCliente) as num_cliente,
        substr(DtCriacao,1,10) as dataDia
    FROM clientes
    GROUP BY dataDia

)
SELECT
    dataDia,
    SUM(num_cliente) OVER(ORDER BY dataDia ASC) as acumuladoDiaClientes
    
FROM clientesDia

