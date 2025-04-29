# Scrapper da Amazon

O mini projeto tem como finalidade implementar testes em cima de uma função simples

## O que o get_products faz

O get_products é uma função que retorna os últimos *8* produtos na lista de ofertas da amazon, contendo os seguintes atributos:
- products
    - Um array de produtos, contendo *product_name*, *product_offer*, e *product_image*
- length
    - O tamanho do retorno de produtos
- run_time
    - O tempo para rodar o script, em segundos

## Passos para executar

Siga as instruções do Python Venv para ativar o ambiente virtual na pasta venv. Após isso, rode `python get_products.py` para ver o retorno

## Casos de teste

- O script deve rodar em menos de 20 segundos
- O script deve retornar 8 produtos
- Cada produto deve ter product_name, product_offer, e product_image não nulos
