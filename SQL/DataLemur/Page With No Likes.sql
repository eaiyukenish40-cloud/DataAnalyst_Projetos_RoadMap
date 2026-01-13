-- Assume you're given two tables containing data about Facebook Pages and their respective likes (as in "Like a Facebook Page").
-- Write a query to return the IDs of the Facebook pages that have zero likes. The output should be sorted in ascending order based on the page IDs.


/* Tabela: pages
   Armazena os metadados das páginas.
*/
CREATE TABLE pages (
    page_id INT PRIMARY KEY,               -- Identificador único (Chave Primária)
    page_name VARCHAR(255) NOT NULL        -- Nome da página (Obrigatório)
);

/* Tabela: page_likes
   Tabela de relacionamento entre usuários e páginas.
*/
CREATE TABLE page_likes (
    user_id INT NOT NULL,
    page_id INT NOT NULL,
    liked_date DATETIME NOT NULL,
    
    -- Definimos uma Chave Primária Composta para evitar curtidas duplicadas
    PRIMARY KEY (user_id, page_id),
    
    -- Chave Estrangeira: Garante que a página curtida realmente exista na tabela 'pages'
    CONSTRAINT fk_page 
        FOREIGN KEY (page_id) 
        REFERENCES pages(page_id)
        ON DELETE CASCADE                  -- Se a página for deletada, as curtidas somem automaticamente
);

INSERT INTO pages (page_id, page_name) 
VALUES 
    (20001, 'SQL Solutions'),
    (20045, 'Brain Exercises'),
    (20701, 'Tips for Data Analysts'),
    (31111,	'Postgres Crash Course'),
	(32728,	'Break the thread');
    
INSERT INTO page_likes (user_id, page_id, liked_date) 
VALUES 
    (111, 20001, '2022-04-08 00:00:00'),
    (121, 20045, '2022-03-12 00:00:00'),
    (156, 20001, '2022-07-25 00:00:00'),
    (255, 20045, '2022-07-19 00:00:00'),
    (125, 20001, '2022-07-19 00:00:00'),
    (144, 31111, '2022-06-21 00:00:00'),
    (125, 31111, '2022-07-04 00:00:00');
    

-- Resolução
-- 1.O problema envolve a junção de informações de duas fontes diferentes que são linkadas por meio da page_id. Sendo um identificador primário único na tabela pages.
-- 2. Visto que queremos encontrar quais paginas não tiveram likes de usuários, queremos encontrar quais page_id não aparecem na tabela page_likes.
-- 3. É necessário usar um join, foi escolhido o left join para preservar as informações da tabela pages, e encontrar a junção em comum com a page_likes.
-- 4. Nessa junção, caso algum identificado de pages não fosse encontrado em page_likes, as colunas retornadas seriam vazias, justamente o que buscamos
-- 5. Por fim, basta filtrar as informações nulas, com o WHERE IS NULL para encontrar quais paginas não tiveram likes.
SELECT p.page_id FROM pages p
LEFT JOIN page_likes pl ON pl.page_id = p.page_id
WHERE pl.liked_date IS NULL;