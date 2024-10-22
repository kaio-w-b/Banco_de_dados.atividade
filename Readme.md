# Sistema de Gerenciamento de Mercadinho 🏪

## Descrição do Projeto
Este é um projeto de banco de dados que implementa um sistema completo para gerenciamento de um mercadinho. O sistema foi desenvolvido para facilitar o controle de vendas, estoque, clientes e funcionários, oferecendo uma solução integrada para pequenos estabelecimentos comerciais.

## Estrutura do Sistema

### Cadastro de Pessoas
O sistema mantém um cadastro base de pessoas com as seguintes informações:
- CPF (identificador único)
- Nome
- Email
- Telefone

### Clientes
Os clientes são cadastrados com benefícios especiais:
- Identificação por CPF
- Sistema de descontos especiais para:
  - Fãs de One Piece
  - Torcedores do Flamengo
  - Pessoas de Sousa
- Senha para acesso ao sistema
- Histórico completo de compras

### Funcionários
O sistema possui controle de funcionários com:
- Identificação por CPF
- Cargo
- Senha de acesso
- Registro de vendas realizadas

### Produtos
Controle completo de produtos com:
- Nome do produto
- Quantidade em estoque
- Código do produto
- Preço de compra
- Preço de venda
- Indicador se é fabricado em Mari

### Sistema de Vendas
O processo de venda funciona da seguinte forma:

1. **Verificação do Cliente**
   - O cliente é identificado no sistema
   - O sistema verifica automaticamente se há direito a descontos especiais

2. **Controle de Estoque**
   - Durante a venda, o sistema verifica automaticamente a disponibilidade dos produtos
   - Impede vendas de produtos sem estoque suficiente
   - Atualiza o estoque automaticamente após cada venda

3. **Processamento de Descontos**
   - Aplica 10% de desconto para clientes que:
     - São fãs de One Piece
     - Torcem para o Flamengo
     - São de Sousa

4. **Registro da Venda**
   - Data e hora da venda
   - Identificação do cliente e funcionário
   - Valor total
   - Descontos aplicados
   - Método de pagamento
   - Status do pagamento

### Funcionalidades Especiais

1. **Controle de Estoque**
   - Alerta para produtos com quantidade inferior a 5 unidades
   - Identificação de produtos fabricados em Mari
   - Histórico de vendas por produto

2. **Relatórios**
   - Vendas por período
   - Desempenho dos funcionários
   - Histórico de compras por cliente
   - Produtos mais vendidos

3. **Sistema de Autenticação**
   - Login por CPF ou email
   - Níveis de acesso diferenciados para clientes e funcionários

4. **Gestão de Vendas**
   - Acompanhamento do status de pagamento
   - Histórico completo de transações
   - Detalhamento de itens por venda

### Segurança e Integridade
- Todas as operações são validadas antes de serem executadas
- Sistema de senhas para proteção dos dados
- Verificações de estoque em tempo real
- Backup automático das informações

Este sistema foi projetado para ser intuitivo e eficiente, permitindo que pequenos mercados mantenham um controle preciso de suas operações, desde o gerenciamento de estoque até o relacionamento com clientes, proporcionando uma experiência comercial organizada e profissional.
