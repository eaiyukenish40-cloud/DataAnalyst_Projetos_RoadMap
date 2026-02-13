-- Tabela transacao_produto: idTransacaoProduto	IdTransacao	IdProduto	QtdeProduto	vlProduto

-- Tabela transacoes: IdTransacao	IdCliente	DtCriacao	QtdePontos	DescSistemaOrigem

-- Tabela clientes: idCliente	flEmail	flTwitch	flYouTube	flBlueSky	flInstagram	qtdePontos	DtCriacao	DtAtualizacao

-- Tabela produtos: IdProduto	DescNomeProduto	DescDescricaoProduto	DescCategoriaProduto

-- Qual o dia da semana mais ativo de cada usuário?

-- O insight de negócio, através do dia da semana mais ativo, pode ser utilizado para criar campanhas de marketing mais assertivas, como promoções ou descontos específicos para os dias em que os clientes estão mais propensos a realizar transações. Além disso, essa informação pode ajudar a otimizar o atendimento ao cliente, alocando recursos de forma mais eficiente nos dias de maior movimento.
WITH dias_semana_transacoes_user AS(
    SELECT
        DISTINCT IdCliente,
        CASE WHEN strftime('%w', substr(DtCriacao,1,10)) = '0' THEN 'Domingo'
            WHEN strftime('%w', substr(DtCriacao,1,10)) = '1' THEN 'Segunda-feira'
            WHEN strftime('%w', substr(DtCriacao,1,10)) = '2' THEN 'Terça-feira'
            WHEN strftime('%w', substr(DtCriacao,1,10)) = '3' THEN 'Quarta-feira'
            WHEN strftime('%w', substr(DtCriacao,1,10)) = '4' THEN 'Quinta-feira'
            WHEN strftime('%w', substr(DtCriacao,1,10)) = '5' THEN 'Sexta-feira'
            WHEN strftime('%w', substr(DtCriacao,1,10)) = '6' THEN 'Sábado'
        END AS DiaSemana,
        COUNT(DISTINCT IdTransacao) AS QtdeTransacoes
    FROM transacoes
    GROUP BY IdCliente, DiaSemana
),
rankDiasAtivos AS (
    SELECT
        IdCliente,
        DiaSemana,
        QtdeTransacoes,
        ROW_NUMBER() OVER(PARTITION BY IdCliente ORDER BY QtdeTransacoes DESC) AS RankDiasAtivos
    FROM dias_semana_transacoes_user
)
SELECT * FROM rankDiasAtivos
WHERE RankDiasAtivos = 1

    