SELECT * FROM olist.order_items;

describe order_items;

alter table order_items
modify column order_id varchar(40),
modify column order_item_id tinyint,
modify column product_id varchar(40),
modify column seller_id varchar(40),
modify column shipping_limit_date datetime,
modify column price decimal(10,2),
modify column freight_value decimal(10,2);

alter table order_items
add primary key (order_id,order_item_id);

alter table order_items
add constraint fk_itens_order
foreign key (order_id)
references olist_orders(order_id),
add constraint fk_itens_product
foreign key (product_id)
references olist_products(product_id);

#não é primary
select order_id, count(order_id) as num from order_items
group by order_id
order by num desc;
#having num > 1;

select product_id, count(product_id) as num from order_items
group by product_id
having num > 1;

select seller_id, count(seller_id) as num from order_items
group by seller_id
having num > 1;

# conferir se há negativos
select order_item_id from order_items
group by order_item_id;

select price from order_items
order by price desc;

select freight_value from order_items
order by freight_value desc;

#conferir atributo único para primary key composta:
select order_id, order_item_id, count(*) as num from order_items
group by order_id,order_item_id
having num > 1;