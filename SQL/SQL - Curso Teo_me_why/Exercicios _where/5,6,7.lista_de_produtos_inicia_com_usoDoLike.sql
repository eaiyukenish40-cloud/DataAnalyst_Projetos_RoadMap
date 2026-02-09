SELECT
*
FROM produtos
WHERE DescDescricaoProduto LIKE '%chapéu%';
--inicia com: '%Venda de' 
--termina com: 'Lover%' 

--%nome: indica que o texto pode ter qualquer coisa antes de "nome"
--nome%: indica que o texto deve começar com "nome"
--%nome%: indica que o texto pode ter qualquer coisa antes e depois de "nome